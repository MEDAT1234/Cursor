# ✅ إصلاح خطأ: "Le chemin d'accès spécifié est introuvable"

## 🔴 المشكلة

حاولت تشغيل:
```batch
venv\Scripts\activate.bat
```

لكن ظهر خطأ: **"Le chemin d'accès spécifié est introuvable"** (المسار المحدد غير موجود)

هذا يعني أن مجلد `venv` غير موجود بعد!

## ✅ الحل - اتبع هذه الخطوات بالضبط:

### الخطوة 1: افتح موجه الأوامر (Command Prompt)

1. اضغط `Win + R`
2. اكتب: `cmd`
3. اضغط Enter

### الخطوة 2: انتقل إلى مجلد المشروع

```batch
cd C:\Users\smart\OneDrive\Desktop\Cursor-cursor-automated-asmr-video-generation-and-tiktok-posting-b904
```

### الخطوة 3: شغّل سكريبت الإعداد (هذا ينشئ مجلد venv!)

```batch
setup.bat
```

**انتظر 2-3 دقائق** بينما يقوم بـ:
- إنشاء مجلد `venv`
- تثبيت حزم Python
- تحميل متصفح Chrome

يجب أن ترى: `✅ Setup complete!`

### الخطوة 4: الآن يمكنك التفعيل

```batch
venv\Scripts\activate.bat
```

سترى `(venv)` في بداية السطر ✅

### الخطوة 5: اختبر البوت

```batch
python bot.py --mode test
```

## 🎯 الأوامر الكاملة (انسخ والصق):

```batch
REM 1. الانتقال إلى مجلد المشروع
cd C:\Users\smart\OneDrive\Desktop\Cursor-cursor-automated-asmr-video-generation-and-tiktok-posting-b904

REM 2. تشغيل الإعداد (المرة الأولى فقط)
setup.bat

REM 3. تفعيل البيئة الافتراضية
venv\Scripts\activate.bat

REM 4. اختبار إنشاء الفيديو
python bot.py --mode test

REM 5. نشر أول فيديو
python bot.py --mode once

REM 6. تشغيل الوضع الآلي
start_bot.bat
```

## 📋 العملية الكاملة:

```batch
C:\Users\smart\...\> setup.bat
🐍 Checking Python version...
Python 3.11.x
📦 Creating virtual environment...
✅ Virtual environment created
... (التثبيت يستمر)
✅ Setup complete!

C:\Users\smart\...\> venv\Scripts\activate.bat
(venv) C:\Users\smart\...\>

(venv) C:\Users\smart\...\> python bot.py --mode test
🎬 Starting video generation...
...
✅ Video generated successfully!
```

## ⚠️ إذا فشل setup.bat:

### تحقق من تثبيت Python:

```batch
python --version
```

**يجب أن يظهر:** `Python 3.8.x` أو أحدث

**إذا لم يكن مثبتاً:**
1. حمّل من: https://www.python.org/downloads/
2. ثبّت مع تفعيل ✅ "Add Python to PATH"
3. أعد تشغيل Command Prompt
4. حاول مجدداً

### الإعداد اليدوي (إذا لم يعمل setup.bat):

```batch
REM إنشاء البيئة الافتراضية
python -m venv venv

REM تفعيلها
venv\Scripts\activate.bat

REM ترقية pip
python -m pip install --upgrade pip

REM تثبيت الحزم
pip install moviepy numpy Pillow pydub playwright python-dotenv schedule scipy requests

REM تثبيت المتصفح
playwright install chromium

REM إنشاء ملف الإعدادات
copy .env.example .env

echo ✅ الإعداد اليدوي اكتمل!
```

## 🎉 مؤشرات النجاح:

✅ مجلد `venv` موجود في مجلد المشروع
✅ `(venv)` يظهر في موجه الأوامر بعد التفعيل
✅ لا توجد أخطاء عند تشغيل `python bot.py --mode test`

## 📞 ما زلت تواجه مشاكل؟

### المشكلة: "python: command not found"
**الحل:** Python غير مثبت أو غير موجود في PATH

### المشكلة: "Access denied" (رفض الوصول)
**الحل:** شغّل Command Prompt كمسؤول (انقر بالزر الأيمن → تشغيل كمسؤول)

### المشكلة: "pip: command not found"
**الحل:**
```batch
python -m pip install --upgrade pip
```

### المشكلة: الإعداد يستغرق وقتاً طويلاً
**الحل:** هذا طبيعي! يحمّل ~500 ميغابايت من الحزم. كن صبوراً.

## ✅ ما يجب أن يكون لديك بعد الإعداد:

```
مجلدك\
├── venv\                    ← هذا المجلد يجب أن يكون موجوداً الآن!
│   ├── Scripts\
│   │   └── activate.bat     ← هذا الملف يجب أن يكون موجوداً!
│   └── Lib\
├── bot.py
├── setup.bat
├── requirements.txt
└── .env                     ← ينشئه setup
```

## 🎯 قائمة تحقق سريعة:

- [ ] Python مثبت (`python --version` يعمل)
- [ ] أنت في المجلد الصحيح (استخدم `cd` للانتقال لمجلد المشروع)
- [ ] شغّلت `setup.bat` أولاً
- [ ] مجلد `venv` موجود (تحقق بأمر `dir`)
- [ ] ثم يمكنك تشغيل `venv\Scripts\activate.bat`

## 📝 تذكر:

**الترتيب مهم:**
1. `setup.bat` (ينشئ venv)
2. `venv\Scripts\activate.bat` (يفعله)
3. `python bot.py` (يشغل البوت)

لا يمكنك تخطي الخطوة 1!

## 🎯 ملخص سريع:

```batch
# الأمر الأول: الإعداد
setup.bat

# بعد انتهاء الإعداد: التفعيل
venv\Scripts\activate.bat

# ثم: الاختبار
python bot.py --mode test
```

## 📞 هل تحتاج مساعدة أكثر؟

افتح الملفات:
- `WINDOWS_SETUP.md` - دليل Windows بالإنجليزية
- `README_AR.md` - الدليل الكامل بالعربية
- `FIX_ERROR_WINDOWS.md` - إصلاح الأخطاء بالإنجليزية
