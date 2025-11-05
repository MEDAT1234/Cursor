#!/usr/bin/env python3
"""
ASMR TikTok Bot - Main Automation Script
Generates ASMR videos and posts them to TikTok automatically
"""

import os
import sys
import time
import schedule
import random
from datetime import datetime
from dotenv import load_dotenv
import logging

from video_generator import VideoGenerator
from tiktok_uploader import TikTokUploader


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class ASMRBot:
    def __init__(self):
        """Initialize the ASMR Bot"""
        # Load environment variables
        load_dotenv()
        
        # Configuration
        self.session_id = os.getenv('TIKTOK_SESSION_ID')
        self.username = os.getenv('TIKTOK_USERNAME')
        self.video_width = int(os.getenv('VIDEO_WIDTH', 1080))
        self.video_height = int(os.getenv('VIDEO_HEIGHT', 1920))
        self.video_duration = int(os.getenv('VIDEO_DURATION', 15))
        self.fps = int(os.getenv('FPS', 30))
        
        # ASMR types to rotate
        asmr_types_str = os.getenv('ASMR_TYPES', 'rain,fire,waves,typing,whisper')
        self.asmr_types = [t.strip() for t in asmr_types_str.split(',')]
        
        # Post times
        post_times_str = os.getenv('POST_TIMES', '09:00,14:00,20:00')
        self.post_times = [t.strip() for t in post_times_str.split(',')]
        
        # Language setting (en or ar)
        self.language = os.getenv('LANGUAGE', 'en')
        
        # Initialize components
        self.video_generator = VideoGenerator(
            width=self.video_width,
            height=self.video_height,
            duration=self.video_duration,
            fps=self.fps
        )
        
        self.uploader = TikTokUploader(session_id=self.session_id, language=self.language)
        
        # Statistics
        self.stats = {
            'videos_generated': 0,
            'videos_uploaded': 0,
            'errors': 0,
            'last_post': None
        }
        
        logger.info("🤖 ASMR Bot initialized")
        logger.info(f"📊 Config: {self.video_width}x{self.video_height}, {self.video_duration}s, {self.fps}fps")
        logger.info(f"🎵 ASMR Types: {', '.join(self.asmr_types)}")
        logger.info(f"⏰ Post Times: {', '.join(self.post_times)}")
        logger.info(f"🌐 Language: {self.language}")
    
    def generate_and_post(self):
        """Generate a video and post it to TikTok"""
        try:
            logger.info("="*70)
            logger.info("🚀 Starting automated post...")
            logger.info("="*70)
            
            # Select random ASMR type
            asmr_type = random.choice(self.asmr_types)
            logger.info(f"🎵 Selected ASMR type: {asmr_type}")
            
            # Generate video
            logger.info("🎬 Generating video...")
            video_path = self.video_generator.generate_video(asmr_type=asmr_type)
            self.stats['videos_generated'] += 1
            logger.info(f"✅ Video generated: {video_path}")
            
            # Upload to TikTok
            logger.info("📤 Uploading to TikTok...")
            success = self.uploader.upload_video(video_path)
            
            if success:
                self.stats['videos_uploaded'] += 1
                self.stats['last_post'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logger.info("✅ Successfully posted to TikTok!")
            else:
                logger.error("❌ Failed to upload video")
                self.stats['errors'] += 1
            
            # Log statistics
            logger.info("📊 Statistics:")
            logger.info(f"   Videos Generated: {self.stats['videos_generated']}")
            logger.info(f"   Videos Uploaded: {self.stats['videos_uploaded']}")
            logger.info(f"   Errors: {self.stats['errors']}")
            logger.info(f"   Last Post: {self.stats['last_post']}")
            logger.info("="*70)
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Error in generate_and_post: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.stats['errors'] += 1
            return False
    
    def test_generation(self):
        """Test video generation only (no upload)"""
        logger.info("🧪 Testing video generation...")
        
        try:
            asmr_type = random.choice(self.asmr_types)
            logger.info(f"🎵 Generating test video: {asmr_type}")
            
            video_path = self.video_generator.generate_video(asmr_type=asmr_type)
            logger.info(f"✅ Test video generated: {video_path}")
            return video_path
            
        except Exception as e:
            logger.error(f"❌ Test generation failed: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None
    
    def setup_schedule(self):
        """Setup the posting schedule"""
        logger.info("⏰ Setting up schedule...")
        
        for post_time in self.post_times:
            schedule.every().day.at(post_time).do(self.generate_and_post)
            logger.info(f"   ✓ Scheduled post at {post_time}")
        
        logger.info("✅ Schedule configured")
    
    def run(self):
        """Run the bot with scheduling"""
        logger.info("🤖 Starting ASMR Bot...")
        logger.info("="*70)
        
        # Check if session ID is available
        if not self.session_id:
            logger.warning("⚠️  No TikTok session ID found!")
            logger.info("🔑 Starting manual login process...")
            
            session_id = self.uploader.login_manual()
            if session_id:
                logger.info("✅ Login successful!")
                logger.info(f"💾 Add this to your .env file:")
                logger.info(f"   TIKTOK_SESSION_ID={session_id}")
                self.session_id = session_id
                self.uploader.session_id = session_id
            else:
                logger.error("❌ Login failed. Please try again.")
                return
        
        # Setup schedule
        self.setup_schedule()
        
        logger.info("✅ Bot is running!")
        logger.info("⏰ Waiting for scheduled times...")
        logger.info("💡 Press Ctrl+C to stop the bot")
        logger.info("="*70)
        
        # Run scheduled tasks
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
                
        except KeyboardInterrupt:
            logger.info("\n⚠️  Bot stopped by user")
            self.cleanup()
    
    def run_once(self):
        """Generate and post once, then exit"""
        logger.info("🤖 Running bot once...")
        
        # Check if session ID is available
        if not self.session_id:
            logger.warning("⚠️  No TikTok session ID found!")
            logger.info("🔑 Starting manual login process...")
            
            session_id = self.uploader.login_manual()
            if session_id:
                logger.info("✅ Login successful!")
                logger.info(f"💾 Add this to your .env file:")
                logger.info(f"   TIKTOK_SESSION_ID={session_id}")
                self.session_id = session_id
                self.uploader.session_id = session_id
            else:
                logger.error("❌ Login failed. Please try again.")
                return
        
        # Generate and post
        success = self.generate_and_post()
        
        if success:
            logger.info("✅ Done!")
        else:
            logger.error("❌ Failed to complete")
        
        self.cleanup()
    
    def cleanup(self):
        """Cleanup resources"""
        logger.info("🧹 Cleaning up...")
        try:
            self.uploader.close()
        except:
            pass
        logger.info("👋 Goodbye!")


def main():
    """Main entry point"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║           🎵 ASMR TikTok Automation Bot 🎵               ║
    ║                                                           ║
    ║  Automatically generates and posts ASMR videos to TikTok  ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='ASMR TikTok Bot')
    parser.add_argument(
        '--mode',
        choices=['scheduled', 'once', 'test'],
        default='scheduled',
        help='Bot mode: scheduled (default), once, or test'
    )
    args = parser.parse_args()
    
    # Create and run bot
    bot = ASMRBot()
    
    if args.mode == 'scheduled':
        bot.run()
    elif args.mode == 'once':
        bot.run_once()
    elif args.mode == 'test':
        video_path = bot.test_generation()
        if video_path:
            print(f"\n✅ Test successful! Video: {video_path}")
        else:
            print("\n❌ Test failed")
        bot.cleanup()


if __name__ == "__main__":
    main()
