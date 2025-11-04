"""
Filtering system to identify reliable and legitimate airdrops
"""
import re
from typing import Dict, List
from config import BLACKLIST_KEYWORDS, TRUSTED_INDICATORS


class AirdropFilter:
    def __init__(self):
        self.blacklist_keywords = [keyword.lower() for keyword in BLACKLIST_KEYWORDS]
        self.trusted_indicators = [indicator.lower() for indicator in TRUSTED_INDICATORS]
    
    def calculate_reliability_score(self, airdrop: Dict) -> int:
        """
        Calculate a reliability score (0-100) for an airdrop
        Higher score = more reliable
        """
        score = 50  # Start with neutral score
        
        title = airdrop.get('title', '').lower()
        description = airdrop.get('description', '').lower()
        url = airdrop.get('url', '').lower()
        
        combined_text = f"{title} {description} {url}"
        
        # Check for blacklisted keywords (scam indicators)
        for keyword in self.blacklist_keywords:
            if keyword in combined_text:
                score -= 15
        
        # Check for trusted indicators
        trusted_count = 0
        for indicator in self.trusted_indicators:
            if indicator in combined_text:
                trusted_count += 1
                score += 5
        
        # Bonus for multiple trusted indicators
        if trusted_count >= 3:
            score += 10
        
        # Check for proper URL structure
        if self._is_valid_url(url):
            score += 5
        
        # Check for detailed description
        if len(description) > 100:
            score += 5
        
        # Check for blockchain mention
        if any(chain in combined_text for chain in ['ethereum', 'polygon', 'arbitrum', 'optimism', 'solana', 'bsc', 'avalanche']):
            score += 5
        
        # Check for requirements (legitimate airdrops usually have clear requirements)
        requirements = airdrop.get('requirements', [])
        if requirements and len(requirements) > 0:
            score += 5
        
        # Penalty for suspicious patterns
        if re.search(r'\d{2,}x|x\d{2,}', combined_text):  # "10x", "100x" returns
            score -= 10
        
        if re.search(r'send\s+\d+', combined_text):  # "send 0.1 ETH"
            score -= 20
        
        # Check for social media verification requirements (common in legitimate airdrops)
        if any(social in combined_text for social in ['twitter', 'discord', 'telegram', 'follow', 'retweet']):
            score += 5
        
        # Ensure score is within bounds
        return max(0, min(100, score))
    
    def _is_valid_url(self, url: str) -> bool:
        """Check if URL looks legitimate"""
        # Basic URL validation
        if not url.startswith(('http://', 'https://')):
            return False
        
        # Check for suspicious TLDs or patterns
        suspicious_patterns = ['.ru', '.tk', '.ml', '.ga', '.cf', 'bit.ly', 'tinyurl']
        return not any(pattern in url.lower() for pattern in suspicious_patterns)
    
    def is_reliable(self, airdrop: Dict, min_score: int = 60) -> bool:
        """Determine if an airdrop meets the minimum reliability threshold"""
        score = self.calculate_reliability_score(airdrop)
        airdrop['reliability_score'] = score
        return score >= min_score
    
    def extract_requirements(self, text: str) -> List[str]:
        """Extract requirements from airdrop description"""
        requirements = []
        
        # Common requirement patterns
        patterns = [
            r'follow.*twitter',
            r'join.*discord',
            r'join.*telegram',
            r'retweet',
            r'like.*tweet',
            r'connect.*wallet',
            r'complete.*task',
            r'verify.*kyc',
            r'hold.*token',
            r'stake.*token',
            r'provide.*liquidity',
            r'testnet',
            r'mainnet',
        ]
        
        text_lower = text.lower()
        for pattern in patterns:
            if re.search(pattern, text_lower):
                requirements.append(pattern.replace(r'\.*', ' '))
        
        return list(set(requirements))  # Remove duplicates
    
    def extract_blockchain(self, text: str) -> str:
        """Extract blockchain information from text"""
        blockchains = {
            'ethereum': ['ethereum', 'eth', 'erc20', 'erc-20'],
            'polygon': ['polygon', 'matic'],
            'arbitrum': ['arbitrum', 'arb'],
            'optimism': ['optimism', 'op'],
            'solana': ['solana', 'sol'],
            'bsc': ['bsc', 'binance smart chain', 'bnb chain'],
            'avalanche': ['avalanche', 'avax'],
            'cosmos': ['cosmos', 'atom'],
            'polkadot': ['polkadot', 'dot'],
        }
        
        text_lower = text.lower()
        for chain, keywords in blockchains.items():
            if any(keyword in text_lower for keyword in keywords):
                return chain
        
        return 'unknown'
