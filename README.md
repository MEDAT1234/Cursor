# 🤖 بوت تيكتوك - استنساخ ورفع الفيديوهات الترندية

بوت بايثون متطور لاستنساخ فيديوهات تيكتوك الترندية (مثل ASMR)، معالجتها لجعلها فريدة، ورفعها تلقائياً على قناتك.

> 🎯 **مبتدئ؟** ابدأ من [START_HERE.md](START_HERE.md) - 3 خطوات فقط!  
> 📘 **بداية سريعة؟** راجع [QUICK_START.md](QUICK_START.md) للبدء في 5 دقائق!

## ✨ المميزات

- 📥 **تحميل الفيديوهات**: تحميل فيديوهات من تيكتوك باستخدام yt-dlp
- 🎨 **معالجة متقدمة**: تطبيق فلاتر وتأثيرات لجعل الفيديوهات فريدة
  - تغيير السرعة بشكل عشوائي
  - قص الحواف
  - تعديل السطوع والتباين
  - عكس أفقي
  - فلاتر لونية (دافئ، بارد، قديم)
  - إضافة علامة مائية
- 📤 **رفع تلقائي**: رفع الفيديوهات على تيكتوك (يدوي حالياً بسبب قيود تيكتوك)
- ⚙️ **قابل للتخصيص**: إعدادات مرنة عبر ملف .env
- 🎯 **سهل الاستخدام**: واجهة بسيطة وملونة

## 📋 المتطلبات

- Python 3.8 أو أحدث
- FFmpeg (لمعالجة الفيديوهات)
- Chrome/Chromium (للرفع على تيكتوك)

## 🚀 التثبيت

### 1. تثبيت Python وتحديثه

```bash
# تحقق من إصدار Python
python3 --version

# يجب أن يكون 3.8 أو أحدث
```

### 2. تثبيت FFmpeg

#### على Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### على macOS:
```bash
brew install ffmpeg
```

