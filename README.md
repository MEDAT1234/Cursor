# Old Wallet Mnemonic Phrase Generator Bot

A Discord bot that generates BIP39 mnemonic phrases for old cryptocurrency wallet recovery.

## Features

- 🔐 Generate secure BIP39 mnemonic phrases
- 🎯 Support for multiple word counts (12, 15, 18, 21, 24 words)
- 💬 Sends phrases via DM for enhanced security
- ⚠️ Built-in security warnings and best practices
- 📚 Information command to learn about mnemonic phrases

## Commands

### `!generate-phrase [word_count]`
Generates a BIP39 mnemonic phrase for old wallet recovery.

**Usage:**
```
!generate-phrase          # Generates 12-word phrase (default)
!generate-phrase 12       # Generates 12-word phrase
!generate-phrase 24       # Generates 24-word phrase
```

**Supported word counts:** 12, 15, 18, 21, 24

### `!phrase-info`
Displays information about mnemonic phrases and their usage.

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- A Discord Bot Token ([Create one here](https://discord.com/developers/applications))

### 2. Installation

```bash
# Clone or navigate to the project directory
cd /workspace

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your Discord bot token:

```
DISCORD_BOT_TOKEN=your_actual_bot_token_here
```

### 4. Getting a Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot"
5. Under "Token", click "Copy" to copy your bot token
6. Enable "Message Content Intent" under "Privileged Gateway Intents"
7. Go to OAuth2 → URL Generator
8. Select scopes: `bot`
9. Select permissions: `Send Messages`, `Read Message History`
10. Copy the generated URL and use it to invite the bot to your server

### 5. Running the Bot

```bash
python bot.py
```

You should see:
```
<BotName> has connected to Discord!
Bot is ready to generate mnemonic phrases
```

## Security Notice

⚠️ **IMPORTANT SECURITY WARNINGS:**

- **Never share** generated mnemonic phrases with anyone
- **Store phrases securely** offline in a safe location
- **Delete Discord messages** containing phrases after saving them
- This bot generates **real cryptographic keys** - treat them as you would real money
- The bot sends phrases via DM to minimize exposure
- **For recovery purposes only** - use these phrases responsibly

## Technical Details

- **Standard:** BIP39 (Bitcoin Improvement Proposal 39)
- **Language:** English wordlist
- **Entropy Levels:**
  - 12 words = 128 bits
  - 15 words = 160 bits
  - 18 words = 192 bits
  - 21 words = 224 bits
  - 24 words = 256 bits

## Compatibility

These mnemonic phrases are compatible with old wallets that support the BIP39 standard, including:
- Bitcoin Core (with BIP39 support)
- Electrum (BIP39 mode)
- MetaMask
- Trust Wallet
- Ledger & Trezor hardware wallets
- Most modern cryptocurrency wallets

## License

This project is open source and available for wallet recovery purposes.

## Disclaimer

This tool is provided for wallet recovery purposes only. The developers are not responsible for any loss of funds or misuse of generated mnemonic phrases. Always keep your seed phrases secure and never share them with anyone.