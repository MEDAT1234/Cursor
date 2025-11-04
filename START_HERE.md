# 🎵 START HERE - Complete Guide to Run Your ASMR Bot

## 🎯 What You're About to Do

You will set up a bot that:
1. Generates professional ASMR videos automatically
2. Posts them to TikTok without your intervention
3. Runs 24/7 on a schedule

**Time needed:** 10-15 minutes for first setup

---

## 📋 Step-by-Step Instructions

### STEP 1: Install Dependencies (2 minutes)

Open your terminal and run:

**Linux/macOS:**
```bash
cd /workspace
chmod +x setup.sh
./setup.sh
```

**Windows:**
```batch
cd \workspace
setup.bat
```

Wait for: `✅ Setup complete!`

---

### STEP 2: Activate Virtual Environment (10 seconds)

Every time you open a new terminal, run:

**Linux/macOS:**
```bash
cd /workspace
source venv/bin/activate
```

**Windows:**
```batch
cd \workspace
venv\Scripts\activate.bat
```

You'll see `(venv)` appear in your terminal.

---

### STEP 3: Test Video Generation (1 minute)

Create a test video WITHOUT uploading:

**Linux/macOS:**
```bash
python3 bot.py --mode test
```

**Windows:**
```batch
python bot.py --mode test
```

**Expected output:**
```
🎬 Starting video generation...
🔊 Generating ASMR audio...
✨ Creating rain themed visuals...
🎨 Compositing video...
💾 Rendering video to generated_videos/asmr_rain_20251104_120000.mp4...
✅ Video generated successfully: generated_videos/asmr_rain_20251104_120000.mp4
```

**Watch the video:** Open the file in `generated_videos/` folder

---

### STEP 4: Login to TikTok & Post First Video (2 minutes)

**Linux/macOS:**
```bash
python3 bot.py --mode once
```

**Windows:**
```batch
python bot.py --mode once
```

**What will happen:**

1. **Browser Opens**
   ```
   🔑 Please login to TikTok manually...
   📱 Opening TikTok login page...
   ```
   A Chrome window will appear showing TikTok login

2. **You Login**
   - Enter your TikTok username and password
   - Complete any 2FA/verification
   - Wait until you see your TikTok feed
   
3. **Press Enter**
   - Go back to terminal
   - Press `Enter` key
   - Bot saves your session

4. **Bot Creates & Posts Video**
   ```
   🎬 Generating video...
   📤 Uploading to TikTok...
   ✅ Successfully posted to TikTok!
   ```

5. **Save Session ID**
   Terminal shows:
   ```
   💾 Save this session ID for future use:
      abc123xyz789...
   ```
   
   **IMPORTANT:** Copy this and add to `.env` file:
   ```bash
   # Edit .env file
   nano .env   # or notepad .env on Windows
   
   # Add this line:
   TIKTOK_SESSION_ID=abc123xyz789...
   ```

---

### STEP 5: Run Automated Mode (10 seconds)

Now make it run automatically!

**Linux/macOS:**
```bash
./start_bot.sh
```

**Windows:**
```batch
start_bot.bat
```

**You'll see:**
```
╔═══════════════════════════════════════════════════════════╗
║           🎵 ASMR TikTok Automation Bot 🎵               ║
║                                                           ║
║  Automatically generates and posts ASMR videos to TikTok  ║
╚═══════════════════════════════════════════════════════════╝

🤖 Starting ASMR Bot...
======================================================================
⏰ Setting up schedule...
   ✓ Scheduled post at 09:00
   ✓ Scheduled post at 14:00
   ✓ Scheduled post at 20:00
✅ Schedule configured
✅ Bot is running!
⏰ Waiting for scheduled times...
💡 Press Ctrl+C to stop the bot
======================================================================
```

**The bot is now running!** It will:
- Post at 9:00 AM
- Post at 2:00 PM  
- Post at 8:00 PM
- Repeat daily

**To stop:** Press `Ctrl+C`

---

## 📊 Monitor Your Bot

### Check Logs (Real-time)

Open a **new terminal** window:

**Linux/macOS:**
```bash
cd /workspace
tail -f bot.log
```

**Windows PowerShell:**
```powershell
cd \workspace
Get-Content bot.log -Wait -Tail 50
```

