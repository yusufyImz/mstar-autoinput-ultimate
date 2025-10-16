# Kullanıcı Kılavuzu 📖

Club M Star AutoInput - Ultimate Edition için kapsamlı kullanım kılavuzu.

## 📋 İçindekiler

- [Başlarken](#-başlarken)
- [Gösterge Paneli](#-gösterge-paneli)
- [Ayarlar](#️-ayarlar)
- [AI Coach](#-ai-coach)
- [Bulut Senkronizasyon](#️-bulut-senkronizasyon)
- [Mobil Kontrol](#-mobil-kontrol)
- [İpuçları ve Püf Noktaları](#-ipuçları-ve-püf-noktaları)
- [Sık Sorulan Sorular](#-sık-sorulan-sorular)

## 🚀 Başlarken

### İlk Başlatma

1. **Uygulamayı Başlatın**
   ```bash
   python main.py
   ```

2. **Pencere Açılacak**
   - 5 sekme göreceksiniz
   - Her sekme farklı bir özellik içerir

3. **İlk Kurulum**
   - Ayarlar sekmesine gidin
   - Donanım optimizasyonu yapın
   - Zamanlama kalibrasyonu yapın

### Temel Kavramlar

- **Otomasyon**: Oyunu otomatik oynama sistemi
- **ML Engine**: Yapay zeka not algılama motoru
- **AI Coach**: Performans analizi ve öneriler
- **Cloud Sync**: Bulut yedekleme sistemi
- **Mobile API**: Uzaktan kontrol arayüzü

## 📊 Gösterge Paneli

Gösterge paneli, otomasyonu kontrol ettiğiniz ve istatistikleri izlediğiniz ana ekrandır.

### Kontroller

#### ▶️ Başlat Düğmesi

**Ne yapar**: Otomasyonu başlatır

**Nasıl kullanılır**:
1. Club M Star oyununu açın
2. Şarkı seçin ve başlatın
3. AutoInput'ta "Başlat" düğmesine tıklayın
4. Oyun otomatik olarak oynanacak

**Ne zaman kullanılır**:
- Yeni bir şarkı başlatırken
- Otomasyonu ilk kez aktif ederken

#### ⏸️ Duraklat Düğmesi

**Ne yapar**: Otomasyonu geçici olarak durdurur

**Nasıl kullanılır**:
1. Otomasyon çalışırken tıklayın
2. Sistem duraklatılır
3. "Duraklat" düğmesi "Devam Et" olur

**Ne zaman kullanılır**:
- Kısa bir ara verirken
- Ayar değişikliği yaparken
- Manuel kontrol almak isterken

#### ⏹️ Durdur Düğmesi

**Ne yapar**: Otomasyonu tamamen durdurur

**Nasıl kullanılır**:
1. Otomasyon çalışırken veya duraklatılmışken tıklayın
2. Sistem tamamen durur
3. İstatistikler sıfırlanır

**Ne zaman kullanılır**:
- Şarkı bittiğinde
- Tamamen çıkmak istediğinizde
- Sorun yaşandığında

### Durum Göstergesi

**Olası durumlar**:
- ✅ **Hazır**: Sistem başlamaya hazır
- ▶️ **Çalışıyor**: Otomasyon aktif
- ⏸️ **Duraklatıldı**: Geçici olarak durduruldu
- ⏹️ **Durduruldu**: Tamamen durdu
- ❌ **Hata**: Bir sorun oluştu

### İstatistikler

#### Doğruluk
- **Ne gösterir**: Vurduğunuz notların yüzdesi
- **İyi değer**: %85+
- **Mükemmel değer**: %95+

#### Toplam Not
- **Ne gösterir**: Vurulan toplam not sayısı
- **Kullanım**: İlerleme takibi için

#### FPS (Frames Per Second)
- **Ne gösterir**: Saniyedeki kare sayısı
- **Hedef**: 60+ FPS
- **Uyarı**: <30 FPS düşük performans

#### CPU Kullanımı
- **Ne gösterir**: İşlemci kullanım yüzdesi
- **Normal**: %15-25
- **Yüksek**: %50+ (optimizasyon gerekebilir)

#### RAM Kullanımı
- **Ne gösterir**: Bellek kullanımı (MB)
- **Normal**: 800MB-1.5GB
- **Yüksek**: >2GB (ayar değişikliği yapın)

## ⚙️ Ayarlar

Ayarlar sekmesinde sistem yapılandırmasını özelleştirebilirsiniz.

### ML Ayarları

#### Cihaz
- **Seçenekler**: CPU, CUDA
- **Önerilen**: CPU (bu donanım için)
- **Ne zaman CUDA**: Güçlü GPU varsa

#### Quantization
- **Ne yapar**: Modeli hızlandırır
- **Önerilen**: Açık (✓)
- **Kapatın eğer**: Doğruluk düşerse

### Oyun Ayarları

#### Şerit Sayısı
- **Varsayılan**: 9
- **Aralık**: 4-9
- **Ne zaman değiştirin**: Farklı mod oynarken

#### Zamanlama Offset (ms)
- **Ne yapar**: Tuş basma zamanlamasını ayarlar
- **Varsayılan**: 50ms
- **Artırın eğer**: Notlar erken basılıyorsa
- **Azaltın eğer**: Notlar geç basılıyorsa

### Kalibrasyon

**Zamanlama kalibrasyonu nasıl yapılır**:

1. **Kalibre Et** düğmesine tıklayın
2. 10 saniye sistem analiz edecek
3. Önerilen offset değerini göreceksiniz
4. Değer otomatik uygulanır
5. Test edin ve gerekirse manuel ayarlayın

**Ne zaman kalibrasyon yapmalısınız**:
- İlk kurulumda
- Performans düştüğünde
- Sistem değişikliğinden sonra
- Düzenli aralıklarla (haftada bir)

### Ayarları Kaydetme

1. Değişiklikleri yapın
2. **💾 Ayarları Kaydet** düğmesine tıklayın
3. Onay mesajı alacaksınız
4. Bazı değişiklikler yeniden başlatma gerektirebilir

## 🤖 AI Coach

AI Coach sekmesi, performansınızı analiz eder ve gelişim önerileri sunar.

### İlerleme Raporu

**Gösterilen bilgiler**:
- Toplam oturum sayısı
- Toplam not sayısı
- Başarılı hit sayısı
- Genel doğruluk yüzdesi
- Son 20 oturum ortalaması
- Ortalama zamanlama hatası
- Gelişim trendi
- Mevcut beceri seviyesi

**Beceri seviyeleri**:
1. **Başlangıç**: %0-65 doğruluk
2. **Orta**: %65-80 doğruluk
3. **İleri**: %80-90 doğruluk
4. **Uzman**: %90-95 doğruluk
5. **Usta**: %95+ doğruluk

### Öneriler

AI Coach size özel öneriler sunar:

**Öneriler şunları içerir**:
- Doğruluk geliştirme tavsiyeleri
- Zamanlama iyileştirme önerileri
- Beceri seviyesine göre hedefler
- Zayıf alanları güçlendirme ipuçları
- Antrenman planları

**Örnek öneriler**:

```
🎯 Doğruluk çok düşük. Daha yavaş parçalarla başlayın ve odaklanın.
💡 Not pozisyonlarını ezberlemek için önce sadece izleyin.
⏰ Zamanlama hatası yüksek. Kalibrasyon yapın.
📈 Doğruluğu artırmak için pratik yapın. Hedef: %70+
✨ İyi ilerleme! Daha zorlu parçaları deneyebilirsiniz.
```

### Bilgileri Güncelleme

**🔄 Güncelle** düğmesine tıklayarak:
- En son performans verilerini görüntüleyin
- Yeni öneriler alın
- İlerleme trendini kontrol edin

**Ne sıklıkta güncellemeliyim**:
- Her oturumdan sonra
- Yeni rekor kırdığınızda
- Haftalık ilerleme kontrolü için

### Antrenman Önerileri

Her beceri seviyesi için özel antrenman programları:

**Başlangıç Seviyesi**:
- Yavaş tempo şarkılar (60-80 BPM)
- Günde 15-20 dakika pratik
- Tek sütun notlarına odaklanma
- Not pozisyonlarını görsel öğrenme
- Metronom kullanımı

**Orta Seviye**:
- Orta tempo şarkılar (80-120 BPM)
- İki notlu kombinasyonlar
- Farklı pattern türleri
- Combo koruma odaklı
- Günde 30 dakika pratik

**İleri Seviye**:
- Hızlı tempo (120-160 BPM)
- Karmaşık chord kombinasyonları
- Stream bölümler
- Farklı zorluk seviyeleri
- 45+ dakika yoğun pratik

**Uzman/Usta**:
- En zorlu şarkılar
- Full combo hedefi
- Turnuva modu
- Record kırma
- Topluluk etkinlikleri

## ☁️ Bulut Senkronizasyon

Bulut Senkronizasyon sekmesi, verilerinizi yedeklemenizi sağlar.

### Durum

**Bağlantı durumları**:
- ✅ **Bağlı**: Bulut senkronizasyonu aktif
- ⚠️ **Çevrimdışı**: Yerel mod aktif
- ❌ **Hata**: Bağlantı sorunu

### İşlemler

#### ⬆️ Ayarları Yedekle

**Ne yapar**: Mevcut ayarları buluta yükler

**Nasıl kullanılır**:
1. Ayarlarınızı yapılandırın
2. "Ayarları Yedekle" düğmesine tıklayın
3. Onay mesajı bekleyin

**Ne zaman kullanılır**:
- Önemli değişikliklerden sonra
- Sistem formatlamadan önce
- Periyodik yedekleme için

#### ⬇️ Ayarları Geri Yükle

**Ne yapar**: Buluttan ayarları indirir

**Nasıl kullanılır**:
1. "Ayarları Geri Yükle" düğmesine tıklayın
2. Onay mesajı bekleyin
3. Uygulamayı yeniden başlatın

**Ne zaman kullanılır**:
- Yeni bilgisayara geçişte
- Ayar sorunlarında
- Varsayılan ayarlara dönmek için

#### 🔄 Skorları Senkronize Et

**Ne yapar**: Oyun skorlarını bulutla senkronize eder

**Nasıl kullanılır**:
1. Birkaç oyun oynayın
2. "Skorları Senkronize Et" düğmesine tıklayın
3. Senkronizasyon tamamlanmasını bekleyin

**Ne zaman kullanılır**:
- Önemli skorlardan sonra
- Cihaz değişikliklerinde
- Düzenli olarak (haftada bir)

### Log

Log alanı, senkronizasyon işlemlerinin kaydını tutar:

```
[14:30:25] Ayarlar yedeklendi
[14:31:10] Skorlar senkronize edildi
[14:32:05] Profil güncellendi
```

### Çevrimdışı Mod

İnternet bağlantısı yoksa:
- Sistem otomatik çevrimdışı moda geçer
- Tüm veriler yerel olarak saklanır
- Bağlantı geldiğinde otomatik senkronize olur

## 📱 Mobil Kontrol

Mobil Kontrol sekmesi, uzaktan erişim için API bilgilerini gösterir.

### Sunucu Bilgisi

**Gösterilen bilgiler**:
- Sunucu durumu (Çalışıyor/Durduruldu)
- Sunucu URL'si (örn: http://192.168.1.100:5000)
- Port numarası (varsayılan: 5000)

### Mobil Cihazdan Bağlanma

1. **Aynı Ağda Olun**
   - Bilgisayar ve mobil cihaz aynı WiFi'de olmalı

2. **URL'yi Kopyalayın**
   - Mobil Kontrol sekmesinden URL'yi not edin

3. **Tarayıcıda Açın**
   - Mobil cihazınızda tarayıcıyı açın
   - URL'yi girin
   - API dokümantasyonu görüntülenecek

4. **API Kullanın**
   - Endpoint'leri kullanarak kontrol edin
   - JSON formatında veri alın

### API Endpoint'leri

**Durum Kontrolü**:
```bash
GET /api/status
```

**Başlat/Durdur**:
```bash
POST /api/start
POST /api/stop
POST /api/pause
POST /api/resume
```

**İstatistikler**:
```bash
GET /api/statistics
GET /api/performance
```

**AI Coach**:
```bash
GET /api/coach/analysis
GET /api/coach/recommendations
GET /api/coach/training
```

Detaylı API dokümantasyonu: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

### Mobil Uygulama (Gelecek)

Gelecekte özel mobil uygulama gelecek:
- Android ve iOS desteği
- Push bildirimleri
- Canlı istatistikler
- Kolay kontroller

## 💡 İpuçları ve Püf Noktaları

### Performans İpuçları

1. **Yüksek FPS için**:
   - Diğer ağır programları kapatın
   - Oyunu tam ekran oynayın
   - SSD kullanın
   - Cache size'ı artırın

2. **Düşük RAM kullanımı için**:
   - Batch size'ı küçültün
   - Cache size'ı azaltın
   - Tarayıcı sekmelerini kapatın

3. **Düşük CPU kullanımı için**:
   - CPU threads'i azaltın
   - Quantization'ı açın
   - Gereksiz servisleri kapatın

### Doğruluk İpuçları

1. **Zamanlama**:
   - Düzenli kalibrasyon yapın
   - Offset'i küçük adımlarla ayarlayın
   - Test ederek optimize edin

2. **Görüntü Kalitesi**:
   - Oyunu yüksek çözünürlükte oynayın
   - Ekran parlaklığını ayarlayın
   - Windowed moddan kaçının

3. **Sistem Optimizasyonu**:
   - Windows güncelleme yapmayın oyun sırasında
   - Arka plan uygulamalarını kapatın
   - Virus taraması durdurun

### Genel İpuçları

1. **İlk Kullanım**:
   - Kolay şarkılarla başlayın
   - Ayarları test edin
   - Performansı izleyin

2. **Düzenli Bakım**:
   - Haftalık kalibrasyon
   - Aylık ayar kontrolü
   - Log dosyalarını temizleyin

3. **Sorun Önleme**:
   - Düzenli yedekleme yapın
   - Ayarları not edin
   - Güncellemeleri takip edin

## ❓ Sık Sorulan Sorular

### Genel Sorular

**S: Otomasyon yasal mı?**
C: Bu eğitim amaçlı bir projedir. Oyun kurallarına uygun kullanmanız önerilir.

**S: Hangi oyunlarda çalışır?**
C: Club M Star için tasarlanmıştır. Diğer ritim oyunları için uyarlama gerekebilir.

**S: GPU gerekli mi?**
C: Hayır, CPU optimizasyonu ile çalışır. GPU opsiyoneldir.

### Teknik Sorular

**S: Neden doğruluk düşük?**
C:
- Zamanlama offset'ini kalibre edin
- Ekran çözünürlüğünü kontrol edin
- Model eğitimi gerekebilir
- Sistem performansını kontrol edin

**S: FPS neden düşük?**
C:
- Diğer programları kapatın
- Batch size azaltın
- CPU threads azaltın
- Ekran çözünürlüğünü düşürün

**S: Mobil bağlanamıyorum?**
C:
- Aynı WiFi ağında olun
- Güvenlik duvarını kontrol edin
- Port 5000 açık olmalı
- IP adresini doğrulayın

**S: Bulut senkronizasyon çalışmıyor?**
C:
- İnternet bağlantınızı kontrol edin
- Çevrimdışı mod aktif olabilir
- Yerel yedekleme kullanın
- API endpoint'lerini kontrol edin

### Performans Sorular

**S: Çok fazla RAM kullanıyor?**
C:
- config.json'da batch_size azaltın
- cache_size_mb değerini düşürün
- Gereksiz programları kapatın

**S: CPU kullanımı çok yüksek?**
C:
- cpu_threads değerini azaltın
- quantization aktif olsun
- Diğer servisleri durdurun

**S: Gecikmeli çalışıyor?**
C:
- Zamanlama offset'ini artırın
- Sistem kaynaklarını kontrol edin
- Arka plan işlemlerini kapatın

## 📚 Ek Kaynaklar

- **Kurulum Kılavuzu**: [INSTALLATION_TR.md](INSTALLATION_TR.md)
- **API Dokümantasyonu**: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- **GitHub Deposu**: [mstar-autoinput-ultimate](https://github.com/yusufyImz/mstar-autoinput-ultimate)
- **Sorun Bildirimi**: [GitHub Issues](https://github.com/yusufyImz/mstar-autoinput-ultimate/issues)

## 📞 Destek

Yardıma mı ihtiyacınız var?

- **Email**: yusufyilmazz@outlook.com.tr
- **GitHub**: [@yusufyImz](https://github.com/yusufyImz)
- **Issues**: [Sorun bildirin](https://github.com/yusufyImz/mstar-autoinput-ultimate/issues)

---

**İyi kullanımlar! 🎮**
