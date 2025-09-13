from flask import Flask, request, jsonify, render_template, session, g
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import subprocess
import shlex
import os
import json
import logging
import time
import hashlib
import secrets
from functools import wraps
from config import config

# Initialize Flask app
app = Flask(__name__, static_folder='static', static_url_path='/static')

# Load configuration
config_name = os.environ.get('FLASK_ENV', 'default')
app.config.from_object(config[config_name])

# Initialize extensions
CORS(app, origins=app.config['CORS_ORIGINS'])
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    storage_uri=app.config['RATELIMIT_STORAGE_URL'],
    default_limits=[app.config['RATELIMIT_DEFAULT']]
)

# Setup logging
logging.basicConfig(
    level=getattr(logging, app.config['LOG_LEVEL']),
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler(app.config['LOG_FILE']),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Security decorators
def require_auth(f):
    """Require authentication for API endpoints"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

def log_command_execution(f):
    """Log command execution for security monitoring"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        start_time = time.time()
        client_ip = get_remote_address()
        user_agent = request.headers.get('User-Agent', 'Unknown')
        
        logger.info(f"Command execution started from {client_ip} - {user_agent}")
        
        try:
            result = f(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"Command execution completed in {execution_time:.2f}s")
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"Command execution failed after {execution_time:.2f}s: {str(e)}")
            raise
    return decorated_function

# Allowed commands for security
ALLOWED_COMMANDS = {
    'ls': ['ls', '-la'],
    'pwd': ['pwd'],
    'date': ['date'],
    'whoami': ['whoami'],
    'echo': ['echo'],
    'cat': ['cat'],
    'head': ['head'],
    'tail': ['tail'],
    'grep': ['grep'],
    'find': ['find'],
    'ps': ['ps', 'aux'],
    'top': ['top', '-n', '1'],
    'df': ['df', '-h'],
    'free': ['free', '-h'],
    'uname': ['uname', '-a'],
    'uptime': ['uptime'],
    'history': ['history'],
    'env': ['env'],
    'which': ['which'],
    'whereis': ['whereis'],
    'file': ['file'],
    'wc': ['wc'],
    'sort': ['sort'],
    'uniq': ['uniq'],
    'cut': ['cut'],
    'awk': ['awk'],
    'sed': ['sed'],
    'tr': ['tr'],
    'xargs': ['xargs'],
    'tee': ['tee'],
    'less': ['less'],
    'more': ['more'],
    'man': ['man'],
    'help': ['help'],
    'clear': ['clear'],
    'cd': ['cd'],
    'mkdir': ['mkdir'],
    'rmdir': ['rmdir'],
    'touch': ['touch'],
    'cp': ['cp'],
    'mv': ['mv'],
    'rm': ['rm'],
    'chmod': ['chmod'],
    'chown': ['chown'],
    'ln': ['ln'],
    'tar': ['tar'],
    'zip': ['zip'],
    'unzip': ['unzip'],
    'git': ['git'],
    'python': ['python'],
    'python3': ['python3'],
    'node': ['node'],
    'npm': ['npm'],
    'pip': ['pip'],
    'pip3': ['pip3'],
    'brew': ['brew'],
    'apt': ['apt'],
    'yum': ['yum'],
    'systemctl': ['systemctl'],
    'service': ['service'],
    'netstat': ['netstat'],
    'ss': ['ss'],
    'ping': ['ping'],
    'curl': ['curl'],
    'wget': ['wget'],
    'ssh': ['ssh'],
    'scp': ['scp'],
    'rsync': ['rsync'],
    'crontab': ['crontab'],
    'at': ['at'],
    'kill': ['kill'],
    'killall': ['killall'],
    'nohup': ['nohup'],
    'screen': ['screen'],
    'tmux': ['tmux'],
    'vim': ['vim'],
    'nano': ['nano'],
    'emacs': ['emacs'],
    'vi': ['vi'],
    'joe': ['joe'],
    'pico': ['pico'],
}

def is_command_allowed(command_parts):
    """Check if the command is in the allowed list"""
    if not command_parts:
        return False
    
    base_command = command_parts[0]
    return base_command in ALLOWED_COMMANDS

