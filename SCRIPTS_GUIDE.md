# 📜 Kurulum Script'leri Rehberi

Bu belge, proje ile birlikte gelen otomatik kurulum script'lerinin detaylı açıklamasını içerir.

## 📦 Script Listesi

### 1. `setup.bat` - Ana Kurulum Script'i ⭐

**Amaç:** Sıfırdan tam kurulum yapar.

**Ne yapar?**
1. ✅ Yönetici yetkisi kontrolü
2. ✅ İnternet bağlantısı kontrolü
3. ✅ Disk alanı kontrolü (minimum 3GB)
4. ✅ Winget varlığını kontrol eder
5. ✅ Git kurulumu (gerekirse)
6. ✅ Python 3.11+ kurulumu (gerekirse)
7. ✅ pip güncelleme
8. ✅ PyTorch CPU versiyonu kurulumu
9. ✅ Tüm paketleri `requirements.txt`'ten yükleme
10. ✅ Gerekli klasörleri oluşturma (`models/`, `cache/`, `logs/`, `user_data/`)
11. ✅ Detaylı log dosyası (`setup.log`) oluşturma
12. ✅ Kullanıcıya programı başlatma seçeneği sunma

**Kullanım:**
```cmd
SAĞ TIKLA → "Yönetici olarak çalıştır"
```

**Özellikler:**
- 🌐 Türkçe kullanıcı mesajları
- 📝 Detaylı loglama
- ⚠️ Hata yönetimi
- 🎨 Renkli terminal çıktısı
- ⏱️ Süre: 10-20 dakika

**Log dosyası:** `setup.log`

---

### 2. `quick-start.bat` - Hızlı Başlatma ⚡

**Amaç:** Programı kontroller yaparak başlatır.

**Ne yapar?**
1. ✅ Python kurulu mu kontrol eder
2. ✅ `main.py` dosyası var mı kontrol eder
3. ✅ Gerekli klasörler var mı kontrol eder (yoksa oluşturur)
4. ✅ Gerekli Python paketleri kurulu mu kontrol eder
5. ✅ Eksik paket varsa kullanıcıya kurulum seçeneği sunar
6. ✅ Programı başlatır

**Kullanım:**
```cmd
Çift tıkla
```

**Özellikler:**
- 🚀 Tek tıkla başlatma
- 🔍 Otomatik kontroller
- ⚠️ Eksiklik varsa bildirim
- 🎯 Hata durumunda yardım mesajları

**Süre:** 5 saniye

---

### 3. `install-python-packages.bat` - Paket Kurulumu 📦

**Amaç:** Sadece Python paketlerini yükler.

**Ne yapar?**
1. ✅ Python ve pip varlığını kontrol eder
2. ✅ pip'i günceller
3. ✅ `requirements.txt` dosyasını okur
4. ✅ Kullanıcıdan onay ister
5. ✅ PyTorch'u özel index ile yükler (CPU versiyonu)
6. ✅ Her paketi tek tek yükler ve kontrol eder
7. ✅ İlerleme gösterir (1/11, 2/11, ...)
8. ✅ Kurulum sonunda tüm paketleri doğrular

**Kullanım:**
```cmd
Çift tıkla
"E" tuşuna bas (onay için)
```

**Özellikler:**
- 📊 Paket bazlı ilerleme gösterimi
- ✅ Her paketin kurulum doğrulaması
- 🔄 PyTorch için özel index kullanımı
- 💡 Kullanıcı dostu mesajlar

**Süre:** 5-15 dakika

**Yüklenen paketler:**
1. torch (2.0.1 CPU)
2. torchvision (0.15.2 CPU)
3. opencv-python (4.8.1.78)
4. numpy (1.24.3)
5. flask (3.0.0)
6. flask-cors (4.0.0)
7. pillow (10.1.0)
8. pynput (1.7.6)
9. mss (9.0.1)
10. requests (2.31.0)
11. psutil (5.9.6)

---

### 4. `check-system.bat` - Sistem Kontrolü 🔍

**Amaç:** Sistem bilgilerini toplar ve detaylı rapor oluşturur.

