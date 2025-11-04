"""
Base collector class for all airdrop data sources
"""
from abc import ABC, abstractmethod
from typing import List, Dict


class BaseCollector(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def collect(self) -> List[Dict]:
        """
        Collect airdrops from the data source
        Returns a list of airdrop dictionaries
        """
        pass
    
    def _create_airdrop_dict(self, title: str, url: str, description: str = '', **kwargs) -> Dict:
        """Helper method to create a standardized airdrop dictionary"""
        return {
            'title': title,
            'url': url,
            'description': description,
            'source': self.name,
            **kwargs
        }
