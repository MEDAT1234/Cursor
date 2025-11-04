import discord
from discord.ext import commands
from mnemonic import Mnemonic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready to generate mnemonic phrases')

@bot.command(name='generate-phrase', help='Generates a mnemonic phrase for old wallet recovery')
async def generate_phrase(ctx, word_count: int = 12):
    """
    Generate a BIP39 mnemonic phrase for old wallet recovery
    Usage: !generate-phrase [12|15|18|21|24]
    Default: 12 words
    """
    # Validate word count
    valid_counts = [12, 15, 18, 21, 24]
    if word_count not in valid_counts:
        await ctx.send(f"❌ Invalid word count. Please choose from: {', '.join(map(str, valid_counts))}")
        return
    
    try:
        # Generate mnemonic phrase
        mnemo = Mnemonic("english")
        
        # Calculate strength based on word count
        # 12 words = 128 bits, 15 = 160, 18 = 192, 21 = 224, 24 = 256
        strength_map = {
            12: 128,
            15: 160,
            18: 192,
            21: 224,
            24: 256
        }
        strength = strength_map[word_count]
        
        # Generate the mnemonic
        mnemonic_phrase = mnemo.generate(strength=strength)
        
        # Create an embed for better presentation
        embed = discord.Embed(
            title="🔐 Mnemonic Phrase Generated",
            description="**IMPORTANT:** Keep this phrase secure and private!",
            color=discord.Color.gold()
        )
        
        embed.add_field(
            name=f"Your {word_count}-word Mnemonic Phrase:",
            value=f"||{mnemonic_phrase}||",
            inline=False
        )
        
        embed.add_field(
            name="⚠️ Security Warning",
            value=(
                "• Never share this phrase with anyone\n"
                "• Store it in a secure location\n"
                "• This phrase provides full access to your wallet\n"
                "• Delete this message after saving the phrase"
            ),
            inline=False
        )
        
        embed.set_footer(text="BIP39 Standard | Old Wallet Compatible")
        
        # Send as DM for security
        try:
            await ctx.author.send(embed=embed)
            await ctx.send("✅ Mnemonic phrase sent to your DMs for security!")
        except discord.Forbidden:
            # If DM fails, send in channel with warning
            await ctx.send(
                "⚠️ **WARNING:** Could not DM you. Sending here (DELETE THIS MESSAGE AFTER SAVING!):",
                embed=embed
            )
            
    except Exception as e:
        await ctx.send(f"❌ Error generating mnemonic: {str(e)}")
        print(f"Error: {e}")

@bot.command(name='phrase-info', help='Information about mnemonic phrases')
async def phrase_info(ctx):
    """Display information about BIP39 mnemonic phrases"""
    embed = discord.Embed(
        title="📚 Mnemonic Phrase Information",
        description="BIP39 mnemonic phrases for cryptocurrency wallets",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="What is a Mnemonic Phrase?",
        value=(
            "A mnemonic phrase (or seed phrase) is a list of words that store "
            "all the information needed to recover a cryptocurrency wallet."
        ),
        inline=False
    )
    
    embed.add_field(
        name="Word Count Options",
        value=(
            "• **12 words** - 128 bits of entropy (most common)\n"
            "• **15 words** - 160 bits of entropy\n"
            "• **18 words** - 192 bits of entropy\n"
            "• **21 words** - 224 bits of entropy\n"
            "• **24 words** - 256 bits of entropy (maximum security)"
        ),
        inline=False
    )
    
    embed.add_field(
        name="Usage",
        value="`!generate-phrase [12|15|18|21|24]`\nExample: `!generate-phrase 12`",
        inline=False
    )
    
    embed.set_footer(text="Compatible with old wallets using BIP39 standard")
    
    await ctx.send(embed=embed)

# Run the bot
if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not TOKEN:
        print("Error: DISCORD_BOT_TOKEN not found in environment variables!")
        print("Please create a .env file with your bot token")
        exit(1)
    
    bot.run(TOKEN)
