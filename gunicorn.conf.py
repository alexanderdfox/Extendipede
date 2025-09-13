# Gunicorn configuration for production deployment

import os
import multiprocessing

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
backlog = 2048

# Worker processes
workers = int(os.environ.get('WORKERS', multiprocessing.cpu_count() * 2 + 1))
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests, to prevent memory leaks
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = os.environ.get('ACCESS_LOG', 'logs/access.log')
errorlog = os.environ.get('ERROR_LOG', 'logs/error.log')
loglevel = os.environ.get('LOG_LEVEL', 'info')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'extendipede'

# Server mechanics
daemon = False
pidfile = os.environ.get('PID_FILE', 'logs/gunicorn.pid')
user = os.environ.get('USER', None)
group = os.environ.get('GROUP', None)
tmp_upload_dir = None

# SSL (if needed)
keyfile = os.environ.get('SSL_KEYFILE', None)
certfile = os.environ.get('SSL_CERTFILE', None)

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Performance tuning
preload_app = True
worker_tmp_dir = '/dev/shm'  # Use RAM for worker temp files

# Environment variables
raw_env = [
    f'FLASK_ENV={os.environ.get("FLASK_ENV", "production")}',
    f'SECRET_KEY={os.environ.get("SECRET_KEY", "change-me-in-production")}',
]

# Graceful timeout for worker restarts
graceful_timeout = 30

# Enable worker recycling
reload = os.environ.get('RELOAD', 'false').lower() == 'true'
