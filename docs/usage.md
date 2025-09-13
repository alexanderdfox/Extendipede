# Extendipede Web - Usage Guide

## 🌐 Overview

Extendipede Web is a modern web-based command pipeline simulator that visualizes how commands flow through pipeline stages with animated LED states synchronized to an AC signal. It's perfect for learning, debugging, monitoring, and visualizing command execution processes.

## 🚀 Quick Start

### Option 1: Standalone Version (No Server Required)
```bash
# Simply open the HTML file in any web browser
open extendipede_standalone.html
# or double-click the file
```

### Option 2: Flask Server Version (Real Command Execution)
```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python3 app.py

# Open browser to: http://localhost:8000
```

## 🎯 Core Features

### Pipeline Visualization
- **Animated LED States**: Watch commands flow through configurable pipeline stages
- **AC Signal Control**: Real-time sine wave voltage display controls pipeline timing
- **Stage-by-Stage Progress**: See commands advance through each pipeline stage
- **Visual Feedback**: Active (●) and inactive (○) LED states with smooth animations

### Interactive Controls
- **Pipeline States**: Adjust number of stages (1-200)
- **AC Frequency**: Control pipeline speed (0.1-1000 Hz)
- **Animation Speed**: Modify display refresh rate (10-500ms)
- **Steps per Cycle**: Fine-tune pipeline granularity (10-100)

### Command Execution
- **Real Commands**: Execute actual shell commands (Flask version)
- **Simulated Commands**: Safe demonstration mode (Standalone version)
- **Security**: Whitelist of allowed commands for safe execution
- **Output Display**: View command results when they complete

## 📋 Basic Usage

### 1. Configure Parameters
Adjust the pipeline settings in the controls section:
- **Pipeline States**: More stages = longer visualization
- **AC Frequency**: Higher frequency = faster pipeline
- **Animation Speed**: Lower values = smoother animation
- **Steps per Cycle**: More steps = finer control

### 2. Execute Commands
Enter commands in the input field:
```bash
# Basic system commands
ls
pwd
date
whoami

# Echo commands
echo Hello World
echo "This is a test"

# Website fetching with curl
curl -s https://httpbin.org/json
curl -s https://api.github.com
curl -s https://jsonplaceholder.typicode.com/posts/1
```

### 3. Watch the Animation
- Commands flow through pipeline stages
- LED states pulse and animate
- AC voltage controls timing
- Output appears when complete

## 🌐 Website Fetching Examples

### API Endpoints
```bash
# JSON APIs
curl -s https://httpbin.org/json
curl -s https://jsonplaceholder.typicode.com/posts/1
curl -s https://api.github.com

# Weather APIs
curl -s "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY"

# News APIs
curl -s https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_KEY
```

### Website Content
```bash
# Fetch HTML content
curl -s https://example.com
curl -s https://github.com
curl -s https://stackoverflow.com

# Get headers only
curl -I https://example.com

# Follow redirects
curl -L https://example.com
```

### Data Processing
```bash
# Fetch and process JSON
curl -s https://api.github.com/repos/microsoft/vscode | jq '.name'

# Get specific data
curl -s https://jsonplaceholder.typicode.com/users/1 | jq '.name'

# Filter results
curl -s https://jsonplaceholder.typicode.com/posts | jq '.[0:5]'
```

## 🔧 Advanced Usage

### Custom Commands
The Flask version supports a wide range of commands:

#### File Operations
```bash
ls -la
find . -name "*.py"
grep -r "pattern" .
cat file.txt
head -20 file.txt
tail -f logfile.log
```

#### System Information
```bash
ps aux
top -n 1
df -h
free -h
uname -a
uptime
```

#### Network Operations
```bash
ping -c 4 google.com
netstat -an
ss -tuln
curl -v https://example.com
wget -O file.html https://example.com
```

#### Text Processing
```bash
awk '{print $1}' file.txt
sed 's/old/new/g' file.txt
sort file.txt
uniq file.txt
cut -d',' -f1 data.csv
```

### Pipeline Customization

#### For Learning
- **Fewer Stages (10-20)**: Easier to follow
- **Lower Frequency (10-30 Hz)**: Slower, more visible
- **Higher Animation Speed (100-200ms)**: Smoother for beginners

#### For Monitoring
- **More Stages (100-200)**: Longer visualization
- **Higher Frequency (60-120 Hz)**: Faster processing
- **Lower Animation Speed (25-50ms)**: Real-time feel

#### For Demos
- **Medium Stages (50-100)**: Good balance
- **Standard Frequency (60 Hz)**: Natural feel
- **Medium Animation Speed (50-100ms)**: Engaging but not overwhelming

## 🎨 Visual Customization

### Understanding the Display
- **AC Voltage**: Shows the sine wave controlling pipeline timing
- **Current Command**: Displays the command being processed
- **Pipeline Stages**: Visual representation of command flow
- **LED States**: Active (●) and inactive (○) indicators
- **Command Output**: Results appear when processing completes

### Animation Behavior
- **Positive AC Cycle**: Commands advance through stages
- **Negative AC Cycle**: Stages reset, preparing for next cycle
- **LED Pulsing**: Active stages pulse with green glow
- **Smooth Transitions**: Fluid movement between states

