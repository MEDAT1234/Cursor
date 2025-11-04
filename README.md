# Discord Auto Sender (Remote) - Multitasking Bot

A powerful automation tool for managing multiple Discord channels with intelligent message automation and multitasking capabilities.

![Discord Bot](https://img.shields.io/badge/Discord-Bot-7289DA?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

## 🌟 Features

### Core Functionality
- **🔀 Multitasking**: Run multiple channels simultaneously with independent worker threads
- **🤖 Smart Message Generation**: AI-powered message generation with natural variations
- **⏱️ Intelligent Delays**: Random delay ranges (60-100s default) to appear human-like
- **🎯 Channel Management**: Support for unlimited Discord channels
- **🔄 Flexible Channel Modes**:
  - Mode 0: Random channel selection
  - Mode 1: First channel priority
  - Mode 2: Sequential rotation

### Advanced Features
- **🌐 Remote Browser Control**: Uses Selenium with remote debugging (port 9222)
- **⏯️ Full Control**: Start, Pause, Resume, and Stop operations
- **📊 Real-time Status**: Live progress tracking and current operation display
- **🔔 Notifications**: Optional desktop notifications for important events
- **💾 Auto-save**: Automatic configuration and channel list persistence
- **📝 Logging**: Comprehensive logging system for debugging

### User Interface
- **🎨 Modern GUI**: Clean, Discord-inspired dark theme interface
- **📱 Intuitive Design**: Easy-to-use controls and configuration
- **👁️ Live Monitoring**: Real-time display of current channel, message, and progress
- **🔧 Easy Configuration**: Simple setup for Chrome, chromedriver, and settings

## 📋 Requirements

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (matching your Chrome version)
- Discord account

## 🚀 Installation

### 1. Clone or Download
```bash
git clone <repository-url>
cd discord-auto-sender
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download ChromeDriver
Download ChromeDriver from: https://chromedriver.chromium.org/
- Match your Chrome version
- Extract to a known location

## ⚙️ Configuration

### Initial Setup

1. **Chrome Path**: 
   - Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - Linux: `/usr/bin/google-chrome`
   - Mac: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

2. **ChromeDriver Path**: 
   - Point to where you extracted chromedriver
   - Example: `C:/Users/hp/Desktop/discord bot/chromedriver.exe`

3. **Remote Debugging Port**: 
   - Default: `9222`
   - Change if port is in use

4. **Delay Range**: 
   - Minimum: 60 seconds (default)
   - Maximum: 100 seconds (default)
   - Adjust based on your needs

5. **Channel Mode**:
   - `0`: Random - Picks random channel each time
   - `1`: First - Always uses first channel (single channel mode)
   - `2`: Sequential - Rotates through channels in order

### Adding Channels

1. Copy Discord channel URL from browser
   - Format: `https://discord.com/channels/SERVER_ID/CHANNEL_ID`
2. Paste into "Add Discord Channel URL" field
3. Click "Add" button
4. Repeat for all channels you want to automate

## 🎮 Usage

### Basic Operation

1. **Launch the Application**
```bash
python discord_auto_sender.py
```

2. **Configure Settings**
   - Enter Chrome and ChromeDriver paths
   - Set delay range
   - Choose channel mode
   - Enable/disable notifications

3. **Add Channels**
   - Add one or more Discord channel URLs

4. **Generate Messages**
   - Click "🔄 Regenerate Messages" to create message pool
   - Or start bot (messages auto-generate if empty)

5. **Start Bot**
   - Click "▶ Start" to begin automation
   - Bot will create worker threads for each channel (multitasking!)

6. **Control Bot**
   - **Pause**: Temporarily pause all workers
   - **Resume**: Resume from paused state
   - **Stop**: Stop all workers and close browsers

### Multitasking Explained

When you start the bot with multiple channels:
- **Each channel gets its own worker thread**
- **All channels run simultaneously and independently**
- **Each worker has its own browser instance**
- **Messages are sent in parallel across all channels**

Example:
```
Channel 1 → Worker Thread 1 → Browser 1 → Sends message every 60-100s
Channel 2 → Worker Thread 2 → Browser 2 → Sends message every 60-100s
Channel 3 → Worker Thread 3 → Browser 3 → Sends message every 60-100s
```

All three channels operate at the same time!

## 📊 Message Generation

The bot includes an intelligent message generator with:

- **Diverse Templates**: Multiple message patterns
- **Natural Variations**: Greetings, topics, questions, casual messages
- **Emoji Support**: Contextual emoji usage
- **Customization**: Easy to modify message templates

### Message Types

1. **Casual Messages**: Friendly, community-focused
2. **Conversational**: Natural discussion starters
3. **Promotional**: Product/service mentions
4. **Timestamped**: Messages with time stamps

### Customizing Messages

Edit `message_generator.py` to customize:
- Greeting phrases
- Topic templates
- Question formats
- Emoji selections
- Message templates

## 🔍 How It Works

### Architecture

```
┌─────────────────────────────────────────────────┐
│            Discord Auto Sender GUI              │
│  ┌─────────────────────────────────────────┐   │
│  │     Configuration Manager               │   │
│  │  - Paths, Ports, Delays, Modes          │   │
│  └─────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────┐   │
│  │     Channel Manager                      │   │
│  │  - Add/Remove Channels                   │   │
│  │  - Store Channel URLs                    │   │
│  └─────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────┐   │
│  │     Message Generator                    │   │
│  │  - Generate Random Messages              │   │
│  │  - Template System                       │   │
│  └─────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────┐   │
│  │     Worker Thread Manager (Multitasking)│   │
│  │  ┌───────────┐ ┌───────────┐ ┌────────┐│   │
│  │  │ Worker 1  │ │ Worker 2  │ │Worker N││   │
│  │  │ Channel 1 │ │ Channel 2 │ │Channel N││   │
│  │  │ Browser 1 │ │ Browser 2 │ │Browser N││   │
│  │  └───────────┘ └───────────┘ └────────┘│   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
           │                  │                 │
           ▼                  ▼                 ▼
     [Discord Ch 1]     [Discord Ch 2]   [Discord Ch N]
```

### Workflow

1. **Initialization**: Load config, setup UI
2. **Configuration**: User sets paths and preferences
3. **Channel Setup**: User adds Discord channel URLs
4. **Message Generation**: Create message pool
5. **Start Workers**: Launch thread for each channel
6. **Parallel Execution**: 
   - Each worker independently:
     - Navigates to its channel
     - Selects random message
     - Sends message
     - Waits random delay
     - Repeats
7. **Control & Monitor**: User can pause/resume/stop anytime

## 🛡️ Safety Features

- **Human-like Delays**: Random delays between messages (60-100s)
- **Rate Limiting**: Configurable delay ranges
- **Error Handling**: Automatic recovery from errors
- **Graceful Shutdown**: Properly closes all browser instances
- **Logging**: All actions logged for review

## ⚠️ Important Notes

### Discord Terms of Service
- **Read Discord's Terms**: https://discord.com/terms
- **Automation Policy**: Automation bots may violate Discord TOS
- **Use Responsibly**: Only use on servers you own/have permission
- **Risk**: Account may be banned for automation
- **Educational Purpose**: This tool is for learning automation concepts

### Best Practices
- ✅ Use only on test servers or servers you own
- ✅ Set reasonable delay ranges (60+ seconds)
- ✅ Don't spam channels
- ✅ Monitor bot activity
- ✅ Stop bot if issues occur
- ❌ Don't use on public servers without permission
- ❌ Don't bypass rate limits
- ❌ Don't send harmful/spam content

## 🐛 Troubleshooting

### Bot Won't Start
- ✓ Check Chrome path is correct
- ✓ Check ChromeDriver path is correct
- ✓ Verify ChromeDriver matches Chrome version
- ✓ Ensure port 9222 isn't in use
- ✓ Check if channels are added

### Messages Not Sending
- ✓ Verify you're logged into Discord in browser
- ✓ Check if message selectors are current (Discord may update)
- ✓ Look at console logs for errors
- ✓ Ensure you have permission to send messages in channel

### Multitasking Issues
- ✓ Check if system has enough resources
- ✓ Reduce number of channels if experiencing lag
- ✓ Increase delay range to reduce load

### Browser Issues
- ✓ Update Chrome to latest version
- ✓ Download matching ChromeDriver
- ✓ Close other Chrome instances
- ✓ Check remote debugging port

## 📝 Logs

Logs are saved to `discord_bot.log`:
```bash
# View logs
cat discord_bot.log

# Follow logs in real-time
tail -f discord_bot.log
```

## 🔧 Advanced Customization

### Custom Message Templates

Edit `message_generator.py`:
```python
self.custom_messages = [
    "Your custom message here",
    "Another custom message",
    # Add more...
]
```

### Adjust Worker Count

By default, 1 worker per channel. To limit workers:
```python
# In discord_auto_sender.py, modify start_workers()
max_workers = 3
for i, channel in enumerate(self.channels[:max_workers]):
    # ... worker creation code
```

### Change Selenium Selectors

If Discord updates their HTML structure:
```python
# In send_message_to_channel(), update selector:
message_box = driver.find_element(By.CSS_SELECTOR, "div[new-selector]")
```

## 📊 Performance

- **Memory**: ~100-200MB per browser instance
- **CPU**: Low usage, spikes during message sending
- **Network**: Minimal bandwidth usage
- **Recommended**: 
  - 4GB+ RAM for 5+ channels
  - Stable internet connection
  - Modern CPU (2+ cores)

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Better error handling
- More message templates
- UI enhancements
- Additional automation features
- Cross-platform testing

## 📄 License

This project is for educational purposes only. Use at your own risk.

## ⚡ Quick Start Guide

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download ChromeDriver
# https://chromedriver.chromium.org/

# 3. Run the bot
python discord_auto_sender.py

# 4. Configure in GUI:
#    - Set Chrome path
#    - Set ChromeDriver path
#    - Add Discord channels
#    - Generate messages
#    - Click Start!
```

## 🎯 Use Cases

- ✅ **Testing**: Test Discord bots on your own server
- ✅ **Community Engagement**: Automated updates for your community
- ✅ **Learning**: Understand automation and multithreading
- ✅ **Development**: Develop Discord-related tools
- ❌ **Spam**: Don't use for spam or malicious purposes

## 🌈 Features Highlight

| Feature | Description | Status |
|---------|-------------|--------|
| Multitasking | Parallel channel management | ✅ Implemented |
| Message Gen | AI-powered messages | ✅ Implemented |
| GUI | Modern dark theme UI | ✅ Implemented |
| Auto-save | Config persistence | ✅ Implemented |
| Logging | Comprehensive logs | ✅ Implemented |
| Pause/Resume | Full control | ✅ Implemented |
| Notifications | Desktop alerts | ✅ Implemented |
| Remote Debug | Port 9222 support | ✅ Implemented |

## 📞 Support

For issues or questions:
1. Check troubleshooting section
2. Review logs in `discord_bot.log`
3. Verify configuration settings
4. Test with single channel first

## 🎓 Learning Resources

- **Selenium**: https://selenium-python.readthedocs.io/
- **Threading**: https://docs.python.org/3/library/threading.html
- **Tkinter**: https://docs.python.org/3/library/tkinter.html
- **Discord API**: https://discord.com/developers/docs

---

**Remember**: Use this tool responsibly and ethically. Always respect Discord's Terms of Service and community guidelines.

**Made with ❤️ for automation enthusiasts!**
