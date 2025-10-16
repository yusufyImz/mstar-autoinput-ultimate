@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

:: Set console colors
color 0A

:: Define log file
set "LOG_FILE=setup.log"

:: Clear screen
cls

echo ========================================
echo  Club M Star AutoInput - Ultimate Edition
echo  Otomatik Kurulum Scripti v1.0
echo ========================================
echo.
echo Kurulum başlatılıyor...
echo.

:: Start logging
echo [%date% %time%] Kurulum başlatıldı >> %LOG_FILE%

:: Check for administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ⚠️  Yönetici yetkisi gerekli!
    echo.
    echo Bu script bazı programları kurmak için yönetici yetkisi gerektirir.
    echo Script'i sağ tıklayıp "Yönetici olarak çalıştır" seçeneğini kullanın.
    echo.
    echo [%date% %time%] HATA: Yönetici yetkisi yok >> %LOG_FILE%
    pause
    exit /b 1
)

echo ✓ Yönetici yetkisi onaylandı
echo [%date% %time%] Yönetici yetkisi onaylandı >> %LOG_FILE%
echo.

:: Check internet connection
echo 📡 İnternet bağlantısı kontrol ediliyor...
ping -n 1 8.8.8.8 > nul 2>&1
if %errorLevel% neq 0 (
    echo ⚠️  İnternet bağlantısı bulunamadı!
    echo Kurulum için internet bağlantısı gereklidir.
    echo.
    echo [%date% %time%] HATA: İnternet bağlantısı yok >> %LOG_FILE%
    pause
    exit /b 1
)
echo ✓ İnternet bağlantısı aktif
echo [%date% %time%] İnternet bağlantısı aktif >> %LOG_FILE%
echo.

:: Check disk space (require at least 3GB)
echo 💾 Disk alanı kontrol ediliyor...
for /f "tokens=3" %%a in ('dir /-c ^| find "bytes free"') do set FREE_SPACE=%%a
set /a FREE_GB=%FREE_SPACE:~0,-9%
if %FREE_GB% LSS 3 (
    echo ⚠️  Yetersiz disk alanı! (En az 3GB gerekli)
    echo Mevcut boş alan: %FREE_GB% GB
    echo.
    echo [%date% %time%] HATA: Yetersiz disk alanı >> %LOG_FILE%
    pause
    exit /b 1
)
echo ✓ Yeterli disk alanı mevcut (%FREE_GB% GB)
echo [%date% %time%] Disk alanı: %FREE_GB% GB >> %LOG_FILE%
echo.

:: Check if winget is available
echo 🔍 Winget kontrol ediliyor...
winget --version > nul 2>&1
if %errorLevel% equ 0 (
    echo ✓ Winget mevcut
    echo [%date% %time%] Winget mevcut >> %LOG_FILE%
    set "WINGET_AVAILABLE=1"
) else (
    echo ⚠️  Winget bulunamadı
    echo Winget olmadan kurulum manuel indirme ile devam edecek.
    echo [%date% %time%] Winget bulunamadı >> %LOG_FILE%
    set "WINGET_AVAILABLE=0"
)
echo.

:: Check if Git is installed
echo 🔍 Git kontrol ediliyor...
git --version > nul 2>&1
if %errorLevel% equ 0 (
    for /f "tokens=3" %%v in ('git --version') do (
        echo ✓ Git zaten kurulu ^(%%v^)
        echo [%date% %time%] Git zaten kurulu ^(%%v^) >> %LOG_FILE%
    )
) else (
    echo → Git bulunamadı. Kurulum yapılıyor...
    echo [%date% %time%] Git bulunamadı, kurulacak >> %LOG_FILE%
    
    if "%WINGET_AVAILABLE%"=="1" (
        echo    Winget ile Git kuruluyor...
        winget install --id Git.Git -e --silent --accept-package-agreements --accept-source-agreements
        if %errorLevel% equ 0 (
            echo ✓ Git başarıyla kuruldu!
            echo [%date% %time%] Git başarıyla kuruldu ^(winget^) >> %LOG_FILE%
        ) else (
            echo ⚠️  Git kurulumu başarısız oldu
            echo [%date% %time%] HATA: Git kurulumu başarısız >> %LOG_FILE%
            echo Manuel kurulum için: https://git-scm.com/download/win
            pause
        )
    ) else (
        echo    Manuel indirme gerekli
        echo    Git indirmek için: https://git-scm.com/download/win
        echo    Kurulumdan sonra bu script'i tekrar çalıştırın.
        echo [%date% %time%] Git manuel kurulum gerekli >> %LOG_FILE%
        start https://git-scm.com/download/win
        pause
    )
    
    :: Refresh environment variables
    call refreshenv > nul 2>&1
)
echo.

