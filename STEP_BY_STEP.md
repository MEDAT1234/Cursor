# 📋 Step-by-Step Guide to Run the ASMR TikTok Bot

## ✅ Prerequisites Check

Before starting, make sure you have:
- [ ] A computer (Linux, macOS, or Windows)
- [ ] Python 3.8 or higher installed
- [ ] A TikTok account
- [ ] Internet connection

### Check Python Installation

```bash
# Open terminal/command prompt and run:
python3 --version    # Linux/macOS
python --version     # Windows

# You should see: Python 3.8.x or higher
```

**Don't have Python?** Download from: https://www.python.org/downloads/

---

## 🚀 Step 1: Download the Project

You already have the files in `/workspace/`. If you need to move them:

```bash
# Navigate to the project folder
cd /workspace
```

---

## 🔧 Step 2: Run Setup Script

This installs all dependencies automatically.

### On Linux/macOS:

```bash
# Make the script executable
chmod +x setup.sh

# Run setup
./setup.sh
```

### On Windows:

```batch
# Double-click setup.bat
# OR run in Command Prompt:
setup.bat
```

**What happens:**
- Creates virtual environment
- Installs Python packages
- Installs browser for automation
- Creates `.env` configuration file

**Wait for:** "✅ Setup complete!" message

---

## ⚙️ Step 3: Configure Settings (Optional)

Edit the `.env` file to customize:

### On Linux/macOS:
```bash
nano .env
# OR
vim .env
# OR
code .env    # If you have VS Code
```

### On Windows:
```batch
notepad .env
```

### Basic Configuration (Optional - defaults work fine):

```env
# Posting schedule (when to post each day)
POST_TIMES=09:00,14:00,20:00

# Which ASMR types to generate
ASMR_TYPES=rain,fire,waves,typing,whisper

# Video settings
VIDEO_DURATION=15
```

**Save and close** the file.

> 💡 **Tip:** You can skip this step and use defaults!

---

## 🧪 Step 4: Test Video Generation

Test that everything works WITHOUT uploading to TikTok.

### Activate Virtual Environment:

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```batch
venv\Scripts\activate.bat
```

You'll see `(venv)` in your terminal prompt.

### Generate Test Video:

**Linux/macOS:**
```bash
python3 bot.py --mode test
```

**Windows:**
```batch
python bot.py --mode test
```

**What happens:**
1. Bot generates ASMR audio (takes 10-20 seconds)
2. Creates video with visuals (takes 30-60 seconds)
3. Saves to `generated_videos/` folder
4. Shows: "✅ Test video generated: generated_videos/asmr_xxx.mp4"

**Check the video:**
```bash
# Linux/macOS
ls -lh generated_videos/
open generated_videos/*.mp4    # Opens the video

# Windows
dir generated_videos
start generated_videos\*.mp4   # Opens the video
```

> ✅ **If you see the video, everything works!**

---

## 🎬 Step 5: Post Your First Video

Now let's generate and post to TikTok!

### Run Once Mode:

**Linux/macOS:**
```bash
python3 bot.py --mode once
```

**Windows:**
```batch
python bot.py --mode once
```

### What Happens Next:

1. **Browser Opens Automatically**
   - A Chrome browser window will appear
   - You'll see TikTok login page

2. **Login to TikTok**
   - Enter your username/email and password
   - Complete any verification (SMS, email, etc.)
   - Wait until you see your TikTok feed

3. **Press Enter in Terminal**
   - Go back to the terminal
   - Press **Enter** when login is complete
   - Bot extracts and saves your session

4. **Bot Generates Video**
   - Creates ASMR audio
   - Renders video
   - Shows progress messages

5. **Bot Uploads to TikTok**
   - Browser navigates to upload page
   - Uploads video file
   - Adds caption and hashtags
   - Publishes automatically

6. **Done!**
   - You'll see: "✅ Video uploaded successfully!"
   - Check your TikTok profile to see the post

**Important:** Save the session ID shown in terminal:
```
💾 Save this session ID for future use:
   TIKTOK_SESSION_ID=abc123xyz...
```

Add this to your `.env` file so you don't need to login again:
```env
TIKTOK_SESSION_ID=abc123xyz...
```

---

## 🤖 Step 6: Run Automated Mode

Now set it up to run automatically on a schedule!

### Option A: Simple Start (Recommended)

**Linux/macOS:**
```bash
./start_bot.sh
```

**Windows:**
```batch
start_bot.bat
```

### Option B: Manual Start

**Linux/macOS:**
```bash
source venv/bin/activate
python3 bot.py --mode scheduled
```

**Windows:**
```batch
venv\Scripts\activate.bat
python bot.py --mode scheduled
```

### What Happens:

```
🤖 Starting ASMR Bot...
✅ Bot is running!
⏰ Waiting for scheduled times...
💡 Press Ctrl+C to stop the bot
```

