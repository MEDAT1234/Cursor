"""
وحدة تحميل الفيديوهات من تيكتوك
تقوم بتحميل الفيديوهات الترندية حسب الفئة المحددة
"""

import os
import json
import time
import yt_dlp
from pathlib import Path
from typing import List, Dict
from colorama import Fore, Style, init

init(autoreset=True)


class TikTokDownloader:
    """فئة لتحميل الفيديوهات من تيكتوك"""
    
    def __init__(self, download_folder: str = "downloads"):
        self.download_folder = Path(download_folder)
        self.download_folder.mkdir(exist_ok=True)
        self.downloaded_videos = []
        
    def search_trending_videos(self, keyword: str, max_results: int = 10) -> List[str]:
        """
        البحث عن فيديوهات ترندية بناءً على كلمة مفتاحية
        
        Args:
            keyword: الكلمة المفتاحية للبحث (مثل: asmr)
            max_results: عدد النتائج المطلوبة
            
        Returns:
            قائمة بروابط الفيديوهات
        """
        print(f"{Fore.CYAN}🔍 البحث عن فيديوهات {keyword}...")
        
        # قائمة روابط تيكتوك للاختبار
        # في الواقع، يمكن استخدام TikTokApi أو web scraping للبحث
        search_url = f"https://www.tiktok.com/search?q={keyword}"
        
        print(f"{Fore.YELLOW}⚠️  ملاحظة: للحصول على أفضل النتائج، استخدم روابط مباشرة للفيديوهات")
        print(f"{Fore.YELLOW}   أو استخدم TikTok API للبحث المتقدم")
        
        return []
    
    def download_video(self, url: str, video_id: str = None) -> Dict:
        """
        تحميل فيديو واحد من تيكتوك
        
        Args:
            url: رابط الفيديو
            video_id: معرف الفيديو (اختياري)
            
        Returns:
            معلومات الفيديو المحمل
        """
        if not video_id:
            video_id = f"video_{int(time.time())}"
            
        output_path = self.download_folder / f"{video_id}.mp4"
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': str(output_path),
            'quiet': False,
            'no_warnings': False,
            'extract_flat': False,
            'nocheckcertificate': True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }
        
        try:
            print(f"{Fore.CYAN}⬇️  تحميل الفيديو: {url}")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                video_info = {
                    'id': video_id,
                    'title': info.get('title', 'Untitled'),
                    'description': info.get('description', ''),
                    'duration': info.get('duration', 0),
                    'views': info.get('view_count', 0),
                    'likes': info.get('like_count', 0),
                    'path': str(output_path),
                    'url': url,
                    'downloaded_at': time.time()
                }
                
                self.downloaded_videos.append(video_info)
                
                print(f"{Fore.GREEN}✅ تم تحميل الفيديو: {video_info['title']}")
                print(f"{Fore.GREEN}   المسار: {output_path}")
                
                return video_info
                
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في تحميل الفيديو: {str(e)}")
            return None
    
    def download_multiple_videos(self, urls: List[str]) -> List[Dict]:
        """
        تحميل عدة فيديوهات
        
        Args:
            urls: قائمة روابط الفيديوهات
            
        Returns:
            قائمة معلومات الفيديوهات المحملة
        """
        print(f"{Fore.CYAN}📥 بدء تحميل {len(urls)} فيديو...")
        
        downloaded = []
        for i, url in enumerate(urls, 1):
            print(f"\n{Fore.MAGENTA}[{i}/{len(urls)}] معالجة الفيديو...")
            video_id = f"video_{i}_{int(time.time())}"
            video_info = self.download_video(url, video_id)
            
            if video_info:
                downloaded.append(video_info)
                
            # انتظار قصير بين التحميلات
            if i < len(urls):
                time.sleep(2)
        
        print(f"\n{Fore.GREEN}✅ تم تحميل {len(downloaded)} فيديو بنجاح")
        return downloaded
    
    def download_from_file(self, file_path: str) -> List[Dict]:
        """
        تحميل فيديوهات من ملف يحتوي على روابط
        
        Args:
            file_path: مسار الملف
            
        Returns:
            قائمة معلومات الفيديوهات المحملة
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip()]
            
            return self.download_multiple_videos(urls)
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في قراءة الملف: {str(e)}")
            return []
    
    def save_metadata(self, output_file: str = "metadata.json"):
        """
        حفظ معلومات الفيديوهات المحملة
        
        Args:
            output_file: مسار ملف الحفظ
        """
        metadata_path = self.download_folder / output_file
        
        try:
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(self.downloaded_videos, f, indent=2, ensure_ascii=False)
            
            print(f"{Fore.GREEN}✅ تم حفظ البيانات الوصفية في: {metadata_path}")
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في حفظ البيانات: {str(e)}")
    
    def get_downloaded_videos(self) -> List[Dict]:
        """الحصول على قائمة الفيديوهات المحملة"""
        return self.downloaded_videos


if __name__ == "__main__":
    # مثال على الاستخدام
    downloader = TikTokDownloader()
    
    # مثال: تحميل فيديو واحد
    # downloader.download_video("https://www.tiktok.com/@username/video/1234567890")
    
    # مثال: تحميل من ملف
    # downloader.download_from_file("video_urls.txt")
    
    print(f"{Fore.YELLOW}⚠️  للاستخدام، قم بتوفير روابط الفيديوهات")
    print(f"{Fore.YELLOW}   يمكنك إنشاء ملف video_urls.txt وإضافة الروابط فيه")
