# Cryptocurrency Airdrop Capture Bot 🚀

An automated bot that captures exclusive and reliable cryptocurrency airdrops from multiple sources, filters them for legitimacy, and notifies you about new opportunities.

## Features ✨

- **Multiple Data Sources**: Collects airdrops from RSS feeds and web scraping
- **Smart Filtering**: Analyzes airdrops with a reliability scoring system (0-100)
- **Scam Detection**: Automatically filters out suspicious airdrops using blacklist keywords
- **Database Storage**: Stores all discovered airdrops in a SQLite database
- **Notifications**: Console and Telegram notifications for new airdrops
- **Blockchain Detection**: Automatically identifies the blockchain (Ethereum, Solana, etc.)
- **Requirement Extraction**: Parses and lists airdrop participation requirements
- **Scheduled Updates**: Runs continuously with configurable update intervals

## Prerequisites 📋

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection

## Step-by-Step Installation Guide 🔧

### Step 1: Clone or Download the Repository

If you haven't already, navigate to the project directory in your terminal:

```bash
cd /workspace
```

### Step 2: Install Python Dependencies

Install all required packages using pip:

```bash
pip install -r requirements.txt
```

**What gets installed:**
- `requests` - For making HTTP requests
- `beautifulsoup4` - For web scraping
- `feedparser` - For parsing RSS feeds
- `python-telegram-bot` - For Telegram notifications (optional)
- `schedule` - For scheduling periodic updates
- `python-dotenv` - For environment variable management
- `lxml` - For HTML/XML parsing

### Step 3: Configure the Bot

Create a configuration file by copying the example:

```bash
cp .env.example .env
```

Open the `.env` file in a text editor and customize your settings:

```bash
# Use any text editor, for example:
nano .env
# or
vim .env
# or open in your preferred editor
```

**Basic Configuration (Required):**
```env
DATABASE_PATH=airdrops.db
UPDATE_INTERVAL=30
MIN_RELIABILITY_SCORE=60
ENABLE_WEB_SCRAPING=true
ENABLE_RSS_FEEDS=true
```

**Optional: Telegram Notifications**

To receive notifications via Telegram:

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow the instructions to create your bot
3. Copy the bot token you receive
4. Search for `@userinfobot` on Telegram
5. Send `/start` to get your Chat ID
6. Add these to your `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### Step 4: Test the Installation

Run a single collection cycle to test everything works:

```bash
python bot.py once
```

You should see output like:
```
🚀 Initializing Airdrop Capture Bot...
✓ RSS Feed collector enabled
✓ Web scraper enabled
✓ Minimum reliability score: 60/100
✓ Update interval: 30 minutes
================================================================================
🔄 Starting collection cycle
...
```

## Running the Bot 🤖

### Option 1: Continuous Mode (Recommended)

Run the bot continuously with automatic updates every X minutes (configured in `.env`):

```bash
python bot.py continuous
```

The bot will:
- Run immediately on start
- Continue running and check for new airdrops every 30 minutes (or your configured interval)
- Display notifications in the console
- Send Telegram notifications if configured

**To stop the bot:** Press `Ctrl+C`

### Option 2: Single Run Mode

Run the bot once and exit:

```bash
python bot.py once
```

Use this for:
- Testing
- Manual checks
- Running via cron jobs

### Option 3: View Statistics

View current statistics without running a collection:

```bash
python bot.py stats
```

## Running in the Background 🔄

### Linux/Mac (using nohup)

```bash
nohup python bot.py continuous > bot.log 2>&1 &
```

To stop:
```bash
ps aux | grep bot.py
kill <process_id>
```

### Linux/Mac (using screen)

```bash
# Start a screen session
screen -S airdrop-bot

# Run the bot
python bot.py continuous

# Detach from screen: Press Ctrl+A then D

# Reattach later
screen -r airdrop-bot
```

### Windows (using PowerShell)

```powershell
Start-Process python -ArgumentList "bot.py continuous" -WindowStyle Hidden
```

### Using systemd (Linux - Production)

Create a service file:

```bash
sudo nano /etc/systemd/system/airdrop-bot.service
```

Add this content (adjust paths):

```ini
[Unit]
Description=Cryptocurrency Airdrop Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/workspace
ExecStart=/usr/bin/python3 /workspace/bot.py continuous
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable airdrop-bot
sudo systemctl start airdrop-bot

# Check status
sudo systemctl status airdrop-bot

# View logs
sudo journalctl -u airdrop-bot -f
```

## Configuration Options ⚙️

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_PATH` | `airdrops.db` | Path to SQLite database file |
| `UPDATE_INTERVAL` | `30` | Minutes between collection cycles |
| `MIN_RELIABILITY_SCORE` | `60` | Minimum score (0-100) for airdrops |
| `ENABLE_WEB_SCRAPING` | `true` | Enable web scraping collector |
| `ENABLE_RSS_FEEDS` | `true` | Enable RSS feed collector |
| `ENABLE_TWITTER` | `false` | Enable Twitter monitoring (requires API key) |
| `TELEGRAM_BOT_TOKEN` | - | Your Telegram bot token |
| `TELEGRAM_CHAT_ID` | - | Your Telegram chat ID |

