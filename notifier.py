"""
Notification system for new airdrops
"""
import os
from typing import Dict, List
from datetime import datetime


class Notifier:
    def __init__(self):
        self.telegram_enabled = False
        self.console_enabled = True
        
        # Try to initialize Telegram bot if credentials are provided
        try:
            from telegram import Bot
            from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
            
            if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
                self.telegram_bot = Bot(token=TELEGRAM_BOT_TOKEN)
                self.telegram_chat_id = TELEGRAM_CHAT_ID
                self.telegram_enabled = True
                print("✓ Telegram notifications enabled")
        except Exception as e:
            print(f"Telegram notifications disabled: {e}")
    
    def notify(self, airdrops: List[Dict]):
        """Send notifications for new airdrops"""
        if not airdrops:
            return
        
        for airdrop in airdrops:
            if self.console_enabled:
                self._console_notify(airdrop)
            
            if self.telegram_enabled:
                self._telegram_notify(airdrop)
    
    def _console_notify(self, airdrop: Dict):
        """Print notification to console"""
        print("\n" + "="*80)
        print(f"🎁 NEW AIRDROP DETECTED")
        print("="*80)
        print(f"Title: {airdrop['title']}")
        print(f"Reliability Score: {airdrop.get('reliability_score', 'N/A')}/100")
        print(f"URL: {airdrop['url']}")
        print(f"Source: {airdrop['source']}")
        
        if airdrop.get('blockchain'):
            print(f"Blockchain: {airdrop['blockchain']}")
        
        if airdrop.get('value_estimate'):
            print(f"Estimated Value: {airdrop['value_estimate']}")
        
        if airdrop.get('description'):
            desc = airdrop['description'][:200]
            print(f"Description: {desc}...")
        
        if airdrop.get('requirements'):
            print(f"Requirements: {', '.join(airdrop['requirements'][:5])}")
        
        print("="*80 + "\n")
    
    def _telegram_notify(self, airdrop: Dict):
        """Send notification via Telegram"""
        try:
            message = self._format_telegram_message(airdrop)
            self.telegram_bot.send_message(
                chat_id=self.telegram_chat_id,
                text=message,
                parse_mode='HTML',
                disable_web_page_preview=False
            )
        except Exception as e:
            print(f"Failed to send Telegram notification: {e}")
    
    def _format_telegram_message(self, airdrop: Dict) -> str:
        """Format airdrop information for Telegram"""
        score = airdrop.get('reliability_score', 0)
        
        # Score emoji
        if score >= 80:
            score_emoji = "🟢"
        elif score >= 60:
            score_emoji = "🟡"
        else:
            score_emoji = "🔴"
        
        message = f"🎁 <b>NEW AIRDROP</b>\n\n"
        message += f"<b>{airdrop['title']}</b>\n\n"
        message += f"{score_emoji} Reliability: {score}/100\n"
        message += f"📡 Source: {airdrop['source']}\n"
        
        if airdrop.get('blockchain'):
            message += f"⛓️ Chain: {airdrop['blockchain'].title()}\n"
        
        if airdrop.get('value_estimate'):
            message += f"💰 Value: {airdrop['value_estimate']}\n"
        
        if airdrop.get('description'):
            desc = airdrop['description'][:300]
            message += f"\n📝 {desc}...\n"
        
        if airdrop.get('requirements'):
            reqs = airdrop['requirements'][:3]
            message += f"\n✅ Requirements:\n"
            for req in reqs:
                message += f"  • {req}\n"
        
        message += f"\n🔗 <a href='{airdrop['url']}'>View Airdrop</a>"
        
        return message
    
    def send_summary(self, stats: Dict):
        """Send a summary of collected airdrops"""
        if self.console_enabled:
            print("\n" + "="*80)
            print("📊 AIRDROP BOT SUMMARY")
            print("="*80)
            print(f"Total Active Airdrops: {stats.get('total_active', 0)}")
            print(f"Total Notified: {stats.get('total_notified', 0)}")
            print(f"Average Reliability: {stats.get('average_reliability', 0)}/100")
            print("="*80 + "\n")
        
        if self.telegram_enabled:
            try:
                message = f"📊 <b>Airdrop Bot Summary</b>\n\n"
                message += f"Active Airdrops: {stats.get('total_active', 0)}\n"
                message += f"Notified: {stats.get('total_notified', 0)}\n"
                message += f"Avg Reliability: {stats.get('average_reliability', 0)}/100\n"
                message += f"\nLast update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                
                self.telegram_bot.send_message(
                    chat_id=self.telegram_chat_id,
                    text=message,
                    parse_mode='HTML'
                )
            except Exception as e:
                print(f"Failed to send Telegram summary: {e}")
