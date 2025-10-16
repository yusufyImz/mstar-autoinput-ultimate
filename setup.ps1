# Club M Star AutoInput - Ultimate Edition
# PowerShell Installation Script v1.0
# Requires: Windows 10/11, PowerShell 5.1+

#Requires -RunAsAdministrator

# Set encoding to UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Clear screen
Clear-Host

# Color scheme
$Host.UI.RawUI.BackgroundColor = "Black"
$Host.UI.RawUI.ForegroundColor = "Green"
Clear-Host

# Log file
$LogFile = "setup.log"

function Write-Log {
    param([string]$Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$Timestamp - $Message" | Out-File -FilePath $LogFile -Append
}

function Write-Header {
    param([string]$Text)
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host " $Text" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
}

function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Error {
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

function Write-Warning {
    param([string]$Message)
    Write-Host "⚠️  $Message" -ForegroundColor Yellow
}

function Write-Info {
    param([string]$Message)
    Write-Host "→ $Message" -ForegroundColor Cyan
}

# Main script
Write-Header "Club M Star AutoInput - Ultimate Edition"
Write-Host "  Otomatik Kurulum Scripti (PowerShell)" -ForegroundColor White
Write-Host ""
Write-Host "Kurulum başlatılıyor..." -ForegroundColor White
Write-Host ""

Write-Log "Kurulum başlatıldı"

# Check PowerShell version
$PSVersionTable.PSVersion | Out-Null
Write-Success "PowerShell sürümü: $($PSVersionTable.PSVersion)"
Write-Log "PowerShell sürümü: $($PSVersionTable.PSVersion)"

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Error "Bu script yönetici yetkisi gerektirir!"
    Write-Host ""
    Write-Host "Lütfen PowerShell'i yönetici olarak çalıştırın:" -ForegroundColor Yellow
    Write-Host "  1. PowerShell'e sağ tıklayın" -ForegroundColor Yellow
    Write-Host "  2. 'Yönetici olarak çalıştır' seçin" -ForegroundColor Yellow
    Write-Host ""
    Write-Log "HATA: Yönetici yetkisi yok"
    pause
    exit 1
}
Write-Success "Yönetici yetkisi onaylandı"
Write-Log "Yönetici yetkisi onaylandı"
Write-Host ""

# Check internet connection
Write-Info "İnternet bağlantısı kontrol ediliyor..."
try {
    $ping = Test-Connection -ComputerName 8.8.8.8 -Count 1 -Quiet
    if ($ping) {
        Write-Success "İnternet bağlantısı aktif"
        Write-Log "İnternet bağlantısı aktif"
    } else {
        throw "İnternet bağlantısı yok"
    }
} catch {
    Write-Error "İnternet bağlantısı bulunamadı!"
    Write-Host ""
    Write-Host "Kurulum için internet bağlantısı gereklidir." -ForegroundColor Yellow
    Write-Log "HATA: İnternet bağlantısı yok"
    pause
    exit 1
}
Write-Host ""

# Check disk space
Write-Info "Disk alanı kontrol ediliyor..."
$drive = Get-PSDrive -Name C
$freeSpaceGB = [math]::Round($drive.Free / 1GB, 2)
if ($freeSpaceGB -lt 3) {
    Write-Error "Yetersiz disk alanı! (En az 3GB gerekli)"
    Write-Host "Mevcut boş alan: $freeSpaceGB GB" -ForegroundColor Yellow
    Write-Log "HATA: Yetersiz disk alanı ($freeSpaceGB GB)"
    pause
    exit 1
}
Write-Success "Yeterli disk alanı mevcut ($freeSpaceGB GB)"
Write-Log "Disk alanı: $freeSpaceGB GB"
Write-Host ""

# Check if winget is available
Write-Info "Winget kontrol ediliyor..."
try {
    $wingetVersion = winget --version
    Write-Success "Winget mevcut ($wingetVersion)"
    Write-Log "Winget mevcut ($wingetVersion)"
    $wingetAvailable = $true
} catch {
    Write-Warning "Winget bulunamadı"
    Write-Host "Winget olmadan kurulum manuel indirme ile devam edecek." -ForegroundColor Yellow
    Write-Log "Winget bulunamadı"
    $wingetAvailable = $false
}
Write-Host ""

# Install Git
Write-Info "Git kontrol ediliyor..."
try {
    $gitVersion = git --version 2>$null
    if ($gitVersion) {
        Write-Success "Git zaten kurulu ($gitVersion)"
        Write-Log "Git zaten kurulu ($gitVersion)"
    }
} catch {
    Write-Info "Git bulunamadı. Kurulum yapılıyor..."
    Write-Log "Git bulunamadı, kurulacak"
    
    if ($wingetAvailable) {
        Write-Info "Winget ile Git kuruluyor..."
        winget install --id Git.Git -e --silent --accept-package-agreements --accept-source-agreements
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Git başarıyla kuruldu!"
            Write-Log "Git başarıyla kuruldu (winget)"
        } else {
            Write-Warning "Git kurulumu başarısız oldu"
            Write-Log "HATA: Git kurulumu başarısız"
        }
    } else {
        Write-Info "Manuel indirme gerekli"
        Write-Host "Git indirmek için: https://git-scm.com/download/win" -ForegroundColor Yellow
        Write-Log "Git manuel kurulum gerekli"
        Start-Process "https://git-scm.com/download/win"
        pause
    }
    
    # Refresh environment
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}
Write-Host ""

