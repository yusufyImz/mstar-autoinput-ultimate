# 🚀 Otomatik Kurulum Kılavuzu

**Club M Star AutoInput - Ultimate Edition** için tek tıkla otomatik kurulum rehberi.

## 📋 İçindekiler

- [Hızlı Başlangıç](#-hızlı-başlangıç)
- [Script'ler](#-scriptler)
- [Adım Adım Kurulum](#-adım-adım-kurulum)
- [Sorun Giderme](#-sorun-giderme)
- [Sık Sorulan Sorular](#-sık-sorulan-sorular)
- [Manuel Kurulum](#-manuel-kurulum)

---

## ⚡ Hızlı Başlangıç

### En Kolay Yol (Önerilen)

1. **`setup.bat`** dosyasına **sağ tıklayın**
2. **"Yönetici olarak çalıştır"** seçeneğini seçin
3. ☕ Bekleyin (10-15 dakika)
4. ✅ Kurulum tamamlandığında **"E"** tuşuna basın

**Hepsi bu kadar!** 🎉

---

## 📜 Script'ler

Projedeki otomatik kurulum script'leri:

### 1. `setup.bat` - Ana Kurulum Script'i ⭐

**Ne yapar?**
- Yönetici yetkisi kontrolü
- İnternet bağlantısı kontrolü
- Git kurulumu (otomatik)
- Python 3.11+ kurulumu (otomatik)
- Tüm Python paketlerini yükleme
- Klasör yapısını oluşturma
- Kurulum logu tutma

**Ne zaman kullanılır?**
- İlk kurulum
- Tamamen temiz bir sisteme kurulum
- Programlar eksikse (Git, Python)

**Nasıl kullanılır?**
```cmd
1. setup.bat'e SAĞ TIKLA
2. "Yönetici olarak çalıştır" seç
3. Bekle (10-15 dakika)
```

**Dikkat!** ⚠️
- Yönetici yetkisi gereklidir
- İnternet bağlantısı gereklidir
- En az 3GB boş disk alanı gereklidir

---

### 2. `quick-start.bat` - Hızlı Başlatma 🚀

**Ne yapar?**
- Python kurulu mu kontrol eder
- Gerekli klasörler var mı kontrol eder
- Eksik paketleri tespit eder
- Programı başlatır

**Ne zaman kullanılır?**
- Kurulum tamamlandıktan sonra
- Her program açmak istediğinizde

**Nasıl kullanılır?**
```cmd
Çift tıkla - Hepsi bu! 😊
```

**Avantajları:**
- Tek tıkla başlatma
- Otomatik kontroller
- Sorun varsa bildirim

---

### 3. `install-python-packages.bat` - Paket Kurulumu 📦

**Ne yapar?**
- Sadece Python paketlerini yükler
- pip'i günceller
- Her paketin kurulumunu kontrol eder
- İlerleme gösterir

**Ne zaman kullanılır?**
- Python ve Git zaten kurulu
- Sadece paketler yüklenecek
- Paket hatası oluştuysa

**Nasıl kullanılır?**
```cmd
Çift tıkla
"E" tuşuna bas (onay için)
Bekle (5-10 dakika)
```

**İpucu:** 💡
PyTorch yaklaşık 700MB'tır. İndirme hızınız yavaşsa sabırlı olun!

---

### 4. `check-system.bat` - Sistem Kontrolü 🔍

**Ne yapar?**
- Sistem bilgilerini toplar (CPU, RAM, Disk)
- Git ve Python kurulumunu kontrol eder
- Tüm paketleri kontrol eder
- Detaylı rapor oluşturur (`system-check.txt`)

**Ne zaman kullanılır?**
- Sorun yaşandığında
- Kurulum öncesi sistem kontrolü
- Destek isterken (raporu paylaşın)

**Nasıl kullanılır?**
```cmd
Çift tıkla
Rapor otomatik oluşturulur
"E" tuşuna bas (raporu açmak için)
```

**Rapor içeriği:**
- İşletim sistemi bilgisi
- Donanım özellikleri
- Kurulu programlar
- Eksik paketler listesi

---

### 5. `setup.ps1` - PowerShell Kurulum (Alternatif) 💻

**Ne yapar?**
- `setup.bat` ile aynı işlevi görür
- Modern PowerShell script'i
- Renkli ve detaylı çıktı

**Ne zaman kullanılır?**
- PowerShell tercih ediliyorsa
- .bat script'i sorun veriyorsa

**Nasıl kullanılır?**
```powershell
1. PowerShell'i YÖNETİCİ olarak aç
2. Proje klasörüne git
3. .\setup.ps1 komutunu çalıştır
```

**Not:** ⚠️
PowerShell Execution Policy hatası alırsanız:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📖 Adım Adım Kurulum

### Senaryo 1: Tamamen Boş Sistem

**Durum:** Hiçbir program kurulu değil

**Adımlar:**

1️⃣ **Projeyi İndir**
   - GitHub'dan ZIP indir ve çıkar
   - VEYA Git varsa: `git clone https://github.com/yusufyImz/mstar-autoinput-ultimate.git`

2️⃣ **setup.bat'i Çalıştır**
   ```
   SAĞ TIKLA → "Yönetici olarak çalıştır"
   ```

3️⃣ **Bekle**
   - Git indirilip kurulacak (2-3 dakika)
   - Python indirilip kurulacak (3-5 dakika)
   - Paketler yüklenecek (5-10 dakika)

4️⃣ **Başlat**
   - Kurulum sonunda "E" tuşuna bas
   - VEYA sonra `quick-start.bat` kullan

**Toplam Süre:** ⏱️ 10-20 dakika

---

### Senaryo 2: Python ve Git Kurulu

**Durum:** Sadece paketler yüklenecek

**Adımlar:**

1️⃣ **Paket Kurulum Script'ini Çalıştır**
   ```
   install-python-packages.bat (çift tıkla)
   ```

2️⃣ **Onay Ver**
   - "E" tuşuna bas

3️⃣ **Bekle**
   - Paketler yüklenecek (5-10 dakika)

4️⃣ **Başlat**
   ```
   quick-start.bat (çift tıkla)
   ```

**Toplam Süre:** ⏱️ 5-10 dakika

---

### Senaryo 3: Her Şey Kurulu, Sadece Çalıştır

**Durum:** Kurulum zaten yapılmış

**Adım:**

```
quick-start.bat (çift tıkla)
```

**Toplam Süre:** ⏱️ 5 saniye

---

## 🔧 Sorun Giderme

### Genel Kontrol

Sorun yaşıyorsanız önce sistem kontrolü yapın:

```
check-system.bat (çift tıkla)
```

Raporu inceleyin ve eksik ne varsa kurun.

---

### Sık Karşılaşılan Sorunlar

#### ❌ "python komutu tanınmıyor"

**Sebep:** Python PATH'e eklenmemiş

**Çözüm 1:** Python'u yeniden kur
```
1. Python kurulum dosyasını indir
2. "Add Python to PATH" kutusunu İŞARETLE ✅
3. Install Now
```

**Çözüm 2:** PATH'e manuel ekle
```
1. Windows Arama → "Environment Variables"
2. "Path" değişkenini düzenle
3. Python klasörünü ekle (örn: C:\Python311\)
4. Tamam → Terminali yeniden aç
```

**Çözüm 3:** Tam yol ile çalıştır
```cmd
C:\Python311\python.exe main.py
```

---

#### ❌ "Yönetici yetkisi gerekli"

**Sebep:** Script yönetici olarak çalıştırılmamış

**Çözüm:**
```
1. Script'e SAĞ TIKLA
2. "Yönetici olarak çalıştır" seç
```

**Alternatif:**
```
1. Komut İstemi'ni yönetici olarak aç
2. Proje klasörüne git
3. setup.bat komutunu çalıştır
```

---

#### ❌ "pip bulunamadı"

**Sebep:** pip Python ile kurulmamış (çok nadir)

**Çözüm:**
```cmd
python -m ensurepip --upgrade
```

Sonra pip'i güncelle:
```cmd
python -m pip install --upgrade pip
```

---

#### ❌ "ModuleNotFoundError: No module named 'torch'"

**Sebep:** PyTorch kurulmamış veya kurulamadı

**Çözüm 1:** Tekrar kur
```cmd
pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
```

**Çözüm 2:** requirements.txt'ten kur
```cmd
pip install -r requirements.txt
```

**Çözüm 3:** Manuel kurulum
```cmd
install-python-packages.bat (çift tıkla)
```

---

#### ❌ "İnternet bağlantısı bulunamadı"

**Sebep:** İnternet bağlantısı yok veya güvenlik duvarı engelliyor

**Çözüm:**
```
1. İnternet bağlantınızı kontrol edin
2. Güvenlik duvarı/antivirus ayarlarını kontrol edin
3. VPN kullanıyorsanız kapatın
4. Proxy ayarlarını kontrol edin
```

---

#### ❌ "Yetersiz disk alanı"

**Sebep:** 3GB'dan az boş disk alanı

**Çözüm:**
```
1. Gereksiz dosyaları silin
2. Disk Temizleme aracını kullanın
3. Başka bir sürücüye kurulum yapın
```

---

#### ❌ "Port 5000 already in use"

**Sebep:** Başka bir program 5000 portunu kullanıyor

**Çözüm 1:** Port'u kullanan programı bul ve kapat
```cmd
netstat -ano | findstr :5000
taskkill /PID [PID_numarası] /F
```

**Çözüm 2:** config.json'da port değiştir
```json
{
  "mobile": {
    "server_port": 5001
  }
}
```

---

#### ⚠️ "Kurulum çok yavaş"

**Sebep:** PyTorch büyük bir dosya (700MB)

**Çözüm:**
```
1. Sabırlı olun ☕
2. İndirme hızınızı kontrol edin
3. Alternatif mirror kullanın (script'te otomatik)
```

**İpucu:** Kahve molası verin, script çalışmaya devam eder!

---

#### ❌ "GUI açılmıyor / Pencere görünmüyor"

**Sebep 1:** Tkinter kurulu değil

**Çözüm:** Python'u yeniden kur (Tkinter dahil edilmeli)

**Sebep 2:** Grafik sürücü sorunu

**Çözüm:**
```
1. Grafik sürücülerini güncelle
2. Windows güncellemelerini yap
3. Sanal makine kullanıyorsanız guest tools kur
```

**Sebep 3:** Antivirüs engelliyor

**Çözüm:**
```
1. Antivirüs'ü geçici olarak kapat
2. Python'u ve proje klasörünü istisna listesine ekle
```

---

#### ⚠️ "Yüksek CPU/RAM kullanımı"

**Sebep:** Varsayılan ayarlar yüksek performans için

**Çözüm:** config.json'u düzenle
```json
{
  "hardware": {
    "cpu_threads": 1,
    "batch_size": 4,
    "cache_size_mb": 256
  }
}
```

**Önerilen ayarlar:**

8GB RAM için:
```json
{
  "cpu_threads": 1,
  "batch_size": 4,
  "cache_size_mb": 256
}
```

16GB+ RAM için:
```json
{
  "cpu_threads": 2,
  "batch_size": 8,
  "cache_size_mb": 512
}
```

---

## ❓ Sık Sorulan Sorular

### Kurulum hakkında

**S: Kurulum ne kadar sürer?**
- Boş sistemde: 10-20 dakika
- Python kurulu: 5-10 dakika
- Her şey kurulu: 5 saniye

**S: İnternet olmadan kurulum yapabilir miyim?**
- Hayır, ilk kurulum için internet gerekli
- Ancak bir kez kurulduktan sonra offline çalışır

**S: Hangi Windows sürümleri destekleniyor?**
- Windows 10 (64-bit)
- Windows 11
- Windows Server 2019+

**S: 32-bit sistem destekleniyor mu?**
- Hayır, sadece 64-bit

**S: Antivirüs uyarı veriyor, güvenli mi?**
- Evet, güvenli
- Script sadece resmi kaynaklardan program indirir
- Antivirüs'e istisna ekleyebilirsiniz

---

### Gereksinimler hakkında

**S: GPU gerekli mi?**
- Hayır, CPU versiyonu kurulur
- GPU kullanmak isterseniz manuel kurulum gerekir

**S: En az ne kadar RAM gerekli?**
- Minimum: 8GB
- Önerilen: 16GB+
- Rahat kullanım: 28GB (test sistemimiz)

**S: Python sürümü önemli mi?**
- Evet, 3.11+ gerekli
- Script otomatik doğru sürümü kurar

---

### Kullanım hakkında

**S: Her seferinde setup.bat çalıştırmam gerekir mi?**
- Hayır, sadece ilk kurulum için
- Sonrasında quick-start.bat kullanın

**S: Programı nasıl güncellerim?**
```cmd
git pull
pip install -r requirements.txt --upgrade
```

**S: Ayarlarım silinir mi?**
- Hayır, config.json ve user_data/ korunur
- Ancak yedek almanız önerilir

---

## 🔨 Manuel Kurulum

Otomatik kurulum çalışmazsa manuel adımlar:

### 1. Git Kurulumu

1. İndir: https://git-scm.com/download/win
2. Kurulum dosyasını çalıştır
3. Varsayılan ayarlarla devam et
4. Doğrula: `git --version`

### 2. Python Kurulumu

1. İndir: https://www.python.org/downloads/
2. Python 3.11+ seç
3. ✅ **"Add Python to PATH" kutusunu İŞARETLE**
4. "Install Now" tıkla
5. Doğrula: `python --version`

### 3. Pip Güncellemesi

```cmd
python -m pip install --upgrade pip
```

### 4. Paket Kurulumu

PyTorch (CPU):
```cmd
pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
```

Diğer paketler:
```cmd
pip install opencv-python==4.8.1.78
pip install numpy==1.24.3
pip install flask==3.0.0
pip install flask-cors==4.0.0
pip install pillow==10.1.0
pip install pynput==1.7.6
pip install mss==9.0.1
pip install requests==2.31.0
pip install psutil==5.9.6
```

### 5. Klasör Oluşturma

```cmd
mkdir models
mkdir cache
mkdir logs
mkdir user_data
```

### 6. Başlatma

```cmd
python main.py
```

---

## 📞 Destek

### Hala sorun mu var?

1. **Sistem Kontrolü Raporu Oluştur**
   ```
   check-system.bat (çift tıkla)
   ```

2. **Log Dosyalarını Kontrol Et**
   - `setup.log` - Kurulum logu
   - `logs/error.log` - Hata logu
   - `logs/app.log` - Uygulama logu

3. **GitHub Issue Aç**
   - Sorununu detaylı anlat
   - `system-check.txt` dosyasını ekle
   - Log dosyalarından ilgili bölümleri ekle
   - Ekran görüntüsü ekle

4. **E-posta Gönder**
   - yusufyilmazz@outlook.com.tr
   - Konu: "Kurulum Sorunu - [Kısa açıklama]"

---

## ✅ Kurulum Sonrası Kontrol Listesi

Kurulumun başarılı olduğundan emin olmak için:

- [ ] `python --version` komutu çalışıyor (3.11+)
- [ ] `git --version` komutu çalışıyor
- [ ] `pip --version` komutu çalışıyor
- [ ] Tüm klasörler mevcut (models, cache, logs, user_data)
- [ ] config.json dosyası var
- [ ] check-system.bat ✅ veriyor
- [ ] quick-start.bat ile GUI açılıyor
- [ ] Gösterge panelinde istatistikler görünüyor
- [ ] Başlat/Durdur düğmeleri çalışıyor

---

## 🎉 Kurulum Tamamlandı!

Tebrikler! Artık Club M Star AutoInput kullanmaya hazırsınız.

**Sonraki adımlar:**

1. 📖 **Kullanım Kılavuzu:** [USER_GUIDE_TR.md](USER_GUIDE_TR.md)
2. 🎮 **İlk kullanım:** Oyunu aç ve "Başlat" butonuna bas
3. ⚙️ **Ayarlar:** Sisteminize göre optimize et
4. 📱 **Mobil kontrol:** Akıllı telefonunuzdan kontrol edin

**İyi oyunlar! 🎮🎉**

---

## 📝 Notlar

- Script'ler düzenli olarak güncellenir
- Yeni sürümler için GitHub deposunu kontrol edin
- Geri bildirimlerinizi bekliyoruz!

**Versiyon:** 1.0  
**Son güncelleme:** 2025-10-16  
**Lisans:** MIT
