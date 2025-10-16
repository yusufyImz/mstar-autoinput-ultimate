# 🧪 Script Test Rehberi

Bu belge, otomatik kurulum script'lerinin test edilmesi için kullanılabilir.

## ⚠️ Test Öncesi Uyarılar

**DİKKAT:** Test ortamında kullanın, production sistemde dikkatli olun!

### Test Ortamı Hazırlığı

1. **Sanal Makine Önerisi**
   - Windows 10/11 sanal makinesi kullanın
   - VirtualBox, VMware, veya Hyper-V
   - Snapshot alın (geri dönebilmek için)

2. **Temiz Sistem**
   - Python kurulu olmasın (tam test için)
   - Git kurulu olmasın (tam test için)
   - Veya mevcut kurulumları test edin

---

## 📋 Test Senaryoları

### Senaryo 1: Tamamen Boş Sistem

**Başlangıç Durumu:**
- ❌ Python yok
- ❌ Git yok
- ❌ Hiçbir paket yok

**Test Adımları:**

1. **Projeyi İndir**
   ```cmd
   GitHub'dan ZIP indir ve çıkar
   ```

2. **setup.bat'i Çalıştır**
   ```cmd
   SAĞ TIKLA → "Yönetici olarak çalıştır"
   ```

3. **Bekle ve Gözlemle**
   - [ ] Yönetici yetkisi istedi mi?
   - [ ] İnternet bağlantısı kontrolü yapıldı mı?
   - [ ] Disk alanı kontrol edildi mi?
   - [ ] Git indirilip kuruldu mu?
   - [ ] Python indirilip kuruldu mu?
   - [ ] PyTorch kuruldu mu?
   - [ ] Tüm paketler yüklendi mi?
   - [ ] Klasörler oluşturuldu mu?
   - [ ] setup.log dosyası oluşturuldu mu?

4. **Kurulum Sonrası Kontrol**
   ```cmd
   git --version
   python --version
   pip list
   ```

5. **Programı Başlat**
   ```cmd
   quick-start.bat (çift tıkla)
   ```

**Beklenen Sonuç:**
- ✅ Kurulum başarılı
- ✅ GUI açılıyor
- ✅ Tüm özellikler çalışıyor

**Toplam Süre:** ~15-20 dakika

---

### Senaryo 2: Python ve Git Kurulu

**Başlangıç Durumu:**
- ✅ Python 3.11+ kurulu
- ✅ Git kurulu
- ❌ Paketler yok

**Test Adımları:**

1. **install-python-packages.bat Çalıştır**
   ```cmd
   Çift tıkla
   "E" tuşuna bas
   ```

2. **Bekle ve Gözlemle**
   - [ ] pip güncellendi mi?
   - [ ] PyTorch kuruldu mu?
   - [ ] Her paket tek tek kuruldu mu?
   - [ ] İlerleme gösterildi mi (1/11, 2/11, ...)?
   - [ ] Doğrulama yapıldı mı?

3. **Kurulum Sonrası Kontrol**
   ```cmd
   python -c "import torch, cv2, flask"
   ```

4. **Programı Başlat**
   ```cmd
   quick-start.bat
   ```

**Beklenen Sonuç:**
- ✅ Paketler kuruldu
- ✅ GUI açılıyor

**Toplam Süre:** ~5-10 dakika

---

### Senaryo 3: Her Şey Kurulu

**Başlangıç Durumu:**
- ✅ Python 3.11+ kurulu
- ✅ Git kurulu
- ✅ Tüm paketler kurulu

**Test Adımları:**

1. **quick-start.bat Çalıştır**
   ```cmd
   Çift tıkla
   ```

2. **Gözlemle**
   - [ ] Python kontrolü yapıldı mı?
   - [ ] Klasörler kontrol edildi mi?
   - [ ] Paketler kontrol edildi mi?
   - [ ] Program başladı mı?

**Beklenen Sonuç:**
- ✅ Hemen açılıyor (5 saniye)

**Toplam Süre:** ~5 saniye

---

### Senaryo 4: Sistem Kontrolü

**Test Adımları:**

1. **check-system.bat Çalıştır**
   ```cmd
   Çift tıkla
   ```

2. **Bekle ve Gözlemle**
   - [ ] İşletim sistemi bilgisi alındı mı?
   - [ ] CPU bilgisi alındı mı?
   - [ ] RAM bilgisi alındı mı?
   - [ ] Disk bilgisi alındı mı?
   - [ ] Git kontrolü yapıldı mı?
   - [ ] Python kontrolü yapıldı mı?
   - [ ] Paket kontrolü yapıldı mı?
   - [ ] Klasör kontrolü yapıldı mı?
   - [ ] system-check.txt oluşturuldu mu?

