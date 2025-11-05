# 🚀 ابدأ هنا!

مرحباً بك في **بوت تيكتوك لاستنساخ ورفع الفيديوهات**! 

## ⚡ 3 خطوات فقط للبدء

### 1️⃣ التثبيت (دقيقة واحدة)

```bash
# تثبيت المكتبات
pip install -r requirements.txt

# أو استخدام سكريبت الإعداد
python setup.py
```

### 2️⃣ الإعدادات (دقيقة واحدة)

```bash
# نسخ ملف الإعدادات
cp .env.example .env

# تحرير الإعدادات
nano .env
# غيّر: TIKTOK_USERNAME و TIKTOK_PASSWORD
```

### 3️⃣ التشغيل (دقيقة واحدة)

```bash
# أضف روابط الفيديوهات في video_urls.txt
echo "https://www.tiktok.com/@user/video/123" > video_urls.txt

# شغّل البوت
python main.py
```

---

## 📚 ملفات التوثيق

اختر ما يناسبك:

| الملف | متى تقرأه؟ |
|------|------------|
| 📘 [README.md](README.md) | دليل شامل كامل |
| ⚡ [QUICK_START.md](QUICK_START.md) | البداية السريعة (5 دقائق) |
| 📁 [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | فهم بنية المشروع |
| 💡 [examples.py](examples.py) | أمثلة عملية |
| 🤝 [CONTRIBUTING.md](CONTRIBUTING.md) | المساهمة في المشروع |

---

## 🎯 حسب مستواك

### 🟢 مبتدئ؟

```bash
# 1. شغّل الإعداد التلقائي
python setup.py

# 2. اتبع التعليمات
python main.py
```

### 🟡 متوسط؟

```python
# استخدم الوحدات بشكل منفصل
from video_downloader import TikTokDownloader
downloader = TikTokDownloader()
downloader.download_video('https://...')
```

### 🔴 متقدم؟

```python
# خصص كل شيء
from main import TikTokBot
bot = TikTokBot()
# أضف تأثيراتك المخصصة
# راجع examples.py
```

---

## 🔧 اختبار التثبيت

قبل البدء، اختبر أن كل شيء يعمل:

```bash
python test_installation.py
```

سيتحقق هذا من:
- ✅ Python 3.8+
- ✅ المكتبات المطلوبة
- ✅ FFmpeg
- ✅ الملفات والإعدادات

---

## 🎬 مثال سريع

### السيناريو: تحميل ومعالجة فيديو ASMR

```bash
# 1. إنشاء ملف الروابط
cat > video_urls.txt << EOF
https://www.tiktok.com/@asmr_user/video/1234567890
EOF

# 2. تشغيل البوت
python main.py

# 3. النتيجة:
# ✅ downloads/video_1_*.mp4 (الفيديو الأصلي)
# ✅ processed/video_1_*_final.mp4 (الفيديو المعالج)
```

---

## ⚠️ ملاحظات مهمة

### قبل البدء:

1. ⚡ **FFmpeg مطلوب**
   ```bash
   # Ubuntu/Debian
   sudo apt install ffmpeg
   
   # macOS
   brew install ffmpeg
   ```

2. 🔐 **حدد بيانات تيكتوك**
   - في ملف `.env`
   - `TIKTOK_USERNAME` و `TIKTOK_PASSWORD`

3. 🎯 **احصل على روابط الفيديوهات**
   - افتح تيكتوك في المتصفح
   - ابحث عن "asmr" أو أي كلمة
   - انسخ روابط الفيديوهات

### أثناء الاستخدام:

- 📤 الرفع على تيكتوك يتطلب تدخل يدوي حالياً
- 🎨 المعالجة تستغرق 1-3 دقائق لكل فيديو
- 📥 التحميل يعتمد على سرعة الإنترنت

---

## 🆘 مشاكل شائعة

### "FFmpeg not found"
```bash
sudo apt install ffmpeg
```

### "yt-dlp can't download"
```bash
pip install -U yt-dlp
```

### "فشل تسجيل الدخول"
- تأكد من صحة بيانات الدخول
- سجل يدوياً في المتصفح

---

## 📞 الدعم

| المشكلة | الحل |
|---------|------|
| 🐛 خطأ تقني | راجع [README.md](README.md) → حل المشاكل |
| 💡 كيفية الاستخدام | راجع [examples.py](examples.py) |
| 🤔 سؤال عام | راجع [QUICK_START.md](QUICK_START.md) |

---

## 🎉 جاهز للبدء؟

### الطريقة السريعة:

```bash
# واحد، اثنان، ثلاثة!
python setup.py && python main.py
```

### الطريقة الآمنة:

```bash
# 1. اختبار
python test_installation.py

# 2. إعداد
nano .env

# 3. تشغيل
python main.py
```

---

## 🌟 نصيحة أخيرة

**ابدأ بفيديو واحد للتجربة!**

```bash
# تجربة مع فيديو واحد
echo "https://www.tiktok.com/@user/video/123" > video_urls.txt
python main.py
```

---

## 💖 استمتع!

هذا البوت صُنع بـ ❤️ لمساعدتك في إنشاء محتوى رائع.

استخدمه بمسؤولية واحترم حقوق المبدعين! 🙏

---

**الخطوة التالية**: افتح [QUICK_START.md](QUICK_START.md) للتفاصيل! 📘
