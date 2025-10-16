# Club M Star AutoInput - Ultimate Edition 🎮

<div align="center">

**Tam Otomatik ML Destekli Ritim Oyunu Asistanı**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## 🆕 Yeni: Otomatik Kurulum Script'leri!

Artık **tek tıkla** kurulum yapabilirsiniz! 🚀

| Script | Açıklama | Kullanım |
|--------|----------|----------|
| 🎯 **setup.bat** | Ana kurulum script'i - Git, Python ve paketleri otomatik kurar | Yönetici olarak çalıştır |
| ⚡ **quick-start.bat** | Hızlı başlatma - Programı tek tıkla başlat | Çift tıkla |
| 📦 **install-python-packages.bat** | Sadece Python paketlerini yükler | Çift tıkla |
| 🔍 **check-system.bat** | Sistem kontrolü ve detaylı rapor oluşturur | Çift tıkla |
| 💻 **setup.ps1** | PowerShell kurulum script'i (alternatif) | Yönetici olarak çalıştır |

📖 **Detaylı rehber:** [KURULUM.md](KURULUM.md)

---

## 📋 İçindekiler

- [Otomatik Kurulum Script'leri](#-yeni-otomatik-kurulum-scriptleri)
- [Genel Bakış](#-genel-bakış)
- [Özellikler](#-özellikler)
- [Sistem Gereksinimleri](#-sistem-gereksinimleri)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Özellik Detayları](#-özellik-detayları)
- [Sorun Giderme](#-sorun-giderme)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

## 🎯 Genel Bakış

Club M Star AutoInput - Ultimate Edition, Club M Star ritim oyunu için geliştirilmiş kapsamlı bir ML destekli otomasyon sistemidir. CPU optimizasyonu ile Intel i7-7700 ve AMD RX 6400 donanımında mükemmel performans sunar.

### Neden Bu Proje?

- **🤖 Yapay Zeka Destekli**: PyTorch tabanlı not algılama ve performans analizi
- **☁️ Bulut Senkronizasyonu**: Ayarlarınızı ve skorlarınızı güvenle yedekleyin
- **📱 Mobil Kontrol**: Telefonunuzdan uzaktan kontrol edin
- **🎓 AI Coach**: Kişiselleştirilmiş gelişim önerileri
- **⚡ Yüksek Performans**: CPU optimizasyonu ile düşük kaynak kullanımı

## ✨ Özellikler

### 🎮 Temel Özellikler

- **Otomatik Not Algılama**: ML modeli ile yüksek doğrulukta not tanıma
- **9 Şerit Desteği**: Tüm zorluk seviyelerinde çalışır
- **Zamanlama Optimizasyonu**: Otomatik kalibrasyon sistemi
- **Gerçek Zamanlı İstatistikler**: FPS, doğruluk, CPU/RAM kullanımı

### 🤖 AI Coach Sistemi

- **Performans Analizi**: Detaylı oturum analizleri
- **Beceri Seviyesi Değerlendirmesi**: Başlangıç'tan Usta'ya kadar
- **Kişiselleştirilmiş Öneriler**: Türkçe öneriler ve antrenman planları
- **İlerleme Takibi**: Grafik ve istatistiklerle gelişiminizi izleyin
- **Zayıf Noktaları Belirleme**: Hangi alanlarda gelişmeniz gerektiğini gösterir

### ☁️ Bulut Senkronizasyonu

- **Ayar Yedekleme/Geri Yükleme**: Ayarlarınızı kaybetmeyin
- **Skor Senkronizasyonu**: Skorlarınızı güvenle saklayın
- **Profil Verisi**: Kullanıcı profilinizi senkronize edin
- **Çevrimdışı Mod**: İnternet olmadan da çalışır
- **Çakışma Çözümü**: Akıllı veri birleştirme

### 📱 Mobil Kontrol

- **RESTful API**: Tam özellikli API
- **Uzaktan Kontrol**: Başlat/durdur/duraklat
- **Canlı İstatistikler**: Gerçek zamanlı performans verileri
- **Yapılandırma Yönetimi**: Uzaktan ayar değiştirme
- **Durum İzleme**: Anlık sistem durumu

### ⚙️ Performans Özellikleri

- **CPU Optimizasyonu**: Intel i7-7700 için optimize edilmiş
- **Model Quantization**: Daha hızlı inference için
- **Akıllı Önbellekleme**: 512MB cache ile hızlı erişim
- **Çoklu İş Parçacığı**: 2 thread ile verimli işlem
- **Düşük RAM Kullanımı**: 2GB altında RAM kullanımı

## 💻 Sistem Gereksinimleri

### Donanım (Test Edilmiş Konfigürasyon)

- **CPU**: Intel Core i7-7700 (4 çekirdek, 8 thread, 3.6-4.2 GHz)
- **GPU**: AMD Radeon RX 6400 (4GB VRAM, RDNA 2) - Opsiyonel
- **RAM**: 28GB DDR4 2400MHz (minimum 8GB)
- **Depolama**: 1TB Corsair Force SSD (minimum 2GB boş alan)
- **Ekran**: 1920x1080 veya daha yüksek çözünürlük

### Yazılım

- **İşletim Sistemi**: Windows 10/11 (64-bit)
- **Python**: 3.11 veya üzeri
- **PyTorch**: 2.0.1+ (CPU versiyonu)
- **OpenCV**: 4.8.1+
- **Flask**: 3.0.0+

## 🚀 Kurulum

### ⚡ Tek Tıkla Otomatik Kurulum (Önerilen) 🆕

**En kolay yol!** Hiçbir teknik bilgiye ihtiyaç yok:

1. **Projeyi İndirin**
   - [ZIP olarak indir](https://github.com/yusufyImz/mstar-autoinput-ultimate/archive/refs/heads/main.zip) ve çıkar
   - VEYA: `git clone https://github.com/yusufyImz/mstar-autoinput-ultimate.git`

2. **Kurulum Script'ini Çalıştır**
   ```cmd
   setup.bat dosyasına SAĞ TIKLA → "Yönetici olarak çalıştır"
   ```

3. **Bekle** ☕ (10-15 dakika)
   - Git otomatik kurulur
   - Python 3.11+ otomatik kurulur
   - Tüm paketler otomatik yüklenir

4. **Başlat!** 🎉
   ```cmd
   quick-start.bat (çift tıkla)
   ```

**Otomatik kurulum script'i şunları yapar:**
- ✅ Sistem kontrolü (RAM, disk alanı, internet)
- ✅ Git kurulumu (gerekiyorsa)
- ✅ Python 3.11+ kurulumu (gerekiyorsa)
- ✅ Tüm Python paketlerini yükleme
- ✅ Klasör yapısını oluşturma
- ✅ Detaylı log tutma

📖 **Detaylı kurulum rehberi:** [KURULUM.md](KURULUM.md)

---

### 🛠️ Manuel Kurulum

Otomatik kurulumu tercih etmiyorsanız:

1. **Python Kurulumu**
   ```bash
   # Python 3.11+ yükleyin: https://www.python.org/downloads/
   python --version  # Kontrol edin
   ```

2. **Projeyi İndirin**
   ```bash
   git clone https://github.com/yusufyImz/mstar-autoinput-ultimate.git
   cd mstar-autoinput-ultimate
   ```

3. **Bağımlılıkları Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

4. **Uygulamayı Başlatın**
   ```bash
   python main.py
   ```

### 📚 Ek Kaynaklar

- **Otomatik Kurulum:** [KURULUM.md](KURULUM.md) - Tek tıkla kurulum rehberi
- **Manuel Kurulum:** [INSTALLATION_TR.md](INSTALLATION_TR.md) - Detaylı adım adım kurulum
- **Kullanım Kılavuzu:** [USER_GUIDE_TR.md](USER_GUIDE_TR.md) - Özellikler ve kullanım

## 📖 Kullanım

### İlk Başlatma

1. **Uygulamayı Başlatın**: `python main.py`
2. **Ayarları Yapın**: ⚙️ Ayarlar sekmesinden yapılandırın
3. **Kalibre Edin**: Zamanlama offset'ini kalibre edin
4. **Başlatın**: ▶️ Başlat düğmesine tıklayın

### Temel Kullanım

```bash
# Ana uygulamayı başlat
python main.py

# Sadece mobil sunucuyu başlat
python mobile_server.py

# Yapılandırmayı test et
python config_manager.py

# ML engine'i test et
python ml_engine.py
```

### GUI Kullanımı

1. **📊 Gösterge Paneli**: 
   - Otomasyonu başlatın/durdurun
   - İstatistikleri görüntüleyin
   - Sistem kaynaklarını izleyin

2. **⚙️ Ayarlar**:
   - ML ayarlarını yapılandırın
   - Oyun parametrelerini ayarlayın
   - Zamanlama offset'ini kalibre edin

3. **🤖 AI Coach**:
   - İlerleme raporunu görüntüleyin
   - Kişiselleştirilmiş öneriler alın
   - Beceri seviyenizi öğrenin

4. **☁️ Bulut Senkronizasyon**:
   - Ayarları yedekleyin/geri yükleyin
   - Skorları senkronize edin
   - Senkronizasyon loglarını görüntüleyin

5. **📱 Mobil Kontrol**:
   - Sunucu bilgilerini görün
   - API endpoint'lerini kontrol edin
   - Mobil bağlantı kurun

### Mobil Bağlantı

1. Uygulamayı başlatın
2. Mobil Kontrol sekmesinden IP adresini not edin
3. Mobil cihazınızda tarayıcıda bu adresi açın
4. API endpoint'lerini kullanarak kontrol edin

Detaylı kullanım kılavuzu için [USER_GUIDE_TR.md](USER_GUIDE_TR.md) dosyasına bakın.

## 🔧 Özellik Detayları

### ML Engine

CPU optimizasyonu ile PyTorch tabanlı not algılama:

- **Model**: Özel CNN mimarisi
- **Quantization**: INT8 quantization ile 2-3x hız artışı
- **Batch Processing**: 16 batch size ile verimli işlem
- **Caching**: Pattern önbellekleme ile hızlı tanıma

### AI Coach

Performans analizinize dayalı kişiselleştirilmiş öneriler:

- **5 Beceri Seviyesi**: Başlangıç, Orta, İleri, Uzman, Usta
- **Türkçe Öneriler**: Anlaşılır ve uygulanabilir öneriler
- **Antrenman Planları**: Seviyenize özel egzersizler
- **Zayıf Alan Analizi**: Geliştirilmesi gereken noktalar

### Bulut Senkronizasyonu

Verilerinizi güvenle yedekleyin:

- **Otomatik Yedekleme**: Periyodik otomatik yedekleme
- **Çevrimdışı Destek**: İnternet olmadan da çalışır
- **Çakışma Çözümü**: Akıllı veri birleştirme
- **Şifreleme**: Güvenli veri aktarımı (planlanan)

### Mobil API

RESTful API ile tam kontrol:

```bash
# Durum kontrolü
curl http://localhost:5000/api/status

# Otomasyonu başlat
curl -X POST http://localhost:5000/api/start

# İstatistikleri al
curl http://localhost:5000/api/statistics
```

API dokümantasyonu için [API_DOCUMENTATION.md](API_DOCUMENTATION.md) dosyasına bakın.

## 🔧 Yapılandırma

### config.json

```json
{
  "hardware": {
    "cpu_threads": 2,
    "use_gpu": false,
    "cache_size_mb": 512,
    "batch_size": 16
  },
  "ml": {
    "model_path": "models/note_detector.pth",
    "quantization": true,
    "device": "cpu"
  },
  "game": {
    "lanes": 9,
    "timing_offset_ms": 50,
    "accuracy_threshold": 0.95
  }
}
```

### Performans Ayarları

**Yüksek Performans İçin:**
- `cpu_threads`: 2-4
- `batch_size`: 16-32
- `cache_size_mb`: 512-1024
- `quantization`: true

**Düşük RAM İçin:**
- `batch_size`: 4-8
- `cache_size_mb`: 256
- `quantization`: true

## 🛠️ Sorun Giderme

### Yaygın Sorunlar

**1. Model Yüklenmiyor**
```
Çözüm: models/ klasörünü oluşturun veya yeni model eğitin
```

**2. Yüksek CPU Kullanımı**
```
Çözüm: cpu_threads ve batch_size değerlerini düşürün
```

**3. Mobil Sunucu Başlamıyor**
```
Çözüm: Port 5000'in kullanımda olmadığından emin olun
```

**4. Zamanlama Sorunları**
```
Çözüm: Zamanlama kalibrasyonu yapın (Ayarlar sekmesi)
```

**5. Düşük FPS**
```
Çözüm: Diğer uygulamaları kapatın, cache_size'ı artırın
```

### Log Dosyaları

```bash
# Ana log
logs/app.log

# Performans logları
logs/performance.log

# Hata logları
logs/error.log
```

### Destek

Sorun mu yaşıyorsunuz? 

- **GitHub Issues**: [Sorun bildirin](https://github.com/yusufyImz/mstar-autoinput-ultimate/issues)
- **Email**: yusufyilmazz@outlook.com.tr
- **Dokümantasyon**: [Wiki](https://github.com/yusufyImz/mstar-autoinput-ultimate/wiki)

## 📊 Performans Benchmarks

| Metrik | Değer |
|--------|-------|
| Ortalama FPS | 60+ |
| CPU Kullanımı | 15-25% |
| RAM Kullanımı | 800MB-1.5GB |
| Inference Süresi | 10-15ms |
| Doğruluk | 95%+ |

## 🗺️ Geliştirme Yol Haritası

- [x] Temel otomasyon sistemi
- [x] ML destekli not algılama
- [x] AI Coach sistemi
- [x] Bulut senkronizasyonu
- [x] Mobil kontrol API
- [ ] Web tabanlı dashboard
- [ ] Mobil uygulama (Android/iOS)
- [ ] Gelişmiş pattern tanıma
- [ ] Çoklu oyun desteği
- [ ] Topluluk özellikleri

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 Geliştirici

**Yusuf Yılmaz**
- GitHub: [@yusufyImz](https://github.com/yusufyImz)
- Email: yusufyilmazz@outlook.com.tr

## 🙏 Teşekkürler

- PyTorch ekibine harika ML framework'ü için
- OpenCV topluluğuna görüntü işleme araçları için
- Flask ekibine basit ve güçlü web framework'ü için

## 📝 Notlar

- Bu proje eğitim ve araştırma amaçlıdır
- Oyun kurallarına uygun kullanın
- Otomasyonu sorumlu bir şekilde kullanın
- Hesabınızın güvenliğinden siz sorumlusunuz

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with ❤️ in Turkey 🇹🇷

</div>