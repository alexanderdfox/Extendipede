# Troubleshooting Guide

## Common Issues and Solutions

### 1. "Error: undefined" in Browser Console

**Problem**: JavaScript shows "Error: undefined" when trying to execute commands.

**Solution**: 
- The application requires authentication
- A login modal should appear automatically
- Use credentials: `admin` / `extendipede2024`
- If modal doesn't appear, refresh the page

**Root Cause**: Authentication is required for command execution in production mode.

### 2. Static Files Not Loading (404 Errors)

**Problem**: CSS and JavaScript files return 404 errors.

**Symptoms**:
```
GET /style.css HTTP/1.1" 404 -
GET /script.js HTTP/1.1" 404 -
```

**Solution**:
- Ensure Flask app is configured with `static_folder='static'`
- Check that files exist in `static/` directory
- Verify template uses `url_for('static', filename='...')`
- Restart the Flask application

### 3. Docker Container Won't Start

**Problem**: Docker containers fail to start or exit immediately.

**Common Causes**:
- Port conflicts (8000, 6379, 80, 443)
- Missing environment variables
- Redis connection issues
- SSL certificate problems

**Solutions**:
```bash
# Check if ports are in use
lsof -i :8000
lsof -i :6379
lsof -i :80
lsof -i :443

# Stop conflicting services
sudo lsof -ti:8000 | xargs kill -9

# Rebuild containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### 4. Authentication Issues

**Problem**: Cannot login or authentication fails.

**Solutions**:
- Check credentials: `admin` / `extendipede2024`
- Verify Redis is running: `docker-compose ps`
- Check authentication endpoint: `curl -k https://localhost/auth/status`
- Clear browser cookies and try again

### 5. Rate Limiting Errors

**Problem**: "Too Many Requests" error when executing commands.

**Solution**:
- Wait 1 minute before retrying
- Check Redis connection: `docker-compose logs redis`
- Restart Redis if needed: `docker-compose restart redis`

### 6. SSL Certificate Warnings

**Problem**: Browser shows "Not Secure" or certificate warnings.

**Solution**:
- This is expected with self-signed certificates
- Click "Advanced" → "Proceed to localhost"
- For production, use proper SSL certificates

### 7. Command Execution Failures

**Problem**: Commands fail to execute or return errors.

**Common Causes**:
- Command not in allowed list
- Command too long (>1000 characters)
- Dangerous patterns detected
- Command timeout (>30 seconds)

**Solutions**:
- Check allowed commands: `curl -k https://localhost/api/allowed-commands`
- Use shorter commands
- Avoid dangerous patterns like `rm -rf`, `sudo`, etc.
- Check command syntax

### 8. Performance Issues

**Problem**: Application is slow or unresponsive.

**Solutions**:
- Check system resources: `docker stats`
- Monitor logs: `docker-compose logs -f`
- Restart containers: `docker-compose restart`
- Check Redis memory usage

### 9. Log Analysis

**View Application Logs**:
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f extendipede
docker-compose logs -f nginx
docker-compose logs -f redis

# Last 100 lines
docker-compose logs --tail=100 extendipede
```

**Log Locations**:
- Application logs: `logs/app.log`
- Access logs: `logs/access.log`
- Error logs: `logs/error.log`
- Nginx logs: Docker container logs

### 10. Health Check Failures

**Problem**: Health checks fail or return errors.

**Check Health Status**:
```bash
# Application health
curl -k https://localhost/health

# Metrics
curl -k https://localhost/metrics

# Status
curl -k https://localhost/api/status
```

**Solutions**:
- Restart application: `docker-compose restart extendipede`
- Check Redis connection
- Verify all services are running: `docker-compose ps`

## Debugging Commands

### Check Service Status
```bash
docker-compose ps
docker-compose logs --tail=50
```

### Test Endpoints
```bash
# Health check
curl -k https://localhost/health

# Authentication status
curl -k https://localhost/auth/status

# Login test
curl -k -X POST https://localhost/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "extendipede2024"}'

# Command execution test
curl -k -X POST https://localhost/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "echo hello"}' \
  -b cookies.txt
```

### Reset Everything
```bash
# Stop all services
docker-compose down

# Remove volumes (WARNING: This will delete all data)
docker-compose down -v

# Rebuild and restart
docker-compose build --no-cache
docker-compose up -d
```

## Getting Help

If you're still experiencing issues:

1. **Check the logs** for specific error messages
2. **Verify system requirements** (Docker, Python 3.11+)
3. **Test with minimal configuration** (development mode)
4. **Check network connectivity** and firewall settings
5. **Review the installation guide** for proper setup

## Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `Connection refused` | Service not running | Start Docker services |
| `Permission denied` | File permissions | Check file ownership |
| `Port already in use` | Port conflict | Stop conflicting service |
| `Module not found` | Missing dependency | Install requirements |
| `Authentication failed` | Wrong credentials | Use `admin`/`extendipede2024` |
| `Rate limit exceeded` | Too many requests | Wait 1 minute |
| `Command not allowed` | Security restriction | Use allowed commands only |