3. **Raporu Kontrol Et**
   ```cmd
   notepad system-check.txt
   ```

**Beklenen Sonuç:**
- ✅ Detaylı rapor oluşturuldu
- ✅ Eksikler tespit edildi

**Toplam Süre:** ~15 saniye

---

### Senaryo 5: PowerShell Kurulum

**Test Adımları:**

1. **PowerShell'i Yönetici Olarak Aç**
   ```powershell
   Windows + X → "Windows PowerShell (Yönetici)"
   ```

2. **Execution Policy Ayarla** (gerekirse)
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **setup.ps1 Çalıştır**
   ```powershell
   cd [proje_klasörü]
   .\setup.ps1
   ```

4. **Bekle ve Gözlemle**
   - [ ] Renkli çıktı var mı?
   - [ ] Yönetici kontrolü yapıldı mı?
   - [ ] Kurulumlar başarılı mı?
   - [ ] Log dosyası oluşturuldu mu?

**Beklenen Sonuç:**
- ✅ setup.bat ile aynı işlevi görüyor
- ✅ Renkli ve temiz çıktı

**Toplam Süre:** ~15-20 dakika

---

## 🔍 Özel Test Durumları

### Test 1: Yönetici Yetkisi Olmadan

**Adımlar:**
```cmd
setup.bat'e NORMAL çift tıkla (yönetici değil)
```

**Beklenen:**
- ❌ "Yönetici yetkisi gerekli" mesajı
- ℹ️ Nasıl yönetici olarak çalıştırılacağı açıklanmalı

---

### Test 2: İnternet Bağlantısı Yok

**Adımlar:**
```cmd
İnternet bağlantısını kes
setup.bat'i çalıştır
```

**Beklenen:**
- ❌ "İnternet bağlantısı bulunamadı" mesajı
- ℹ️ Bağlantı kontrolü önerisi

---

### Test 3: Yetersiz Disk Alanı

**Adımlar:**
```cmd
Disk dolu bir sistem (3GB'dan az)
setup.bat'i çalıştır
```

**Beklenen:**
- ❌ "Yetersiz disk alanı" mesajı
- ℹ️ Ne kadar alan gerektiği belirtilmeli

---

### Test 4: Python PATH'de Değil

**Adımlar:**
```cmd
Python kurulu ama PATH'de yok
quick-start.bat'i çalıştır
```

**Beklenen:**
- ❌ "Python bulunamadı" mesajı
- ℹ️ Çözüm önerileri (PATH ekleme, setup.bat çalıştırma)

---

### Test 5: Eksik Paket

**Adımlar:**
```cmd
Bir paketi sil (örn: pip uninstall torch)
quick-start.bat'i çalıştır
```

**Beklenen:**
- ⚠️ "Bazı paketler yüklü değil" uyarısı
- ℹ️ install-python-packages.bat önerisi

---

### Test 6: requirements.txt Yok

**Adımlar:**
```cmd
requirements.txt'i sil veya yeniden adlandır
setup.bat'i çalıştır
```

**Beklenen:**
- ❌ "requirements.txt bulunamadı" mesajı
- ℹ️ Dosya nerede olmalı açıklaması

---

## 📊 Kontrol Listesi

### setup.bat Kontrolü

- [ ] Yönetici yetkisi kontrolü çalışıyor
- [ ] İnternet bağlantısı kontrolü çalışıyor
- [ ] Disk alanı kontrolü çalışıyor
- [ ] Winget otomatik tespit ediliyor
- [ ] Git kurulumu çalışıyor (winget varsa)
- [ ] Python kurulumu çalışıyor (winget varsa)
- [ ] pip güncelleme çalışıyor
- [ ] PyTorch CPU kurulumu çalışıyor
- [ ] Tüm paketler yükleniyor
- [ ] Klasörler oluşturuluyor
- [ ] setup.log dosyası oluşturuluyor
- [ ] Türkçe mesajlar görüntüleniyor
- [ ] Renkli çıktı çalışıyor
- [ ] Kullanıcıya başlatma seçeneği sunuluyor

### quick-start.bat Kontrolü

