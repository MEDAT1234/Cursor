"""
Web scraper for popular airdrop listing websites
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from .base_collector import BaseCollector
import time


class WebScraper(BaseCollector):
    def __init__(self):
        super().__init__("Web Scraper")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def collect(self) -> List[Dict]:
        """Collect airdrops from various websites"""
        airdrops = []
        
        # Collect from AirdropAlert.com
        airdrops.extend(self._scrape_airdrop_alert())
        
        return airdrops
    
    def _scrape_airdrop_alert(self) -> List[Dict]:
        """Scrape airdrops from AirdropAlert.com"""
        airdrops = []
        
        try:
            url = "https://airdropalert.com"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                print(f"Failed to fetch {url}: Status {response.status_code}")
                return airdrops
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find airdrop listings (this is a generic pattern, actual selectors may vary)
            airdrop_cards = soup.find_all('div', class_=['airdrop-card', 'airdrop-item'])
            
            for card in airdrop_cards[:15]:  # Limit to first 15
                try:
                    title_elem = card.find(['h2', 'h3', 'a'])
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text().strip()
                    link = title_elem.get('href', '') if title_elem.name == 'a' else ''
                    
                    if link and not link.startswith('http'):
                        link = url + link
                    
                    description_elem = card.find(['p', 'div'], class_=['description', 'excerpt'])
                    description = description_elem.get_text().strip() if description_elem else ''
                    
                    if title and link:
                        airdrop = self._create_airdrop_dict(
                            title=title,
                            url=link,
                            description=description
                        )
                        airdrops.append(airdrop)
                except Exception as e:
                    print(f"Error parsing airdrop card: {e}")
                    continue
            
            time.sleep(1)  # Be respectful with rate limiting
            
        except Exception as e:
            print(f"Error scraping AirdropAlert: {e}")
        
        return airdrops
    
    def _scrape_airdrops_io(self) -> List[Dict]:
        """Scrape airdrops from Airdrops.io"""
        airdrops = []
        
        try:
            url = "https://airdrops.io"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                return airdrops
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Generic pattern for airdrop listings
            airdrop_items = soup.find_all(['article', 'div'], class_=['airdrop', 'listing-item'])
            
            for item in airdrop_items[:15]:
                try:
                    title_elem = item.find(['h2', 'h3', 'a'])
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text().strip()
                    link = title_elem.get('href', '')
                    
                    if link and not link.startswith('http'):
                        link = url + link
                    
                    description = ''
                    desc_elem = item.find(['p', 'div'], class_=['description', 'summary'])
                    if desc_elem:
                        description = desc_elem.get_text().strip()
                    
                    if title and link:
                        airdrop = self._create_airdrop_dict(
                            title=title,
                            url=link,
                            description=description
                        )
                        airdrops.append(airdrop)
                except Exception as e:
                    continue
            
            time.sleep(1)
            
        except Exception as e:
            print(f"Error scraping Airdrops.io: {e}")
        
        return airdrops
