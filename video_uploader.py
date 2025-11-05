"""
وحدة رفع الفيديوهات على تيكتوك
تستخدم Selenium للتحكم الآلي في المتصفح
"""

import os
import time
from pathlib import Path
from typing import Dict, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style, init

init(autoreset=True)


class TikTokUploader:
    """فئة لرفع الفيديوهات على تيكتوك"""
    
    def __init__(self, username: str, password: str, headless: bool = False):
        """
        تهيئة رافع الفيديوهات
        
        Args:
            username: اسم المستخدم في تيكتوك
            password: كلمة المرور
            headless: تشغيل المتصفح في وضع الخلفية
        """
        self.username = username
        self.password = password
        self.headless = headless
        self.driver = None
        self.is_logged_in = False
        
    def _init_driver(self):
        """تهيئة متصفح Chrome"""
        print(f"{Fore.CYAN}🌐 تهيئة المتصفح...")
        
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument("--headless")
        
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # إضافة user agent طبيعي
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # إخفاء خاصية webdriver
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        
        print(f"{Fore.GREEN}✅ تم تهيئة المتصفح بنجاح")
    
    def login(self) -> bool:
        """
        تسجيل الدخول إلى تيكتوك
        
        Returns:
            True إذا نجح تسجيل الدخول
        """
        if not self.driver:
            self._init_driver()
        
        print(f"{Fore.CYAN}🔐 تسجيل الدخول إلى تيكتوك...")
        
        try:
            # الذهاب إلى صفحة تسجيل الدخول
            self.driver.get("https://www.tiktok.com/login")
            time.sleep(3)
            
            # ملاحظة: تيكتوك لديه حماية قوية ضد البوتات
            # قد تحتاج إلى استخدام cookies محفوظة أو تسجيل دخول يدوي
            
            print(f"{Fore.YELLOW}⚠️  ملاحظة مهمة:")
            print(f"{Fore.YELLOW}   تيكتوك لديه حماية قوية ضد التشغيل الآلي")
            print(f"{Fore.YELLOW}   للحصول على أفضل النتائج:")
            print(f"{Fore.YELLOW}   1. قم بتسجيل الدخول يدوياً في المتصفح الذي سيفتح")
            print(f"{Fore.YELLOW}   2. أو استخدم ملفات cookies المحفوظة")
            print(f"{Fore.YELLOW}   3. أو استخدم TikTok API الرسمي للمطورين")
            
            # انتظار تسجيل الدخول اليدوي
            print(f"\n{Fore.CYAN}⏳ في انتظار تسجيل الدخول اليدوي...")
            print(f"{Fore.CYAN}   سيتم المتابعة تلقائياً بعد تسجيل الدخول")
            
            # الانتظار حتى يتم تسجيل الدخول (التحقق من وجود زر الرفع)
            wait = WebDriverWait(self.driver, 300)  # انتظار 5 دقائق
            
            # البحث عن زر الرفع كدليل على نجاح تسجيل الدخول
            try:
                wait.until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'upload')]"))
                )
                self.is_logged_in = True
                print(f"{Fore.GREEN}✅ تم تسجيل الدخول بنجاح!")
                return True
            except:
                print(f"{Fore.RED}❌ انتهت مهلة تسجيل الدخول")
                return False
            
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في تسجيل الدخول: {str(e)}")
            return False
    
    def upload_video(self, video_path: str, caption: str = "", 
                     hashtags: List[str] = None, 
                     privacy: str = "public") -> bool:
        """
        رفع فيديو على تيكتوك
        
        Args:
            video_path: مسار الفيديو
            caption: وصف الفيديو
            hashtags: قائمة الهاشتاقات
            privacy: خصوصية الفيديو (public, friends, private)
            
        Returns:
            True إذا نجح الرفع
        """
        if not self.is_logged_in:
            print(f"{Fore.YELLOW}⚠️  يجب تسجيل الدخول أولاً")
            if not self.login():
                return False
        
        if not os.path.exists(video_path):
            print(f"{Fore.RED}❌ الفيديو غير موجود: {video_path}")
            return False
        
        print(f"\n{Fore.CYAN}📤 رفع الفيديو: {Path(video_path).name}")
        
        try:
            # الذهاب إلى صفحة الرفع
            self.driver.get("https://www.tiktok.com/upload")
            time.sleep(3)
            
            # البحث عن حقل رفع الملف
            wait = WebDriverWait(self.driver, 30)
            
            # ملاحظة: العناصر تتغير باستمرار في واجهة تيكتوك
            # قد تحتاج إلى تحديث selectors
            
            print(f"{Fore.YELLOW}⚠️  ملاحظة:")
            print(f"{Fore.YELLOW}   يرجى رفع الفيديو يدوياً في المتصفح")
            print(f"{Fore.YELLOW}   تيكتوك لديه واجهة معقدة تتغير باستمرار")
            print(f"{Fore.YELLOW}   للرفع الآلي الكامل، يُنصح باستخدام TikTok API الرسمي")
            
            # إعداد الوصف
            full_caption = caption
            if hashtags:
                hashtag_string = " ".join([f"#{tag.strip('#')}" for tag in hashtags])
                full_caption = f"{caption} {hashtag_string}"
            
            print(f"\n{Fore.CYAN}📝 الوصف المقترح:")
            print(f"{Fore.WHITE}{full_caption}")
            
            # الانتظار حتى يتم الرفع يدوياً
            print(f"\n{Fore.CYAN}⏳ في انتظار إكمال الرفع اليدوي...")
            input(f"{Fore.YELLOW}اضغط Enter بعد إتمام الرفع...")
            
            print(f"{Fore.GREEN}✅ تم الرفع بنجاح!")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في رفع الفيديو: {str(e)}")
            return False
    
    def upload_multiple_videos(self, video_info_list: List[Dict],
                               default_hashtags: List[str] = None) -> List[bool]:
        """
        رفع عدة فيديوهات
        
        Args:
            video_info_list: قائمة معلومات الفيديوهات
            default_hashtags: هاشتاقات افتراضية
            
        Returns:
            قائمة بنتائج الرفع
        """
        print(f"{Fore.CYAN}📤 رفع {len(video_info_list)} فيديو...\n")
        
        results = []
        for i, info in enumerate(video_info_list, 1):
            print(f"\n{Fore.MAGENTA}[{i}/{len(video_info_list)}] رفع فيديو...")
            
            video_path = info.get('processed_path') or info.get('path')
            caption = info.get('caption', f"فيديو رقم {i}")
            hashtags = info.get('hashtags', default_hashtags or [])
            
            success = self.upload_video(video_path, caption, hashtags)
            results.append(success)
            
            if success and i < len(video_info_list):
                print(f"{Fore.CYAN}⏳ انتظار قبل رفع الفيديو التالي...")
                time.sleep(5)
        
        successful = sum(results)
        print(f"\n{Fore.GREEN}✅ تم رفع {successful}/{len(video_info_list)} فيديو بنجاح!")
        
        return results
    
    def close(self):
        """إغلاق المتصفح"""
        if self.driver:
            print(f"{Fore.CYAN}🔒 إغلاق المتصفح...")
            self.driver.quit()
            self.driver = None
            self.is_logged_in = False
            print(f"{Fore.GREEN}✅ تم الإغلاق")
    
    def __enter__(self):
        """دعم context manager"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """دعم context manager"""
        self.close()


class TikTokUploaderPlaywright:
    """
    نسخة بديلة باستخدام Playwright
    أكثر موثوقية وأقل اكتشافاً من قبل تيكتوك
    """
    
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        print(f"{Fore.YELLOW}⚠️  Playwright uploader - يتطلب تثبيت Playwright")
        print(f"{Fore.YELLOW}   قم بتشغيل: playwright install chromium")
    
    def upload_video(self, video_path: str, caption: str = "", hashtags: List[str] = None):
        """رفع فيديو باستخدام Playwright"""
        print(f"{Fore.CYAN}📤 رفع الفيديو باستخدام Playwright...")
        print(f"{Fore.YELLOW}⚠️  هذه الميزة تتطلب تطوير إضافي")
        print(f"{Fore.YELLOW}   يُنصح باستخدام TikTok API الرسمي للرفع الآلي الكامل")
        

if __name__ == "__main__":
    print(f"{Fore.YELLOW}⚠️  للاستخدام، قم بتوفير بيانات تسجيل الدخول")
    print(f"{Fore.YELLOW}   مثال:")
    print(f"{Fore.YELLOW}   uploader = TikTokUploader('username', 'password')")
    print(f"{Fore.YELLOW}   uploader.login()")
    print(f"{Fore.YELLOW}   uploader.upload_video('video.mp4', 'وصف الفيديو', ['tag1', 'tag2'])")