### Check Generated Videos

```bash
# Linux/macOS
ls -lh generated_videos/

# Windows
dir generated_videos
```

---

## ⚙️ Customize Settings (Optional)

Edit `.env` file:

```bash
# Linux/macOS
nano .env

# Windows
notepad .env
```

**Common settings:**

```env
# Change posting times (24-hour format)
POST_TIMES=08:00,12:00,16:00,20:00

# Choose which ASMR types to generate
ASMR_TYPES=rain,waves,fire         # Just these 3
# OR
ASMR_TYPES=rain,fire,waves,typing,whisper  # All 5

# Change video duration (seconds)
VIDEO_DURATION=20

# Your TikTok session (from Step 4)
TIKTOK_SESSION_ID=your_session_id_here
```

**After changing settings:**
1. Stop the bot (Ctrl+C)
2. Restart: `./start_bot.sh`

---

## 🎯 Quick Command Reference

```bash
# 1. Setup (first time only)
./setup.sh

# 2. Activate environment (every time)
source venv/bin/activate

# 3. Test video generation
python3 bot.py --mode test

# 4. Post one video
python3 bot.py --mode once

# 5. Run automated
./start_bot.sh

# 6. Stop bot
Press Ctrl+C

# 7. View logs
tail -f bot.log
```

---

## ❓ Troubleshooting

### "python3: command not found"
Try: `python --version` and use `python` instead of `python3`

### "Permission denied"
Run: `chmod +x setup.sh start_bot.sh`

### Video generation fails
Install ffmpeg:
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### Browser doesn't open
Reinstall Playwright:
```bash
source venv/bin/activate
playwright install chromium
```

### Upload to TikTok fails
1. Delete `TIKTOK_SESSION_ID` from `.env`
2. Run `python3 bot.py --mode once` again
3. Login when browser opens

---

## 📚 Additional Documentation

- **`STEP_BY_STEP.md`** - Detailed instructions with explanations
- **`COMMANDS_CHEATSHEET.md`** - Quick command reference
- **`README.md`** - Complete documentation
- **`QUICKSTART.md`** - 5-minute quick start
- **`OVERVIEW.md`** - Technical overview

---

## ✅ Success Checklist

After following these steps, you should have:

- [x] Installed all dependencies
- [x] Generated a test video
- [x] Logged into TikTok
- [x] Posted your first video
- [x] Bot running on schedule
- [x] Logs showing activity

---

## 🎉 Congratulations!

Your ASMR TikTok bot is now:
- ✅ **Generating** professional videos
- ✅ **Posting** automatically to TikTok
- ✅ **Running** 24/7 on schedule
- ✅ **Logging** all activity

**No more manual work needed!**

---

## 🚀 What Happens Next?

### Today:
- Bot posts at scheduled times (9am, 2pm, 8pm)
- Check `bot.log` to see activity
- Verify posts appear on your TikTok

### This Week:
- 21 videos posted automatically
- No manual intervention
- Monitor performance

### This Month:
- 90+ videos posted
- Growing TikTok presence
- Established content library

---

## 💡 Pro Tips

1. **Run on a server** for true 24/7 operation (VPS, cloud, etc.)
2. **Monitor first week** to ensure everything runs smoothly
3. **Adjust schedule** based on when your audience is most active
4. **Engage with comments** to boost algorithm ranking
5. **Track which ASMR types** get the most views

---

## 📞 Need More Help?

1. Read `STEP_BY_STEP.md` for detailed explanations
2. Check `bot.log` for error messages  
3. Review troubleshooting section above
4. Read `README.md` for advanced configuration

---

**You're all set! Happy automating! 🎵✨**

---

## 🎬 Visual Workflow

```
START
  ↓
[Run ./setup.sh] → Installs everything
  ↓
[Activate venv] → source venv/bin/activate
  ↓
[Test Mode] → python3 bot.py --mode test
  ↓
[Post Once] → python3 bot.py --mode once → Login to TikTok
  ↓
[Save Session ID] → Add to .env file
  ↓
[Run Automated] → ./start_bot.sh
  ↓
[Bot Running!] → Posts at 9am, 2pm, 8pm daily
  ↓
Monitor with: tail -f bot.log
  ↓
[SUCCESS! 🎉]
```
