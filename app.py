from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import subprocess
import shlex
import os
import json

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)  # Enable CORS for all routes

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
    """Execute a shell command safely"""
    try:
        # Parse the command
        command_parts = shlex.split(command)
        
        if not is_command_allowed(command_parts):
            return {
                'success': False,
                'output': f"Command '{command_parts[0]}' is not allowed for security reasons.",
                'error': 'Command not in allowed list'
            }
        
        # Execute the command
        result = subprocess.run(
            command_parts,
            capture_output=True,
            text=True,
            timeout=30,  # 30 second timeout
            cwd=os.getcwd()  # Run in current directory
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


@app.route('/api/execute', methods=['POST'])
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
        'current_directory': os.getcwd()
    })

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
