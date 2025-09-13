# Development Guide

## Development Setup

### Prerequisites
- Python 3.11 or higher
- Node.js (for frontend development)
- Git
- Docker (optional, for testing)

### Local Development

1. **Clone the repository**:
```bash
git clone https://github.com/alexanderdfox/Extendipede.git
cd Extendipede
```

2. **Create virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**:
```bash
cp env.example .env
# Edit .env with your development settings
```

5. **Run in development mode**:
```bash
python app.py
```

The application will be available at `http://localhost:8000`

## Project Structure

```
Extendipede/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker container definition
├── docker-compose.yml   # Multi-container setup
├── nginx.conf          # Nginx configuration
├── gunicorn.conf.py    # Gunicorn configuration
├── deploy.sh           # Deployment script
├── env.example         # Environment variables template
├── .gitignore         # Git ignore rules
├── README.md          # Project overview
├── static/            # Static files (CSS, JS)
│   ├── style.css
│   └── script.js
├── templates/         # HTML templates
│   └── index.html
├── docs/              # Documentation
│   ├── README.md
│   ├── index.md
│   ├── installation.md
│   ├── usage.md
│   ├── api.md
│   ├── examples.md
│   ├── production.md
│   ├── troubleshooting.md
│   └── development.md
├── logs/              # Application logs
└── ssl/               # SSL certificates
```

## Development Workflow

### 1. Frontend Development

**File**: `static/script.js`
- Main JavaScript application logic
- Handles UI interactions and API calls
- Authentication and command execution

**File**: `static/style.css`
- CSS styling and animations
- Dark theme implementation
- Responsive design

**File**: `templates/index.html`
- HTML structure
- Flask template integration

### 2. Backend Development

**File**: `app.py`
- Flask application setup
- API endpoints
- Authentication and security
- Command execution logic

**File**: `config.py`
- Environment-based configuration
- Development, production, and testing settings

### 3. Testing

**Run tests**:
```bash
# Unit tests (if implemented)
python -m pytest

# Integration tests
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "echo test"}'
```

**Test authentication**:
```bash
# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "extendipede2024"}'

# Check status
curl http://localhost:8000/auth/status
```

### 4. Docker Development

**Build and run**:
```bash
docker-compose up --build
```

**Debug mode**:
```bash
# Run with debug logging
FLASK_ENV=development docker-compose up
```

**Access logs**:
```bash
docker-compose logs -f extendipede
```

## Code Style Guidelines

### Python
- Follow PEP 8 style guide
- Use type hints where appropriate
- Document functions with docstrings
- Use meaningful variable names

### JavaScript
- Use modern ES6+ features
- Follow consistent indentation (2 spaces)
- Use meaningful function and variable names
- Comment complex logic

### CSS
- Use consistent naming conventions
- Group related styles together
- Use CSS custom properties for theming
- Keep selectors specific but not overly complex

## API Development

### Adding New Endpoints

1. **Define route in `app.py`**:
```python
@app.route('/api/new-endpoint', methods=['POST'])
@require_auth
@log_command_execution
def new_endpoint():
    # Implementation
    pass
```

2. **Add to JavaScript**:
```javascript
async newFunction() {
    const response = await fetch('/api/new-endpoint', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: 'value' })
    });
    return await response.json();
}
```

3. **Update documentation**:
- Add endpoint to `docs/api.md`
- Include examples in `docs/examples.md`

### Security Considerations

- Always use `@require_auth` for protected endpoints
- Validate input data
- Use rate limiting for API endpoints
- Log security-relevant events
- Sanitize command inputs

## Debugging

### Frontend Debugging
- Use browser developer tools
- Check console for JavaScript errors
- Monitor network requests
- Use `console.log()` for debugging

### Backend Debugging
- Enable Flask debug mode: `FLASK_ENV=development`
- Check application logs in `logs/` directory
- Use `print()` statements for debugging
- Monitor Docker logs: `docker-compose logs -f`

### Common Debug Commands
```bash
# Check application status
curl http://localhost:8000/health

# Test authentication
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "extendipede2024"}'

# Test command execution
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"command": "ls"}' \
  -b cookies.txt
```

## Performance Optimization

### Frontend
- Minimize DOM manipulations
- Use efficient event listeners
- Implement proper error handling
- Optimize animations

### Backend
- Use connection pooling
- Implement caching where appropriate
- Optimize database queries
- Use async operations where possible

### Docker
- Use multi-stage builds
- Optimize layer caching
- Minimize image size
- Use .dockerignore effectively

## Contributing

### Before Submitting
1. **Test your changes** thoroughly
2. **Update documentation** if needed
3. **Follow code style** guidelines
4. **Add tests** for new functionality
5. **Check for security** vulnerabilities

### Pull Request Process
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
6. Address review feedback

### Code Review Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Security considerations addressed
- [ ] Performance impact assessed
- [ ] Error handling implemented

## Environment Variables

### Development
```bash
FLASK_ENV=development
SECRET_KEY=dev-secret-key
CORS_ORIGINS=http://localhost:8000
LOG_LEVEL=DEBUG
```

### Production
```bash
FLASK_ENV=production
SECRET_KEY=your-secure-secret-key
CORS_ORIGINS=https://yourdomain.com
LOG_LEVEL=INFO
RATELIMIT_STORAGE_URL=redis://redis:6379
```

## Useful Commands

### Development
```bash
# Start development server
python app.py

# Install new dependency
pip install package-name
pip freeze > requirements.txt

# Run linting
flake8 app.py
```

### Docker
```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild from scratch
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Git
```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to remote
git push origin main
```
