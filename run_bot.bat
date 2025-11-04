@echo off
REM Discord Auto Sender Launcher Script for Windows

echo =========================================
echo    Discord Auto Sender (Remote) Bot
echo =========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Python detected
python --version
echo.

echo Checking dependencies...
pip show selenium >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo Dependencies installed
)

echo.
echo Launching Discord Auto Sender...
echo.

REM Run the bot
python discord_auto_sender.py

echo.
echo Bot closed. Goodbye!
pause