The bot will now:
- Run continuously in the background
- Generate videos at scheduled times (default: 9am, 2pm, 8pm)
- Post automatically to TikTok
- Log everything to `bot.log`

**To stop:** Press `Ctrl+C` in the terminal

---

## 📊 Step 7: Monitor the Bot

### View Live Logs

**Linux/macOS:**
```bash
# In a new terminal window
tail -f bot.log
```

**Windows:**
```batch
# In a new Command Prompt
powershell Get-Content bot.log -Wait -Tail 50
```

### Check Generated Videos

```bash
# Linux/macOS
ls -lh generated_videos/

# Windows
dir generated_videos
```

### View Statistics

The bot logs statistics after each post:
```
📊 Statistics:
   Videos Generated: 5
   Videos Uploaded: 5
   Errors: 0
   Last Post: 2025-11-04 14:00:23
```

---

## 🎯 Summary of Commands

### Quick Reference

| Action | Linux/macOS | Windows |
|--------|-------------|---------|
| **Setup** | `./setup.sh` | `setup.bat` |
| **Activate env** | `source venv/bin/activate` | `venv\Scripts\activate.bat` |
| **Test** | `python3 bot.py --mode test` | `python bot.py --mode test` |
| **Post once** | `python3 bot.py --mode once` | `python bot.py --mode once` |
| **Run automated** | `./start_bot.sh` | `start_bot.bat` |
| **View logs** | `tail -f bot.log` | `Get-Content bot.log -Wait` |
| **Stop bot** | Press `Ctrl+C` | Press `Ctrl+C` |

---

## 🔄 Daily Operation

Once set up, your daily routine is simple:

### Morning (First Time)
```bash
./start_bot.sh    # Start the bot
```

### During the Day
- Bot runs automatically
- Posts at scheduled times
- No intervention needed

### Evening (Optional)
```bash
tail -f bot.log   # Check what happened today
```

### Before Bed (Optional)
- Press `Ctrl+C` to stop
- OR leave it running overnight

---

## 🐛 Troubleshooting

### Issue: "python3: command not found"
**Solution:**
```bash
# Try without the 3
python --version
python bot.py --mode test
```

### Issue: "Permission denied: ./setup.sh"
**Solution:**
```bash
chmod +x setup.sh start_bot.sh
./setup.sh
```

### Issue: Video generation fails
**Solution:**
```bash
# Install ffmpeg
# Ubuntu/Debian:
sudo apt-get install ffmpeg

# macOS:
brew install ffmpeg

# Windows: Download from ffmpeg.org
```

### Issue: Browser doesn't open
**Solution:**
```bash
# Reinstall Playwright
source venv/bin/activate
playwright install chromium
```

### Issue: Upload fails
**Solution:**
1. Delete session ID from `.env`
2. Run `python3 bot.py --mode once` again
3. Login manually when browser opens

### Issue: Bot stops unexpectedly
**Solution:**
```bash
# Check logs
tail -n 50 bot.log

# Restart bot
./start_bot.sh
```

---

## 📱 Running on a Server (Advanced)

Want to run 24/7 on a remote server?

### Using screen (Linux):
```bash
# Install screen
sudo apt-get install screen

# Start a screen session
screen -S asmr-bot

# Activate and run bot
source venv/bin/activate
python3 bot.py --mode scheduled

# Detach: Press Ctrl+A, then D

# Reattach later:
screen -r asmr-bot
```

### Using systemd (Linux):
Create `/etc/systemd/system/asmr-bot.service`:
```ini
[Unit]
Description=ASMR TikTok Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/workspace
ExecStart=/workspace/venv/bin/python3 /workspace/bot.py --mode scheduled
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable asmr-bot
sudo systemctl start asmr-bot
sudo systemctl status asmr-bot
```

---

## ✅ Success Checklist

After completing all steps, you should have:

- [x] Setup script completed successfully
- [x] Test video generated in `generated_videos/`
- [x] Successfully logged into TikTok
- [x] First video posted to your TikTok account
- [x] Bot running in scheduled mode
- [x] Logs showing in `bot.log`
- [x] Understanding of how to start/stop bot

---

## 🎉 You're Done!

Your ASMR TikTok bot is now:
- ✅ Fully set up
- ✅ Configured
- ✅ Tested
- ✅ Running automatically
- ✅ Posting to TikTok

**Congratulations!** 🎊

The bot will now generate and post ASMR videos automatically. No more manual work needed!

---

## 📞 Need Help?

1. Check `bot.log` for error messages
2. Read the troubleshooting section above
3. Review `README.md` for detailed info
4. Check that all steps were completed

---

## 🚀 Next Steps

1. **Monitor first few posts** - Make sure they look good
2. **Adjust schedule if needed** - Edit POST_TIMES in `.env`
3. **Try different ASMR types** - Modify ASMR_TYPES in `.env`
4. **Set up server** - For 24/7 operation (optional)
5. **Engage with followers** - Reply to comments

**Happy automating!** 🎵✨
