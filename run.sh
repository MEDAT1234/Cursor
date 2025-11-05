#!/bin/bash

# سكريبت تشغيل بوت تيكتوك
# يقوم بتفعيل البيئة الافتراضية وتشغيل البوت

echo "🤖 بوت تيكتوك - استنساخ ورفع الفيديوهات"
echo "======================================"
echo ""

# التحقق من وجود البيئة الافتراضية
if [ ! -d "venv" ]; then
    echo "⚠️  البيئة الافتراضية غير موجودة"
    echo "📦 إنشاء بيئة افتراضية..."
    python3 -m venv venv
fi

# تفعيل البيئة الافتراضية
echo "🔄 تفعيل البيئة الافتراضية..."
source venv/bin/activate

# التحقق من تثبيت المكتبات
if [ ! -f "venv/installed.flag" ]; then
    echo "📦 تثبيت المكتبات المطلوبة..."
    pip install -r requirements.txt
    touch venv/installed.flag
fi

# تشغيل البوت
echo ""
echo "🚀 تشغيل البوت..."
echo ""
python main.py

# إلغاء التفعيل
deactivate
