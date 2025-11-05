"""
أمثلة على استخدام البوت بطرق مختلفة
"""

from main import TikTokBot
from video_downloader import TikTokDownloader
from video_processor import VideoProcessor
from video_uploader import TikTokUploader


def example_1_full_bot():
    """
    مثال 1: استخدام البوت الكامل
    """
    print("\n" + "="*60)
    print("مثال 1: استخدام البوت الكامل")
    print("="*60 + "\n")
    
    # إنشاء البوت
    bot = TikTokBot()
    
    # تشغيل البوت مع روابط مباشرة
    urls = [
        'https://www.tiktok.com/@username/video/1234567890',
        'https://www.tiktok.com/@username/video/0987654321',
    ]
    
    bot.run(urls=urls)


def example_2_download_only():
    """
    مثال 2: تحميل الفيديوهات فقط
    """
    print("\n" + "="*60)
    print("مثال 2: تحميل الفيديوهات فقط")
    print("="*60 + "\n")
    
    # إنشاء المحمّل
    downloader = TikTokDownloader("downloads")
    
    # تحميل فيديو واحد
    video_info = downloader.download_video(
        'https://www.tiktok.com/@username/video/1234567890'
    )
    
    if video_info:
        print(f"\n✅ تم التحميل: {video_info['title']}")
        print(f"   المسار: {video_info['path']}")
        print(f"   المدة: {video_info['duration']} ثانية")
        print(f"   المشاهدات: {video_info['views']:,}")
    
    # حفظ البيانات الوصفية
    downloader.save_metadata()


def example_3_process_only():
    """
    مثال 3: معالجة الفيديوهات فقط
    """
    print("\n" + "="*60)
    print("مثال 3: معالجة الفيديوهات فقط")
    print("="*60 + "\n")
    
    # إنشاء المعالج
    processor = VideoProcessor("processed")
    
    # معالجة فيديو واحد
    video_path = "downloads/video_1.mp4"  # استبدل بالمسار الصحيح
    
    result = processor.process_video_complete(
        video_path,
        apply_filter=True,
        add_watermark_text="@YourChannel"
    )
    
    if result:
        print(f"\n✅ تمت المعالجة")
        print(f"   الملف الأصلي: {result['original_path']}")
        print(f"   الملف المعالج: {result['processed_path']}")


def example_4_custom_effects():
    """
    مثال 4: تطبيق تأثيرات مخصصة
    """
    print("\n" + "="*60)
    print("مثال 4: تطبيق تأثيرات مخصصة")
    print("="*60 + "\n")
    
    processor = VideoProcessor("processed")
    
    video_path = "downloads/video_1.mp4"
    
    # 1. تطبيق التأثيرات العشوائية فقط
    temp1 = processor.apply_random_effects(video_path)
    
    # 2. تطبيق فلتر لوني محدد
    temp2 = processor.apply_color_filter(temp1, filter_type="warm")
    
    # 3. إضافة علامة مائية
    final = processor.add_watermark(temp2, "My Channel")
    
    print(f"\n✅ الفيديو النهائي: {final}")


def example_5_batch_processing():
    """
    مثال 5: معالجة دفعة من الفيديوهات
    """
    print("\n" + "="*60)
    print("مثال 5: معالجة دفعة من الفيديوهات")
    print("="*60 + "\n")
    
    processor = VideoProcessor("processed")
    
    # قائمة الفيديوهات
    video_paths = [
        "downloads/video_1.mp4",
        "downloads/video_2.mp4",
        "downloads/video_3.mp4",
    ]
    
    # معالجة جميع الفيديوهات
    results = processor.process_multiple_videos(
        video_paths,
        apply_filter=True,
        add_watermark_text="@MyChannel"
    )
    
    print(f"\n✅ تمت معالجة {len(results)} فيديو")


def example_6_upload_with_custom_captions():
    """
    مثال 6: رفع الفيديوهات مع عناوين مخصصة
    """
    print("\n" + "="*60)
    print("مثال 6: رفع الفيديوهات مع عناوين مخصصة")
    print("="*60 + "\n")
    
    # إنشاء الرافع
    uploader = TikTokUploader("your_username", "your_password")
    
    try:
        # تسجيل الدخول
        if uploader.login():
            
            # قائمة الفيديوهات مع معلوماتها
            videos = [
                {
                    'path': 'processed/video_1_final.mp4',
                    'caption': 'فيديو ASMR مريح 😌',
                    'hashtags': ['asmr', 'relaxing', 'satisfying']
                },
                {
                    'path': 'processed/video_2_final.mp4',
                    'caption': 'محتوى مميز 🔥',
                    'hashtags': ['viral', 'fyp', 'trending']
                },
            ]
            
            # رفع كل فيديو
            for video in videos:
                uploader.upload_video(
                    video['path'],
                    video['caption'],
                    video['hashtags']
                )
    
    finally:
        uploader.close()