## 🔒 Security Features

### Command Whitelist
The Flask version includes security measures:
- **Allowed Commands**: Only pre-approved commands can execute
- **Timeout Protection**: Commands timeout after 30 seconds
- **Error Handling**: Safe error reporting without system exposure
- **CORS Support**: Proper cross-origin request handling

### Safe Commands
Common allowed commands include:
- File operations: `ls`, `cat`, `head`, `tail`, `grep`, `find`
- System info: `ps`, `top`, `df`, `free`, `uname`, `uptime`
- Text processing: `awk`, `sed`, `sort`, `uniq`, `cut`, `wc`
- Network: `ping`, `curl`, `wget`, `netstat`, `ss`
- Development: `git`, `python`, `node`, `npm`, `pip`

## 🚨 Troubleshooting

### Common Issues

#### Commands Not Executing
- **Check Whitelist**: Ensure command is in allowed list
- **Verify Server**: Flask server must be running
- **Check Console**: Look for JavaScript errors
- **Network Issues**: Ensure internet connection for curl commands

#### Animation Problems
- **JavaScript Disabled**: Enable JavaScript in browser
- **Browser Compatibility**: Use modern browsers (Chrome, Firefox, Safari, Edge)
- **File Loading**: Ensure all files load correctly
- **Performance**: Reduce animation speed if laggy

#### Server Issues
- **Dependencies**: Install requirements.txt
- **Port Conflicts**: Check if port 8000 is available
- **Python Version**: Use Python 3.6+
- **Permissions**: Ensure proper file permissions

### Performance Optimization

#### For Large Outputs
- **Truncate Results**: Use `head` or `tail` to limit output
- **Filter Data**: Use `grep` or `awk` to reduce content
- **Pagination**: Process data in chunks

#### For Smooth Animation
- **Reduce Stages**: Fewer pipeline stages = smoother animation
- **Lower Frequency**: Slower AC frequency = more stable display
- **Increase Animation Speed**: Higher refresh rate = smoother motion

## 📚 Use Cases

### Educational
- **Command Line Learning**: Visualize Unix/Linux commands
- **System Administration**: Understand system processes
- **API Learning**: See web requests flow through
- **Debugging Training**: Learn troubleshooting workflows

### Professional
- **System Monitoring**: Watch system commands execute
- **API Testing**: Test REST endpoints visually
- **DevOps Workflows**: Visualize deployment processes
- **Performance Analysis**: Monitor command execution times

### Creative
- **Algorithm Visualization**: See algorithms execute step-by-step
- **Data Art**: Create visual representations of data flows
- **Interactive Demos**: Impressive technical presentations
- **Performance Art**: Visualize system performance as art

## 🔮 Advanced Features

### Custom Command Integration
```python
# Add new commands to app.py
ALLOWED_COMMANDS = {
    'your_command': ['your_command', 'arg1', 'arg2'],
    # ... existing commands
}
```

### Animation Customization
```javascript
// Modify defaults in script.js
this.numStates = 50;        // Fewer pipeline stages
this.frequency = 30;        // Slower frequency
this.sleepTime = 100;       // Slower animation
```

### Styling Changes
```css
/* Modify colors in style.css */
:root {
    --primary-color: #00ff88;    /* Change LED color */
    --bg-gradient: #1a1a2e;      /* Change background */
}
```

## 📖 Examples

### Basic System Commands
```bash
# List files
ls -la

# Show current directory
pwd

# Display date and time
date

# Show current user
whoami

# System information
uname -a
```

### Web Content Fetching
```bash
# Fetch JSON data
curl -s https://httpbin.org/json

# Get GitHub API info
curl -s https://api.github.com

# Fetch blog post
curl -s https://jsonplaceholder.typicode.com/posts/1

# Get website content
curl -s https://example.com
```

### Data Processing
```bash
# Process JSON
curl -s https://api.github.com/repos/microsoft/vscode | jq '.name'

# Filter data
curl -s https://jsonplaceholder.typicode.com/users | jq '.[0:5]'

# Extract specific fields
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
```

## 🎯 Best Practices

### For Learning
1. Start with simple commands
2. Use fewer pipeline stages initially
3. Watch the AC signal behavior
4. Experiment with different frequencies
5. Try the demo commands first

### For Production Use
1. Use the Flask version for real commands
2. Monitor command execution times
3. Implement proper error handling
4. Use appropriate timeouts
5. Monitor system resources

### For Presentations
1. Use medium pipeline stages (50-100)
2. Set frequency to 60 Hz for natural feel
3. Use demo commands for reliability
4. Prepare example outputs
5. Test beforehand

## 📞 Support

### Getting Help
- **Documentation**: Check this usage guide
- **Examples**: Try the demo commands
- **Troubleshooting**: See troubleshooting section
- **GitHub**: Check the repository for issues

### Contributing
- **Bug Reports**: Report issues on GitHub
- **Feature Requests**: Suggest new features
- **Code Contributions**: Submit pull requests
- **Documentation**: Help improve this guide

---

**Enjoy exploring the Extendipede pipeline simulator!** 🚀

The visual pipeline makes complex technical processes accessible and engaging, turning abstract command execution into something tangible and beautiful.
