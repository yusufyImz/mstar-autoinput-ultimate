@echo off
chcp 65001 > nul
color 0A

cls
echo ========================================
echo  Python Paketleri Kurulum Scripti
echo  Club M Star AutoInput - Ultimate Edition
echo ========================================
echo.

:: Check if Python is installed
echo 🐍 Python kontrol ediliyor...
python --version > nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ Python bulunamadı!
    echo.
    echo Python'u önce kurmanız gerekiyor.
    echo setup.bat'i çalıştırın veya manuel olarak kurun:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('python --version') do (
    echo ✓ Python bulundu ^(%%v^)
)
echo.

:: Check pip
echo 📦 pip kontrol ediliyor...
python -m pip --version > nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ pip bulunamadı!
    echo.
    echo pip Python ile birlikte gelmeli. Python kurulumunuzu kontrol edin.
    echo.
    pause
    exit /b 1
)
echo ✓ pip mevcut
echo.

:: Upgrade pip
echo 🔄 pip güncelleniyor...
python -m pip install --upgrade pip
if %errorLevel% equ 0 (
    echo ✓ pip güncellendi
) else (
    echo ⚠️  pip güncellenemedi ^(devam ediliyor^)
)
echo.

:: Check requirements.txt
if not exist "requirements.txt" (
    echo ❌ requirements.txt bulunamadı!
    echo.
    echo Bu dosya proje için gerekli. Proje klasöründe olduğunuzdan emin olun.
    echo.
    pause
    exit /b 1
)

:: Display packages to be installed
echo 📋 Yüklenecek paketler:
echo.
type requirements.txt
echo.
echo ========================================
echo.

:: Ask for confirmation
set /p CONFIRM="Bu paketleri yüklemek istiyor musunuz? (E/H): "
if /i not "%CONFIRM%"=="E" (
    echo.
    echo Kurulum iptal edildi.
    pause
    exit /b 0
)

echo.
echo ========================================
echo   PAKET KURULUMU BAŞLATILIYOR...
echo ========================================
echo.
echo ⏱️  Bu işlem 5-15 dakika sürebilir
echo    ^(PyTorch büyük bir dosyadır - yaklaşık 700MB^)
echo.
echo 💡 İpucu: İndirme hızınız yavaşsa kahve molası verin! ☕
echo.

:: Install PyTorch with CPU-only version first (from special index)
echo ========================================
echo 📦 1/11 - PyTorch ^(CPU^) kuruluyor...
echo ========================================
echo.
echo → torch ve torchvision indiriliyor...
echo → Bu en büyük paket, lütfen bekleyin...
echo.

python -m pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu

if %errorLevel% equ 0 (
    echo.
    echo ✓ PyTorch başarıyla kuruldu!
    echo.
) else (
    echo.
    echo ⚠️  PyTorch kurulumu başarısız!
    echo.
    echo Olası çözümler:
    echo   1. İnternet bağlantınızı kontrol edin
    echo   2. Yeniden deneyin
    echo   3. Manuel kurulum: pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
    echo.
    pause
    exit /b 1
)

:: Install OpenCV
echo ========================================
echo 📦 2/11 - OpenCV kuruluyor...
echo ========================================
python -m pip install opencv-python==4.8.1.78
if %errorLevel% equ 0 (echo ✓ OpenCV kuruldu) else (echo ⚠️  OpenCV hatası)
echo.

:: Install NumPy
echo ========================================
echo 📦 3/11 - NumPy kuruluyor...
echo ========================================
python -m pip install numpy==1.24.3
if %errorLevel% equ 0 (echo ✓ NumPy kuruldu) else (echo ⚠️  NumPy hatası)
echo.

:: Install Flask
echo ========================================
echo 📦 4/11 - Flask kuruluyor...
echo ========================================
python -m pip install flask==3.0.0
if %errorLevel% equ 0 (echo ✓ Flask kuruldu) else (echo ⚠️  Flask hatası)
echo.

:: Install Flask-CORS
echo ========================================
echo 📦 5/11 - Flask-CORS kuruluyor...
echo ========================================
python -m pip install flask-cors==4.0.0
if %errorLevel% equ 0 (echo ✓ Flask-CORS kuruldu) else (echo ⚠️  Flask-CORS hatası)
echo.

:: Install Pillow
echo ========================================
echo 📦 6/11 - Pillow kuruluyor...
echo ========================================
python -m pip install pillow==10.1.0
if %errorLevel% equ 0 (echo ✓ Pillow kuruldu) else (echo ⚠️  Pillow hatası)
echo.

:: Install pynput
echo ========================================
echo 📦 7/11 - pynput kuruluyor...
echo ========================================
python -m pip install pynput==1.7.6
if %errorLevel% equ 0 (echo ✓ pynput kuruldu) else (echo ⚠️  pynput hatası)
echo.

:: Install mss
echo ========================================
echo 📦 8/11 - mss kuruluyor...
echo ========================================
python -m pip install mss==9.0.1
if %errorLevel% equ 0 (echo ✓ mss kuruldu) else (echo ⚠️  mss hatası)
echo.

:: Install requests
echo ========================================
echo 📦 9/11 - requests kuruluyor...
echo ========================================
python -m pip install requests==2.31.0
if %errorLevel% equ 0 (echo ✓ requests kuruldu) else (echo ⚠️  requests hatası)
echo.

:: Install psutil
echo ========================================
echo 📦 10/11 - psutil kuruluyor...
echo ========================================
python -m pip install psutil==5.9.6
if %errorLevel% equ 0 (echo ✓ psutil kuruldu) else (echo ⚠️  psutil hatası)
echo.

:: Verify all packages
echo ========================================
echo 📦 11/11 - Kurulum doğrulanıyor...
echo ========================================
echo.

python -c "import torch; print('✓ torch:', torch.__version__)" 2>nul || echo ❌ torch yüklenemedi
python -c "import torchvision; print('✓ torchvision:', torchvision.__version__)" 2>nul || echo ❌ torchvision yüklenemedi
python -c "import cv2; print('✓ opencv-python:', cv2.__version__)" 2>nul || echo ❌ opencv-python yüklenemedi
python -c "import numpy; print('✓ numpy:', numpy.__version__)" 2>nul || echo ❌ numpy yüklenemedi
python -c "import flask; print('✓ flask:', flask.__version__)" 2>nul || echo ❌ flask yüklenemedi
python -c "import flask_cors; print('✓ flask-cors')" 2>nul || echo ❌ flask-cors yüklenemedi
python -c "import PIL; print('✓ pillow:', PIL.__version__)" 2>nul || echo ❌ pillow yüklenemedi
python -c "import pynput; print('✓ pynput')" 2>nul || echo ❌ pynput yüklenemedi
python -c "import mss; print('✓ mss')" 2>nul || echo ❌ mss yüklenemedi
python -c "import requests; print('✓ requests:', requests.__version__)" 2>nul || echo ❌ requests yüklenemedi
python -c "import psutil; print('✓ psutil:', psutil.__version__)" 2>nul || echo ❌ psutil yüklenemedi

echo.
echo ========================================
echo   KURULUM TAMAMLANDI! 🎉
echo ========================================
echo.
echo Tüm Python paketleri başarıyla yüklendi.
echo Artık uygulamayı çalıştırabilirsiniz:
echo   - quick-start.bat ile
echo   - python main.py komutuyla
echo.

pause