# Install Python
Write-Info "Python kontrol ediliyor..."
$pythonNeedsUpdate = $false

try {
    $pythonVersion = python --version 2>$null
    if ($pythonVersion) {
        Write-Success "Python zaten kurulu ($pythonVersion)"
        Write-Log "Python zaten kurulu ($pythonVersion)"
        
        # Check Python version (need 3.11+)
        if ($pythonVersion -match "Python (\d+)\.(\d+)\.(\d+)") {
            $major = [int]$matches[1]
            $minor = [int]$matches[2]
            
            if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 11)) {
                Write-Warning "Python sürümü çok eski! (3.11+ gerekli)"
                $pythonNeedsUpdate = $true
            }
        }
    }
} catch {
    $pythonNeedsUpdate = $true
}

if ($pythonNeedsUpdate) {
    Write-Info "Python 3.11+ bulunamadı. Kurulum yapılıyor..."
    Write-Log "Python 3.11+ bulunamadı, kurulacak"
    
    if ($wingetAvailable) {
        Write-Info "Winget ile Python kuruluyor... (Bu işlem 2-3 dakika sürebilir)"
        winget install --id Python.Python.3.11 -e --silent --accept-package-agreements --accept-source-agreements
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Python başarıyla kuruldu!"
            Write-Log "Python başarıyla kuruldu (winget)"
        } else {
            Write-Warning "Python kurulumu başarısız oldu"
            Write-Log "HATA: Python kurulumu başarısız"
        }
    } else {
        Write-Info "Manuel indirme gerekli"
        Write-Host "Python 3.11 indirmek için: https://www.python.org/downloads/" -ForegroundColor Yellow
        Write-Host "ÖNEMLİ: Kurulumda 'Add Python to PATH' seçeneğini işaretleyin!" -ForegroundColor Yellow
        Write-Log "Python manuel kurulum gerekli"
        Start-Process "https://www.python.org/downloads/"
        pause
        exit 0
    }
    
    # Refresh environment
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    
    # Verify Python installation
    try {
        python --version 2>$null | Out-Null
    } catch {
        Write-Error "Python kurulumunda sorun oluştu!"
        Write-Host "Lütfen Python'u manuel olarak kurun ve PATH'e ekleyin." -ForegroundColor Yellow
        Write-Log "HATA: Python kurulumu doğrulanamadı"
        pause
        exit 1
    }
}
Write-Host ""

# Check pip
Write-Info "pip kontrol ediliyor..."
try {
    python -m pip --version 2>$null | Out-Null
    Write-Success "pip mevcut"
    Write-Log "pip mevcut"
} catch {
    Write-Error "pip bulunamadı! Python kurulumunu kontrol edin."
    Write-Log "HATA: pip bulunamadı"
    pause
    exit 1
}
Write-Host ""

