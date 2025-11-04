"""
RSS Feed collector for airdrop information
"""
import feedparser
from typing import List, Dict
from .base_collector import BaseCollector
from config import RSS_FEEDS


class RSSCollector(BaseCollector):
    def __init__(self):
        super().__init__("RSS Feeds")
        self.feeds = RSS_FEEDS
    
    def collect(self) -> List[Dict]:
        """Collect airdrops from RSS feeds"""
        airdrops = []
        
        for feed_url in self.feeds:
            try:
                feed = feedparser.parse(feed_url)
                
                for entry in feed.entries[:10]:  # Limit to recent 10 entries
                    # Filter for airdrop-related content
                    if self._is_airdrop_related(entry):
                        airdrop = self._create_airdrop_dict(
                            title=entry.get('title', ''),
                            url=entry.get('link', ''),
                            description=self._clean_description(entry.get('summary', '')),
                            end_date=entry.get('published', '')
                        )
                        airdrops.append(airdrop)
            except Exception as e:
                print(f"Error collecting from RSS feed {feed_url}: {e}")
        
        return airdrops
    
    def _is_airdrop_related(self, entry: Dict) -> bool:
        """Check if an RSS entry is related to airdrops"""
        airdrop_keywords = ['airdrop', 'token distribution', 'free tokens', 'claim', 'giveaway']
        
        title = entry.get('title', '').lower()
        summary = entry.get('summary', '').lower()
        
        return any(keyword in title or keyword in summary for keyword in airdrop_keywords)
    
    def _clean_description(self, html_text: str) -> str:
        """Remove HTML tags from description"""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup.get_text().strip()[:500]  # Limit to 500 chars
