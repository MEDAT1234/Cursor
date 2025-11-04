"""
TikTok Uploader
Uploads videos to TikTok using browser automation
"""

import os
import time
import random
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout


class TikTokUploader:
    def __init__(self, session_id=None):
        """
        Initialize TikTok uploader
        
        Args:
            session_id: TikTok session cookie (optional, will use manual login if not provided)
        """
        self.session_id = session_id
        self.browser = None
        self.context = None
        self.page = None
        
        # Hashtags for ASMR content
        self.base_hashtags = [
            "#asmr", "#asmrsounds", "#asmrvideo", "#relaxing",
            "#sleep", "#satisfying", "#calming", "#meditation",
            "#sleepaid", "#anxiety", "#stress", "#peaceful"
        ]
        
        self.specific_hashtags = {
            'rain': ["#rain", "#rainsounds", "#rainyday", "#rainasmr"],
            'fire': ["#fireplace", "#fire", "#cozy", "#fireasmr"],
            'waves': ["#ocean", "#waves", "#beach", "#oceanwaves"],
            'typing': ["#typing", "#keyboard", "#typingasmr", "#work"],
            'whisper': ["#whisper", "#softspoken", "#whisperasmr", "#tingles"]
        }
    
    def _get_captions(self, video_type):
        """Generate caption with hashtags for the video"""
        captions = {
            'rain': [
                "Relaxing rain sounds for sleep and study 🌧️💤",
                "Let the rain wash away your stress 🌧️✨",
                "Perfect rain sounds for deep sleep 🌧️😴",
                "Peaceful rain ambience for relaxation 🌧️🎧"
            ],
            'fire': [
                "Cozy fireplace sounds for relaxation 🔥💤",
                "Warm and peaceful fire crackling 🔥✨",
                "Perfect fireplace ambience for sleep 🔥😴",
                "Crackling fire sounds for stress relief 🔥🎧"
            ],
            'waves': [
                "Calming ocean waves for peaceful sleep 🌊💤",
                "Relaxing beach sounds for meditation 🌊✨",
                "Peaceful ocean waves ambience 🌊😴",
                "Soothing waves for deep relaxation 🌊🎧"
            ],
            'typing': [
                "Satisfying keyboard typing sounds ⌨️💤",
                "Relaxing typing ASMR for focus ⌨️✨",
                "Peaceful keyboard sounds for study ⌨️😴",
                "Soothing typing ambience ⌨️🎧"
            ],
            'whisper': [
                "Soft whisper ASMR for sleep 💜💤",
                "Gentle whispers for relaxation 💜✨",
                "Peaceful whisper sounds 💜😴",
                "Calming whisper ASMR 💜🎧"
            ]
        }
        
        caption = random.choice(captions.get(video_type, captions['waves']))
        
        # Add hashtags
        specific_tags = self.specific_hashtags.get(video_type, [])
        all_tags = self.base_hashtags + specific_tags
        random.shuffle(all_tags)
        
        # TikTok allows up to 2200 characters
        hashtag_string = " ".join(all_tags[:20])  # Use up to 20 hashtags
        
        return f"{caption}\n\n{hashtag_string}"
    
    def _detect_video_type(self, video_path):
        """Detect ASMR type from video filename"""
        filename = os.path.basename(video_path).lower()
        for asmr_type in ['rain', 'fire', 'waves', 'typing', 'whisper']:
            if asmr_type in filename:
                return asmr_type
        return 'waves'  # Default
    
    def setup_browser(self, headless=True):
        """Initialize browser with Playwright"""
        print("🌐 Setting up browser...")
        
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(
            headless=headless,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        
        # Create browser context
        self.context = self.browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        # Add session cookie if provided
        if self.session_id:
            self.context.add_cookies([{
                'name': 'sessionid',
                'value': self.session_id,
                'domain': '.tiktok.com',
                'path': '/'
            }])
        
        self.page = self.context.new_page()
        print("✅ Browser ready")
    
    def login_manual(self):
        """Manual login process (opens browser for user to login)"""
        print("🔑 Please login to TikTok manually...")
        print("📱 Opening TikTok login page...")
        
        self.setup_browser(headless=False)
        self.page.goto('https://www.tiktok.com/login')
        
        print("\n" + "="*60)
        print("⚠️  MANUAL LOGIN REQUIRED")
        print("="*60)
        print("Please complete the following steps:")
        print("1. Login to your TikTok account in the browser")
        print("2. Complete any verification if needed")
        print("3. Wait for the page to fully load")
        print("4. Press Enter here when you see your TikTok feed...")
        print("="*60 + "\n")
        
        input("Press Enter after logging in...")
        
        # Get session cookies
        cookies = self.context.cookies()
        session_cookie = next((c for c in cookies if c['name'] == 'sessionid'), None)
        
        if session_cookie:
            print("✅ Login successful!")
            print(f"💾 Save this session ID for future use:")
            print(f"   {session_cookie['value']}")
            return session_cookie['value']
        else:
            print("❌ Could not find session cookie. Please try again.")
            return None
    
    def upload_video(self, video_path, caption=None):
        """
        Upload video to TikTok
        
        Args:
            video_path: Path to the video file
            caption: Video caption (auto-generated if not provided)
        
        Returns:
            bool: True if upload successful
        """
        if not os.path.exists(video_path):
            print(f"❌ Video file not found: {video_path}")
            return False
        
        try:
            # Setup browser if not already done
            if not self.page:
                self.setup_browser(headless=False)
            
            print(f"📤 Uploading video: {video_path}")
            
            # Navigate to upload page
            print("🌐 Navigating to TikTok upload page...")
            self.page.goto('https://www.tiktok.com/upload', wait_until='networkidle')
            time.sleep(3)
            
            # Check if logged in
            if 'login' in self.page.url.lower():
                print("⚠️  Not logged in. Starting manual login...")
                session_id = self.login_manual()
                if not session_id:
                    return False
                self.page.goto('https://www.tiktok.com/upload', wait_until='networkidle')
                time.sleep(3)
            
            # Upload video file
            print("📁 Selecting video file...")
            file_input = self.page.locator('input[type="file"]').first
            file_input.set_input_files(os.path.abspath(video_path))
            
            print("⏳ Waiting for video to upload...")
            time.sleep(10)  # Wait for upload to process
            
            # Generate caption if not provided
            if not caption:
                video_type = self._detect_video_type(video_path)
                caption = self._get_captions(video_type)
            
            print("✍️  Adding caption and hashtags...")
            
            # Add caption
            try:
                # Try different selectors for caption input
                caption_selectors = [
                    '[placeholder*="caption"]',
                    '[placeholder*="description"]',
                    'div[contenteditable="true"]',
                    '.public-DraftEditor-content'
                ]
                
                caption_added = False
                for selector in caption_selectors:
                    try:
                        caption_field = self.page.locator(selector).first
                        if caption_field.is_visible(timeout=2000):
                            caption_field.click()
                            time.sleep(0.5)
                            caption_field.fill(caption)
                            caption_added = True
                            break
                    except:
                        continue
                
                if not caption_added:
                    print("⚠️  Could not find caption field (trying alternative method)...")
                    self.page.keyboard.press('Tab')
                    time.sleep(0.5)
                    self.page.keyboard.type(caption)
            except Exception as e:
                print(f"⚠️  Caption error: {e}")
            
            time.sleep(2)
            
            # Set video settings
            print("⚙️  Configuring video settings...")
            
            try:
                # Try to find and click "Who can view this video" dropdown
                privacy_button = self.page.locator('text=Who can view').first
                if privacy_button.is_visible(timeout=3000):
                    privacy_button.click()
                    time.sleep(1)
                    # Select "Public"
                    public_option = self.page.locator('text=Public').first
                    if public_option.is_visible(timeout=2000):
                        public_option.click()
                        time.sleep(1)
            except:
                print("⚠️  Using default privacy settings")
            
            # Wait for video processing
            print("⏳ Waiting for video processing to complete...")
            max_wait = 60  # Maximum 60 seconds
            wait_time = 0
            while wait_time < max_wait:
                try:
                    # Check if post button is enabled
                    post_button = self.page.locator('button:has-text("Post")').first
                    if post_button.is_enabled():
                        break
                except:
                    pass
                time.sleep(2)
                wait_time += 2
                if wait_time % 10 == 0:
                    print(f"   Still processing... ({wait_time}s)")
            
            # Click post button
            print("🚀 Publishing video...")
            try:
                post_button = self.page.locator('button:has-text("Post")').first
                post_button.click()
                
                # Wait for upload confirmation
                print("⏳ Waiting for upload confirmation...")
                time.sleep(10)
                
                # Check for success
                if 'upload' not in self.page.url.lower():
                    print("✅ Video uploaded successfully!")
                    return True
                else:
                    print("⚠️  Upload may have succeeded, but couldn't confirm")
                    return True
                    
            except Exception as e:
                print(f"❌ Error clicking post button: {e}")
                return False
                
        except Exception as e:
            print(f"❌ Upload error: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def close(self):
        """Close browser"""
        if self.browser:
            self.browser.close()
            print("🔒 Browser closed")


if __name__ == "__main__":
    # Test uploader
    print("TikTok Uploader Test")
    print("="*60)
    
    uploader = TikTokUploader()
    
    # For testing, you would need a video file
    # uploader.upload_video("path/to/test/video.mp4")
    
    print("\nNote: For first time use, you'll need to login manually.")
    print("The script will save your session ID for future automated uploads.")
