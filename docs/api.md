# API Reference

## 🌐 Overview

The Extendipede Web API provides endpoints for command execution, status checking, and configuration management. The API is built with Flask and supports JSON responses.

## 🔗 Base URL

```
http://localhost:8000
```

## 📋 Endpoints

### 1. Execute Command

Execute a shell command and return the output.

**Endpoint:** `POST /api/execute`

**Request Body:**
```json
{
  "command": "ls -la"
}
```

**Response:**
```json
{
  "success": true,
  "output": "total 24\ndrwxr-xr-x  5 user  staff  160 Sep 12 22:00 .\ndrwxr-xr-x  3 user  staff  96 Sep 12 21:45 ..",
  "error": null
}
```

**Error Response:**
```json
{
  "success": false,
  "output": "Command 'invalid_command' is not allowed for security reasons.",
  "error": "Command not in allowed list"
}
```

**Example Usage:**
```bash
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "curl -s https://httpbin.org/json"}'
```

### 2. Get Allowed Commands

Retrieve the list of allowed commands.

**Endpoint:** `GET /api/allowed-commands`

**Response:**
```json
{
  "commands": [
    "ls",
    "pwd",
    "date",
    "whoami",
    "curl",
    "wget",
    "grep",
    "find",
    "ps",
    "top"
  ],
  "count": 81
}
```

**Example Usage:**
```bash
curl http://localhost:8000/api/allowed-commands
```

### 3. Server Status

Get the current server status and configuration.

**Endpoint:** `GET /api/status`

**Response:**
```json
{
  "status": "running",
  "allowed_commands": 81,
  "current_directory": "/Users/alexanderfox/Projects/Extendipede"
}
```

**Example Usage:**
```bash
curl http://localhost:8000/api/status
```

## 🔒 Security

### Command Whitelist

Only commands in the whitelist can be executed. The whitelist includes:

#### File Operations
- `ls`, `pwd`, `cd`, `mkdir`, `rmdir`
- `cat`, `head`, `tail`, `less`, `more`
- `cp`, `mv`, `rm`, `touch`
- `chmod`, `chown`, `ln`

#### System Information
- `ps`, `top`, `htop`
- `df`, `free`, `du`
- `uname`, `uptime`, `whoami`
- `env`, `history`

#### Text Processing
- `grep`, `awk`, `sed`
- `sort`, `uniq`, `cut`
- `wc`, `tr`, `xargs`

#### Network Operations
- `curl`, `wget`
- `ping`, `netstat`, `ss`
- `ssh`, `scp`, `rsync`

#### Development Tools
- `git`, `python`, `python3`
- `node`, `npm`, `pip`, `pip3`
- `vim`, `nano`, `emacs`

### Timeout Protection

Commands are automatically terminated after 30 seconds to prevent hanging processes.

### Error Handling

All errors are safely captured and returned without exposing system internals.

## 📝 Request Examples

### Basic Commands

```bash
# List files
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "ls -la"}'

# Show current directory
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "pwd"}'

# Display date
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "date"}'
```

### Website Fetching

```bash
# Fetch JSON data
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "curl -s https://httpbin.org/json"}'

# Get GitHub API info
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "curl -s https://api.github.com"}'

# Fetch blog post
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "curl -s https://jsonplaceholder.typicode.com/posts/1"}'
```

### System Information

```bash
# Process list
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "ps aux"}'

# Disk usage
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "df -h"}'

# Memory usage
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "free -h"}'
```

### Text Processing

```bash
# Search for patterns
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "grep -r \"pattern\" ."}'

# Count lines
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "wc -l file.txt"}'

# Sort data
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "sort file.txt"}'
```

## 🔧 Response Format

### Success Response
```json
{
  "success": true,
  "output": "Command output here",
  "error": null
}
```

### Error Response
```json
{
  "success": false,
  "output": "Error message here",
  "error": "Error type or details"
}
```

### Field Descriptions

- **success**: Boolean indicating if command executed successfully
- **output**: String containing command output or error message
- **error**: String containing error details (null on success)

## 🚨 Error Codes

### Common Error Types

#### Command Not Allowed
```json
{
  "success": false,
  "output": "Command 'invalid_command' is not allowed for security reasons.",
  "error": "Command not in allowed list"
}
```

#### Command Timeout
```json
{
  "success": false,
  "output": "Command timed out after 30 seconds",
  "error": "Timeout"
}
```

