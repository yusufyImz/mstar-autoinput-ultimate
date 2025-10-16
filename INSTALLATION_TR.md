# Kurulum Kılavuzu 🚀

Bu kılavuz, Club M Star AutoInput - Ultimate Edition'ın adım adım kurulumunu açıklar.

## 📋 İçindekiler

- [Ön Gereksinimler](#-ön-gereksinimler)
- [Sistem Kontrolü](#-sistem-kontrolü)
- [Python Kurulumu](#-python-kurulumu)
- [Proje Kurulumu](#-proje-kurulumu)
- [Bağımlılık Kurulumu](#-bağımlılık-kurulumu)
- [İlk Yapılandırma](#-ilk-yapılandırma)
- [Sorun Giderme](#-sorun-giderme)

## ✅ Ön Gereksinimler

### Minimum Sistem Gereksinimleri

- **İşletim Sistemi**: Windows 10/11 (64-bit)
- **CPU**: Intel Core i5 veya daha iyi (önerilen: i7-7700)
- **RAM**: Minimum 8GB (önerilen: 16GB+)
- **Disk Alanı**: 2GB boş alan
- **İnternet**: İlk kurulum için gerekli

### Önerilen Sistem (Test Edilmiş)

- **CPU**: Intel Core i7-7700
- **GPU**: AMD Radeon RX 6400 (opsiyonel)
- **RAM**: 28GB DDR4 2400MHz
- **Depolama**: SSD

## 🔍 Sistem Kontrolü

Kuruluma başlamadan önce sisteminizi kontrol edin:

### 1. Windows Sürümünü Kontrol Edin

```powershell
# PowerShell'de çalıştırın
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

✅ **Beklenen**: Windows 10 veya 11, 64-bit

### 2. CPU'yu Kontrol Edin

```powershell
# PowerShell'de çalıştırın
wmic cpu get name
```

✅ **Beklenen**: Intel Core i5 veya daha iyi

### 3. RAM'i Kontrol Edin

```powershell
# PowerShell'de çalıştırın
systeminfo | findstr /C:"Total Physical Memory"
```

✅ **Beklenen**: 8GB veya daha fazla

## 🐍 Python Kurulumu

### Adım 1: Python'u İndirin

1. [Python 3.11 indirme sayfasına](https://www.python.org/downloads/) gidin
2. "Download Python 3.11.x" düğmesine tıklayın
3. İndirilen `python-3.11.x-amd64.exe` dosyasını çalıştırın

### Adım 2: Python'u Kurun

1. **ÖNEMLİ**: "Add Python 3.11 to PATH" kutusunu işaretleyin ✅
2. "Install Now" seçeneğine tıklayın
3. Kurulum tamamlanana kadar bekleyin
4. "Disable path length limit" seçeneğine tıklayın (önerilir)

### Adım 3: Kurulumu Doğrulayın

```powershell
# PowerShell veya CMD'de çalıştırın
python --version
```

✅ **Beklenen çıktı**: `Python 3.11.x`

```powershell
pip --version
```

✅ **Beklenen çıktı**: `pip 23.x.x from ...`

### Sorun Giderme: Python PATH Hatası

Python komutu çalışmıyorsa:

1. Windows Arama'da "Environment Variables" yazın
2. "Edit the system environment variables" seçin
3. "Environment Variables" düğmesine tıklayın
4. "Path" değişkenini bulun ve "Edit" tıklayın
5. Python yolunu ekleyin (örn: `C:\Python311\` ve `C:\Python311\Scripts\`)

## 📦 Proje Kurulumu

### Adım 1: Git Kurulumu (Opsiyonel)

Git kurulu değilse:

1. [Git for Windows](https://git-scm.com/download/win) indirin
2. Kurulum sihirbazını varsayılan ayarlarla tamamlayın

**VEYA** projeyi manuel indirin:

1. [GitHub deposuna](https://github.com/yusufyImz/mstar-autoinput-ultimate) gidin
2. "Code" > "Download ZIP" tıklayın
3. ZIP'i çıkarın

### Adım 2: Projeyi İndirin

**Git ile:**

```powershell
# Bilgisayarınızda bir klasör seçin (örn: C:\Projects)
cd C:\Projects

# Projeyi klonlayın
git clone https://github.com/yusufyImz/mstar-autoinput-ultimate.git

# Proje klasörüne girin
cd mstar-autoinput-ultimate
```

**Manuel indirme ile:**

```powershell
# ZIP'i çıkardığınız klasöre gidin
cd C:\Path\To\mstar-autoinput-ultimate
```

## 📚 Bağımlılık Kurulumu

### Adım 1: Pip'i Güncelleyin

```powershell
python -m pip install --upgrade pip
```

### Adım 2: Bağımlılıkları Yükleyin

```powershell
# requirements.txt dosyasından yükleyin
pip install -r requirements.txt
```

⏱️ **Not**: Bu işlem 5-10 dakika sürebilir, özellikle PyTorch indiriliyor.

### Adım 3: Kurulumu Doğrulayın

```powershell
# Her bir paketi kontrol edin
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import cv2; print('OpenCV:', cv2.__version__)"
python -c "import flask; print('Flask:', flask.__version__)"
```

✅ **Beklenen**: Hata almadan sürüm numaraları

### Sorun Giderme: Bağımlılık Hataları

**PyTorch kurulum hatası:**

```powershell
# CPU versiyonunu manuel kurun
pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
```

**OpenCV hatası:**

```powershell
pip install opencv-python==4.8.1.78 --force-reinstall
```

**Genel hata:**

```powershell
# Bağımlılıkları tek tek kurun
pip install torch==2.0.1
pip install opencv-python==4.8.1.78
pip install flask==3.0.0
pip install flask-cors==4.0.0
pip install pillow==10.1.0
pip install pynput==1.7.6
pip install mss==9.0.1
pip install requests==2.31.0
pip install psutil==5.9.6
```

## ⚙️ İlk Yapılandırma

### Adım 1: Dizinleri Oluşturun

```powershell
# Gerekli dizinleri oluşturun
mkdir models
mkdir cache
mkdir logs
mkdir user_data
```

### Adım 2: Yapılandırma Dosyasını Kontrol Edin

`config.json` dosyası otomatik olarak oluşturulmalıdır. Kontrol edin:

```powershell
# Dosyayı görüntüleyin
type config.json
```

Yoksa, varsayılan ayarlarla oluşturulacaktır.

### Adım 3: İlk Çalıştırma

```powershell
# Uygulamayı başlatın
python main.py
```

✅ **Beklenen**: GUI penceresi açılmalı

### Adım 4: Donanım Optimizasyonu

1. GUI'de **⚙️ Ayarlar** sekmesine gidin
2. Ayarları sisteminize göre yapın:

   **8GB RAM için:**
   - Batch Size: 4-8
   - CPU Threads: 1-2

   **16GB+ RAM için:**
   - Batch Size: 16
   - CPU Threads: 2

   **28GB RAM için (test sistemi):**
   - Batch Size: 16
   - CPU Threads: 2

3. **💾 Ayarları Kaydet** düğmesine tıklayın

### Adım 5: Zamanlama Kalibrasyonu

1. **⚙️ Ayarlar** sekmesinde
2. **Kalibre Et** düğmesine tıklayın
3. 10 saniye bekleyin
4. Önerilen offset değerini uygulayın

## 🎮 İlk Kullanım

### Test Etme

1. Club M Star oyununu başlatın
2. AutoInput uygulamasında **📊 Gösterge Paneli** sekmesine gidin
3. **▶️ Başlat** düğmesine tıklayın
4. İstatistikleri izleyin

### Mobil Kontrolü Test Etme

1. **📱 Mobil Kontrol** sekmesine gidin
2. Sunucu URL'sini not edin (örn: `http://192.168.1.100:5000`)
3. Mobil cihazınızda tarayıcıda bu URL'yi açın
4. API endpoint'lerini test edin

## 🔧 Sorun Giderme

### Genel Sorunlar

**1. "python" komutu tanınmıyor**

```powershell
# PATH'e Python ekleyin veya tam yolu kullanın
C:\Python311\python.exe main.py
```

**2. ModuleNotFoundError**

```powershell
# Eksik modülü yükleyin
pip install [modül_adı]
```

**3. GUI açılmıyor**

- Tkinter kurulu olduğundan emin olun (Python ile birlikte gelir)
- Grafik sürücülerini güncelleyin
- Windows güvenlik duvarını kontrol edin

**4. Yüksek CPU kullanımı**

- `config.json`'da `cpu_threads` değerini 1'e düşürün
- `batch_size` değerini azaltın
- Diğer uygulamaları kapatın

**5. "Port already in use" hatası**

```powershell
# Port 5000'i kullanan programı bulun
netstat -ano | findstr :5000

# İşlemi sonlandırın (PID ile)
taskkill /PID [PID_numarası] /F
```

### Log Dosyaları

Sorun yaşıyorsanız log dosyalarını kontrol edin:

```powershell
# Son hataları görüntüle
type logs\error.log

# Uygulama logunu görüntüle
type logs\app.log
```

### Performans Sorunları

**Düşük FPS:**
- Ekran çözünürlüğünü düşürün
- Diğer ağır programları kapatın
- SSD kullandığınızdan emin olun

**Yüksek RAM kullanımı:**
- `cache_size_mb` değerini 256'ya düşürün
- `batch_size` değerini 4'e düşürün
- Tarayıcı sekmelerini kapatın

## 📞 Destek

Hala sorun mu yaşıyorsunuz?

1. **GitHub Issues**: [Sorun bildirin](https://github.com/yusufyImz/mstar-autoinput-ultimate/issues)
2. **Email**: yusufyilmazz@outlook.com.tr
3. **Dokümantasyon**: [Wiki](https://github.com/yusufyImz/mstar-autoinput-ultimate/wiki)

## ✅ Kurulum Kontrol Listesi

Kurulumun tamamlandığından emin olmak için:

- [ ] Python 3.11+ kurulu ve PATH'de
- [ ] Tüm bağımlılıklar yüklü
- [ ] Proje dosyaları indirildi
- [ ] Gerekli dizinler oluşturuldu
- [ ] config.json dosyası var
- [ ] GUI başarıyla açılıyor
- [ ] Donanım optimizasyonu yapıldı
- [ ] Zamanlama kalibrasyonu tamamlandı
- [ ] Mobil sunucu çalışıyor

## 🎉 Başarılı!

Kurulum tamamlandı! Artık kullanmaya başlayabilirsiniz.

Kullanım kılavuzu için: [USER_GUIDE_TR.md](USER_GUIDE_TR.md)

---

**İyi oyunlar! 🎮**
