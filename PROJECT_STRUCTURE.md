# 📁 هيكل المشروع

## 📂 الملفات الرئيسية

### 🤖 ملفات البوت الأساسية

| الملف | الوصف |
|------|-------|
| `main.py` | 🎯 السكريبت الرئيسي - نقطة البداية |
| `config.py` | ⚙️ إدارة الإعدادات والتكوين |
| `video_downloader.py` | 📥 وحدة تحميل الفيديوهات من تيكتوك |
| `video_processor.py` | 🎨 وحدة معالجة وتطبيق التأثيرات |
| `video_uploader.py` | 📤 وحدة رفع الفيديوهات على تيكتوك |

### 📚 ملفات التوثيق

| الملف | الوصف |
|------|-------|
| `README.md` | 📖 الدليل الكامل المفصل |
| `QUICK_START.md` | ⚡ دليل البداية السريعة |
| `PROJECT_STRUCTURE.md` | 📁 هذا الملف - شرح الهيكل |
| `examples.py` | 💡 أمثلة عملية للاستخدام |

### 🔧 ملفات الإعداد

| الملف | الوصف |
|------|-------|
| `requirements.txt` | 📦 قائمة المكتبات المطلوبة |
| `.env.example` | 🔐 نموذج ملف الإعدادات |
| `.env` | 🔐 الإعدادات الفعلية (لا يُرفع على Git) |
| `.gitignore` | 🚫 ملفات يتم تجاهلها في Git |
| `setup.py` | 🛠️ سكريبت الإعداد التلقائي |

### 🚀 ملفات التشغيل

| الملف | الوصف |
|------|-------|
| `run.sh` | 🐧 سكريبت تشغيل على Linux/macOS |
| `run.bat` | 🪟 سكريبت تشغيل على Windows |
| `video_urls.txt` | 🔗 ملف روابط الفيديوهات |

### 📄 ملفات أخرى

| الملف | الوصف |
|------|-------|
| `LICENSE` | ⚖️ رخصة المشروع |

## 📂 المجلدات

| المجلد | الوصف |
|--------|-------|
| `downloads/` | 📥 الفيديوهات المحملة من تيكتوك |
| `processed/` | 🎨 الفيديوهات بعد المعالجة |
| `uploaded/` | ✅ الفيديوهات التي تم رفعها |
| `venv/` | 🐍 البيئة الافتراضية لـ Python |

## 🔄 تدفق العمل (Workflow)

```
┌─────────────────┐
│ video_urls.txt  │ ← إضافة روابط الفيديوهات
└────────┬────────┘
         ↓
┌────────▼────────┐
│   التحميل       │ ← video_downloader.py
│  downloads/     │
└────────┬────────┘
         ↓
┌────────▼────────┐
│   المعالجة      │ ← video_processor.py
│  processed/     │
└────────┬────────┘
         ↓
┌────────▼────────┐
│    الرفع        │ ← video_uploader.py
│  uploaded/      │
└─────────────────┘
```

## 🎯 كيفية البدء

### للمبتدئين

```bash
# 1. الإعداد
python setup.py

# 2. تحديث الإعدادات
nano .env

# 3. إضافة روابط
nano video_urls.txt

# 4. التشغيل
python main.py
```

### للمستخدمين المتقدمين

```bash
# استخدام الوحدات بشكل منفصل
python -c "from video_downloader import TikTokDownloader; ..."

# أو استخدام الأمثلة
python examples.py
```

## 📊 الوحدات (Modules)

### 1. video_downloader.py

**الفئات:**
- `TikTokDownloader`: تحميل الفيديوهات

**الدوال الرئيسية:**
- `download_video()`: تحميل فيديو واحد
- `download_multiple_videos()`: تحميل عدة فيديوهات
- `download_from_file()`: تحميل من ملف روابط
- `save_metadata()`: حفظ البيانات الوصفية

### 2. video_processor.py

**الفئات:**
- `VideoProcessor`: معالجة الفيديوهات

**الدوال الرئيسية:**
- `apply_random_effects()`: تطبيق تأثيرات عشوائية
- `apply_color_filter()`: تطبيق فلتر لوني
- `add_watermark()`: إضافة علامة مائية
- `process_video_complete()`: معالجة كاملة
- `process_multiple_videos()`: معالجة دفعة

### 3. video_uploader.py

**الفئات:**
- `TikTokUploader`: رفع الفيديوهات (Selenium)
- `TikTokUploaderPlaywright`: رفع الفيديوهات (Playwright)

