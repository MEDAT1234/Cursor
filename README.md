# 🎵 ASMR TikTok Automation Bot

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

An intelligent automation bot that generates high-quality ASMR videos and automatically posts them to TikTok without any manual intervention.

## ✨ Features

- 🎬 **Automated Video Generation**: Creates stunning ASMR videos with custom visuals
- 🔊 **5 ASMR Types**: Rain, Fire, Ocean Waves, Keyboard Typing, and Whisper sounds
- 🎨 **Beautiful Visuals**: Animated gradients and particle effects
- 📱 **Auto-Posting**: Automatically uploads to TikTok with captions and hashtags
- ⏰ **Scheduling**: Set multiple posting times throughout the day
- 🤖 **100% Automated**: No intervention needed after setup
- 📊 **Logging**: Tracks all activities and errors
- 🎯 **SEO Optimized**: Auto-generated captions with trending hashtags

## 🎥 ASMR Types

The bot generates the following types of ASMR content:

1. **Rain Sounds** 🌧️ - Relaxing rain with occasional droplets
2. **Fire Crackling** 🔥 - Cozy fireplace ambiance
3. **Ocean Waves** 🌊 - Peaceful beach sounds
4. **Keyboard Typing** ⌨️ - Satisfying mechanical keyboard ASMR
5. **Soft Whispers** 💜 - Gentle breathing and whisper sounds

Each video includes:
- Custom animated gradient background
- Professional text overlays
- Auto-generated captions
- Trending hashtags
- 15-60 second duration (configurable)
- Vertical format (1080x1920) perfect for TikTok

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- TikTok account
- Linux, macOS, or Windows

### Installation

#### Linux/macOS

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Run setup script
chmod +x setup.sh
./setup.sh

# Edit configuration
nano .env
```

#### Windows

```batch
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Run setup script
setup.bat

# Edit configuration
notepad .env
```

### Configuration

Edit the `.env` file with your settings:

```env
# TikTok Credentials (optional - will prompt for login if not provided)
TIKTOK_SESSION_ID=your_session_id_here
TIKTOK_USERNAME=your_username_here

# Video Settings
VIDEO_WIDTH=1080
VIDEO_HEIGHT=1920
VIDEO_DURATION=15
FPS=30

# Posting Schedule (24-hour format, comma-separated)
POST_TIMES=09:00,14:00,20:00

# ASMR Settings
ASMR_TYPES=rain,fire,waves,typing,whisper
```

## 📖 Usage

### Test Mode (Recommended First)

Test video generation without uploading:

```bash
# Linux/macOS
source venv/bin/activate
python3 bot.py --mode test

# Windows
venv\Scripts\activate.bat
python bot.py --mode test
```

### One-Time Post

Generate and post a single video:

```bash
python3 bot.py --mode once
```

### Scheduled Mode (Automated)

Run the bot with scheduled posting:

```bash
# Linux/macOS
./start_bot.sh

# Windows
start_bot.bat

# Or manually:
python3 bot.py --mode scheduled
```

The bot will:
1. Run continuously in the background
2. Generate videos at scheduled times
3. Automatically post to TikTok
4. Log all activities to `bot.log`

## 🔐 TikTok Authentication

### First Time Setup

On first run, the bot will:
1. Open a browser window
2. Navigate to TikTok login page
3. Wait for you to login manually
4. Extract and save your session ID

### Subsequent Runs

Once you have the session ID:
1. Add it to your `.env` file
2. The bot will login automatically
3. No manual intervention needed

### Session Management

- Sessions typically last 30-90 days
- If login fails, delete `TIKTOK_SESSION_ID` from `.env`
- The bot will prompt for manual login again

## 📁 Project Structure

```
.
├── bot.py                  # Main automation script
├── asmr_generator.py       # Audio generation module
├── video_generator.py      # Video creation module
├── tiktok_uploader.py      # TikTok upload module
├── requirements.txt        # Python dependencies
├── .env                    # Configuration (create from .env.example)
├── .env.example           # Configuration template
├── setup.sh               # Linux/macOS setup script
├── setup.bat              # Windows setup script
├── start_bot.sh           # Linux/macOS start script
├── start_bot.bat          # Windows start script
├── generated_videos/      # Output directory for videos
└── bot.log               # Activity log file
```

## 🛠️ Advanced Configuration

### Custom Video Settings

Edit `bot.py` or pass environment variables:

```python
# Video dimensions
VIDEO_WIDTH=1080      # Width in pixels
VIDEO_HEIGHT=1920     # Height in pixels

