@echo off
echo 🎵 ASMR TikTok Bot - Setup Script 🎵
echo ======================================
echo.

REM Check Python version
echo 🐍 Checking Python version...
python --version

if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Create virtual environment
echo.
echo 📦 Creating virtual environment...
python -m venv venv

if %errorlevel% neq 0 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment created

REM Activate virtual environment
echo.
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo.
echo 📚 Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

REM Install Playwright browsers
echo.
echo 🌐 Installing Playwright browsers...
playwright install chromium

if %errorlevel% neq 0 (
    echo ⚠️  Warning: Failed to install Playwright browsers
    echo    You can manually install them later with: playwright install chromium
)

REM Create .env file if it doesn't exist
if not exist .env (
    echo.
    echo 📝 Creating .env file from template...
    copy .env.example .env
    echo ✅ Created .env file
    echo ⚠️  Please edit .env and add your TikTok credentials
) else (
    echo.
    echo ℹ️  .env file already exists
)

REM Create directories
echo.
echo 📁 Creating directories...
if not exist generated_videos mkdir generated_videos
if not exist logs mkdir logs

echo.
echo ======================================
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Edit the .env file with your settings:
echo    notepad .env
echo.
echo 3. Run the bot:
echo    python bot.py --mode test        # Test video generation
echo    python bot.py --mode once        # Generate and post once
echo    python bot.py --mode scheduled   # Run with schedule
echo.
echo ======================================
pause
