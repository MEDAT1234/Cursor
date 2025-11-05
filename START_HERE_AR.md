# 🎵 ابدأ من هنا - دليل كامل لتشغيل بوت ASMR

## 🎯 ما الذي ستفعله

ستقوم بإعداد بوت يقوم بـ:
1. إنشاء فيديوهات ASMR احترافية تلقائياً
2. نشرها على تيك توك دون تدخلك
3. العمل 24/7 حسب جدول زمني

**الوقت المطلوب:** 10-15 دقيقة للإعداد الأولي

---

## 📋 التعليمات خطوة بخطوة

### الخطوة 1: تثبيت المتطلبات (دقيقتان)

افتح موجه الأوامر (Command Prompt):

**Windows:**
```batch
cd C:\Users\smart\OneDrive\Desktop\Cursor-cursor-automated-asmr-video-generation-and-tiktok-posting-b904
setup.bat
```

انتظر حتى ترى: `✅ Setup complete!`

---

### الخطوة 2: تفعيل البيئة الافتراضية (10 ثوان)

في كل مرة تفتح موجه أوامر جديد، شغّل:

**Windows:**
```batch
cd C:\Users\smart\OneDrive\Desktop\Cursor-cursor-automated-asmr-video-generation-and-tiktok-posting-b904
venv\Scripts\activate.bat
```

سترى `(venv)` في بداية السطر.

---

### الخطوة 3: اختبار إنشاء الفيديو (دقيقة واحدة)

أنشئ فيديو اختبار دون رفعه:

**Windows:**
```batch
python bot.py --mode test
```

**النتيجة المتوقعة:**
```
🎬 Starting video generation...
🔊 Generating ASMR audio...
✨ Creating rain themed visuals...
🎨 Compositing video...
💾 Rendering video to generated_videos/asmr_rain_20251104_120000.mp4...
✅ Video generated successfully: generated_videos/asmr_rain_20251104_120000.mp4
```

**شاهد الفيديو:** افتح الملف في مجلد `generated_videos\`

---

### الخطوة 4: تسجيل دخول تيك توك ونشر أول فيديو (دقيقتان)

**Windows:**
```batch
python bot.py --mode once
```

**ما سيحدث:**

1. **المتصفح يفتح**
   ```
   🔑 Please login to TikTok manually...
   📱 Opening TikTok login page...
   ```
   ستظهر نافذة Chrome مع صفحة تسجيل دخول تيك توك

2. **أنت: سجّل الدخول**
   - أدخل اسم المستخدم وكلمة المرور لتيك توك
   - أكمل أي تحقق ثنائي/تحقق
   - انتظر حتى ترى صفحة تيك توك الرئيسية
   
3. **أنت: اضغط Enter**
   - ارجع لموجه الأوامر
   - اضغط مفتاح `Enter`
   - البوت يحفظ جلستك

4. **البوت ينشئ وينشر الفيديو**
   ```
   🎬 Generating video...
   📤 Uploading to TikTok...
   ✅ Successfully posted to TikTok!
   ```

5. **احفظ معرف الجلسة**
   موجه الأوامر يعرض:
   ```
   💾 Save this session ID for future use:
      abc123xyz789...
   ```
   
   **مهم جداً:** انسخ هذا وأضفه إلى ملف `.env`:
   ```batch
   # عدّل ملف .env
   notepad .env
   
   # أضف هذا السطر:
   TIKTOK_SESSION_ID=abc123xyz789...
   ```

---

### الخطوة 5: تشغيل الوضع الآلي (10 ثوان)

الآن اجعله يعمل تلقائياً!

**Windows:**
```batch
start_bot.bat
```

**سترى:**
```
╔═══════════════════════════════════════════════════════════╗
║           🎵 ASMR TikTok Automation Bot 🎵               ║
║                                                           ║
║  Automatically generates and posts ASMR videos to TikTok  ║
╚═══════════════════════════════════════════════════════════╝

🤖 Starting ASMR Bot...
======================================================================
⏰ Setting up schedule...
   ✓ Scheduled post at 09:00
   ✓ Scheduled post at 14:00
   ✓ Scheduled post at 20:00
✅ Schedule configured
✅ Bot is running!
⏰ Waiting for scheduled times...
💡 Press Ctrl+C to stop the bot
======================================================================
```

**البوت يعمل الآن!** سينشر في:
- 9:00 صباحاً
- 2:00 ظهراً  
- 8:00 مساءً
- يتكرر يومياً

**للإيقاف:** اضغط `Ctrl+C`

---

## 📊 راقب بوتك

### تحقق من السجلات (مباشرة)

افتح نافذة موجه أوامر **جديدة**:

**Windows PowerShell:**
```powershell
cd C:\Users\smart\OneDrive\Desktop\Cursor-cursor-automated-asmr-video-generation-and-tiktok-posting-b904
Get-Content bot.log -Wait -Tail 50
```

### تحقق من الفيديوهات المُنشأة

```batch
dir generated_videos
explorer generated_videos
```

---

## ⚙️ تخصيص الإعدادات (اختياري)

عدّل ملف `.env`:

```batch
notepad .env
```

**الإعدادات الشائعة:**

```env
# تغيير أوقات النشر (صيغة 24 ساعة)
POST_TIMES=08:00,12:00,16:00,20:00

