@echo off
chcp 65001 > nul
color 0A

cls
echo ========================================
echo  Club M Star AutoInput - Ultimate Edition
echo  Hızlı Başlatma
echo ========================================
echo.

:: Check if Python is installed
echo 🐍 Python kontrol ediliyor...
python --version > nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ Python bulunamadı!
    echo.
    echo Python kurulu değil veya PATH'e eklenmemiş.
    echo.
    echo Çözüm:
    echo   1. setup.bat'i çalıştırın (otomatik kurulum)
    echo   VEYA
    echo   2. Python'u manuel olarak kurun: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('python --version') do (
    echo ✓ Python bulundu ^(%%v^)
)
echo.

:: Check if main.py exists
echo 📄 Ana dosya kontrol ediliyor...
if not exist "main.py" (
    echo ❌ main.py bulunamadı!
    echo.
    echo Bu script'i proje klasöründe çalıştırdığınızdan emin olun.
    echo.
    pause
    exit /b 1
)
echo ✓ main.py bulundu
echo.

:: Check required folders
echo 📁 Klasörler kontrol ediliyor...
set "MISSING_FOLDERS=0"

if not exist "models" (
    echo ⚠️  models\ klasörü bulunamadı, oluşturuluyor...
    mkdir models
    set "MISSING_FOLDERS=1"
)

if not exist "cache" (
    echo ⚠️  cache\ klasörü bulunamadı, oluşturuluyor...
    mkdir cache
    set "MISSING_FOLDERS=1"
)

if not exist "logs" (
    echo ⚠️  logs\ klasörü bulunamadı, oluşturuluyor...
    mkdir logs
    set "MISSING_FOLDERS=1"
)

if not exist "user_data" (
    echo ⚠️  user_data\ klasörü bulunamadı, oluşturuluyor...
    mkdir user_data
    set "MISSING_FOLDERS=1"
)

if %MISSING_FOLDERS% equ 0 (
    echo ✓ Tüm klasörler mevcut
)
echo.

:: Check if requirements are installed
echo 📦 Paketler kontrol ediliyor...
python -c "import torch, cv2, flask" > nul 2>&1
if %errorLevel% neq 0 (
    echo ⚠️  Bazı gerekli paketler yüklü değil!
    echo.
    echo Paketleri yüklemek için:
    echo   1. setup.bat'i çalıştırın (tam kurulum)
    echo   VEYA
    echo   2. install-python-packages.bat'i çalıştırın (sadece paketler)
    echo.
    set /p INSTALL_NOW="Şimdi paketleri yüklemek ister misiniz? (E/H): "
    if /i "!INSTALL_NOW!"=="E" (
        call install-python-packages.bat
        if %errorLevel% neq 0 (
            echo.
            echo Paket yükleme başarısız. Lütfen manuel olarak yükleyin.
            pause
            exit /b 1
        )
    ) else (
        echo.
        echo Paketler yüklenmeden uygulama çalışmayacaktır.
        pause
        exit /b 1
    )
) else (
    echo ✓ Gerekli paketler yüklü
)
echo.

:: All checks passed, start the application
echo ========================================
echo   BAŞLATILIYOR... 🚀
echo ========================================
echo.
echo Uygulama açılıyor...
echo GUI penceresi açılmazsa Ctrl+C ile durdurup yeniden deneyin.
echo.

:: Start the application
python main.py

:: If application exits with error
if %errorLevel% neq 0 (
    echo.
    echo ========================================
    echo   HATA OLUŞTU! ❌
    echo ========================================
    echo.
    echo Uygulama bir hata ile kapandı.
    echo.
    echo Olası çözümler:
    echo   1. setup.bat'i çalıştırarak tam kurulum yapın
    echo   2. check-system.bat ile sistem durumunu kontrol edin
    echo   3. logs\ klasöründeki hata kayıtlarını inceleyin
    echo   4. KURULUM.md dosyasındaki sorun giderme bölümüne bakın
    echo.
    echo Hata kodu: %errorLevel%
    echo.
)

pause
