# Examples & Use Cases

## 🎯 Quick Start Examples

### Basic System Commands
```bash
# List files and directories
ls -la

# Show current working directory
pwd

# Display current date and time
date

# Show current user
whoami

# System information
uname -a

# System uptime
uptime
```

### Website Fetching with Curl
```bash
# Fetch JSON data from APIs
curl -s https://httpbin.org/json
curl -s https://api.github.com
curl -s https://jsonplaceholder.typicode.com/posts/1

# Get website content
curl -s https://example.com
curl -s https://github.com
curl -s https://stackoverflow.com

# Fetch headers only
curl -I https://example.com

# Follow redirects
curl -L https://example.com
```

## 🌐 Web Development Examples

### API Testing
```bash
# Test REST API endpoints
curl -X GET https://jsonplaceholder.typicode.com/posts
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Post", "body": "Test content", "userId": 1}'

# Test GitHub API
curl -s https://api.github.com/repos/microsoft/vscode
curl -s https://api.github.com/users/octocat

# Test weather API
curl -s "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"
```

### Data Processing
```bash
# Fetch and process JSON
curl -s https://jsonplaceholder.typicode.com/posts | jq '.[0:5]'
curl -s https://api.github.com/repos/microsoft/vscode | jq '.name'

# Extract specific fields
curl -s https://jsonplaceholder.typicode.com/users/1 | jq '.name'
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq '.title'

# Filter and transform data
curl -s https://jsonplaceholder.typicode.com/posts | jq '.[] | select(.userId == 1)'
curl -s https://jsonplaceholder.typicode.com/users | jq '.[] | {name: .name, email: .email}'
```

### Website Monitoring
```bash
# Check website status
curl -I https://example.com
curl -I https://github.com
curl -I https://stackoverflow.com

# Monitor response times
curl -w "@curl-format.txt" -o /dev/null -s https://example.com

# Check SSL certificate
curl -I https://example.com 2>&1 | grep -i "ssl\|tls"
```

## 🔧 System Administration Examples

### System Information
```bash
# Process information
ps aux
ps aux | grep python
top -n 1

# Memory usage
free -h
cat /proc/meminfo

# Disk usage
df -h
du -sh *
du -h --max-depth=1

# Network information
netstat -an
ss -tuln
ifconfig
ip addr show
```

### File Operations
```bash
# File listing and searching
ls -la
find . -name "*.py"
find . -type f -size +100M
grep -r "pattern" .
grep -r "import" . --include="*.py"

# File manipulation
cat file.txt
head -20 file.txt
tail -f logfile.log
wc -l file.txt
sort file.txt
uniq file.txt
```

### Log Analysis
```bash
# System logs
tail -f /var/log/syslog
tail -f /var/log/auth.log
grep "ERROR" /var/log/syslog
grep "Failed" /var/log/auth.log

# Application logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
grep "404" /var/log/nginx/access.log
```

## 📊 Data Analysis Examples

### Text Processing
```bash
# Count occurrences
grep -c "pattern" file.txt
awk '{count[$1]++} END {for (word in count) print word, count[word]}' file.txt

# Extract data
awk '{print $1, $3}' file.txt
cut -d',' -f1,3 data.csv
sed 's/old/new/g' file.txt

# Sort and filter
sort file.txt
sort -nr file.txt
uniq file.txt
sort file.txt | uniq -c
```

### Data Extraction
```bash
# Extract URLs from text
grep -o 'https://[^[:space:]]*' file.txt
grep -o 'http://[^[:space:]]*' file.txt

# Extract email addresses
grep -o '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' file.txt

# Extract phone numbers
grep -o '[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}' file.txt
```

### JSON Processing
```bash
# Parse JSON data
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
curl -s https://api.github.com/repos/microsoft/vscode | jq '.name, .description'

# Filter JSON data
curl -s https://jsonplaceholder.typicode.com/posts | jq '.[] | select(.userId == 1)'
curl -s https://jsonplaceholder.typicode.com/users | jq '.[] | {name: .name, email: .email}'

# Transform JSON data
curl -s https://jsonplaceholder.typicode.com/posts | jq '.[] | {id: .id, title: .title}'
```

## 🚀 DevOps Examples

### Deployment Monitoring
```bash
# Check service status
systemctl status nginx
systemctl status apache2
systemctl status docker

# Check running containers
docker ps
docker ps -a
docker images

# Check system resources
htop
iotop
nethogs
```

### Configuration Management
```bash
# Check configuration files
cat /etc/nginx/nginx.conf
cat /etc/apache2/apache2.conf
cat /etc/docker/daemon.json

# Validate configurations
nginx -t
apache2ctl configtest
docker info
```

### Backup and Recovery
```bash
# Create backups
tar -czf backup.tar.gz /path/to/data
rsync -av /source/ /destination/
dd if=/dev/sda of=/dev/sdb bs=4M

# Check backup integrity
tar -tzf backup.tar.gz
md5sum backup.tar.gz
```