# Video duration
VIDEO_DURATION=15     # Duration in seconds (15-60)

# Frame rate
FPS=30               # Frames per second (24-60)
```

### Custom Posting Schedule

Add multiple posting times in `.env`:

```env
# Post 4 times a day
POST_TIMES=08:00,12:00,17:00,21:00

# Post every 2 hours
POST_TIMES=00:00,02:00,04:00,06:00,08:00,10:00,12:00,14:00,16:00,18:00,20:00,22:00
```

### Select Specific ASMR Types

Customize which sounds to generate:

```env
# Only rain and waves
ASMR_TYPES=rain,waves

# All types
ASMR_TYPES=rain,fire,waves,typing,whisper
```

## 🐳 Running with Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium --with-deps

COPY . .

CMD ["python", "bot.py", "--mode", "scheduled"]
```

Build and run:

```bash
docker build -t asmr-bot .
docker run -d --name asmr-bot -v $(pwd)/.env:/app/.env asmr-bot
```

## 📊 Monitoring

### Check Logs

```bash
# View real-time logs
tail -f bot.log

# View last 50 lines
tail -n 50 bot.log
```

### Log Contents

The bot logs:
- Video generation status
- Upload attempts and results
- Error messages with stack traces
- Statistics (videos generated, uploaded, errors)
- Scheduled job execution

### Statistics

The bot tracks:
- Total videos generated
- Total videos uploaded
- Number of errors
- Last successful post time

## 🔧 Troubleshooting

### Common Issues

**Video generation fails:**
```bash
# Install system dependencies
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from: https://ffmpeg.org/download.html
```

**Playwright browser fails:**
```bash
# Reinstall browsers
playwright install chromium
playwright install-deps chromium
```

**TikTok upload fails:**
- Check your session ID is valid
- Try manual login again
- Check internet connection
- Verify TikTok account is not restricted

**Permission denied on scripts:**
```bash
# Linux/macOS
chmod +x setup.sh start_bot.sh
```

### Debug Mode

Run with verbose logging:

```bash
# Add debug logging
export LOG_LEVEL=DEBUG
python3 bot.py --mode test
```

## 🎯 Best Practices

1. **Test First**: Always run `--mode test` before scheduling
2. **Monitor Initially**: Watch the first few posts to ensure everything works
3. **Optimal Posting Times**: Post during peak hours (9am, 2pm, 8pm)
4. **Consistency**: Keep a regular posting schedule
5. **Variety**: Enable all ASMR types for diverse content
6. **Backup Session**: Save your `TIKTOK_SESSION_ID` securely

## ⚠️ Important Notes

- **TikTok Terms**: Ensure automation complies with TikTok's terms of service
- **Rate Limits**: Don't post too frequently (recommended: 3-5 times per day)
- **Content Quality**: The bot generates high-quality content, but monitor performance
- **Account Safety**: Use a dedicated account for automation
- **Session Security**: Keep your session ID private and secure

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- MoviePy for video editing
- Playwright for browser automation
- NumPy and SciPy for audio generation
- The ASMR community for inspiration

## 📧 Support

For issues, questions, or suggestions:

1. Check the troubleshooting section
2. Review existing issues
3. Create a new issue with details

## 🚀 Future Enhancements

- [ ] AI-generated ASMR voice-overs
- [ ] More visual effects and themes
- [ ] Instagram and YouTube Shorts support
- [ ] Analytics dashboard
- [ ] Custom audio library support
- [ ] Multi-account management
- [ ] Cloud deployment guides

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Made with ❤️ for the ASMR community**

*Automate your content creation and grow your TikTok presence effortlessly!*