:: Check if Python is installed
echo 🐍 Python kontrol ediliyor...
python --version > nul 2>&1
if %errorLevel% equ 0 (
    for /f "tokens=2" %%v in ('python --version') do (
        set "PY_VERSION=%%v"
        echo ✓ Python zaten kurulu ^(!PY_VERSION!^)
        echo [%date% %time%] Python zaten kurulu ^(!PY_VERSION!^) >> %LOG_FILE%
        
        :: Check Python version (need 3.11+)
        for /f "tokens=1,2 delims=." %%a in ("!PY_VERSION!") do (
            set "PY_MAJOR=%%a"
            set "PY_MINOR=%%b"
        )
        
        if !PY_MAJOR! LSS 3 (
            echo ⚠️  Python sürümü çok eski! ^(3.11+ gerekli^)
            set "PYTHON_NEEDS_UPDATE=1"
        ) else if !PY_MAJOR! EQU 3 (
            if !PY_MINOR! LSS 11 (
                echo ⚠️  Python sürümü çok eski! ^(3.11+ gerekli^)
                set "PYTHON_NEEDS_UPDATE=1"
            )
        )
    )
) else (
    set "PYTHON_NEEDS_UPDATE=1"
)

if defined PYTHON_NEEDS_UPDATE (
    echo → Python 3.11+ bulunamadı. Kurulum yapılıyor...
    echo [%date% %time%] Python 3.11+ bulunamadı, kurulacak >> %LOG_FILE%
    
    if "%WINGET_AVAILABLE%"=="1" (
        echo    Winget ile Python kuruluyor... ^(Bu işlem 2-3 dakika sürebilir^)
        winget install --id Python.Python.3.11 -e --silent --accept-package-agreements --accept-source-agreements
        if %errorLevel% equ 0 (
            echo ✓ Python başarıyla kuruldu!
            echo [%date% %time%] Python başarıyla kuruldu ^(winget^) >> %LOG_FILE%
        ) else (
            echo ⚠️  Python kurulumu başarısız oldu
            echo [%date% %time%] HATA: Python kurulumu başarısız >> %LOG_FILE%
            echo Manuel kurulum için: https://www.python.org/downloads/
            pause
        )
    ) else (
        echo    Manuel indirme gerekli
        echo    Python 3.11 indirmek için: https://www.python.org/downloads/
        echo    ÖNEMLİ: Kurulumda "Add Python to PATH" seçeneğini işaretleyin!
        echo    Kurulumdan sonra bu script'i tekrar çalıştırın.
        echo [%date% %time%] Python manuel kurulum gerekli >> %LOG_FILE%
        start https://www.python.org/downloads/
        pause
        exit /b 0
    )
    
    :: Refresh environment variables
    call refreshenv > nul 2>&1
    
    :: Verify Python installation
    python --version > nul 2>&1
    if %errorLevel% neq 0 (
        echo ⚠️  Python kurulumunda sorun oluştu!
        echo Lütfen Python'u manuel olarak kurun ve PATH'e ekleyin.
        echo [%date% %time%] HATA: Python kurulumu doğrulanamadı >> %LOG_FILE%
        pause
        exit /b 1
    )
)
echo.

:: Check pip
echo 📦 pip kontrol ediliyor...
python -m pip --version > nul 2>&1
if %errorLevel% neq 0 (
    echo ⚠️  pip bulunamadı! Python kurulumunu kontrol edin.
    echo [%date% %time%] HATA: pip bulunamadı >> %LOG_FILE%
    pause
    exit /b 1
)
echo ✓ pip mevcut
echo [%date% %time%] pip mevcut >> %LOG_FILE%
echo.

:: Upgrade pip
echo 🔄 pip güncelleniyor...
echo [%date% %time%] pip güncelleniyor >> %LOG_FILE%
python -m pip install --upgrade pip --quiet
if %errorLevel% equ 0 (
    echo ✓ pip güncellendi
    echo [%date% %time%] pip başarıyla güncellendi >> %LOG_FILE%
) else (
    echo ⚠️  pip güncellemesi başarısız ^(devam ediliyor^)
    echo [%date% %time%] UYARI: pip güncellemesi başarısız >> %LOG_FILE%
)
echo.

