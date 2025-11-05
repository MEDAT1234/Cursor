#!/usr/bin/env python3
"""
البوت الرئيسي لاستنساخ ورفع فيديوهات تيكتوك
يقوم بتحميل فيديوهات ترندية، معالجتها، ورفعها على حسابك
"""

import sys
import time
import shutil
from pathlib import Path
from typing import List
from colorama import Fore, Style, init

from config import Config
from video_downloader import TikTokDownloader
from video_processor import VideoProcessor
from video_uploader import TikTokUploader

init(autoreset=True)


class TikTokBot:
    """البوت الرئيسي لإدارة العملية الكاملة"""
    
    def __init__(self):
        self.config = Config
        self.downloader = None
        self.processor = None
        self.uploader = None
        
        # إنشاء المجلدات المطلوبة
        self.config.create_folders()
    
    def setup(self) -> bool:
        """
        إعداد البوت والتحقق من الإعدادات
        
        Returns:
            True إذا تم الإعداد بنجاح
        """
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}🤖 بوت تيكتوك - استنساخ ورفع الفيديوهات")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # طباعة الإعدادات
        self.config.print_config()
        
        # التحقق من الإعدادات
        if not self.config.validate():
            print(f"\n{Fore.RED}❌ فشل التحقق من الإعدادات!")
            print(f"{Fore.YELLOW}يرجى تحديث ملف .env بالمعلومات الصحيحة")
            return False
        
        # تهيئة المكونات
        self.downloader = TikTokDownloader(str(self.config.DOWNLOAD_FOLDER))
        self.processor = VideoProcessor(str(self.config.PROCESSED_FOLDER))
        
        print(f"{Fore.GREEN}✅ تم إعداد البوت بنجاح!\n")
        return True
    
    def download_videos(self, urls: List[str] = None, url_file: str = None) -> List:
        """
        تحميل الفيديوهات
        
        Args:
            urls: قائمة روابط مباشرة
            url_file: ملف يحتوي على روابط
            
        Returns:
            قائمة معلومات الفيديوهات المحملة
        """
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}المرحلة 1: تحميل الفيديوهات")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        
        if url_file:
            print(f"{Fore.CYAN}📄 تحميل من ملف: {url_file}")
            videos = self.downloader.download_from_file(url_file)
        elif urls:
            print(f"{Fore.CYAN}🔗 تحميل من روابط مباشرة")
            videos = self.downloader.download_multiple_videos(urls)
        else:
            print(f"{Fore.YELLOW}⚠️  لم يتم توفير روابط")
            print(f"{Fore.YELLOW}يرجى توفير روابط الفيديوهات للتحميل")
            return []
        
        # حفظ البيانات الوصفية
        if videos:
            self.downloader.save_metadata()
        
        return videos
    
    def process_videos(self, videos: List) -> List:
        """
        معالجة الفيديوهات المحملة
        
        Args:
            videos: قائمة معلومات الفيديوهات
            
        Returns:
            قائمة معلومات الفيديوهات المعالجة
        """
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}المرحلة 2: معالجة الفيديوهات")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        
        if not videos:
            print(f"{Fore.YELLOW}⚠️  لا توجد فيديوهات للمعالجة")
            return []
        
        video_paths = [v['path'] for v in videos]
        
        # خيارات المعالجة
        watermark_text = self.config.WATERMARK_TEXT if self.config.ADD_WATERMARK else None
        
        processed = self.processor.process_multiple_videos(
            video_paths,
            apply_filter=self.config.APPLY_FILTERS,
            add_watermark_text=watermark_text
        )
        
        return processed
    
    def upload_videos(self, processed_videos: List) -> bool:
        """
        رفع الفيديوهات على تيكتوك
        
        Args:
            processed_videos: قائمة الفيديوهات المعالجة
            
        Returns:
            True إذا نجح الرفع
        """
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}المرحلة 3: رفع الفيديوهات")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        
        if not processed_videos:
            print(f"{Fore.YELLOW}⚠️  لا توجد فيديوهات للرفع")
            return False
        
        if not self.config.AUTO_UPLOAD:
            print(f"{Fore.YELLOW}⚠️  الرفع التلقائي معطل")
            print(f"{Fore.YELLOW}يمكنك العثور على الفيديوهات المعالجة في: {self.config.PROCESSED_FOLDER}")
            return True
        
        # تهيئة الرافع
        self.uploader = TikTokUploader(
            self.config.TIKTOK_USERNAME,
            self.config.TIKTOK_PASSWORD,
            headless=False  # نافذة مرئية للتفاعل اليدوي
        )
        
        try:
            # تسجيل الدخول
            if not self.uploader.login():
                print(f"{Fore.RED}❌ فشل تسجيل الدخول")
                return False
            
            # إعداد معلومات الرفع
            hashtags = self.config.get_hashtags_list() if self.config.ADD_HASHTAGS else []
            
            video_info_list = []
            for i, video in enumerate(processed_videos, 1):
                caption = self.config.UPLOAD_CAPTION or f"فيديو {i} #fyp"
                video_info_list.append({
                    'processed_path': video['processed_path'],
                    'caption': caption,
                    'hashtags': hashtags
                })
            
            # رفع الفيديوهات
            results = self.uploader.upload_multiple_videos(video_info_list, hashtags)
            
            # نقل الفيديوهات المرفوعة بنجاح
            for i, success in enumerate(results):
                if success:
                    video_path = Path(processed_videos[i]['processed_path'])
                    uploaded_path = self.config.UPLOADED_FOLDER / video_path.name
                    shutil.move(str(video_path), str(uploaded_path))
                    print(f"{Fore.GREEN}✅ تم نقل الفيديو إلى: {uploaded_path}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في عملية الرفع: {str(e)}")
            return False
        finally:
            if self.uploader:
                self.uploader.close()
    
    def run(self, urls: List[str] = None, url_file: str = None):
        """
        تشغيل البوت بالكامل
        
        Args:
            urls: قائمة روابط مباشرة
            url_file: ملف يحتوي على روابط
        """
        start_time = time.time()
        
        # الإعداد
        if not self.setup():
            return
        
        try:
            # 1. تحميل الفيديوهات
            videos = self.download_videos(urls, url_file)
            
            if not videos:
                print(f"\n{Fore.RED}❌ لم يتم تحميل أي فيديوهات!")
                return
            
            # 2. معالجة الفيديوهات
            processed = self.process_videos(videos)
            
            if not processed:
                print(f"\n{Fore.RED}❌ لم يتم معالجة أي فيديوهات!")
                return
            
            # 3. رفع الفيديوهات
            self.upload_videos(processed)
            
            # النتيجة النهائية
            elapsed_time = time.time() - start_time
            print(f"\n{Fore.GREEN}{'='*60}")
            print(f"{Fore.GREEN}✅ اكتملت العملية بنجاح!")
            print(f"{Fore.GREEN}{'='*60}")
            print(f"{Fore.CYAN}⏱️  الوقت المستغرق: {elapsed_time:.2f} ثانية")
            print(f"{Fore.CYAN}📊 عدد الفيديوهات المحملة: {len(videos)}")
            print(f"{Fore.CYAN}📊 عدد الفيديوهات المعالجة: {len(processed)}")
            print(f"{Fore.GREEN}{'='*60}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}⚠️  تم إيقاف البوت بواسطة المستخدم")
        except Exception as e:
            print(f"\n{Fore.RED}❌ خطأ غير متوقع: {str(e)}")
            import traceback
            traceback.print_exc()
        finally:
            if self.uploader:
                self.uploader.close()


