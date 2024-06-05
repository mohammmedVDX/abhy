@echo off
mode con: cols=100 lines=10
color 0C

REM حلقة دائمة لطباعة الرسالة والانتظار
:loop
echo هناك خطأ ما في النظام. يرجى إعادة التشغيل لحل المشكلة.
timeout /t 1 >nul
goto loop
