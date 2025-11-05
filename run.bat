@echo off
REM سكريبت تشغيل بوت تيكتوك على Windows

echo.
echo ====================================
echo بوت تيكتوك - استنساخ ورفع الفيديوهات
echo ====================================
echo.

REM التحقق من وجود البيئة الافتراضية
if not exist "venv\" (
    echo البيئة الافتراضية غير موجودة
    echo إنشاء بيئة افتراضية...
    python -m venv venv
)

REM تفعيل البيئة الافتراضية
echo تفعيل البيئة الافتراضية...
call venv\Scripts\activate.bat

REM التحقق من تثبيت المكتبات
if not exist "venv\installed.flag" (
    echo تثبيت المكتبات المطلوبة...
    pip install -r requirements.txt
    type nul > venv\installed.flag
)

REM تشغيل البوت
echo.
echo تشغيل البوت...
echo.
python main.py

REM إلغاء التفعيل
call deactivate

pause