**Ne yapar?**
1. ✅ İşletim sistemi bilgisi
2. ✅ CPU bilgisi (model, çekirdek sayısı)
3. ✅ RAM bilgisi (toplam, kullanılabilir)
4. ✅ Disk alanı bilgisi
5. ✅ Git versiyonu kontrolü
6. ✅ Python versiyonu ve yolu
7. ✅ pip versiyonu
8. ✅ Tüm Python paketlerinin versiyonları
9. ✅ Proje klasörlerinin varlığı
10. ✅ Yapılandırma dosyası kontrolü
11. ✅ Sistem performansı (CPU, RAM kullanımı)
12. ✅ Detaylı rapor dosyası (`system-check.txt`)

**Kullanım:**
```cmd
Çift tıkla
"E" tuşuna bas (raporu açmak için)
```

**Özellikler:**
- 📊 Kapsamlı sistem analizi
- 📄 Ayrıntılı rapor dosyası
- ✅ Eksik paket tespiti
- 💻 Donanım bilgileri
- 🔍 Sorun giderme için ideal

**Süre:** 10-15 saniye

**Rapor dosyası:** `system-check.txt`

---

### 5. `setup.ps1` - PowerShell Kurulum 💻

**Amaç:** Modern PowerShell ile tam kurulum.

**Ne yapar?**
- `setup.bat` ile aynı işlevleri yerine getirir
- PowerShell'in gelişmiş özelliklerini kullanır
- Daha temiz ve renkli çıktı

**Kullanım:**
```powershell
PowerShell'i YÖNETİCİ olarak aç
cd [proje_klasörü]
.\setup.ps1
```

**Özellikler:**
- 🎨 Renkli çıktı (Green, Red, Yellow, Cyan)
- 📝 Detaylı loglama
- ⚡ Modern PowerShell özellikleri
- 🔧 Daha iyi hata yönetimi

**Not:** PowerShell Execution Policy hatası alırsanız:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🎯 Kullanım Senaryoları

### Senaryo 1: İlk Kurulum (Hiçbir Şey Yok)

```
1. setup.bat'e SAĞ TIKLA → "Yönetici olarak çalıştır"
2. 10-15 dakika bekle
3. "E" tuşuna bas (programı başlatmak için)
```

**VEYA** sonraki kullanımlar için:
```
quick-start.bat'e çift tıkla
```

---

### Senaryo 2: Python ve Git Kurulu

```
1. install-python-packages.bat'e çift tıkla
2. "E" tuşuna bas (onay için)
3. 5-10 dakika bekle
4. quick-start.bat'e çift tıkla
```

---

### Senaryo 3: Her Şey Hazır, Sadece Başlat

```
quick-start.bat'e çift tıkla
```

---

### Senaryo 4: Sorun Var, Kontrol Et

```
check-system.bat'e çift tıkla
system-check.txt dosyasını incele
Eksik paketleri tespit et
```

---

## 🔧 Script İçinde Kullanılan Teknolojiler

### Batch Script Özellikleri

- **`chcp 65001`**: UTF-8 encoding (Türkçe karakter desteği)
- **`color 0A`**: Yeşil metin (terminal renklendirmesi)
- **`setlocal enabledelayedexpansion`**: Değişken genişletmesi
- **`net session`**: Yönetici yetkisi kontrolü
- **`ping 8.8.8.8`**: İnternet bağlantısı kontrolü
- **`winget`**: Windows Package Manager (otomatik kurulum)
- **`for /f`**: Döngüler ve metin işleme
- **`if exist`**: Dosya/klasör varlık kontrolü
- **`> nul 2>&1`**: Hata çıktısı gizleme

### PowerShell Özellikleri

- **`#Requires -RunAsAdministrator`**: Yönetici yetkisi zorunluluğu
- **`[Console]::OutputEncoding`**: UTF-8 encoding
- **`Write-Host -ForegroundColor`**: Renkli çıktı
- **`Test-Connection`**: Ping testi
- **`Get-PSDrive`**: Disk bilgisi
- **`Test-Path`**: Dosya varlık kontrolü

---

## 📝 Log Dosyaları

### `setup.log`

Kurulum işlemlerinin detaylı kaydı:

