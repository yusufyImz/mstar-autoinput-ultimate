@echo off
chcp 65001 > nul
color 0B

cls
echo ========================================
echo  Sistem Kontrol Scripti
echo  Club M Star AutoInput - Ultimate Edition
echo ========================================
echo.
echo Sistem bilgileri toplanıyor...
echo.

:: Create report file
set "REPORT_FILE=system-check.txt"
echo ======================================== > %REPORT_FILE%
echo   Sistem Kontrol Raporu >> %REPORT_FILE%
echo   Tarih: %date% %time% >> %REPORT_FILE%
echo ======================================== >> %REPORT_FILE%
echo. >> %REPORT_FILE%

:: Windows Version
echo 🖥️  İşletim Sistemi
echo ======================================== >> %REPORT_FILE%
echo İşletim Sistemi: >> %REPORT_FILE%
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" >> %REPORT_FILE%
echo. >> %REPORT_FILE%

echo ✓ İşletim sistemi bilgisi alındı

:: CPU Information
echo 🔧 CPU Bilgisi
echo ======================================== >> %REPORT_FILE%
echo CPU: >> %REPORT_FILE%
wmic cpu get name,numberofcores,numberoflogicalprocessors >> %REPORT_FILE%
echo. >> %REPORT_FILE%

echo ✓ CPU bilgisi alındı

:: RAM Information
echo 💾 Bellek ^(RAM^)
echo ======================================== >> %REPORT_FILE%
echo Bellek: >> %REPORT_FILE%
systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory" >> %REPORT_FILE%
echo. >> %REPORT_FILE%

echo ✓ RAM bilgisi alındı

:: Disk Space
echo 💿 Disk Alanı
echo ======================================== >> %REPORT_FILE%
echo Disk Alanı: >> %REPORT_FILE%
wmic logicaldisk get caption,freespace,size >> %REPORT_FILE%
echo. >> %REPORT_FILE%

echo ✓ Disk bilgisi alındı

:: Check Git
echo 📦 Git Kurulumu
echo ======================================== >> %REPORT_FILE%
echo Git Kontrolü: >> %REPORT_FILE%
git --version >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ Git kurulu >> %REPORT_FILE%
    echo ✓ Git kurulu
) else (
    echo ❌ Git kurulu değil >> %REPORT_FILE%
    echo ❌ Git kurulu değil
)
echo. >> %REPORT_FILE%

:: Check Python
echo 🐍 Python Kurulumu
echo ======================================== >> %REPORT_FILE%
echo Python Kontrolü: >> %REPORT_FILE%
python --version >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ Python kurulu >> %REPORT_FILE%
    echo ✓ Python kurulu
    
    :: Python path
    where python >> %REPORT_FILE% 2>&1
    
    :: Check Python version details
    python -c "import sys; print(f'Python Yolu: {sys.executable}')" >> %REPORT_FILE% 2>&1
    python -c "import sys; print(f'Python Sürüm Bilgisi: {sys.version}')" >> %REPORT_FILE% 2>&1
) else (
    echo ❌ Python kurulu değil >> %REPORT_FILE%
    echo ❌ Python kurulu değil
)
echo. >> %REPORT_FILE%

:: Check pip
echo 📦 pip Kurulumu
echo ======================================== >> %REPORT_FILE%
echo pip Kontrolü: >> %REPORT_FILE%
python -m pip --version >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ pip kurulu >> %REPORT_FILE%
    echo ✓ pip kurulu
) else (
    echo ❌ pip kurulu değil >> %REPORT_FILE%
    echo ❌ pip kurulu değil
)
echo. >> %REPORT_FILE%

:: Check installed Python packages
echo 📚 Yüklü Python Paketleri
echo ======================================== >> %REPORT_FILE%
echo Yüklü Paketler: >> %REPORT_FILE%
echo. >> %REPORT_FILE%

:: Check each required package
set "ALL_INSTALLED=1"

