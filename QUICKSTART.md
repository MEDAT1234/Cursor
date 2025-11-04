# 🚀 Quick Start Guide

Get your ASMR bot running in 5 minutes!

## Step 1: Setup (2 minutes)

### Linux/macOS
```bash
chmod +x setup.sh
./setup.sh
```

### Windows
```batch
setup.bat
```

## Step 2: Configure (1 minute)

Edit `.env` file:
```bash
# Linux/macOS
nano .env

# Windows
notepad .env
```

**Minimum required:** Just leave defaults! The bot will handle TikTok login automatically.

## Step 3: Test (1 minute)

```bash
# Activate environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows

# Test video generation
python3 bot.py --mode test  # Linux/macOS
python bot.py --mode test   # Windows
```

This creates a test video in `generated_videos/` folder.

## Step 4: First Post (1 minute)

```bash
python3 bot.py --mode once  # Linux/macOS
python bot.py --mode once   # Windows
```

The bot will:
1. Open a browser
2. Ask you to login to TikTok
3. Generate a video
4. Post it automatically
5. Save your session for future use

## Step 5: Automate!

```bash
./start_bot.sh        # Linux/macOS
start_bot.bat         # Windows
```

The bot now runs 24/7 and posts automatically at:
- 9:00 AM
- 2:00 PM
- 8:00 PM

## 🎉 Done!

Your ASMR bot is now running! It will:
- ✅ Generate unique ASMR videos
- ✅ Post them automatically
- ✅ Add captions and hashtags
- ✅ Track everything in `bot.log`

## Customization

Want different posting times? Edit `.env`:
```env
POST_TIMES=10:00,15:00,20:00
```

Want specific ASMR types only?
```env
ASMR_TYPES=rain,waves
```

## Need Help?

Check the full [README.md](README.md) for:
- Troubleshooting
- Advanced configuration
- Best practices
- FAQ

## Pro Tips

1. **Test first!** Always use `--mode test` before going live
2. **Monitor logs**: `tail -f bot.log`
3. **Start small**: Use default 3 posts/day
4. **Be patient**: First video might take 2-3 minutes
5. **Save session ID**: Backup your `.env` file!

Happy automating! 🎵✨