:: Install Python packages
echo 📚 Python paketleri yükleniyor...
echo    Bu işlem 5-15 dakika sürebilir ^(PyTorch büyük bir paket^)
echo    Lütfen bekleyin...
echo.
echo [%date% %time%] Python paketleri yükleniyor >> %LOG_FILE%

if exist requirements.txt (
    :: Install PyTorch first with CPU-only version
    echo → PyTorch kuruluyor ^(CPU versiyonu^)...
    python -m pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
    if %errorLevel% equ 0 (
        echo ✓ PyTorch kuruldu
        echo [%date% %time%] PyTorch kuruldu >> %LOG_FILE%
    ) else (
        echo ⚠️  PyTorch kurulumu başarısız
        echo [%date% %time%] HATA: PyTorch kurulumu başarısız >> %LOG_FILE%
    )
    echo.
    
    :: Install other packages
    echo → Diğer paketler kuruluyor...
    python -m pip install -r requirements.txt --quiet
    if %errorLevel% equ 0 (
        echo ✓ Tüm paketler başarıyla yüklendi!
        echo [%date% %time%] Tüm paketler yüklendi >> %LOG_FILE%
    ) else (
        echo ⚠️  Bazı paketler yüklenemedi
        echo Detaylar için setup.log dosyasını kontrol edin.
        echo [%date% %time%] HATA: Paket yükleme başarısız >> %LOG_FILE%
    )
) else (
    echo ⚠️  requirements.txt dosyası bulunamadı!
    echo [%date% %time%] HATA: requirements.txt bulunamadı >> %LOG_FILE%
)
echo.

:: Create necessary folders
echo 📁 Klasörler oluşturuluyor...
echo [%date% %time%] Klasörler oluşturuluyor >> %LOG_FILE%

if not exist "models" (
    mkdir models
    echo ✓ models\ oluşturuldu
    echo [%date% %time%] models\ klasörü oluşturuldu >> %LOG_FILE%
)

if not exist "cache" (
    mkdir cache
    echo ✓ cache\ oluşturuldu
    echo [%date% %time%] cache\ klasörü oluşturuldu >> %LOG_FILE%
)

if not exist "logs" (
    mkdir logs
    echo ✓ logs\ oluşturuldu
    echo [%date% %time%] logs\ klasörü oluşturuldu >> %LOG_FILE%
)

if not exist "user_data" (
    mkdir user_data
    echo ✓ user_data\ oluşturuldu
    echo [%date% %time%] user_data\ klasörü oluşturuldu >> %LOG_FILE%
)
echo.

:: Check config.json
echo ⚙️  Yapılandırma dosyası kontrol ediliyor...
if not exist "config.json" (
    echo → config.json bulunamadı, varsayılan ayarlar kullanılacak
    echo [%date% %time%] config.json bulunamadı >> %LOG_FILE%
) else (
    echo ✓ config.json mevcut
    echo [%date% %time%] config.json mevcut >> %LOG_FILE%
)
echo.

:: Installation complete
echo ========================================
echo   KURULUM TAMAMLANDI! 🎉
echo ========================================
echo.
echo ✓ Tüm gerekli programlar kuruldu
echo ✓ Python paketleri yüklendi
echo ✓ Klasör yapısı oluşturuldu
echo ✓ Yapılandırma hazır
echo.
echo [%date% %time%] Kurulum başarıyla tamamlandı >> %LOG_FILE%
echo.
echo Programı başlatmak için:
echo   1. quick-start.bat'e çift tıklayın
echo   VEYA
echo   2. Komut satırında: python main.py
echo.
echo Detaylı kullanım için: KURULUM.md dosyasını okuyun
echo.
echo ========================================
echo.

:: Ask to start the application
set /p START_NOW="Programı şimdi başlatmak ister misiniz? (E/H): "
if /i "%START_NOW%"=="E" (
    echo.
    echo Uygulama başlatılıyor...
    echo [%date% %time%] Uygulama kullanıcı tarafından başlatıldı >> %LOG_FILE%
    python main.py
) else (
    echo.
    echo İyi günler! 👋
    echo [%date% %time%] Kurulum tamamlandı, uygulama başlatılmadı >> %LOG_FILE%
)

pause