def execute_command(command):
    """Execute a shell command safely with enhanced security"""
    try:
        # Validate command length
        if len(command) > app.config['MAX_COMMAND_LENGTH']:
            return {
                'success': False,
                'output': f"Command too long. Maximum length is {app.config['MAX_COMMAND_LENGTH']} characters.",
                'error': 'Command too long'
            }
        
        # Parse the command
        command_parts = shlex.split(command)
        
        if not is_command_allowed(command_parts):
            logger.warning(f"Blocked command attempt: {command}")
            return {
                'success': False,
                'output': f"Command '{command_parts[0]}' is not allowed for security reasons.",
                'error': 'Command not in allowed list'
            }
        
        # Additional security checks
        dangerous_patterns = ['rm -rf', 'sudo', 'su -', 'chmod 777', 'passwd', 'useradd']
        if any(pattern in command.lower() for pattern in dangerous_patterns):
            logger.warning(f"Blocked dangerous command: {command}")
            return {
                'success': False,
                'output': "Command contains potentially dangerous operations.",
                'error': 'Dangerous command blocked'
            }
        
        # Execute the command
        result = subprocess.run(
            command_parts,
            capture_output=True,
            text=True,
            timeout=app.config['COMMAND_TIMEOUT'],
            cwd=os.getcwd(),
            env=os.environ.copy()  # Use current environment
        )
        
        if result.returncode == 0:
            return {
                'success': True,
                'output': result.stdout.strip() if result.stdout else 'Command executed successfully (no output)',
                'error': None
            }
        else:
            return {
                'success': False,
                'output': result.stderr.strip() if result.stderr else 'Command failed with no error message',
                'error': f'Command failed with return code {result.returncode}'
            }
            
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'output': 'Command timed out after 30 seconds',
            'error': 'Timeout'
        }
    except Exception as e:
        return {
            'success': False,
            'output': f'Error executing command: {str(e)}',
            'error': str(e)
        }

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/auth/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    """Simple authentication endpoint"""
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        # Simple authentication (in production, use proper auth)
        if username == 'admin' and password == 'extendipede2024':
            session['authenticated'] = True
            session['username'] = username
            session.permanent = True
            logger.info(f"User {username} logged in from {get_remote_address()}")
            return jsonify({'success': True, 'message': 'Login successful'})
        else:
            logger.warning(f"Failed login attempt for {username} from {get_remote_address()}")
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
            
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return jsonify({'success': False, 'message': 'Login failed'}), 500

@app.route('/auth/logout', methods=['POST'])
def logout():
    """Logout endpoint"""
    username = session.get('username', 'unknown')
    session.clear()
    logger.info(f"User {username} logged out")
    return jsonify({'success': True, 'message': 'Logout successful'})

@app.route('/auth/status')
def auth_status():
    """Check authentication status"""
    return jsonify({
        'authenticated': session.get('authenticated', False),
        'username': session.get('username', None)
    })


@app.route('/api/execute', methods=['POST'])
@limiter.limit("10 per minute")
@require_auth
@log_command_execution
def execute():
    """Execute a command via API"""
    try:
        data = request.get_json()
        command = data.get('command', '').strip()
        
        if not command:
            return jsonify({
                'success': False,
                'output': 'No command provided',
                'error': 'Empty command'
            })
        
        result = execute_command(command)
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"API execute error: {str(e)}")
        return jsonify({
            'success': False,
            'output': f'Server error: {str(e)}',
            'error': str(e)
        })

@app.route('/api/allowed-commands', methods=['GET'])
def get_allowed_commands():
    """Get list of allowed commands"""
    return jsonify({
        'commands': list(ALLOWED_COMMANDS.keys()),
        'count': len(ALLOWED_COMMANDS)
    })

@app.route('/api/status', methods=['GET'])
def status():
    """Get server status"""
    return jsonify({
        'status': 'running',
        'allowed_commands': len(ALLOWED_COMMANDS),
        'current_directory': os.getcwd(),
        'version': '1.0.0',
        'environment': config_name,
        'authenticated': session.get('authenticated', False)
    })

@app.route('/health')
def health_check():
    """Health check endpoint for load balancers"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'uptime': time.time() - g.get('start_time', time.time())
    })

@app.route('/metrics')
def metrics():
    """Basic metrics endpoint"""
    if not app.config['ENABLE_METRICS']:
        return jsonify({'error': 'Metrics disabled'}), 403
    
    return jsonify({
        'commands_executed': g.get('commands_executed', 0),
        'uptime': time.time() - g.get('start_time', time.time()),
        'memory_usage': os.popen('ps -o pid,ppid,cmd,%mem,%cpu -p ' + str(os.getpid())).read()
    })

@app.before_request
def before_request():
    """Set up request context"""
    g.start_time = time.time()
    g.commands_executed = g.get('commands_executed', 0)

@app.after_request
def after_request(response):
    """Add security headers"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Move HTML file to templates directory
    if os.path.exists('index.html'):
        import shutil
        shutil.move('index.html', 'templates/index.html')
    
    print("Extendipede Web Server Starting...")
    print(f"Allowed commands: {len(ALLOWED_COMMANDS)}")
    print("Open your browser to: http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=8000)