### Reliability Scoring

The bot calculates a reliability score (0-100) for each airdrop based on:

**Positive Indicators (+points):**
- Trusted keywords: verified, official, mainnet, testnet, github, audit, whitepaper
- Valid URL structure
- Detailed description (>100 chars)
- Known blockchain mentioned
- Clear requirements listed
- Social media verification requirements

**Negative Indicators (-points):**
- Blacklisted keywords: "send eth", "private key", "seed phrase", "double your"
- Suspicious URL patterns
- Unrealistic return promises (10x, 100x)
- Request to send cryptocurrency

Only airdrops meeting the `MIN_RELIABILITY_SCORE` threshold are stored and notified.

## Understanding the Output 📊

### Console Notifications

When a new airdrop is found:

```
================================================================================
🎁 NEW AIRDROP DETECTED
================================================================================
Title: Example Protocol Airdrop
Reliability Score: 75/100
URL: https://example.com/airdrop
Source: RSS Feeds
Blockchain: ethereum
Description: Complete testnet tasks to qualify...
Requirements: follow twitter, join discord, connect wallet
================================================================================
```

### Database

All airdrops are stored in `airdrops.db` (SQLite). You can query it:

```bash
sqlite3 airdrops.db "SELECT title, reliability_score, url FROM airdrops ORDER BY reliability_score DESC LIMIT 10;"
```

## Troubleshooting 🔧

### "No module named 'X'" Error

Install missing dependencies:
```bash
pip install -r requirements.txt
```

### "No collectors enabled" Warning

Check your `.env` file and ensure at least one collector is enabled:
```env
ENABLE_WEB_SCRAPING=true
ENABLE_RSS_FEEDS=true
```

### Web Scraping Returns No Results

This can happen if websites change their structure. The bot includes fallback mechanisms and will continue with other sources.

### Telegram Notifications Not Working

1. Verify your bot token is correct
2. Ensure you've started a chat with your bot (send `/start`)
3. Verify your chat ID is correct
4. Check the console for error messages

### Permission Errors

On Linux/Mac, you may need to make the bot executable:
```bash
chmod +x bot.py
```

## Advanced Usage 🚀

### Customizing Data Sources

Edit `config.py` to add or modify RSS feeds and web sources:

```python
RSS_FEEDS = [
    'https://cryptopotato.com/feed/',
    'https://your-custom-feed.com/rss',
]
```

### Adjusting Filters

Modify blacklist and trusted keywords in `config.py`:

```python
BLACKLIST_KEYWORDS = [
    'send eth', 'private key', 'your-custom-keyword'
]

TRUSTED_INDICATORS = [
    'verified', 'official', 'your-trusted-term'
]
```

### Scheduling with Cron (Linux/Mac)

Edit crontab:
```bash
crontab -e
```

Add this line to run every hour:
```
0 * * * * cd /workspace && /usr/bin/python3 bot.py once >> /tmp/airdrop-bot.log 2>&1
```

## Project Structure 📁

```
/workspace/
├── bot.py                 # Main bot orchestrator
├── config.py             # Configuration settings
├── database.py           # Database management
├── filters.py            # Airdrop filtering logic
├── notifier.py           # Notification system
├── requirements.txt      # Python dependencies
├── .env.example          # Example configuration
├── .env                  # Your configuration (create this)
├── airdrops.db          # SQLite database (created automatically)
├── collectors/
│   ├── __init__.py
│   ├── base_collector.py    # Base collector class
│   ├── rss_collector.py     # RSS feed collector
│   └── web_scraper.py       # Web scraping collector
└── README.md            # This file
```

## Security & Best Practices 🔒

1. **Never share your private keys or seed phrases** with any airdrop
2. **Always verify airdrops** on official project channels before participating
3. **Use a separate wallet** for airdrops (not your main holdings)
4. **Be cautious** of airdrops requiring you to send cryptocurrency
5. **Research projects** thoroughly before connecting your wallet
6. **Keep your `.env` file secure** and never commit it to version control

## Limitations ⚠️

- Web scraping may break if websites change their structure
- RSS feeds depend on third-party sources being available
- Reliability scoring is automated and should be verified manually
- Not all legitimate airdrops may be captured
- Some websites may block automated access

## Contributing 🤝

Feel free to customize the bot for your needs:
- Add new collectors for additional data sources
- Improve the filtering algorithm
- Add new notification methods (email, Discord, etc.)
- Enhance the reliability scoring system

## Support 💬

If you encounter issues:
1. Check the troubleshooting section above
2. Review the console output for error messages
3. Verify your `.env` configuration
4. Ensure all dependencies are installed correctly

## Disclaimer ⚠️

This bot is for informational purposes only. Always do your own research (DYOR) before participating in any airdrop. The bot's reliability scoring is automated and not a guarantee of legitimacy. Never share private keys, seed phrases, or send cryptocurrency to participate in airdrops.

---

**Happy Airdrop Hunting! 🎁**
