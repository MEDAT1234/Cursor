#!/usr/bin/env python3
"""
Cryptocurrency Airdrop Capture Bot
Main orchestrator for collecting, filtering, and notifying about airdrops
"""
import time
import schedule
from datetime import datetime
from typing import List, Dict

from database import AirdropDatabase
from filters import AirdropFilter
from notifier import Notifier
from collectors import WebScraper, RSSCollector
from config import (
    UPDATE_INTERVAL, MIN_RELIABILITY_SCORE,
    ENABLE_WEB_SCRAPING, ENABLE_RSS_FEEDS
)


class AirdropBot:
    def __init__(self):
        print("🚀 Initializing Airdrop Capture Bot...")
        
        self.database = AirdropDatabase()
        self.filter = AirdropFilter()
        self.notifier = Notifier()
        
        # Initialize collectors
        self.collectors = []
        
        if ENABLE_RSS_FEEDS:
            self.collectors.append(RSSCollector())
            print("✓ RSS Feed collector enabled")
        
        if ENABLE_WEB_SCRAPING:
            self.collectors.append(WebScraper())
            print("✓ Web scraper enabled")
        
        if not self.collectors:
            print("⚠️  Warning: No collectors enabled! Check your configuration.")
        
        print(f"✓ Minimum reliability score: {MIN_RELIABILITY_SCORE}/100")
        print(f"✓ Update interval: {UPDATE_INTERVAL} minutes")
        print("\n" + "="*80)
    
    def collect_airdrops(self) -> List[Dict]:
        """Collect airdrops from all enabled sources"""
        all_airdrops = []
        
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Collecting airdrops...")
        
        for collector in self.collectors:
            try:
                print(f"  → Collecting from {collector.name}...")
                airdrops = collector.collect()
                all_airdrops.extend(airdrops)
                print(f"    Found {len(airdrops)} potential airdrops")
            except Exception as e:
                print(f"    Error: {e}")
        
        print(f"Total collected: {len(all_airdrops)} airdrops")
        return all_airdrops
    
    def filter_airdrops(self, airdrops: List[Dict]) -> List[Dict]:
        """Filter airdrops based on reliability criteria"""
        reliable_airdrops = []
        
        print(f"Filtering airdrops (min score: {MIN_RELIABILITY_SCORE})...")
        
        for airdrop in airdrops:
            # Calculate reliability score
            score = self.filter.calculate_reliability_score(airdrop)
            airdrop['reliability_score'] = score
            
            # Extract additional information
            description = airdrop.get('description', '')
            airdrop['requirements'] = self.filter.extract_requirements(description)
            airdrop['blockchain'] = self.filter.extract_blockchain(description)
            
            # Check if it meets reliability threshold
            if self.filter.is_reliable(airdrop, MIN_RELIABILITY_SCORE):
                reliable_airdrops.append(airdrop)
        
        print(f"  → {len(reliable_airdrops)} airdrops passed reliability filter")
        return reliable_airdrops
    
    def process_new_airdrops(self, airdrops: List[Dict]):
        """Process and store new airdrops"""
        new_count = 0
        
        for airdrop in airdrops:
            if self.database.add_airdrop(airdrop):
                new_count += 1
        
        if new_count > 0:
            print(f"  → {new_count} new airdrops added to database")
        else:
            print("  → No new airdrops found")
        
        return new_count
    
    def notify_new_airdrops(self):
        """Send notifications for unnotified airdrops"""
        unnotified = self.database.get_unnotified_airdrops()
        
        if unnotified:
            print(f"Sending notifications for {len(unnotified)} new airdrops...")
            self.notifier.notify(unnotified)
            
            # Mark as notified
            for airdrop in unnotified:
                self.database.mark_as_notified(airdrop['id'])
        else:
            print("No new airdrops to notify")
    
    def run_cycle(self):
        """Run one complete collection cycle"""
        try:
            print("\n" + "="*80)
            print(f"🔄 Starting collection cycle")
            print("="*80)
            
            # Step 1: Collect
            airdrops = self.collect_airdrops()
            
            if not airdrops:
                print("No airdrops collected this cycle")
                return
            
            # Step 2: Filter
            reliable_airdrops = self.filter_airdrops(airdrops)
            
            # Step 3: Store
            new_count = self.process_new_airdrops(reliable_airdrops)
            
            # Step 4: Notify
            if new_count > 0:
                self.notify_new_airdrops()
            
            # Step 5: Show stats
            stats = self.database.get_stats()
            print("\n📊 Current Statistics:")
            print(f"  Total active airdrops: {stats['total_active']}")
            print(f"  Average reliability: {stats['average_reliability']}/100")
            
            print("\n✅ Collection cycle completed")
            print("="*80 + "\n")
            
        except Exception as e:
            print(f"❌ Error during collection cycle: {e}")
    
    def run_once(self):
        """Run a single collection cycle"""
        self.run_cycle()
    
    def run_continuous(self):
        """Run the bot continuously with scheduled intervals"""
        print(f"\n🤖 Starting continuous mode (updates every {UPDATE_INTERVAL} minutes)")
        print("Press Ctrl+C to stop\n")
        
        # Run immediately on start
        self.run_cycle()
        
        # Schedule regular updates
        schedule.every(UPDATE_INTERVAL).minutes.do(self.run_cycle)
        
        # Keep running
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\n👋 Stopping bot...")
            stats = self.database.get_stats()
            self.notifier.send_summary(stats)
            print("Bot stopped. Goodbye!")
    
    def show_stats(self):
        """Display current statistics"""
        stats = self.database.get_stats()
        airdrops = self.database.get_all_airdrops(active_only=True)
        
        print("\n" + "="*80)
        print("📊 AIRDROP BOT STATISTICS")
        print("="*80)
        print(f"Total Active Airdrops: {stats['total_active']}")
        print(f"Total Notified: {stats['total_notified']}")
        print(f"Average Reliability Score: {stats['average_reliability']}/100")
        print("="*80)
        
        if airdrops:
            print("\n🎁 Top 10 Airdrops by Reliability:\n")
            for i, airdrop in enumerate(airdrops[:10], 1):
                print(f"{i}. {airdrop['title']}")
                print(f"   Score: {airdrop['reliability_score']}/100 | {airdrop['blockchain']}")
                print(f"   {airdrop['url']}\n")


def main():
    """Main entry point"""
    import sys
    
    bot = AirdropBot()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'once':
            bot.run_once()
        elif command == 'stats':
            bot.show_stats()
        elif command == 'continuous':
            bot.run_continuous()
        else:
            print(f"Unknown command: {command}")
            print("Usage: python bot.py [once|continuous|stats]")
    else:
        # Default: run continuous mode
        bot.run_continuous()


if __name__ == "__main__":
    main()