# اختيار أنواع ASMR المطلوبة
ASMR_TYPES=rain,waves,fire         # فقط هذه الثلاثة
# أو
ASMR_TYPES=rain,fire,waves,typing,whisper  # كل الخمسة

# تغيير مدة الفيديو (بالثواني)
VIDEO_DURATION=20

# جلسة تيك توك الخاصة بك (من الخطوة 4)
TIKTOK_SESSION_ID=your_session_id_here
```

**بعد تغيير الإعدادات:**
1. أوقف البوت (Ctrl+C)
2. أعد التشغيل: `start_bot.bat`

---

## 🎯 مرجع سريع للأوامر

```batch
# 1. الإعداد (مرة واحدة فقط)
setup.bat

# 2. تفعيل البيئة (كل مرة)
venv\Scripts\activate.bat

# 3. اختبار إنشاء الفيديو
python bot.py --mode test

# 4. نشر فيديو واحد
python bot.py --mode once

# 5. تشغيل آلي
start_bot.bat

# 6. إيقاف البوت
اضغط Ctrl+C

# 7. عرض السجلات
type bot.log
```

---

## ❓ حل المشاكل

### "python: command not found"
جرب: `python --version` واستخدم `python` بدلاً من `python3`

### "Le chemin d'accès spécifié est introuvable"
شغّل: `setup.bat` أولاً

### فشل إنشاء الفيديو
ثبّت ffmpeg:
1. حمّل من: https://www.gyan.dev/ffmpeg/builds/
2. استخرج إلى `C:\ffmpeg`
3. أضف `C:\ffmpeg\bin` إلى PATH

### المتصفح لا يفتح
أعد تثبيت Playwright:
```batch
venv\Scripts\activate.bat
playwright install chromium
```

### فشل الرفع على تيك توك
1. احذف `TIKTOK_SESSION_ID` من `.env`
2. شغّل `python bot.py --mode once` مرة أخرى
3. سجل الدخول عند فتح المتصفح

---

## 📚 المستندات الإضافية

- **`START_HERE_AR.md`** - هذا الملف (عربي)
- **`README_AR.md`** - التوثيق الكامل (عربي)
- **`QUICKSTART_AR.md`** - دليل 5 دقائق (عربي)
- **`FIX_ERROR_AR.md`** - حل الأخطاء (عربي)
- **`WINDOWS_SETUP.md`** - دليل Windows (إنجليزي)

---

## ✅ قائمة التحقق من النجاح

بعد اتباع هذه الخطوات، يجب أن يكون لديك:

- [x] تثبيت جميع المتطلبات
- [x] إنشاء فيديو اختبار
- [x] تسجيل دخول إلى تيك توك
- [x] نشر أول فيديو
- [x] البوت يعمل حسب الجدول
- [x] السجلات تعرض النشاط

---

## 🎉 مبروك!

بوت ASMR تيك توك الخاص بك الآن:
- ✅ **يُنشئ** فيديوهات احترافية
- ✅ **ينشر** تلقائياً على تيك توك
- ✅ **يعمل** 24/7 حسب الجدول
- ✅ **يسجّل** جميع الأنشطة

**لا يوجد المزيد من العمل اليدوي!**

---

## 🚀 ماذا يحدث بعد ذلك؟

### اليوم:
- البوت ينشر في الأوقات المحددة (9ص، 2ظ، 8م)
- تحقق من `bot.log` لرؤية النشاط
- تحقق من ظهور المنشورات على تيك توك

### هذا الأسبوع:
- 21 فيديو منشور تلقائياً
- لا يوجد تدخل يدوي
- مراقبة الأداء

### هذا الشهر:
- 90+ فيديو منشور
- نمو حضورك على تيك توك
- مكتبة محتوى راسخة

---

## 💡 نصائح احترافية

1. **شغّل على خادم** للتشغيل الحقيقي 24/7 (VPS، سحابة، إلخ)
2. **راقب الأسبوع الأول** للتأكد من أن كل شيء يعمل بسلاسة
3. **اضبط الجدول** بناءً على الوقت الذي يكون فيه جمهورك أكثر نشاطاً
4. **تفاعل مع التعليقات** لتعزيز تصنيف الخوارزمية
5. **تتبع أنواع ASMR التي** تحصل على أكبر عدد من المشاهدات

---

## 📞 تحتاج مزيداً من المساعدة؟

1. اقرأ `README_AR.md` للتفسيرات التفصيلية
2. تحقق من `bot.log` لرسائل الخطأ  
3. راجع قسم حل المشاكل أعلاه
4. اقرأ `FIX_ERROR_AR.md` للمشاكل الشائعة

---

**أنت جاهز! استمتع بالأتمتة! 🎵✨**

---

## 🎬 سير العمل المرئي

```
البداية
  ↓
[تشغيل setup.bat] → يثبت كل شيء
  ↓
[تفعيل venv] → venv\Scripts\activate.bat
  ↓
[وضع الاختبار] → python bot.py --mode test
  ↓
[نشر مرة] → python bot.py --mode once → تسجيل دخول تيك توك
  ↓
[حفظ معرف الجلسة] → أضف إلى ملف .env
  ↓
[تشغيل آلي] → start_bot.bat
  ↓
[البوت يعمل!] → ينشر في 9ص، 2ظ، 8م يومياً
  ↓
راقب مع: type bot.log
  ↓
[نجاح! 🎉]
```