echo torch: >> %REPORT_FILE%
python -c "import torch; print(f'  Sürüm: {torch.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ torch kurulu
) else (
    echo ❌ torch kurulu değil >> %REPORT_FILE%
    echo ❌ torch kurulu değil
    set "ALL_INSTALLED=0"
)

echo torchvision: >> %REPORT_FILE%
python -c "import torchvision; print(f'  Sürüm: {torchvision.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ torchvision kurulu
) else (
    echo ❌ torchvision kurulu değil >> %REPORT_FILE%
    echo ❌ torchvision kurulu değil
    set "ALL_INSTALLED=0"
)

echo opencv-python: >> %REPORT_FILE%
python -c "import cv2; print(f'  Sürüm: {cv2.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ opencv-python kurulu
) else (
    echo ❌ opencv-python kurulu değil >> %REPORT_FILE%
    echo ❌ opencv-python kurulu değil
    set "ALL_INSTALLED=0"
)

echo numpy: >> %REPORT_FILE%
python -c "import numpy; print(f'  Sürüm: {numpy.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ numpy kurulu
) else (
    echo ❌ numpy kurulu değil >> %REPORT_FILE%
    echo ❌ numpy kurulu değil
    set "ALL_INSTALLED=0"
)

echo flask: >> %REPORT_FILE%
python -c "import flask; print(f'  Sürüm: {flask.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ flask kurulu
) else (
    echo ❌ flask kurulu değil >> %REPORT_FILE%
    echo ❌ flask kurulu değil
    set "ALL_INSTALLED=0"
)

echo flask-cors: >> %REPORT_FILE%
python -c "import flask_cors" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ flask-cors kurulu
) else (
    echo ❌ flask-cors kurulu değil >> %REPORT_FILE%
    echo ❌ flask-cors kurulu değil
    set "ALL_INSTALLED=0"
)

echo pillow: >> %REPORT_FILE%
python -c "import PIL; print(f'  Sürüm: {PIL.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ pillow kurulu
) else (
    echo ❌ pillow kurulu değil >> %REPORT_FILE%
    echo ❌ pillow kurulu değil
    set "ALL_INSTALLED=0"
)

echo pynput: >> %REPORT_FILE%
python -c "import pynput" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ pynput kurulu
) else (
    echo ❌ pynput kurulu değil >> %REPORT_FILE%
    echo ❌ pynput kurulu değil
    set "ALL_INSTALLED=0"
)

echo mss: >> %REPORT_FILE%
python -c "import mss" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ mss kurulu
) else (
    echo ❌ mss kurulu değil >> %REPORT_FILE%
    echo ❌ mss kurulu değil
    set "ALL_INSTALLED=0"
)

echo requests: >> %REPORT_FILE%
python -c "import requests; print(f'  Sürüm: {requests.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ requests kurulu
) else (
    echo ❌ requests kurulu değil >> %REPORT_FILE%
    echo ❌ requests kurulu değil
    set "ALL_INSTALLED=0"
)

echo psutil: >> %REPORT_FILE%
python -c "import psutil; print(f'  Sürüm: {psutil.__version__}')" >> %REPORT_FILE% 2>&1
if %errorLevel% equ 0 (
    echo ✓ psutil kurulu
) else (
    echo ❌ psutil kurulu değil >> %REPORT_FILE%
    echo ❌ psutil kurulu değil
    set "ALL_INSTALLED=0"
)

echo. >> %REPORT_FILE%

:: Check project folders
echo 📁 Proje Klasörleri
echo ======================================== >> %REPORT_FILE%
echo Proje Klasörleri: >> %REPORT_FILE%

if exist "models\" (
    echo ✓ models\ mevcut >> %REPORT_FILE%
    echo ✓ models\ mevcut
) else (
    echo ❌ models\ bulunamadı >> %REPORT_FILE%
    echo ❌ models\ bulunamadı
)