**الدوال الرئيسية:**
- `login()`: تسجيل الدخول
- `upload_video()`: رفع فيديو واحد
- `upload_multiple_videos()`: رفع عدة فيديوهات
- `close()`: إغلاق المتصفح

### 4. config.py

**الفئات:**
- `Config`: إدارة الإعدادات

**الدوال الرئيسية:**
- `validate()`: التحقق من الإعدادات
- `create_folders()`: إنشاء المجلدات
- `get_hashtags_list()`: الحصول على الهاشتاقات
- `print_config()`: طباعة الإعدادات

### 5. main.py

**الفئات:**
- `TikTokBot`: البوت الرئيسي

**الدوال الرئيسية:**
- `setup()`: الإعداد والتحقق
- `download_videos()`: تحميل الفيديوهات
- `process_videos()`: معالجة الفيديوهات
- `upload_videos()`: رفع الفيديوهات
- `run()`: تشغيل البوت الكامل

## 🔧 التخصيص

### إضافة تأثيرات جديدة

في `video_processor.py`:

```python
def my_custom_effect(self, clip):
    # أضف تأثيرك هنا
    return modified_clip
```

### إضافة مصدر تحميل جديد

في `video_downloader.py`:

```python
def download_from_instagram(self, url):
    # أضف كود التحميل من Instagram
    pass
```

### إضافة منصة رفع جديدة

إنشاء `youtube_uploader.py`:

```python
class YouTubeUploader:
    def upload_video(self, video_path):
        # أضف كود الرفع على YouTube
        pass
```

## 📈 التطويرات المستقبلية

### مخطط لها:
- [ ] دعم TikTok API الرسمي
- [ ] تحسين الرفع التلقائي الكامل
- [ ] إضافة جدولة الرفع
- [ ] دعم منصات أخرى (Instagram, YouTube)
- [ ] واجهة رسومية (GUI)
- [ ] تحليلات وإحصائيات

### يمكنك المساهمة:
- إضافة تأثيرات جديدة
- تحسين خوارزميات المعالجة
- إضافة دعم لغات برمجة أخرى
- تحسين التوثيق

## 🐛 التشخيص

### سجلات الأخطاء (Logs)

يمكنك إضافة logging في أي وحدة:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot.log'
)
```

### الوضع التجريبي (Debug Mode)

في `main.py`، غيّر:

```python
# من
headless=False

# إلى
headless=True  # لرؤية المتصفح
```

## 📞 الدعم الفني

### مشاكل شائعة

| المشكلة | الحل | الموقع |
|---------|------|---------|
| فشل التحميل | تحديث yt-dlp | `video_downloader.py` |
| فشل المعالجة | تثبيت FFmpeg | `video_processor.py` |
| فشل الرفع | تسجيل دخول يدوي | `video_uploader.py` |

### موارد مفيدة

- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [MoviePy Documentation](https://zulko.github.io/moviepy/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)

## 🎓 تعلّم المزيد

### للمبتدئين في Python

1. تعلم أساسيات Python
2. فهم البيئات الافتراضية
3. تعلم إدارة الحزم مع pip

### للمبتدئين في معالجة الفيديو

1. تعلم أساسيات FFmpeg
2. فهم codecs وformats
3. تعلم MoviePy

### للمبتدئين في Web Scraping

1. تعلم Selenium
2. فهم CSS Selectors
3. تعلم التعامل مع CAPTCHA

## 🏆 الإضافات المميزة

### إضافة إشعارات

```python
# في main.py
def send_notification(message):
    # أضف كود الإشعار (Telegram, Email, etc.)
    pass
```

### إضافة قاعدة بيانات

```python
# إضافة SQLite لتتبع الفيديوهات
import sqlite3

def save_to_db(video_info):
    # حفظ في قاعدة البيانات
    pass
```

### إضافة واجهة ويب

```python
# استخدام Flask أو FastAPI
from flask import Flask

app = Flask(__name__)

@app.route('/upload')
def upload():
    # واجهة رفع الفيديوهات
    pass
```

## 🎉 الخلاصة

هذا المشروع يوفر:
- ✅ بنية واضحة ومنظمة
- ✅ وحدات قابلة لإعادة الاستخدام
- ✅ توثيق شامل باللغة العربية
- ✅ أمثلة عملية
- ✅ سهولة في التخصيص

استمتع باستخدام البوت! 🚀

---

آخر تحديث: نوفمبر 2024
