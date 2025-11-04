"""
Database management for the Airdrop Capture Bot
"""
import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional
from config import DATABASE_PATH


class AirdropDatabase:
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS airdrops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT UNIQUE NOT NULL,
                description TEXT,
                source TEXT NOT NULL,
                reliability_score INTEGER,
                requirements TEXT,
                end_date TEXT,
                value_estimate TEXT,
                blockchain TEXT,
                tags TEXT,
                discovered_at TEXT NOT NULL,
                notified BOOLEAN DEFAULT 0,
                is_active BOOLEAN DEFAULT 1
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS airdrop_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                airdrop_id INTEGER,
                action TEXT,
                timestamp TEXT,
                details TEXT,
                FOREIGN KEY (airdrop_id) REFERENCES airdrops(id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_airdrop(self, airdrop: Dict) -> bool:
        """Add a new airdrop to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO airdrops (
                    title, url, description, source, reliability_score,
                    requirements, end_date, value_estimate, blockchain,
                    tags, discovered_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                airdrop.get('title'),
                airdrop.get('url'),
                airdrop.get('description'),
                airdrop.get('source'),
                airdrop.get('reliability_score', 0),
                json.dumps(airdrop.get('requirements', [])),
                airdrop.get('end_date'),
                airdrop.get('value_estimate'),
                airdrop.get('blockchain'),
                json.dumps(airdrop.get('tags', [])),
                datetime.now().isoformat()
            ))
            
            airdrop_id = cursor.lastrowid
            
            # Log to history
            cursor.execute('''
                INSERT INTO airdrop_history (airdrop_id, action, timestamp, details)
                VALUES (?, ?, ?, ?)
            ''', (airdrop_id, 'discovered', datetime.now().isoformat(), ''))
            
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Airdrop already exists
            return False
        finally:
            conn.close()
    
    def get_unnotified_airdrops(self) -> List[Dict]:
        """Get all airdrops that haven't been notified yet"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM airdrops 
            WHERE notified = 0 AND is_active = 1
            ORDER BY reliability_score DESC, discovered_at DESC
        ''')
        
        airdrops = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        # Parse JSON fields
        for airdrop in airdrops:
            airdrop['requirements'] = json.loads(airdrop['requirements'])
            airdrop['tags'] = json.loads(airdrop['tags'])
        
        return airdrops
    
    def mark_as_notified(self, airdrop_id: int):
        """Mark an airdrop as notified"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE airdrops SET notified = 1 WHERE id = ?
        ''', (airdrop_id,))
        
        cursor.execute('''
            INSERT INTO airdrop_history (airdrop_id, action, timestamp, details)
            VALUES (?, ?, ?, ?)
        ''', (airdrop_id, 'notified', datetime.now().isoformat(), ''))
        
        conn.commit()
        conn.close()
    
    def get_all_airdrops(self, active_only: bool = True) -> List[Dict]:
        """Get all airdrops from the database"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if active_only:
            cursor.execute('''
                SELECT * FROM airdrops 
                WHERE is_active = 1
                ORDER BY reliability_score DESC, discovered_at DESC
            ''')
        else:
            cursor.execute('''
                SELECT * FROM airdrops 
                ORDER BY discovered_at DESC
            ''')
        
        airdrops = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        # Parse JSON fields
        for airdrop in airdrops:
            airdrop['requirements'] = json.loads(airdrop['requirements'])
            airdrop['tags'] = json.loads(airdrop['tags'])
        
        return airdrops
    
    def get_stats(self) -> Dict:
        """Get statistics about collected airdrops"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM airdrops WHERE is_active = 1')
        active_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM airdrops WHERE notified = 1')
        notified_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT AVG(reliability_score) FROM airdrops WHERE is_active = 1')
        avg_score = cursor.fetchone()[0] or 0
        
        conn.close()
        
        return {
            'total_active': active_count,
            'total_notified': notified_count,
            'average_reliability': round(avg_score, 2)
        }