if exist "cache\" (
    echo ✓ cache\ mevcut >> %REPORT_FILE%
    echo ✓ cache\ mevcut
) else (
    echo ❌ cache\ bulunamadı >> %REPORT_FILE%
    echo ❌ cache\ bulunamadı
)

if exist "logs\" (
    echo ✓ logs\ mevcut >> %REPORT_FILE%
    echo ✓ logs\ mevcut
) else (
    echo ❌ logs\ bulunamadı >> %REPORT_FILE%
    echo ❌ logs\ bulunamadı
)

if exist "user_data\" (
    echo ✓ user_data\ mevcut >> %REPORT_FILE%
    echo ✓ user_data\ mevcut
) else (
    echo ❌ user_data\ bulunamadı >> %REPORT_FILE%
    echo ❌ user_data\ bulunamadı
)

echo. >> %REPORT_FILE%

:: Check config file
echo ⚙️  Yapılandırma Dosyası
echo ======================================== >> %REPORT_FILE%
echo Yapılandırma: >> %REPORT_FILE%

if exist "config.json" (
    echo ✓ config.json mevcut >> %REPORT_FILE%
    echo ✓ config.json mevcut
) else (
    echo ❌ config.json bulunamadı >> %REPORT_FILE%
    echo ❌ config.json bulunamadı
)

echo. >> %REPORT_FILE%

:: Check main.py
echo 📄 Ana Program Dosyası
echo ======================================== >> %REPORT_FILE%
echo Ana Dosya: >> %REPORT_FILE%

if exist "main.py" (
    echo ✓ main.py mevcut >> %REPORT_FILE%
    echo ✓ main.py mevcut
) else (
    echo ❌ main.py bulunamadı >> %REPORT_FILE%
    echo ❌ main.py bulunamadı
)

echo. >> %REPORT_FILE%

:: System Performance Info
echo 📊 Sistem Performansı
echo ======================================== >> %REPORT_FILE%
echo Sistem Performansı: >> %REPORT_FILE%
python -c "import psutil; print(f'CPU Kullanımı: {psutil.cpu_percent(interval=1)}%%'); print(f'RAM Kullanımı: {psutil.virtual_memory().percent}%%')" >> %REPORT_FILE% 2>&1

echo ✓ Performans bilgisi alındı

echo. >> %REPORT_FILE%

:: Summary
echo ========================================
echo ======================================== >> %REPORT_FILE%
echo   ÖZET >> %REPORT_FILE%
echo ======================================== >> %REPORT_FILE%
echo. >> %REPORT_FILE%

if %ALL_INSTALLED% equ 1 (
    echo ✅ Tüm gerekli paketler kurulu! >> %REPORT_FILE%
    echo ✅ Sistem hazır, uygulama çalıştırılabilir. >> %REPORT_FILE%
    echo.
    echo ✅ Tüm gerekli paketler kurulu!
    echo ✅ Sistem hazır!
) else (
    echo ⚠️  Bazı paketler eksik! >> %REPORT_FILE%
    echo ⚠️  setup.bat veya install-python-packages.bat çalıştırın. >> %REPORT_FILE%
    echo.
    echo ⚠️  Bazı paketler eksik!
    echo ⚠️  Kurulum yapmanız gerekiyor.
)

echo. >> %REPORT_FILE%
echo Detaylı rapor: %REPORT_FILE% >> %REPORT_FILE%
echo ======================================== >> %REPORT_FILE%

echo.
echo ========================================
echo   RAPOR OLUŞTURULDU
echo ========================================
echo.
echo Detaylı rapor '%REPORT_FILE%' dosyasına kaydedildi.
echo Raporu açmak için:
echo   - notepad %REPORT_FILE%
echo   VEYA
echo   - type %REPORT_FILE%
echo.

:: Ask to open report
set /p OPEN_REPORT="Raporu şimdi açmak ister misiniz? (E/H): "
if /i "%OPEN_REPORT%"=="E" (
    notepad %REPORT_FILE%
)

pause