- [ ] Python kontrolü çalışıyor
- [ ] main.py kontrolü çalışıyor
- [ ] Klasör kontrolü çalışıyor
- [ ] Paket kontrolü çalışıyor
- [ ] Eksik paket durumunda kurulum önerisi
- [ ] Program başlatılıyor
- [ ] Hata durumunda yardım mesajı

### install-python-packages.bat Kontrolü

- [ ] Python ve pip kontrolü çalışıyor
- [ ] pip güncelleme çalışıyor
- [ ] requirements.txt kontrolü çalışıyor
- [ ] Kullanıcıdan onay istiyor
- [ ] PyTorch CPU versiyonu kuruluyor
- [ ] Her paket tek tek kuruluyor
- [ ] İlerleme gösterimi (1/11, 2/11, ...)
- [ ] Her paket doğrulanıyor
- [ ] Türkçe mesajlar görüntüleniyor

### check-system.bat Kontrolü

- [ ] İşletim sistemi bilgisi alınıyor
- [ ] CPU bilgisi alınıyor
- [ ] RAM bilgisi alınıyor
- [ ] Disk alanı bilgisi alınıyor
- [ ] Git kontrolü çalışıyor
- [ ] Python kontrolü çalışıyor
- [ ] pip kontrolü çalışıyor
- [ ] Tüm paketler kontrol ediliyor
- [ ] Klasör kontrolü çalışıyor
- [ ] config.json kontrolü çalışıyor
- [ ] system-check.txt oluşturuluyor
- [ ] Rapor açma seçeneği sunuluyor

### setup.ps1 Kontrolü

- [ ] Yönetici yetkisi zorunlu
- [ ] Renkli çıktı çalışıyor
- [ ] setup.bat ile aynı işlevler
- [ ] Log dosyası oluşturuluyor
- [ ] Türkçe mesajlar görüntüleniyor

---

## 🐛 Bilinen Sorunlar ve Testler

### Winget Yoksa

**Test:**
```cmd
winget olmayan bir sistemde setup.bat çalıştır
```

**Beklenen:**
- ⚠️ "Winget bulunamadı" uyarısı
- ℹ️ Manuel indirme linkleri
- ℹ️ Tarayıcıda indirme sayfası açılmalı

---

### Eski Python Versiyonu

**Test:**
```cmd
Python 3.9 kurulu sistem
setup.bat çalıştır
```

**Beklenen:**
- ⚠️ "Python sürümü çok eski" uyarısı
- ℹ️ Python 3.11+ kurulumu önerisi

---

### PyTorch İndirme Hatası

**Test:**
```cmd
PyTorch mirror'ı bloklu ağ
install-python-packages.bat çalıştır
```

**Beklenen:**
- ❌ "PyTorch kurulumu başarısız" mesajı
- ℹ️ Alternatif çözümler
- ℹ️ Manuel kurulum komutu

---

## 📝 Test Raporu Şablonu

Test sonuçlarınızı kaydedin:

```markdown
## Test Raporu

**Tarih:** [TARİH]
**Tester:** [İSİM]
**Sistem:** Windows [VERSİYON]

### Senaryo 1: Boş Sistem
- [ ] Başarılı / [ ] Başarısız
- Notlar: _____

### Senaryo 2: Python ve Git Kurulu
- [ ] Başarılı / [ ] Başarısız
- Notlar: _____

### Senaryo 3: Her Şey Kurulu
- [ ] Başarılı / [ ] Başarısız
- Notlar: _____

### Senaryo 4: Sistem Kontrolü
- [ ] Başarılı / [ ] Başarısız
- Notlar: _____

### Senaryo 5: PowerShell Kurulum
- [ ] Başarılı / [ ] Başarısız
- Notlar: _____

### Sorunlar:
1. _____
2. _____

### Öneriler:
1. _____
2. _____
```

---

## 🎯 Test Başarı Kriterleri

Testlerin başarılı sayılması için:

- ✅ Tüm senaryolar hatasız çalışmalı
- ✅ Türkçe mesajlar doğru görüntülenmeli
- ✅ Log dosyaları oluşturulmalı
- ✅ Hata durumlarında anlaşılır mesajlar
- ✅ Kullanıcı dostu arayüz
- ✅ 10-20 dakikada kurulum tamamlanmalı
- ✅ Program sorunsuz başlamalı

---

## 📞 Test Sonrası

Test sonuçlarını paylaşın:
1. GitHub Issue açın
2. Test raporunu ekleyin
3. Log dosyalarını ekleyin (setup.log, system-check.txt)
4. Ekran görüntüleri ekleyin

**Test ettiğiniz için teşekkürler! 🙏**