#### Command Execution Error
```json
{
  "success": false,
  "output": "Command failed with return code 1",
  "error": "Command failed with return code 1"
}
```

#### Server Error
```json
{
  "success": false,
  "output": "Server error: Internal server error",
  "error": "Internal server error"
}
```

## 🔄 Rate Limiting

Currently, there are no rate limits implemented. For production use, consider implementing:

- Request rate limiting
- Command execution throttling
- Resource usage monitoring

## 📊 Monitoring

### Health Checks

Use the status endpoint to monitor server health:

```bash
# Check server status
curl http://localhost:8000/api/status

# Expected response
{
  "status": "running",
  "allowed_commands": 81,
  "current_directory": "/path/to/extendipede"
}
```

### Logging

The Flask server logs all requests and command executions. Check the console output for:

- Request logs
- Command execution logs
- Error logs
- Performance metrics

## 🛠️ Customization

### Adding New Commands

Edit the `ALLOWED_COMMANDS` dictionary in `app.py`:

```python
ALLOWED_COMMANDS = {
    'your_command': ['your_command', 'arg1', 'arg2'],
    'another_command': ['another_command'],
    # ... existing commands
}
```

### Modifying Timeout

Change the timeout value in the `execute_command` function:

```python
result = subprocess.run(
    command_parts,
    capture_output=True,
    text=True,
    timeout=60,  # Change from 30 to 60 seconds
    cwd=os.getcwd()
)
```

### Custom Error Handling

Modify the error handling in the `execute_command` function:

```python
except subprocess.TimeoutExpired:
    return {
        'success': False,
        'output': 'Command timed out after 60 seconds',  # Custom message
        'error': 'Timeout'
    }
```

## 🔐 Security Best Practices

### Production Deployment

1. **Use HTTPS**: Encrypt all API communications
2. **Implement Authentication**: Add API key or token authentication
3. **Rate Limiting**: Prevent abuse with request limits
4. **Input Validation**: Validate all command inputs
5. **Logging**: Log all API requests and responses
6. **Monitoring**: Monitor API usage and performance

### Command Validation

Always validate commands before execution:

```python
def validate_command(command):
    # Check if command is in whitelist
    if not is_command_allowed(command):
        return False
    
    # Check for dangerous patterns
    dangerous_patterns = ['rm -rf', 'sudo', 'su -']
    for pattern in dangerous_patterns:
        if pattern in command:
            return False
    
    return True
```

## 📚 SDK Examples

### Python SDK

```python
import requests

class ExtendipedeClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
    
    def execute_command(self, command):
        response = requests.post(
            f"{self.base_url}/api/execute",
            json={"command": command}
        )
        return response.json()
    
    def get_status(self):
        response = requests.get(f"{self.base_url}/api/status")
        return response.json()

# Usage
client = ExtendipedeClient()
result = client.execute_command("ls -la")
print(result)
```

### JavaScript SDK

```javascript
class ExtendipedeClient {
    constructor(baseUrl = 'http://localhost:8000') {
        this.baseUrl = baseUrl;
    }
    
    async executeCommand(command) {
        const response = await fetch(`${this.baseUrl}/api/execute`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ command })
        });
        return await response.json();
    }
    
    async getStatus() {
        const response = await fetch(`${this.baseUrl}/api/status`);
        return await response.json();
    }
}

// Usage
const client = new ExtendipedeClient();
const result = await client.executeCommand('ls -la');
console.log(result);
```

## 🎯 Use Cases

### Automation Scripts

```bash
#!/bin/bash
# Automated testing script

# Test basic commands
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "ls -la"}' | jq '.success'

# Test website fetching
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "curl -s https://httpbin.org/json"}' | jq '.output'
```

### Monitoring Integration

```python
# Monitor system health
import requests
import time

def monitor_system():
    client = ExtendipedeClient()
    
    while True:
        # Check disk usage
        result = client.execute_command("df -h")
        if result['success']:
            print(f"Disk usage: {result['output']}")
        
        # Check memory usage
        result = client.execute_command("free -h")
        if result['success']:
            print(f"Memory usage: {result['output']}")
        
        time.sleep(60)  # Check every minute

monitor_system()
```

---

**API Reference Complete!** 🚀

Use this reference to integrate Extendipede Web into your applications, scripts, and monitoring systems.
