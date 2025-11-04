# Quick Start Guide 🚀

Get the Airdrop Bot running in 5 minutes!

## For Windows Users 💻

### 1. Install Python
- Download Python from https://www.python.org/downloads/
- **Important:** Check "Add Python to PATH" during installation
- Open Command Prompt and verify: `python --version`

### 2. Navigate to Project
```cmd
cd C:\path\to\workspace
```

### 3. Install Dependencies
```cmd
pip install -r requirements.txt
```

### 4. Create Configuration
```cmd
copy .env.example .env
notepad .env
```

Edit these lines in `.env`:
```
MIN_RELIABILITY_SCORE=60
UPDATE_INTERVAL=30
```

### 5. Run the Bot
```cmd
python bot.py continuous
```

---

## For Mac/Linux Users 🐧🍎

### 1. Check Python (Usually Pre-installed)
```bash
python3 --version
```

If not installed, install via:
- **Mac:** `brew install python3`
- **Linux:** `sudo apt install python3 python3-pip`

### 2. Navigate to Project
```bash
cd /workspace
```

### 3. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Create Configuration
```bash
cp .env.example .env
nano .env  # or use vim, or any text editor
```

Edit the settings as needed.

### 5. Run the Bot
```bash
python3 bot.py continuous
```

---

## Testing the Bot ✅

Before running continuously, test with a single run:

```bash
python bot.py once
```

You should see:
```
🚀 Initializing Airdrop Capture Bot...
✓ RSS Feed collector enabled
✓ Web scraper enabled
🔄 Starting collection cycle
```

---

## Basic Commands

| Command | What it does |
|---------|-------------|
| `python bot.py continuous` | Run continuously (updates every 30 min) |
| `python bot.py once` | Run once and exit |
| `python bot.py stats` | Show statistics only |

---

## Optional: Setup Telegram Notifications 📱

1. Open Telegram app
2. Search for `@BotFather`
3. Send: `/newbot`
4. Follow instructions and copy your token
5. Search for `@userinfobot`
6. Send: `/start` and copy your chat ID
7. Add to `.env`:
```env
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## Stopping the Bot ⏹️

Press `Ctrl+C` in the terminal window

---

## Common Issues & Fixes 🔧

### "pip: command not found"
- **Windows:** Use `python -m pip install -r requirements.txt`
- **Mac/Linux:** Use `pip3` instead of `pip`

### "Permission denied"
- **Mac/Linux:** Try `sudo pip3 install -r requirements.txt`

### "No module named..."
- Make sure you ran: `pip install -r requirements.txt`
- Try: `python -m pip install <module_name>`

### Bot finds no airdrops
- This is normal if there are no new airdrops at the moment
- Wait for the next cycle (30 minutes by default)
- Lower `MIN_RELIABILITY_SCORE` in `.env` to see more results

---

## What's Next? 📚

- Read the full [README.md](README.md) for advanced usage
- Customize settings in `.env`
- Set up the bot to run in the background
- Add Telegram notifications

---

**You're all set! The bot will now monitor for crypto airdrops automatically. 🎉**