#### على Windows:
قم بتحميل FFmpeg من [الموقع الرسمي](https://ffmpeg.org/download.html) وإضافته لمتغيرات النظام.

### 3. استنساخ المشروع

```bash
git clone <repository-url>
cd <project-folder>
```

### 4. إنشاء بيئة افتراضية (موصى به)

```bash
python3 -m venv venv

# على Linux/macOS:
source venv/bin/activate

# على Windows:
venv\Scripts\activate
```

### 5. تثبيت المكتبات المطلوبة

```bash
pip install -r requirements.txt
```

### 6. تثبيت متصفحات Playwright (اختياري)

```bash
playwright install chromium
```

## ⚙️ الإعداد

### 1. إنشاء ملف الإعدادات

انسخ ملف `.env.example` إلى `.env`:

```bash
cp .env.example .env
```

### 2. تحرير ملف .env

افتح ملف `.env` وعدّل الإعدادات:

```env
# إعدادات تيكتوك
TIKTOK_USERNAME=your_username
TIKTOK_PASSWORD=your_password

# إعدادات الفيديو
VIDEO_CATEGORY=asmr
MAX_VIDEOS_TO_DOWNLOAD=5
VIDEO_MIN_VIEWS=100000

# إعدادات المعالجة
APPLY_FILTERS=true
CHANGE_SPEED=true
ADD_WATERMARK=false
WATERMARK_TEXT=

# إعدادات الرفع
AUTO_UPLOAD=true
UPLOAD_CAPTION=
ADD_HASHTAGS=true
DEFAULT_HASHTAGS=#asmr #satisfying #viral #fyp
```

### 3. إنشاء ملف الروابط

أنشئ ملف `video_urls.txt` وأضف روابط الفيديوهات (رابط واحد في كل سطر):

```
https://www.tiktok.com/@username/video/1234567890
https://www.tiktok.com/@username/video/0987654321
https://www.tiktok.com/@username/video/1122334455
```

## 📖 طريقة الاستخدام

### الطريقة الأساسية

```bash
python main.py
```

سيقوم البوت بـ:
1. قراءة الروابط من `video_urls.txt`
2. تحميل الفيديوهات
3. معالجتها وتطبيق التأثيرات
4. رفعها على تيكتوك (يدوي حالياً)

### الاستخدام البرمجي

يمكنك استخدام البوت كمكتبة في كودك:

```python
from main import TikTokBot

# إنشاء البوت
bot = TikTokBot()

# تشغيل العملية الكاملة
urls = [
    'https://www.tiktok.com/@username/video/1234567890',
    'https://www.tiktok.com/@username/video/0987654321'
]
bot.run(urls=urls)
```

### استخدام الوحدات بشكل منفصل

#### 1. تحميل الفيديوهات فقط

```python
from video_downloader import TikTokDownloader

downloader = TikTokDownloader()
video_info = downloader.download_video('https://www.tiktok.com/@username/video/1234567890')
```

#### 2. معالجة الفيديوهات فقط

```python
from video_processor import VideoProcessor

processor = VideoProcessor()
processed = processor.process_video_complete(
    'downloads/video.mp4',
    apply_filter=True,
    add_watermark_text='@YourChannel'
)
```

#### 3. رفع الفيديوهات فقط

```python
from video_uploader import TikTokUploader

uploader = TikTokUploader('username', 'password')
uploader.login()
uploader.upload_video(
    'processed/video.mp4',
    caption='فيديو رائع!',
    hashtags=['asmr', 'viral', 'fyp']
)
uploader.close()
```

## 🎬 كيفية الحصول على روابط الفيديوهات

### 1. البحث اليدوي

1. افتح تيكتوك في المتصفح
2. ابحث عن الكلمة المفتاحية (مثل: ASMR)
3. افتح الفيديو الذي تريده
4. انسخ الرابط من شريط العنوان
5. ألصقه في `video_urls.txt`

### 2. استخدام أدوات خارجية

يمكنك استخدام أدوات مثل:
- TikTok Scraper
- TikTok API
- أدوات البحث المتقدمة

## 🔧 التخصيص المتقدم

### تعديل التأثيرات

في ملف `video_processor.py`، يمكنك تعديل التأثيرات المطبقة:

```python
# تغيير نطاق السرعة
speed_factor = random.uniform(0.85, 1.15)  # بدلاً من 0.90-1.10

# تعديل السطوع
brightness_factor = random.uniform(0.90, 1.10)  # بدلاً من 0.95-1.05

# إضافة تأثيرات جديدة
clip = clip.fx(vfx.rotate, 2)  # تدوير بسيط
```

### إضافة فلاتر مخصصة

```python
def my_custom_filter(get_frame, t):
    frame = get_frame(t)
    # طبّق التأثير المخصص هنا
    return frame

clip = clip.fl(my_custom_filter)
```

## 📁 هيكل المشروع

```
.
├── main.py                 # السكريبت الرئيسي
├── config.py              # إدارة الإعدادات
├── video_downloader.py    # وحدة تحميل الفيديوهات
├── video_processor.py     # وحدة معالجة الفيديوهات
├── video_uploader.py      # وحدة رفع الفيديوهات
├── requirements.txt       # المكتبات المطلوبة
├── .env.example          # ملف الإعدادات النموذجي
├── .env                  # الإعدادات الفعلية (لا يُرفع على Git)
├── video_urls.txt        # ملف الروابط
├── downloads/            # الفيديوهات المحملة
├── processed/            # الفيديوهات المعالجة
└── uploaded/             # الفيديوهات المرفوعة
```

## ⚠️ ملاحظات مهمة

### حول الرفع التلقائي

حالياً، يتطلب رفع الفيديوهات على تيكتوك تدخل يدوي بسبب:
- نظام الحماية القوي من تيكتوك ضد البوتات
- تغيير واجهة الموقع باستمرار
- متطلبات التحقق (CAPTCHA)

**الحلول المقترحة:**
1. **TikTok API الرسمي**: الحل الأفضل والأكثر موثوقية
2. **استخدام Cookies**: حفظ جلسة تسجيل الدخول
3. **رفع يدوي**: البوت يفتح المتصفح وتقوم بالرفع يدوياً

### حقوق النشر

⚠️ **تنبيه قانوني**: 
- تأكد من حقك في استخدام الفيديوهات
- المعالجة لا تعني بالضرورة تجنب انتهاك حقوق النشر
- استخدم البوت بشكل مسؤول وقانوني
- يُفضل إنشاء محتوى أصلي

### التأثيرات والمعالجة

- التأثيرات المطبقة تجعل الفيديو مختلفاً تقنياً
- لكنها لا تغير المحتوى الأساسي
- استخدم هذا للإلهام وليس للنسخ المباشر

## 🐛 حل المشاكل

### مشكلة: "FFmpeg not found"

**الحل:**
```bash
# تثبيت FFmpeg
sudo apt install ffmpeg  # على Ubuntu/Debian
brew install ffmpeg      # على macOS
```

### مشكلة: "yt-dlp can't download video"

**الحلول:**
- تحديث yt-dlp: `pip install -U yt-dlp`
- تحقق من صحة الرابط
- بعض الفيديوهات قد تكون محمية

### مشكلة: "تسجيل الدخول فشل"

**الحلول:**
- تأكد من صحة اسم المستخدم وكلمة المرور
- تيكتوك قد يطلب تحقق إضافي
- استخدم تسجيل الدخول اليدوي في المتصفح
- جرب استخدام ملفات cookies

### مشكلة: "معالجة الفيديو بطيئة"

**الحلول:**
- قلّل جودة الفيديو
- قلّل عدد التأثيرات المطبقة
- استخدم جهاز بمواصفات أقوى
- عالج الفيديوهات على دفعات

## 🔐 الأمان

- لا تشارك ملف `.env` أبداً
- احفظ بياناتك بشكل آمن
- استخدم كلمات مرور قوية
- فعّل المصادقة الثنائية على حساب تيكتوك

## 📊 الأداء

### متوسط الأوقات

- تحميل فيديو واحد: 10-30 ثانية
- معالجة فيديو (30 ثانية): 1-3 دقائق
- رفع فيديو: 30-60 ثانية (يدوي)

### التحسينات

- استخدام SSD للتخزين المؤقت
- معالج قوي (8+ cores)
- ذاكرة كافية (8GB+ RAM)

## 🤝 المساهمة

المساهمات مرحب بها! يمكنك:
- الإبلاغ عن الأخطاء
- اقتراح ميزات جديدة
- تحسين الكود
- تحسين التوثيق

## 📄 الترخيص

هذا المشروع للأغراض التعليمية فقط. استخدمه بمسؤولية واحترم حقوق الملكية الفكرية.

## 🙏 شكر وتقدير

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - تحميل الفيديوهات
- [MoviePy](https://github.com/Zulko/moviepy) - معالجة الفيديوهات
- [Selenium](https://www.selenium.dev/) - التحكم في المتصفح

## 📞 الدعم

إذا واجهت مشاكل أو لديك أسئلة:
1. راجع قسم حل المشاكل أعلاه
2. تحقق من الإعدادات في `.env`
3. تأكد من تثبيت جميع المتطلبات
4. افتح issue في المشروع

---

**ملاحظة نهائية**: استخدم هذا البوت بشكل أخلاقي ومسؤول. احترم حقوق المبدعين الأصليين وقوانين حقوق النشر.

## 🎬 لقطة شاشة من البوت

البوت يعمل بواجهة ملونة وسهلة الاستخدام في Terminal/CMD.

## 🎯 مثال على النتيجة النهائية

بعد تشغيل البوت:
- ✅ يتم تحميل الفيديوهات من تيكتوك
- ✅ يتم معالجتها وتطبيق تأثيرات فريدة
- ✅ جاهزة للرفع على قناتك

## 📚 جدول المحتويات

- [المميزات](#-المميزات)
- [المتطلبات](#-المتطلبات)
- [التثبيت](#-التثبيت)
- [الإعداد](#️-الإعداد)
- [طريقة الاستخدام](#-طريقة-الاستخدام)
- [التخصيص المتقدم](#-التخصيص-المتقدم)
- [هيكل المشروع](#-هيكل-المشروع)
- [ملاحظات مهمة](#️-ملاحظات-مهمة)
- [حل المشاكل](#-حل-المشاكل)
- [الأمان](#-الأمان)
- [الأداء](#-الأداء)
- [المساهمة](#-المساهمة)
- [الترخيص](#-الترخيص)

---

## 📋 ملفات المشروع

### 📖 التوثيق
- [START_HERE.md](START_HERE.md) - ابدأ هنا (3 خطوات)
- [QUICK_START.md](QUICK_START.md) - البداية السريعة (5 دقائق)
- [README.md](README.md) - هذا الملف - الدليل الكامل
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - شرح هيكل المشروع
- [CONTRIBUTING.md](CONTRIBUTING.md) - دليل المساهمة
- [SUMMARY.md](SUMMARY.md) - ملخص المشروع

### 🐍 الكود الأساسي
- `main.py` - السكريبت الرئيسي
- `config.py` - إدارة الإعدادات
- `video_downloader.py` - تحميل الفيديوهات
- `video_processor.py` - معالجة الفيديوهات
- `video_uploader.py` - رفع الفيديوهات

### 🛠️ الأدوات
- `setup.py` - سكريبت الإعداد
- `test_installation.py` - اختبار التثبيت
- `examples.py` - أمثلة عملية
- `run.sh` / `run.bat` - سكريبتات التشغيل

---

صُنع بـ ❤️ للمبدعين العرب