## 🔍 Security Examples

### Security Scanning
```bash
# Check open ports
nmap -sT localhost
nmap -sU localhost
netstat -tuln

# Check file permissions
ls -la /etc/passwd
ls -la /etc/shadow
find / -perm -4000 2>/dev/null

# Check system integrity
rpm -Va
debsums -c
aide --check
```

### Network Security
```bash
# Check network connections
netstat -an | grep ESTABLISHED
ss -tuln | grep LISTEN
lsof -i :80
lsof -i :443

# Monitor network traffic
tcpdump -i eth0
tcpdump -i eth0 port 80
tcpdump -i eth0 host 192.168.1.1
```

## 📱 Mobile Development Examples

### API Testing for Mobile Apps
```bash
# Test mobile API endpoints
curl -X GET https://api.example.com/mobile/users
curl -X POST https://api.example.com/mobile/auth \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "pass"}'

# Test push notifications
curl -X POST https://api.example.com/push/send \
  -H "Content-Type: application/json" \
  -d '{"device_id": "123", "message": "Hello"}'
```

### Performance Testing
```bash
# Load testing
curl -w "@curl-format.txt" -o /dev/null -s https://api.example.com
ab -n 1000 -c 10 https://api.example.com
wrk -t12 -c400 -d30s https://api.example.com

# Response time testing
curl -w "Time: %{time_total}s\n" -o /dev/null -s https://api.example.com
```

## 🎨 Creative Examples

### Data Visualization
```bash
# Generate data for visualization
curl -s https://jsonplaceholder.typicode.com/posts | jq '.[] | {id: .id, userId: .userId}' > data.json
curl -s https://api.github.com/repos/microsoft/vscode | jq '{name: .name, stars: .stargazers_count, forks: .forks_count}'

# Create charts
curl -s https://jsonplaceholder.typicode.com/posts | jq '.[] | .userId' | sort | uniq -c
```

### Art and Music
```bash
# Generate random data for art
curl -s https://httpbin.org/uuid
curl -s https://api.github.com/repos/microsoft/vscode | jq '.name' | tr '[:upper:]' '[:lower:]'

# Create patterns
for i in {1..10}; do echo "Pattern $i"; done
seq 1 10 | awk '{print "Line " $1}'
```

## 🔬 Scientific Examples

### Data Collection
```bash
# Collect scientific data
curl -s https://api.example.com/sensors/temperature
curl -s https://api.example.com/sensors/humidity
curl -s https://api.example.com/sensors/pressure

# Process scientific data
curl -s https://api.example.com/data | jq '.[] | select(.temperature > 25)'
curl -s https://api.example.com/data | jq '.[] | {time: .timestamp, value: .measurement}'
```

### Research Data
```bash
# Fetch research data
curl -s https://api.example.com/research/papers
curl -s https://api.example.com/research/citations
curl -s https://api.example.com/research/authors

# Analyze research data
curl -s https://api.example.com/research/papers | jq '.[] | {title: .title, citations: .citation_count}'
```

## 🎯 Real-World Use Cases

### E-commerce Monitoring
```bash
# Monitor product availability
curl -s https://api.example.com/products/123
curl -s https://api.example.com/inventory/123

# Check order status
curl -s https://api.example.com/orders/456
curl -s https://api.example.com/shipping/456
```

### Social Media Analytics
```bash
# Fetch social media data
curl -s https://api.twitter.com/1.1/statuses/user_timeline.json
curl -s https://api.facebook.com/v1.0/me/posts

# Analyze engagement
curl -s https://api.example.com/posts/123 | jq '{likes: .likes, shares: .shares, comments: .comments}'
```

### IoT Device Management
```bash
# Monitor IoT devices
curl -s https://api.example.com/devices
curl -s https://api.example.com/devices/123/status

# Control IoT devices
curl -X POST https://api.example.com/devices/123/control \
  -H "Content-Type: application/json" \
  -d '{"action": "turn_on", "value": true}'
```

## 🚀 Advanced Examples

### Automation Scripts
```bash
#!/bin/bash
# Automated system monitoring

# Check system health
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "df -h"}' | jq '.output'

# Monitor website status
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "curl -I https://example.com"}' | jq '.output'

# Check system processes
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "ps aux | grep python"}' | jq '.output'
```

### Integration Examples
```python
# Python integration
import requests
import json

def monitor_system():
    base_url = "http://localhost:8000"
    
    # Check disk usage
    response = requests.post(f"{base_url}/api/execute", 
                           json={"command": "df -h"})
    if response.json()['success']:
        print(f"Disk usage: {response.json()['output']}")
    
    # Check memory usage
    response = requests.post(f"{base_url}/api/execute", 
                           json={"command": "free -h"})
    if response.json()['success']:
        print(f"Memory usage: {response.json()['output']}")

monitor_system()
```

---

**Examples Complete!** 🎉

These examples demonstrate the versatility of Extendipede Web for various use cases, from basic system administration to advanced automation and integration scenarios.
