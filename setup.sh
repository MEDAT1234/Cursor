#!/bin/bash

echo "🎵 ASMR TikTok Bot - Setup Script 🎵"
echo "======================================"
echo ""

# Check Python version
echo "🐍 Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment"
    exit 1
fi

echo "✅ Virtual environment created"

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "📚 Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Install Playwright browsers
echo ""
echo "🌐 Installing Playwright browsers..."
playwright install chromium

if [ $? -ne 0 ]; then
    echo "⚠️  Warning: Failed to install Playwright browsers"
    echo "   You can manually install them later with: playwright install chromium"
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ Created .env file"
    echo "⚠️  Please edit .env and add your TikTok credentials"
else
    echo ""
    echo "ℹ️  .env file already exists"
fi

# Create directories
echo ""
echo "📁 Creating directories..."
mkdir -p generated_videos
mkdir -p logs

echo ""
echo "======================================"
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Edit the .env file with your settings:"
echo "   nano .env"
echo ""
echo "3. Run the bot:"
echo "   python3 bot.py --mode test        # Test video generation"
echo "   python3 bot.py --mode once        # Generate and post once"
echo "   python3 bot.py --mode scheduled   # Run with schedule"
echo ""
echo "======================================"