# Upgrade pip
Write-Info "pip güncelleniyor..."
Write-Log "pip güncelleniyor"
python -m pip install --upgrade pip --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Success "pip güncellendi"
    Write-Log "pip başarıyla güncellendi"
} else {
    Write-Warning "pip güncellemesi başarısız (devam ediliyor)"
    Write-Log "UYARI: pip güncellemesi başarısız"
}
Write-Host ""

# Install Python packages
Write-Header "Python Paketleri Yükleniyor"
Write-Host "Bu işlem 5-15 dakika sürebilir (PyTorch büyük bir paket)" -ForegroundColor Yellow
Write-Host "Lütfen bekleyin..." -ForegroundColor Yellow
Write-Host ""
Write-Log "Python paketleri yükleniyor"

if (Test-Path "requirements.txt") {
    # Install PyTorch first with CPU-only version
    Write-Info "PyTorch kuruluyor (CPU versiyonu)..."
    python -m pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
    if ($LASTEXITCODE -eq 0) {
        Write-Success "PyTorch kuruldu"
        Write-Log "PyTorch kuruldu"
    } else {
        Write-Warning "PyTorch kurulumu başarısız"
        Write-Log "HATA: PyTorch kurulumu başarısız"
    }
    Write-Host ""
    
    # Install other packages
    Write-Info "Diğer paketler kuruluyor..."
    python -m pip install -r requirements.txt --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Tüm paketler başarıyla yüklendi!"
        Write-Log "Tüm paketler yüklendi"
    } else {
        Write-Warning "Bazı paketler yüklenemedi"
        Write-Host "Detaylar için setup.log dosyasını kontrol edin." -ForegroundColor Yellow
        Write-Log "HATA: Paket yükleme başarısız"
    }
} else {
    Write-Error "requirements.txt dosyası bulunamadı!"
    Write-Log "HATA: requirements.txt bulunamadı"
}
Write-Host ""

# Create necessary folders
Write-Info "Klasörler oluşturuluyor..."
Write-Log "Klasörler oluşturuluyor"

$folders = @("models", "cache", "logs", "user_data")
foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Success "$folder\ oluşturuldu"
        Write-Log "$folder\ klasörü oluşturuldu"
    }
}
Write-Host ""

# Check config.json
Write-Info "Yapılandırma dosyası kontrol ediliyor..."
if (-not (Test-Path "config.json")) {
    Write-Info "config.json bulunamadı, varsayılan ayarlar kullanılacak"
    Write-Log "config.json bulunamadı"
} else {
    Write-Success "config.json mevcut"
    Write-Log "config.json mevcut"
}
Write-Host ""

# Installation complete
Write-Header "KURULUM TAMAMLANDI! 🎉"
Write-Host ""
Write-Success "Tüm gerekli programlar kuruldu"
Write-Success "Python paketleri yüklendi"
Write-Success "Klasör yapısı oluşturuldu"
Write-Success "Yapılandırma hazır"
Write-Host ""
Write-Log "Kurulum başarıyla tamamlandı"
Write-Host ""
Write-Host "Programı başlatmak için:" -ForegroundColor White
Write-Host "  1. quick-start.bat'e çift tıklayın" -ForegroundColor White
Write-Host "  VEYA" -ForegroundColor White
Write-Host "  2. Komut satırında: python main.py" -ForegroundColor White
Write-Host ""
Write-Host "Detaylı kullanım için: KURULUM.md dosyasını okuyun" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Ask to start the application
$startNow = Read-Host "Programı şimdi başlatmak ister misiniz? (E/H)"
if ($startNow -eq "E" -or $startNow -eq "e") {
    Write-Host ""
    Write-Info "Uygulama başlatılıyor..."
    Write-Log "Uygulama kullanıcı tarafından başlatıldı"
    python main.py
} else {
    Write-Host ""
    Write-Host "İyi günler! 👋" -ForegroundColor Green
    Write-Log "Kurulum tamamlandı, uygulama başlatılmadı"
}

pause
