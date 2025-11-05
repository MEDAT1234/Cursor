# 🪟 Windows Setup Guide - ASMR TikTok Bot

## System Requirements

- Windows 10 or Windows 11
- Python 3.8 or higher
- At least 4GB RAM
- 2GB free disk space
- Internet connection

## Step-by-Step Installation for Windows

### Step 1: Install Python (if not installed)

1. Download Python from: https://www.python.org/downloads/
2. Run the installer
3. ⚠️ **IMPORTANT:** Check "Add Python to PATH"
4. Click "Install Now"
5. Wait for installation to complete

**Verify installation:**
```batch
python --version
```
You should see: `Python 3.x.x`

### Step 2: Download the Bot Files

If you have the files in a folder, open Command Prompt and navigate:
```batch
cd C:\path\to\workspace
```

### Step 3: Run Setup

Double-click `setup.bat` or run in Command Prompt:
```batch
setup.bat
```

**What happens:**
- Creates virtual environment in `venv` folder
- Installs all Python packages
- Installs Chrome browser for automation
- Creates `.env` configuration file

Wait for: `✅ Setup complete!`

### Step 4: Activate Virtual Environment

Every time you open a new Command Prompt:
```batch
venv\Scripts\activate.bat
```

You'll see `(venv)` at the start of your prompt.

### Step 5: Test Video Generation

```batch
python bot.py --mode test
```

**Wait 1-2 minutes.** A video will be created in `generated_videos` folder.

### Step 6: Configure Settings

Edit `.env` file:
```batch
notepad .env
```

Basic settings (optional - defaults work fine):
```env
VIDEO_DURATION=15
POST_TIMES=09:00,14:00,20:00
ASMR_TYPES=rain,fire,waves,typing,whisper
```

Save and close.

### Step 7: Login to TikTok & Post First Video

```batch
python bot.py --mode once
```

**What happens:**
1. Chrome browser opens automatically
2. TikTok login page appears
3. **You:** Login with your TikTok account
4. Complete any verification (SMS, email)
5. **You:** Go back to Command Prompt, press Enter
6. Bot saves your session
7. Bot generates video
8. Bot uploads to TikTok

**IMPORTANT:** Terminal will show:
```
💾 Save this session ID for future use:
   TIKTOK_SESSION_ID=abc123xyz...
```

Copy this ID and add to `.env`:
```batch
notepad .env
```

Add line:
```env
TIKTOK_SESSION_ID=abc123xyz...
```

Save and close.

### Step 8: Run Automated Mode

Double-click `start_bot.bat` or run:
```batch
start_bot.bat
```

**Bot is now running!** It will:
- Post at 9:00 AM
- Post at 2:00 PM
- Post at 8:00 PM
- Repeat every day

**To stop:** Press `Ctrl+C` in the Command Prompt window

## Windows-Specific Commands

### Open Command Prompt
- Press `Win + R`
- Type `cmd`
- Press Enter

### Navigate to Project Folder
```batch
cd C:\Users\YourName\Desktop\workspace
```

### Activate Environment
```batch
venv\Scripts\activate.bat
```

### Run Bot (3 modes)
```batch
REM Test mode (no upload)
python bot.py --mode test

REM Post once
python bot.py --mode once

REM Automated
python bot.py --mode scheduled
```

### View Logs
```batch
type bot.log
```

### View Recent Logs
```batch
powershell Get-Content bot.log -Tail 50
```

### Monitor Logs Live
```batch
powershell Get-Content bot.log -Wait -Tail 50
```

### Check Generated Videos
```batch
dir generated_videos
```

### Open Video Folder
```batch
explorer generated_videos
```

## Troubleshooting Windows

### "python: command not found"

**Solution:** Python not in PATH
1. Search "Environment Variables" in Windows
2. Edit System Variables
3. Add Python to PATH: `C:\Python3x\` and `C:\Python3x\Scripts\`
4. Restart Command Prompt

### "Permission denied" on scripts

**Solution:** Run Command Prompt as Administrator
1. Right-click Command Prompt
2. Select "Run as Administrator"
3. Navigate to project folder
4. Run setup again

### "Module not found" errors

**Solution:** Reinstall packages
```batch
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Browser doesn't open

**Solution:** Reinstall Playwright
```batch
venv\Scripts\activate.bat
playwright install chromium
```

### Video rendering fails

**Solution:** Install ffmpeg for Windows
1. Download from: https://www.gyan.dev/ffmpeg/builds/
2. Extract to `C:\ffmpeg`
3. Add to PATH: `C:\ffmpeg\bin`
4. Restart Command Prompt

### Port already in use

**Solution:** Kill existing Python processes
```batch
taskkill /F /IM python.exe
```

## Running on Windows Startup (Advanced)

### Method 1: Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Name: "ASMR Bot"
4. Trigger: At startup
5. Action: Start a program
6. Program: `C:\path\to\workspace\start_bot.bat`
7. Finish

### Method 2: Startup Folder

1. Press `Win + R`
2. Type: `shell:startup`
3. Create shortcut to `start_bot.bat`
4. Bot starts on Windows boot

## Running as Windows Service (Advanced)

Create `asmr-bot-service.bat`:
```batch
@echo off
cd C:\path\to\workspace
call venv\Scripts\activate.bat
python bot.py --mode scheduled
```

Use NSSM (Non-Sucking Service Manager):
1. Download NSSM: https://nssm.cc/download
2. Run: `nssm install ASMRBot`
3. Path: `C:\path\to\workspace\asmr-bot-service.bat`
4. Service name: ASMRBot
5. Start service: `nssm start ASMRBot`

## Windows Firewall

If bot can't connect to internet:
1. Open Windows Defender Firewall
2. Allow Python through firewall
3. Allow Chrome through firewall

## Quick Reference

```batch
REM Setup (once)
setup.bat

REM Activate environment
venv\Scripts\activate.bat

REM Test
python bot.py --mode test

REM Post once
python bot.py --mode once

REM Run automated
start_bot.bat

REM View logs
type bot.log

REM Stop bot
Ctrl+C
```

## Windows Folder Structure

```
C:\workspace\
├── venv\                      (Virtual environment)
├── generated_videos\          (Output videos)
├── bot.py                     (Main script)
├── asmr_generator.py          (Audio generator)
├── video_generator.py         (Video creator)
├── tiktok_uploader.py         (Uploader)
├── setup.bat                  (Setup script)
├── start_bot.bat              (Start script)
├── .env                       (Configuration)
├── requirements.txt           (Dependencies)
└── bot.log                    (Activity log)
```

## Performance Tips for Windows

1. **Disable Windows Defender** during video rendering (optional)
2. **Close other programs** when generating videos
3. **Use SSD** for faster rendering
4. **Increase virtual memory** if RAM is low
5. **Run on dedicated machine** for 24/7 operation

## Success!

After following these steps:
- ✅ Bot installed on Windows
- ✅ Test video generated
- ✅ First video posted to TikTok
- ✅ Running automatically

Your Windows machine is now automatically posting ASMR videos to TikTok! 🎉
