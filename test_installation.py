#!/usr/bin/env python3
"""
سكريبت اختبار التثبيت
يتحقق من تثبيت جميع المتطلبات بشكل صحيح
"""

import sys
import subprocess
from colorama import Fore, init

init(autoreset=True)


def print_header():
    """طباعة رأس الاختبار"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'اختبار تثبيت بوت تيكتوك':^60}")
    print(f"{Fore.CYAN}{'='*60}\n")


def check_python():
    """التحقق من Python"""
    print(f"{Fore.CYAN}🐍 التحقق من Python...")
    version = sys.version_info
    
    if version.major >= 3 and version.minor >= 8:
        print(f"{Fore.GREEN}✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"{Fore.RED}❌ Python 3.8+ مطلوب (الحالي: {version.major}.{version.minor})")
        return False


def check_package(package_name, import_name=None):
    """التحقق من تثبيت حزمة"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"{Fore.GREEN}✅ {package_name}")
        return True
    except ImportError:
        print(f"{Fore.RED}❌ {package_name}")
        return False


def check_packages():
    """التحقق من جميع الحزم"""
    print(f"\n{Fore.CYAN}📦 التحقق من المكتبات...")
    
    packages = [
        ('python-dotenv', 'dotenv'),
        ('requests', 'requests'),
        ('moviepy', 'moviepy.editor'),
        ('Pillow', 'PIL'),
        ('opencv-python', 'cv2'),
        ('numpy', 'numpy'),
        ('yt-dlp', 'yt_dlp'),
        ('selenium', 'selenium'),
        ('colorama', 'colorama'),
    ]
    
    all_installed = True
    for package_name, import_name in packages:
        if not check_package(package_name, import_name):
            all_installed = False
    
    return all_installed


def check_ffmpeg():
    """التحقق من FFmpeg"""
    print(f"\n{Fore.CYAN}🎬 التحقق من FFmpeg...")
    
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"{Fore.GREEN}✅ FFmpeg مثبت")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    print(f"{Fore.RED}❌ FFmpeg غير مثبت")
    return False


def check_files():
    """التحقق من الملفات المطلوبة"""
    print(f"\n{Fore.CYAN}📁 التحقق من الملفات...")
    
    import os
    
    files = [
        'main.py',
        'config.py',
        'video_downloader.py',
        'video_processor.py',
        'video_uploader.py',
        'requirements.txt',
        '.env.example',
    ]
    
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"{Fore.GREEN}✅ {file}")
        else:
            print(f"{Fore.RED}❌ {file}")
            all_exist = False
    
    return all_exist


def check_folders():
    """التحقق من المجلدات"""
    print(f"\n{Fore.CYAN}📂 التحقق من المجلدات...")
    
    import os
    
    folders = ['downloads', 'processed', 'uploaded']
    
    for folder in folders:
        if os.path.exists(folder):
            print(f"{Fore.GREEN}✅ {folder}/")
        else:
            print(f"{Fore.YELLOW}⚠️  {folder}/ (سيتم إنشاؤها تلقائياً)")
    
    return True


def check_env():
    """التحقق من ملف .env"""
    print(f"\n{Fore.CYAN}⚙️  التحقق من الإعدادات...")
    
    import os
    
    if os.path.exists('.env'):
        print(f"{Fore.GREEN}✅ ملف .env موجود")
        
        # التحقق من المحتوى
        with open('.env', 'r') as f:
            content = f.read()
        
        required_keys = [
            'TIKTOK_USERNAME',
            'TIKTOK_PASSWORD',
        ]
        
        all_set = True
        for key in required_keys:
            if f"{key}=your_" in content or f"{key}=" not in content:
                print(f"{Fore.YELLOW}⚠️  {key} غير محدد")
                all_set = False
        
        if all_set:
            print(f"{Fore.GREEN}✅ الإعدادات الأساسية محددة")
        else:
            print(f"{Fore.YELLOW}⚠️  يرجى تحديث ملف .env")
        
        return True
    else:
        print(f"{Fore.YELLOW}⚠️  ملف .env غير موجود")
        print(f"{Fore.YELLOW}   قم بنسخه من .env.example")
        return False


def test_import():
    """اختبار استيراد الوحدات"""
    print(f"\n{Fore.CYAN}🔧 اختبار استيراد الوحدات...")
    
    try:
        from config import Config
        print(f"{Fore.GREEN}✅ config.py")
        
        from video_downloader import TikTokDownloader
        print(f"{Fore.GREEN}✅ video_downloader.py")
        
        from video_processor import VideoProcessor
        print(f"{Fore.GREEN}✅ video_processor.py")
        
        from video_uploader import TikTokUploader
        print(f"{Fore.GREEN}✅ video_uploader.py")
        
        from main import TikTokBot
        print(f"{Fore.GREEN}✅ main.py")
        
        return True
    except Exception as e:
        print(f"{Fore.RED}❌ خطأ في الاستيراد: {str(e)}")
        return False


def print_results(results):
    """طباعة النتائج النهائية"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'النتائج':^60}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    total = len(results)
    passed = sum(results.values())
    
    for test_name, passed_test in results.items():
        status = f"{Fore.GREEN}✅" if passed_test else f"{Fore.RED}❌"
        print(f"{status} {test_name}")
    
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}النتيجة: {passed}/{total} اختبارات نجحت")
    
    if passed == total:
        print(f"{Fore.GREEN}{'='*60}")
        print(f"{Fore.GREEN}✅ جميع الاختبارات نجحت!")
        print(f"{Fore.GREEN}{'='*60}\n")
        print(f"{Fore.CYAN}🚀 يمكنك الآن تشغيل البوت:")
        print(f"{Fore.WHITE}   python main.py\n")
        return True
    else:
        print(f"{Fore.YELLOW}{'='*60}")
        print(f"{Fore.YELLOW}⚠️  بعض الاختبارات فشلت")
        print(f"{Fore.YELLOW}{'='*60}\n")
        print(f"{Fore.CYAN}يرجى حل المشاكل أعلاه قبل تشغيل البوت\n")
        return False


def main():
    """الدالة الرئيسية"""
    print_header()
    
    results = {
        'Python 3.8+': check_python(),
        'المكتبات المطلوبة': check_packages(),
        'FFmpeg': check_ffmpeg(),
        'الملفات الأساسية': check_files(),
        'المجلدات': check_folders(),
        'ملف الإعدادات': check_env(),
        'استيراد الوحدات': test_import(),
    }
    
    success = print_results(results)
    
    return 0 if success else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️  تم إيقاف الاختبار")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}❌ خطأ: {str(e)}")
        sys.exit(1)
