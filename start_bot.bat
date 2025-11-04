@echo off
REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the bot in scheduled mode
python bot.py --mode scheduled