def main():
    """الدالة الرئيسية"""
    
    # طباعة رسالة الترحيب
    print(f"\n{Fore.CYAN}{'#'*60}")
    print(f"{Fore.CYAN}#{'':^58}#")
    print(f"{Fore.CYAN}#{'بوت تيكتوك - استنساخ ورفع الفيديوهات':^58}#")
    print(f"{Fore.CYAN}#{'':^58}#")
    print(f"{Fore.CYAN}{'#'*60}\n")
    
    # إنشاء البوت
    bot = TikTokBot()
    
    # التحقق من وجود ملف روابط
    url_file = "video_urls.txt"
    
    if Path(url_file).exists():
        print(f"{Fore.GREEN}✅ تم العثور على ملف الروابط: {url_file}")
        bot.run(url_file=url_file)
    else:
        print(f"{Fore.YELLOW}⚠️  لم يتم العثور على ملف {url_file}")
        print(f"{Fore.YELLOW}يرجى إنشاء الملف وإضافة روابط الفيديوهات (رابط واحد في كل سطر)")
        print(f"\n{Fore.CYAN}أو يمكنك استخدام البوت برمجياً:")
        print(f"{Fore.WHITE}  from main import TikTokBot")
        print(f"{Fore.WHITE}  bot = TikTokBot()")
        print(f"{Fore.WHITE}  urls = ['url1', 'url2', ...]")
        print(f"{Fore.WHITE}  bot.run(urls=urls)")


if __name__ == "__main__":
    main()
