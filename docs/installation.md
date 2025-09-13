# Installation Guide

## 📋 Prerequisites

### System Requirements
- **Operating System**: macOS, Linux, or Windows
- **Python**: Version 3.6 or higher
- **Web Browser**: Modern browser (Chrome, Firefox, Safari, Edge)
- **Internet Connection**: Required for curl commands and web fetching

### Python Dependencies
- **Flask**: Web framework for the server version
- **Flask-CORS**: Cross-origin resource sharing support
- **Werkzeug**: WSGI toolkit

## 🚀 Installation Options

### Option 1: Standalone Version (Recommended for Beginners)

**No installation required!** Simply download and open the HTML file.

```bash
# Download the file
wget https://raw.githubusercontent.com/your-repo/Extendipede/main/extendipede_standalone.html

# Open in browser
open extendipede_standalone.html
# or double-click the file
```

**Advantages:**
- No server setup required
- Works offline
- Safe for demonstrations
- Easy to share

### Option 2: Flask Server Version (Full Features)

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/Extendipede.git
cd Extendipede
```

#### Step 2: Install Dependencies
```bash
# Using pip
pip install -r requirements.txt

# Or using pip3
pip3 install -r requirements.txt

# Or using virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Step 3: Run the Application
```bash
# Start the server
python3 app.py

# The server will start on http://localhost:8000
```

#### Step 4: Open in Browser
```bash
# Open the application
open http://localhost:8000
# or navigate to http://localhost:8000 in your browser
```

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set custom port
export EXTENDIPEDE_PORT=8080

# Optional: Set custom host
export EXTENDIPEDE_HOST=0.0.0.0
```

### Custom Configuration
Edit `app.py` to modify:
- **Port**: Change the default port (8000)
- **Host**: Change the host address
- **Allowed Commands**: Modify the command whitelist
- **Timeout**: Adjust command execution timeout

## 🐳 Docker Installation (Optional)

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "app.py"]
```

### Build and Run
```bash
# Build the image
docker build -t extendipede .

# Run the container
docker run -p 8000:8000 extendipede
```

## 🔒 Security Considerations

### Command Whitelist
The Flask version includes security measures:
- Only pre-approved commands can execute
- Commands timeout after 30 seconds
- Safe error handling
- CORS protection

### Adding New Commands
To add new commands, edit the `ALLOWED_COMMANDS` dictionary in `app.py`:

```python
ALLOWED_COMMANDS = {
    'your_command': ['your_command', 'arg1', 'arg2'],
    # ... existing commands
}
```

### Production Deployment
For production use:
- Use a production WSGI server (Gunicorn, uWSGI)
- Implement proper authentication
- Use HTTPS
- Set up proper logging
- Monitor system resources

## 🚨 Troubleshooting

### Common Installation Issues

#### Python Not Found
```bash
# Install Python
# macOS
brew install python3

# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Windows
# Download from python.org
```

#### Permission Denied
```bash
# Fix permissions
chmod +x app.py

# Or use sudo (not recommended)
sudo python3 app.py
```

#### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use a different port
python3 app.py --port 8080
```

#### Dependencies Not Found
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Or use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Browser Issues

#### JavaScript Disabled
- Enable JavaScript in your browser
- Check browser console for errors
- Try a different browser

#### Files Not Loading
- Check file permissions
- Ensure all files are in correct directories
- Verify Flask server is running

## 📱 Mobile Installation

### iOS
1. Open Safari
2. Navigate to the standalone HTML file
3. Add to Home Screen
4. Use as a web app

### Android
1. Open Chrome
2. Navigate to the standalone HTML file
3. Add to Home Screen
4. Use as a web app

## 🔄 Updates

### Updating the Application
```bash
# Pull latest changes
git pull origin main

# Reinstall dependencies if needed
pip install -r requirements.txt

# Restart the server
python3 app.py
```

### Version Checking
```bash
# Check current version
git log --oneline -1

# Check for updates
git fetch origin
git log HEAD..origin/main --oneline
```

## 📊 Performance Optimization

### For Large Deployments
- Use a production WSGI server
- Implement caching
- Use a reverse proxy (Nginx)
- Monitor system resources

### For Development
- Use virtual environments
- Enable debug mode
- Use hot reloading
- Monitor memory usage

## 🎯 Next Steps

After installation:
1. **Read the Usage Guide**: Check `docs/usage.md`
2. **Try Demo Commands**: Use the built-in examples
3. **Experiment**: Try different pipeline configurations
4. **Explore**: Test various curl commands
5. **Customize**: Modify settings for your needs

## 📞 Support

### Getting Help
- **Documentation**: Check the docs folder
- **GitHub Issues**: Report problems on GitHub
- **Community**: Join discussions
- **Examples**: Try the demo commands

### Contributing
- **Bug Reports**: Help improve the application
- **Feature Requests**: Suggest new features
- **Code Contributions**: Submit pull requests
- **Documentation**: Help improve guides

---

**Installation complete!** 🎉

You're ready to start using Extendipede Web. Check the usage guide for detailed instructions on how to use the application.
