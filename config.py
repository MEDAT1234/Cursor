"""
ملف التكوين والإعدادات
يقوم بتحميل المتغيرات من ملف .env
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()


class Config:
    """فئة الإعدادات"""
    
    # إعدادات تيكتوك
    TIKTOK_USERNAME = os.getenv('TIKTOK_USERNAME', '')
    TIKTOK_PASSWORD = os.getenv('TIKTOK_PASSWORD', '')
    
    # إعدادات الفيديو
    VIDEO_CATEGORY = os.getenv('VIDEO_CATEGORY', 'asmr')
    MAX_VIDEOS_TO_DOWNLOAD = int(os.getenv('MAX_VIDEOS_TO_DOWNLOAD', 5))
    VIDEO_MIN_VIEWS = int(os.getenv('VIDEO_MIN_VIEWS', 100000))
    
    # إعدادات المعالجة
    APPLY_FILTERS = os.getenv('APPLY_FILTERS', 'true').lower() == 'true'
    CHANGE_SPEED = os.getenv('CHANGE_SPEED', 'true').lower() == 'true'
    ADD_WATERMARK = os.getenv('ADD_WATERMARK', 'false').lower() == 'true'
    WATERMARK_TEXT = os.getenv('WATERMARK_TEXT', '')
    
    # إعدادات الرفع
    AUTO_UPLOAD = os.getenv('AUTO_UPLOAD', 'true').lower() == 'true'
    UPLOAD_CAPTION = os.getenv('UPLOAD_CAPTION', '')
    ADD_HASHTAGS = os.getenv('ADD_HASHTAGS', 'true').lower() == 'true'
    DEFAULT_HASHTAGS = os.getenv('DEFAULT_HASHTAGS', '#asmr #satisfying #viral #fyp')
    
    # مجلدات العمل
    BASE_DIR = Path(__file__).parent
    DOWNLOAD_FOLDER = BASE_DIR / os.getenv('DOWNLOAD_FOLDER', 'downloads')
    PROCESSED_FOLDER = BASE_DIR / os.getenv('PROCESSED_FOLDER', 'processed')
    UPLOADED_FOLDER = BASE_DIR / os.getenv('UPLOADED_FOLDER', 'uploaded')
    
    @classmethod
    def create_folders(cls):
        """إنشاء المجلدات المطلوبة"""
        cls.DOWNLOAD_FOLDER.mkdir(exist_ok=True)
        cls.PROCESSED_FOLDER.mkdir(exist_ok=True)
        cls.UPLOADED_FOLDER.mkdir(exist_ok=True)
    
    @classmethod
    def validate(cls) -> bool:
        """
        التحقق من صحة الإعدادات
        
        Returns:
            True إذا كانت الإعدادات صحيحة
        """
        errors = []
        
        if not cls.TIKTOK_USERNAME:
            errors.append("❌ TIKTOK_USERNAME غير محدد")
        
        if not cls.TIKTOK_PASSWORD:
            errors.append("❌ TIKTOK_PASSWORD غير محدد")
        
        if errors:
            print("\n⚠️  أخطاء في الإعدادات:")
            for error in errors:
                print(f"  {error}")
            print("\nيرجى تحديث ملف .env بالمعلومات الصحيحة")
            return False
        
        return True
    
    @classmethod
    def get_hashtags_list(cls) -> list:
        """الحصول على قائمة الهاشتاقات"""
        if cls.DEFAULT_HASHTAGS:
            return [tag.strip() for tag in cls.DEFAULT_HASHTAGS.split()]
        return []
    
    @classmethod
    def print_config(cls):
        """طباعة الإعدادات الحالية"""
        print("\n" + "="*60)
        print("⚙️  الإعدادات الحالية")
        print("="*60)
        
        print(f"\n📱 إعدادات تيكتوك:")
        print(f"  Username: {cls.TIKTOK_USERNAME or '(غير محدد)'}")
        print(f"  Password: {'*' * len(cls.TIKTOK_PASSWORD) if cls.TIKTOK_PASSWORD else '(غير محدد)'}")
        
        print(f"\n🎬 إعدادات الفيديو:")
        print(f"  الفئة: {cls.VIDEO_CATEGORY}")
        print(f"  عدد الفيديوهات: {cls.MAX_VIDEOS_TO_DOWNLOAD}")
        print(f"  الحد الأدنى للمشاهدات: {cls.VIDEO_MIN_VIEWS:,}")
        
        print(f"\n🎨 إعدادات المعالجة:")
        print(f"  تطبيق الفلاتر: {'نعم' if cls.APPLY_FILTERS else 'لا'}")
        print(f"  تغيير السرعة: {'نعم' if cls.CHANGE_SPEED else 'لا'}")
        print(f"  إضافة علامة مائية: {'نعم' if cls.ADD_WATERMARK else 'لا'}")
        if cls.ADD_WATERMARK:
            print(f"  نص العلامة: {cls.WATERMARK_TEXT}")
        
        print(f"\n📤 إعدادات الرفع:")
        print(f"  الرفع التلقائي: {'نعم' if cls.AUTO_UPLOAD else 'لا'}")
        print(f"  إضافة هاشتاقات: {'نعم' if cls.ADD_HASHTAGS else 'لا'}")
        if cls.ADD_HASHTAGS:
            print(f"  الهاشتاقات: {cls.DEFAULT_HASHTAGS}")
        
        print(f"\n📁 المجلدات:")
        print(f"  التحميل: {cls.DOWNLOAD_FOLDER}")
        print(f"  المعالجة: {cls.PROCESSED_FOLDER}")
        print(f"  المرفوعة: {cls.UPLOADED_FOLDER}")
        
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    Config.print_config()
