# Extendipede Web

A production-ready web-based version of the Extendipede command pipeline simulator. This application visualizes how commands flow through a pipeline with animated LED states synchronized to an AC signal, featuring enterprise-grade security, authentication, and deployment capabilities.

## 🚀 Features

- **Interactive Pipeline Visualization**: See commands flow through configurable pipeline stages
- **Real-time AC Signal Display**: Watch the AC voltage waveform that controls the pipeline
- **Secure Command Execution**: Execute real shell commands with authentication and rate limiting
- **Production Ready**: Docker deployment, SSL/HTTPS, Redis caching, comprehensive logging
- **Authentication System**: Secure login with session management
- **Rate Limiting**: Protection against abuse with configurable limits
- **Modern Web UI**: Beautiful, responsive interface with dark theme
- **Comprehensive Documentation**: Complete guides for installation, usage, and development

## 🏗️ Project Structure

```
Extendipede/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker container definition
├── docker-compose.yml   # Multi-container setup
├── nginx.conf          # Nginx reverse proxy config
├── gunicorn.conf.py    # Production WSGI server config
├── deploy.sh           # Automated deployment script
├── env.example         # Environment variables template
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── static/             # Static files (CSS, JS)
│   ├── style.css
│   └── script.js
├── templates/          # HTML templates
│   └── index.html
├── docs/              # Comprehensive documentation
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

## 🚀 Quick Start

### Development Mode
```bash
# Clone and setup
git clone https://github.com/alexanderdfox/Extendipede.git
cd Extendipede

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```

### Production Mode (Docker)
```bash
# Automated deployment
chmod +x deploy.sh
./deploy.sh

# Or manual deployment
docker-compose up -d
```

**Access the application**: `https://localhost` (credentials: `admin` / `extendipede2024`)

## 📖 Documentation

Comprehensive documentation is available in the `docs/` folder:

- **[Installation Guide](docs/installation.md)** - Detailed setup instructions
- **[Usage Guide](docs/usage.md)** - How to use the application
- **[API Documentation](docs/api.md)** - Complete API reference
- **[Examples](docs/examples.md)** - Usage examples and demos
- **[Production Guide](docs/production.md)** - Production deployment
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions
- **[Development Guide](docs/development.md)** - Development setup and guidelines

## 🔐 Security Features

- **Authentication**: Secure login system with session management
- **Rate Limiting**: Protection against abuse (5 requests/minute)
- **Command Validation**: Whitelist of allowed commands only
- **Input Sanitization**: Protection against injection attacks
- **HTTPS Enforcement**: SSL/TLS encryption for all communications
- **Security Headers**: Comprehensive HTTP security headers
- **Logging**: Detailed security event logging

## 🚀 Production Features

- **Docker Deployment**: Multi-container setup with Nginx and Redis
- **SSL/HTTPS**: Automatic SSL certificate generation
- **Load Balancing**: Nginx reverse proxy configuration
- **Caching**: Redis-based session and rate limiting storage
- **Monitoring**: Health checks and metrics endpoints
- **Logging**: Structured logging with file and console output
- **Environment Configuration**: Flexible environment-based settings

## 🛠️ Development

### Quick Development Setup
```bash
# Development mode
python app.py

# With Docker
docker-compose -f docker-compose.dev.yml up
```

### API Endpoints
- `POST /api/execute` - Execute commands (requires auth)
- `GET /api/status` - Application status
- `GET /api/allowed-commands` - List of allowed commands
- `POST /auth/login` - User authentication
- `GET /auth/status` - Authentication status
- `GET /health` - Health check
- `GET /metrics` - Application metrics

## 📋 Requirements

- **Python**: 3.11 or higher
- **Docker**: 20.10+ (for production deployment)
- **Redis**: 6.0+ (for production features)
- **Browser**: Modern browser with JavaScript support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests and documentation
5. Submit a pull request

See [Development Guide](docs/development.md) for detailed contribution guidelines.

## 📄 License

This project is open source. Feel free to modify and distribute according to your needs.

---

**🚀 Ready to explore the Extendipede pipeline simulator!**

For detailed information, check out the comprehensive documentation in the `docs/` folder.
