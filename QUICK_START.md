# 🚀 البداية السريعة

دليل سريع لتشغيل البوت في 5 دقائق!

## ⚡ الخطوات السريعة

### 1️⃣ التثبيت

```bash
# استنساخ المشروع
git clone <repository-url>
cd <project-folder>

# إنشاء بيئة افتراضية
python3 -m venv venv
source venv/bin/activate  # على Linux/macOS
# أو
venv\Scripts\activate  # على Windows

# تشغيل سكريبت الإعداد
python setup.py
```

### 2️⃣ الإعدادات

افتح ملف `.env` وعدّل:

```env
TIKTOK_USERNAME=your_username
TIKTOK_PASSWORD=your_password
```

### 3️⃣ إضافة الروابط

افتح `video_urls.txt` وأضف روابط الفيديوهات:

```
https://www.tiktok.com/@username/video/1234567890
https://www.tiktok.com/@username/video/0987654321
```

### 4️⃣ التشغيل

```bash
python main.py
```

## 🎯 كيفية الحصول على روابط الفيديوهات

### الطريقة 1: من المتصفح

1. افتح تيكتوك في المتصفح
2. ابحث عن "asmr" أو أي كلمة مفتاحية
3. افتح فيديو ترندي
4. انسخ الرابط من شريط العنوان
5. ألصقه في `video_urls.txt`

### الطريقة 2: من تطبيق تيكتوك

1. افتح التطبيق
2. اختر فيديو
3. اضغط "مشاركة" → "نسخ الرابط"
4. ألصقه في `video_urls.txt`

## 📱 مثال عملي كامل

### السيناريو: استنساخ فيديوهات ASMR

```bash
# 1. ابحث عن فيديوهات ASMR في تيكتوك
# 2. انسخ 3-5 روابط لفيديوهات ترندية

# 3. أضفها في video_urls.txt
cat > video_urls.txt << EOF
https://www.tiktok.com/@asmr_creator1/video/7123456789
https://www.tiktok.com/@asmr_creator2/video/7234567890
https://www.tiktok.com/@asmr_creator3/video/7345678901
EOF

# 4. شغّل البوت
python main.py
```

### ما سيحدث:

1. ⬇️ **التحميل**: سيتم تحميل الفيديوهات الثلاثة
2. 🎨 **المعالجة**: 
   - تغيير السرعة بشكل طفيف
   - قص الحواف
   - تعديل الألوان
   - عكس أفقي (عشوائي)
   - إضافة فلتر لوني
3. 📤 **الرفع**: سيُفتح متصفح لتسجيل الدخول والرفع

## 🔧 إعدادات سريعة

### تعطيل العلامة المائية

في `.env`:
```env
ADD_WATERMARK=false
```

### تغيير عدد الفيديوهات

في `.env`:
```env
MAX_VIDEOS_TO_DOWNLOAD=10
```

### تخصيص الهاشتاقات

في `.env`:
```env
DEFAULT_HASHTAGS=#asmr #satisfying #viral #fyp #trending
```

## ⚠️ حل المشاكل السريع

### المشكلة: لا يمكن تحميل الفيديو

**الحل:**
```bash
pip install -U yt-dlp
```

### المشكلة: FFmpeg not found

**الحل:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg
```

### المشكلة: فشل تسجيل الدخول

**الحل:**
- تأكد من صحة اسم المستخدم وكلمة المرور
- سجّل دخول يدوياً في المتصفح الذي سيُفتح
- انتظر 5 دقائق كحد أقصى

## 🎬 أمثلة الاستخدام

### تحميل فقط (بدون معالجة أو رفع)

```python
from video_downloader import TikTokDownloader

downloader = TikTokDownloader()
downloader.download_video('https://www.tiktok.com/@user/video/123')
```

### معالجة فقط (لفيديو محمّل مسبقاً)

```python
from video_processor import VideoProcessor

processor = VideoProcessor()
processor.process_video_complete('downloads/video.mp4')
```

### رفع فقط (لفيديو معالج)

```python
from video_uploader import TikTokUploader

uploader = TikTokUploader('username', 'password')
uploader.login()
uploader.upload_video('processed/video.mp4', 'وصف رائع!', ['tag1', 'tag2'])
uploader.close()
```

## 📊 نصائح للنجاح

### ✅ افعل:
- اختر فيديوهات ترندية (مشاهدات عالية)
- استخدم هاشتاقات شائعة
- ارفع في أوقات الذروة
- نوّع المحتوى

### ❌ لا تفعل:
- نسخ محتوى محمي بحقوق نشر
- رفع نفس الفيديو عدة مرات
- استخدام هاشتاقات غير مرتبطة
- البقاء في فئة واحدة فقط

## 🎯 استراتيجية النجاح

### للمبتدئين:

1. ابدأ بـ 2-3 فيديوهات يومياً
2. اختبر أوقات رفع مختلفة
3. راقب التحليلات
4. عدّل الاستراتيجية بناءً على النتائج

### للمتقدمين:

1. استخدم TikTok Analytics
2. حلل الترندات
3. خصص التأثيرات حسب الفئة
4. اصنع محتوى فريد مستوحى من الترند

## 🔐 نصائح الأمان

- لا تشارك ملف `.env`
- استخدم حساب اختبار أولاً
- فعّل المصادقة الثنائية
- احفظ نسخة احتياطية من الإعدادات

## 📞 الدعم السريع

### وثائق كاملة
```bash
cat README.md
```

### أمثلة مفصلة
```bash
python examples.py
```

### التحقق من الإعدادات
```bash
python -c "from config import Config; Config.print_config()"
```

## 🎉 جاهز؟

```bash
# تأكد من كل شيء
python setup.py

# شغّل البوت
python main.py
```

---

**💡 نصيحة**: ابدأ بفيديو واحد للتجربة أولاً!

**⚠️ تذكير**: استخدم البوت بشكل مسؤول واحترم حقوق النشر.

للمزيد من التفاصيل، راجع `README.md` 📖
