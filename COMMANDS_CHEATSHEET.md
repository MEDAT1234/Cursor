# 🎯 Commands Cheat Sheet

Quick reference for all bot commands.

---

## 📦 SETUP (One Time Only)

### Linux/macOS
```bash
chmod +x setup.sh
./setup.sh
```

### Windows
```batch
setup.bat
```

---

## 🔌 ACTIVATE ENVIRONMENT (Before Each Session)

### Linux/macOS
```bash
source venv/bin/activate
```

### Windows
```batch
venv\Scripts\activate.bat
```

---

## 🎬 RUN THE BOT

### Test Mode (No Upload)
```bash
# Linux/macOS
python3 bot.py --mode test

# Windows
python bot.py --mode test
```

### Post Once (Generate & Upload 1 Video)
```bash
# Linux/macOS
python3 bot.py --mode once

# Windows
python bot.py --mode once
```

### Automated Mode (Run 24/7 with Schedule)
```bash
# Linux/macOS
./start_bot.sh
# OR
python3 bot.py --mode scheduled

# Windows
start_bot.bat
# OR
python bot.py --mode scheduled
```

---

## 📊 MONITORING

### View Logs (Real-time)
```bash
# Linux/macOS
tail -f bot.log

# Windows (PowerShell)
Get-Content bot.log -Wait -Tail 50
```

### Check Generated Videos
```bash
# Linux/macOS
ls -lh generated_videos/

# Windows
dir generated_videos
```

### Stop the Bot
```
Press Ctrl+C in the terminal
```

---

## ⚙️ CONFIGURATION

### Edit Settings
```bash
# Linux/macOS
nano .env

# Windows
notepad .env
```

### Important Settings
```env
POST_TIMES=09:00,14:00,20:00
ASMR_TYPES=rain,fire,waves,typing,whisper
VIDEO_DURATION=15
TIKTOK_SESSION_ID=your_session_here
```

---

## 🔧 TROUBLESHOOTING

### Reinstall Dependencies
```bash
source venv/bin/activate  # or venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Reinstall Browser
```bash
playwright install chromium
```

### Clear Session (Force Re-login)
```bash
# Edit .env and remove or comment out:
# TIKTOK_SESSION_ID=...
```

### View Recent Logs
```bash
# Linux/macOS
tail -n 100 bot.log

# Windows
Get-Content bot.log -Tail 100
```

---

## 🚀 QUICK START WORKFLOW

```bash
# 1. Setup (first time only)
./setup.sh

# 2. Test
source venv/bin/activate
python3 bot.py --mode test

# 3. Post once (with TikTok login)
python3 bot.py --mode once

# 4. Run automated
./start_bot.sh
```

---

## 📂 FILE LOCATIONS

```
bot.py              - Main script
bot.log             - Activity logs
.env                - Your configuration
generated_videos/   - Output videos
venv/              - Virtual environment
```

---

## 💡 PRO TIPS

```bash
# Run in background (Linux/macOS)
nohup ./start_bot.sh > output.log 2>&1 &

# Run in background (screen)
screen -dmS asmr-bot ./start_bot.sh

# Check if bot is running
ps aux | grep bot.py

# Kill bot process
pkill -f bot.py
```

---

## 📞 NEED HELP?

1. Check `bot.log`
2. Read `STEP_BY_STEP.md`
3. Review `README.md`
4. Try test mode first

---

**Remember:** Always activate the virtual environment before running commands!

```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows
```
