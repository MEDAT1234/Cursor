"""
سكريبت الإعداد السريع للمشروع
يقوم بتثبيت المتطلبات وإنشاء الملفات الضرورية
"""

import os
import sys
import subprocess
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def print_header():
    """طباعة رأس البرنامج"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'برنامج إعداد بوت تيكتوك':^60}")
    print(f"{Fore.CYAN}{'='*60}\n")


def check_python_version():
    """التحقق من إصدار Python"""
    print(f"{Fore.CYAN}🐍 التحقق من إصدار Python...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"{Fore.RED}❌ Python 3.8 أو أحدث مطلوب!")
        print(f"{Fore.YELLOW}   الإصدار الحالي: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"{Fore.GREEN}✅ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_ffmpeg():
    """التحقق من تثبيت FFmpeg"""
    print(f"\n{Fore.CYAN}🎬 التحقق من FFmpeg...")
    
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"{Fore.GREEN}✅ FFmpeg مثبت")
            return True
    except FileNotFoundError:
        pass
    
    print(f"{Fore.YELLOW}⚠️  FFmpeg غير مثبت")
    print(f"{Fore.YELLOW}   يرجى تثبيته:")
    print(f"{Fore.WHITE}   - Ubuntu/Debian: sudo apt install ffmpeg")
    print(f"{Fore.WHITE}   - macOS: brew install ffmpeg")
    print(f"{Fore.WHITE}   - Windows: قم بتحميله من ffmpeg.org")
    return False


def install_requirements():
    """تثبيت المتطلبات من requirements.txt"""
    print(f"\n{Fore.CYAN}📦 تثبيت المكتبات المطلوبة...")
    
    try:
        subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
            check=True
        )
        print(f"{Fore.GREEN}✅ تم تثبيت المكتبات بنجاح")
        return True
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}❌ فشل تثبيت المكتبات")
        return False


def create_env_file():
    """إنشاء ملف .env من .env.example"""
    print(f"\n{Fore.CYAN}⚙️  إعداد ملف الإعدادات...")
    
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if env_file.exists():
        print(f"{Fore.YELLOW}⚠️  ملف .env موجود بالفعل")
        response = input(f"{Fore.YELLOW}هل تريد استبداله؟ (y/n): ")
        if response.lower() != 'y':
            print(f"{Fore.CYAN}تم الاحتفاظ بالملف الموجود")
            return True
    
    if env_example.exists():
        with open(env_example, 'r', encoding='utf-8') as src:
            content = src.read()
        
        with open(env_file, 'w', encoding='utf-8') as dst:
            dst.write(content)
        
        print(f"{Fore.GREEN}✅ تم إنشاء ملف .env")
        print(f"{Fore.YELLOW}⚠️  يرجى تحديث الإعدادات في ملف .env")
        return True
    else:
        print(f"{Fore.RED}❌ ملف .env.example غير موجود")
        return False


def create_folders():
    """إنشاء المجلدات المطلوبة"""
    print(f"\n{Fore.CYAN}📁 إنشاء المجلدات...")
    
    folders = ['downloads', 'processed', 'uploaded']
    
    for folder in folders:
        Path(folder).mkdir(exist_ok=True)
        print(f"{Fore.GREEN}✅ {folder}/")
    
    return True


def install_playwright():
    """تثبيت متصفحات Playwright (اختياري)"""
    print(f"\n{Fore.CYAN}🌐 تثبيت متصفحات Playwright (اختياري)...")
    
    response = input(f"{Fore.YELLOW}هل تريد تثبيت Playwright؟ (y/n): ")
    if response.lower() == 'y':
        try:
            subprocess.run(
                ['playwright', 'install', 'chromium'],
                check=True
            )
            print(f"{Fore.GREEN}✅ تم تثبيت Playwright")
            return True
        except subprocess.CalledProcessError:
            print(f"{Fore.YELLOW}⚠️  فشل تثبيت Playwright (يمكن المتابعة بدونه)")
            return False
    else:
        print(f"{Fore.CYAN}تم التخطي")
        return True


def print_next_steps():
    """طباعة الخطوات التالية"""
    print(f"\n{Fore.GREEN}{'='*60}")
    print(f"{Fore.GREEN}✅ اكتمل الإعداد بنجاح!")
    print(f"{Fore.GREEN}{'='*60}\n")
    
    print(f"{Fore.CYAN}📋 الخطوات التالية:")
    print(f"{Fore.WHITE}1. حدّث ملف .env بمعلومات حسابك:")
    print(f"{Fore.YELLOW}   nano .env")
    
    print(f"\n{Fore.WHITE}2. أضف روابط الفيديوهات في video_urls.txt:")
    print(f"{Fore.YELLOW}   nano video_urls.txt")
    
    print(f"\n{Fore.WHITE}3. شغّل البوت:")
    print(f"{Fore.YELLOW}   python main.py")
    
    print(f"\n{Fore.CYAN}📖 للمزيد من المعلومات، راجع README.md\n")


def main():
    """الدالة الرئيسية"""
    print_header()
    
    # التحقق من Python
    if not check_python_version():
        return False
    
    # التحقق من FFmpeg
    ffmpeg_ok = check_ffmpeg()
    
    # تثبيت المتطلبات
    if not install_requirements():
        return False
    
    # إنشاء ملف .env
    if not create_env_file():
        return False
    
    # إنشاء المجلدات
    if not create_folders():
        return False
    
    # تثبيت Playwright (اختياري)
    install_playwright()
    
    # طباعة الخطوات التالية
    print_next_steps()
    
    if not ffmpeg_ok:
        print(f"{Fore.YELLOW}⚠️  تذكير: يجب تثبيت FFmpeg لمعالجة الفيديوهات\n")
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️  تم إيقاف الإعداد")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}❌ خطأ: {str(e)}")
        sys.exit(1)