```
[2025-10-16 06:49:15] Kurulum başlatıldı
[2025-10-16 06:49:16] Yönetici yetkisi onaylandı
[2025-10-16 06:49:17] İnternet bağlantısı aktif
[2025-10-16 06:49:18] Disk alanı: 45 GB
[2025-10-16 06:49:19] Git kontrol ediliyor...
[2025-10-16 06:50:00] Git başarıyla kuruldu (winget)
[2025-10-16 06:50:01] Python kontrol ediliyor...
[2025-10-16 06:52:00] Python başarıyla kuruldu (winget)
[2025-10-16 06:52:05] pip güncelleniyor
[2025-10-16 06:52:30] pip başarıyla güncellendi
[2025-10-16 06:52:35] Python paketleri yükleniyor
[2025-10-16 06:53:00] PyTorch kuruldu
[2025-10-16 07:00:00] Tüm paketler yüklendi
[2025-10-16 07:00:05] models\ klasörü oluşturuldu
[2025-10-16 07:00:06] cache\ klasörü oluşturuldu
[2025-10-16 07:00:07] logs\ klasörü oluşturuldu
[2025-10-16 07:00:08] user_data\ klasörü oluşturuldu
[2025-10-16 07:00:09] config.json mevcut
[2025-10-16 07:00:10] Kurulum başarıyla tamamlandı
```

### `system-check.txt`

Sistem bilgileri raporu:

```
========================================
  Sistem Kontrol Raporu
  Tarih: 16.10.2025 06:53:00
========================================

İşletim Sistemi:
OS Name: Microsoft Windows 11 Home
OS Version: 10.0.22000 N/A Build 22000

CPU:
Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz
NumberOfCores: 4
NumberOfLogicalProcessors: 8

Bellek:
Total Physical Memory: 28,672 MB
Available Physical Memory: 18,234 MB

Python Kontrolü:
Python 3.11.9
✓ Python kurulu

Yüklü Paketler:
✓ torch: 2.0.1+cpu
✓ opencv-python: 4.8.1.78
✓ numpy: 1.24.3
...

ÖZET:
✅ Tüm gerekli paketler kurulu!
✅ Sistem hazır, uygulama çalıştırılabilir.
```

---

## ⚠️ Önemli Notlar

### Güvenlik

1. **Yönetici Yetkisi:** `setup.bat` ve `setup.ps1` yönetici yetkisi gerektirir
2. **Resmi Kaynaklar:** Tüm programlar resmi kaynaklardan indirilir (git-scm.com, python.org)
3. **HTTPS:** Güvenli bağlantılar kullanılır
4. **Winget:** Windows Package Manager güvenilir paket kaynağıdır

### Performans

1. **İndirme Süresi:** PyTorch ~700MB, internet hızınıza bağlı
2. **Kurulum Süresi:** Toplamda 10-20 dakika
3. **Disk Alanı:** Minimum 3GB, önerilen 5GB+

### Sorun Giderme

1. **Antivirüs:** Script'leri engelleyebilir, geçici olarak kapatın
2. **Güvenlik Duvarı:** Indirmeleri engelleyebilir, izin verin
3. **Ağ Proxy:** Şirket ağındaysanız proxy ayarlarını kontrol edin
4. **Execution Policy:** PowerShell için gerekebilir

---

## 🆘 Yardım Alma

Script'lerle ilgili sorun yaşıyorsanız:

1. **`check-system.bat` çalıştırın** → Sisteminizi kontrol edin
2. **`setup.log` dosyasını inceleyin** → Hata mesajlarına bakın
3. **[KURULUM.md](KURULUM.md) okuyun** → Sorun giderme bölümü
4. **GitHub Issue açın** → `system-check.txt` ve `setup.log` ekleyin

---

## 📚 Ek Kaynaklar

- **Otomatik Kurulum:** [KURULUM.md](KURULUM.md)
- **Manuel Kurulum:** [INSTALLATION_TR.md](INSTALLATION_TR.md)
- **Kullanım Kılavuzu:** [USER_GUIDE_TR.md](USER_GUIDE_TR.md)
- **API Dökümantasyonu:** [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

---

**Versiyon:** 1.0  
**Son Güncelleme:** 2025-10-16  
**Geliştirici:** yusufyImz
