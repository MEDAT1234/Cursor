"""
Configuration settings for the Airdrop Capture Bot
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_PATH = os.getenv('DATABASE_PATH', 'airdrops.db')

# Telegram Bot Configuration (optional, for notifications)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

# Twitter/X API Configuration (optional)
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN', '')

# Update interval (in minutes)
UPDATE_INTERVAL = int(os.getenv('UPDATE_INTERVAL', '30'))

# Minimum reliability score (0-100)
MIN_RELIABILITY_SCORE = int(os.getenv('MIN_RELIABILITY_SCORE', '60'))

# Data Sources Configuration
ENABLE_WEB_SCRAPING = os.getenv('ENABLE_WEB_SCRAPING', 'true').lower() == 'true'
ENABLE_RSS_FEEDS = os.getenv('ENABLE_RSS_FEEDS', 'true').lower() == 'true'
ENABLE_TWITTER = os.getenv('ENABLE_TWITTER', 'false').lower() == 'true'

# RSS Feed sources for airdrops
RSS_FEEDS = [
    'https://cryptopotato.com/feed/',
    'https://airdropalert.com/feed',
]

# Web scraping sources
WEB_SOURCES = [
    'https://airdrops.io',
    'https://airdropalert.com',
]

# Blacklisted keywords (scam indicators)
BLACKLIST_KEYWORDS = [
    'send eth', 'send btc', 'private key', 'seed phrase',
    'password', 'double your', 'guaranteed profit',
    'elon musk giveaway', 'official giveaway'
]

# Trusted project indicators
TRUSTED_INDICATORS = [
    'verified', 'official', 'mainnet', 'testnet',
    'github', 'audit', 'whitepaper', 'team'
]
