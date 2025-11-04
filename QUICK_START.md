# 🚀 Quick Start Guide

Get your Discord Auto Sender bot running in 5 minutes!

## Step 1: Install Dependencies (1 minute)

### Windows
```bash
pip install -r requirements.txt
```

### Linux/Mac
```bash
pip3 install -r requirements.txt
```

## Step 2: Download ChromeDriver (2 minutes)

1. Check your Chrome version:
   - Open Chrome
   - Click the 3 dots (⋮) → Help → About Google Chrome
   - Note your version (e.g., 119.0.6045.105)

2. Download matching ChromeDriver:
   - Visit: https://chromedriver.chromium.org/downloads
   - Download the version matching your Chrome
   - Extract to a folder (e.g., Desktop or Downloads)

## Step 3: Get Discord Channel URLs (1 minute)

1. Open Discord in your browser
2. Navigate to the channel you want to automate
3. Copy the URL from address bar
   - Format: `https://discord.com/channels/SERVER_ID/CHANNEL_ID`
4. Repeat for all channels you want to use

## Step 4: Launch the Bot (30 seconds)

### Windows
```bash
python discord_auto_sender.py
```
Or double-click: `run_bot.bat`

### Linux/Mac
```bash
python3 discord_auto_sender.py
```
Or run: `./run_bot.sh`

## Step 5: Configure & Start (30 seconds)

1. **Set Chrome Path**:
   - Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - Linux: `/usr/bin/google-chrome`
   - Mac: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

2. **Set ChromeDriver Path**:
   - Point to where you extracted chromedriver
   - Example: `C:/Users/YourName/Desktop/chromedriver.exe`

3. **Add Channel URL(s)**:
   - Paste Discord channel URL
   - Click "Add"
   - Repeat for multiple channels (for multitasking!)

4. **Click "▶ Start"**!

## 🎉 That's It!

Your bot is now running and will:
- Send messages to all channels simultaneously (multitasking)
- Use random delays (60-100 seconds by default)
- Auto-generate varied messages
- Show real-time progress

## ⚙️ Optional Settings

- **Delay Range**: Adjust 60-100 to your preference
- **Channel Mode**: 
  - `0` = Random channel each time
  - `1` = First channel only
  - `2` = Sequential rotation
- **Notifications**: Check/uncheck for alerts

## 🔧 Troubleshooting

**"ChromeDriver version mismatch"**
- Download ChromeDriver matching your Chrome version exactly

**"Cannot find Chrome"**
- Verify the Chrome path is correct for your OS

**"Messages not sending"**
- Make sure you're logged into Discord in browser
- Check you have permission to send in the channel

**"Bot starts but nothing happens"**
- Check the logs: `discord_bot.log`
- Verify Discord channel URLs are correct

## 📊 Understanding Multitasking

When you add multiple channels:
```
Channel 1 → Worker Thread 1 → Sends messages independently
Channel 2 → Worker Thread 2 → Sends messages independently  
Channel 3 → Worker Thread 3 → Sends messages independently
```

All channels run **at the same time**! That's multitasking in action.

## 🎯 Best Practices

✅ Start with 1-2 channels to test
✅ Use 60+ second delays to avoid rate limits
✅ Only use on servers you own/have permission
✅ Monitor the bot for first few minutes
✅ Check logs if issues occur

## 🆘 Need Help?

1. Read the full README.md
2. Check discord_bot.log for errors
3. Verify all paths are correct
4. Test with single channel first

---

**Happy Automating! 🤖**