def example_7_download_from_file():
    """
    مثال 7: تحميل من ملف روابط
    """
    print("\n" + "="*60)
    print("مثال 7: تحميل من ملف روابط")
    print("="*60 + "\n")
    
    downloader = TikTokDownloader("downloads")
    
    # تحميل من ملف
    videos = downloader.download_from_file("video_urls.txt")
    
    print(f"\n✅ تم تحميل {len(videos)} فيديو")
    
    # طباعة المعلومات
    for i, video in enumerate(videos, 1):
        print(f"\n{i}. {video['title']}")
        print(f"   المشاهدات: {video['views']:,}")
        print(f"   الإعجابات: {video['likes']:,}")
        print(f"   المسار: {video['path']}")


def example_8_complete_workflow():
    """
    مثال 8: سير عمل كامل خطوة بخطوة
    """
    print("\n" + "="*60)
    print("مثال 8: سير عمل كامل خطوة بخطوة")
    print("="*60 + "\n")
    
    # 1. تحميل
    print("الخطوة 1: التحميل")
    downloader = TikTokDownloader("downloads")
    urls = ['https://www.tiktok.com/@username/video/1234567890']
    videos = downloader.download_multiple_videos(urls)
    
    if not videos:
        print("❌ فشل التحميل")
        return
    
    # 2. المعالجة
    print("\nالخطوة 2: المعالجة")
    processor = VideoProcessor("processed")
    video_paths = [v['path'] for v in videos]
    processed = processor.process_multiple_videos(
        video_paths,
        apply_filter=True,
        add_watermark_text="@MyChannel"
    )
    
    if not processed:
        print("❌ فشلت المعالجة")
        return
    
    # 3. الرفع
    print("\nالخطوة 3: الرفع")
    uploader = TikTokUploader("username", "password")
    
    try:
        if uploader.login():
            for video in processed:
                uploader.upload_video(
                    video['processed_path'],
                    "محتوى رائع! #fyp #viral",
                    ['fyp', 'viral', 'trending']
                )
    finally:
        uploader.close()
    
    print("\n✅ اكتمل سير العمل!")


def show_menu():
    """عرض قائمة الأمثلة"""
    print("\n" + "="*60)
    print("أمثلة استخدام بوت تيكتوك")
    print("="*60 + "\n")
    
    examples = [
        "استخدام البوت الكامل",
        "تحميل الفيديوهات فقط",
        "معالجة الفيديوهات فقط",
        "تطبيق تأثيرات مخصصة",
        "معالجة دفعة من الفيديوهات",
        "رفع مع عناوين مخصصة",
        "تحميل من ملف روابط",
        "سير عمل كامل خطوة بخطوة",
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")
    
    print("\n0. خروج")
    print("\n" + "="*60)


def main():
    """الدالة الرئيسية"""
    examples_map = {
        1: example_1_full_bot,
        2: example_2_download_only,
        3: example_3_process_only,
        4: example_4_custom_effects,
        5: example_5_batch_processing,
        6: example_6_upload_with_custom_captions,
        7: example_7_download_from_file,
        8: example_8_complete_workflow,
    }
    
    while True:
        show_menu()
        
        try:
            choice = int(input("\nاختر رقم المثال: "))
            
            if choice == 0:
                print("\nوداعاً! 👋")
                break
            
            if choice in examples_map:
                examples_map[choice]()
                input("\n\nاضغط Enter للمتابعة...")
            else:
                print("\n❌ اختيار غير صحيح!")
        
        except ValueError:
            print("\n❌ يرجى إدخال رقم صحيح!")
        except KeyboardInterrupt:
            print("\n\nتم الإيقاف")
            break


if __name__ == "__main__":
    print("\n⚠️  ملاحظة: هذه أمثلة توضيحية")
    print("يرجى تعديل المسارات والروابط قبل التشغيل\n")
    
    # يمكنك تشغيل مثال محدد مباشرة:
    # example_1_full_bot()
    
    # أو عرض القائمة التفاعلية:
    # main()
    
    print("لتشغيل القائمة التفاعلية، قم بإلغاء التعليق على السطر الأخير")
