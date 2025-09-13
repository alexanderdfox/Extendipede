#!/bin/bash

# Extendipede Web Production Deployment Script

set -e

echo "🚀 Starting Extendipede Web Production Deployment..."

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Please do not run this script as root"
    exit 1
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p ssl
mkdir -p static
mkdir -p templates

# Set proper permissions
echo "🔐 Setting permissions..."
chmod 755 logs
chmod 700 ssl
chmod 755 static
chmod 755 templates

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found. Creating from example..."
    cp env.example .env
    echo "📝 Please edit .env file with your production settings"
    echo "   Especially change SECRET_KEY and CORS_ORIGINS"
    exit 1
fi

# Load environment variables
source .env

# Validate required environment variables
if [ -z "$SECRET_KEY" ] || [ "$SECRET_KEY" = "your-super-secret-key-change-this-in-production" ]; then
    echo "❌ SECRET_KEY must be set in .env file"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create SSL certificates if they don't exist
if [ ! -f ssl/cert.pem ] || [ ! -f ssl/key.pem ]; then
    echo "🔒 Creating self-signed SSL certificates..."
    openssl req -x509 -newkey rsa:4096 -keyout ssl/key.pem -out ssl/cert.pem -days 365 -nodes \
        -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"
fi

# Start Redis if not running
if ! pgrep -x "redis-server" > /dev/null; then
    echo "🔴 Starting Redis server..."
    redis-server --daemonize yes
fi

# Choose deployment method
echo "🎯 Choose deployment method:"
echo "1) Docker Compose (Recommended)"
echo "2) Gunicorn directly"
echo "3) Development server"

read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo "🐳 Deploying with Docker Compose..."
        docker-compose down
        docker-compose build
        docker-compose up -d
        echo "✅ Deployment complete! Access at https://localhost"
        ;;
    2)
        echo "🔧 Deploying with Gunicorn..."
        gunicorn --config gunicorn.conf.py app:app
        ;;
    3)
        echo "🛠️  Starting development server..."
        python app.py
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo "🎉 Deployment completed successfully!"
echo "📊 Check logs with: tail -f logs/extendipede.log"
echo "🏥 Health check: curl https://localhost/health"
echo "📈 Metrics: curl https://localhost/metrics"
