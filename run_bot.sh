#!/bin/bash

# Discord Auto Sender Launcher Script

echo "========================================="
echo "   Discord Auto Sender (Remote) Bot     "
echo "========================================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✅ Python detected: $(python3 --version)"
echo ""

# Check if requirements are installed
echo "📦 Checking dependencies..."
pip3 list | grep -q selenium
if [ $? -ne 0 ]; then
    echo "⚠️  Dependencies not found. Installing..."
    pip3 install -r requirements.txt
else
    echo "✅ Dependencies installed"
fi

echo ""
echo "🚀 Launching Discord Auto Sender..."
echo ""

# Run the bot
python3 discord_auto_sender.py

echo ""
echo "👋 Bot closed. Goodbye!"
