# Extendipede Web

A web-based version of the Extendipede command pipeline simulator. This application visualizes how commands flow through a pipeline with animated LED states synchronized to an AC signal.

## Features

- **Interactive Pipeline Visualization**: See commands flow through configurable pipeline stages
- **Real-time AC Signal Display**: Watch the AC voltage waveform that controls the pipeline
- **Command Execution**: Execute real shell commands (with security restrictions)
- **Configurable Parameters**: Adjust pipeline states, frequency, animation speed, and more
- **Modern Web UI**: Beautiful, responsive interface with dark theme
- **Demo Commands**: Quick access to common commands for testing

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Open in Browser**:
   Navigate to `http://localhost:5000`

## Usage

### Basic Operation

1. **Configure Parameters**:
   - Set the number of pipeline states (default: 100)
   - Adjust AC frequency in Hz (default: 60)
   - Modify steps per cycle (default: 40)
   - Change animation speed in milliseconds (default: 50)

2. **Execute Commands**:
   - Type commands in the input field
   - Click "Run" or press Enter
   - Watch the command flow through the pipeline
   - View the output when the command completes

3. **Demo Commands**:
   - Use the demo buttons for quick testing
   - Try: `ls`, `pwd`, `date`, `whoami`, `echo Hello Extendipede!`

### How It Works

The Extendipede simulator creates a visual representation of a command pipeline:

- **AC Signal**: A sine wave controls the pipeline behavior
- **Positive Half-Cycle**: Commands advance through pipeline stages
- **Negative Half-Cycle**: Pipeline stages reset
- **LED States**: Each stage shows active (●) or inactive (○) states
- **Command Flow**: Commands "travel" through the pipeline stages
- **Output**: Results appear when commands exit the final stage

### Security

The web application includes security measures:

- **Command Whitelist**: Only pre-approved commands can be executed
- **Timeout Protection**: Commands timeout after 30 seconds
- **Error Handling**: Safe error reporting without system exposure
- **CORS Support**: Cross-origin requests properly handled

### Allowed Commands

The application supports a wide range of common Unix/Linux commands including:

- File operations: `ls`, `cat`, `head`, `tail`, `grep`, `find`
- System info: `ps`, `top`, `df`, `free`, `uname`, `uptime`
- Text processing: `awk`, `sed`, `sort`, `uniq`, `cut`, `wc`
- Network: `ping`, `curl`, `wget`, `netstat`, `ss`
- Development: `git`, `python`, `node`, `npm`, `pip`
- And many more...

## File Structure

```
Extendipede/
├── app.py              # Flask backend server
├── requirements.txt    # Python dependencies
├── Extendipede.py      # Original terminal version
├── templates/
│   └── index.html      # Main web page
├── static/
│   ├── style.css       # Styling
│   └── script.js       # Frontend JavaScript
└── README.md           # This file
```

## Development

### Backend (Flask)
- `app.py`: Main Flask application with API endpoints
- `/api/execute`: Execute commands via POST request
- `/api/allowed-commands`: Get list of allowed commands
- `/api/status`: Server status information

### Frontend (JavaScript)
- `script.js`: Main application logic and animation
- Real-time pipeline visualization
- AC signal simulation
- Command execution and result display

### Styling (CSS)
- `style.css`: Modern dark theme with animations
- Responsive design for different screen sizes
- Smooth transitions and visual effects

## Customization

### Adding New Commands
Edit the `ALLOWED_COMMANDS` dictionary in `app.py` to add new commands:

```python
ALLOWED_COMMANDS = {
    'your_command': ['your_command', 'arg1', 'arg2'],
    # ... existing commands
}
```

### Modifying Animation
Adjust animation parameters in `script.js`:

```javascript
// Change default values
this.numStates = 50;        // Fewer pipeline stages
this.frequency = 30;        // Slower frequency
this.sleepTime = 100;        // Slower animation
```

### Styling Changes
Modify `style.css` to change colors, fonts, or layout:

```css
:root {
    --primary-color: #00ff88;    /* Change LED color */
    --bg-gradient: #1a1a2e;      /* Change background */
}
```

## Troubleshooting

### Common Issues

1. **Commands Not Executing**:
   - Check if command is in the allowed list
   - Verify Flask server is running
   - Check browser console for errors

2. **Animation Not Working**:
   - Ensure JavaScript is enabled
   - Check for browser compatibility
   - Verify all files are loaded correctly

3. **Server Won't Start**:
   - Install dependencies: `pip install -r requirements.txt`
   - Check if port 5000 is available
   - Verify Python version compatibility

### Browser Compatibility

- Chrome/Chromium: Full support
- Firefox: Full support
- Safari: Full support
- Edge: Full support
- Internet Explorer: Not supported

## License

This project is open source. Feel free to modify and distribute according to your needs.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

---

**Enjoy exploring the Extendipede pipeline simulator!** 🚀
