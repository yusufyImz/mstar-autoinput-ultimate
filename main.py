"""
Club M Star AutoInput - Ultimate Edition
Main application with Tkinter GUI
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
from typing import Optional

# Import project modules
from config_manager import ConfigManager
from ml_engine import MLEngine
from game_controller import GameController
from ai_coach import AICoach
from cloud_sync import CloudSync
from mobile_server import MobileServer
from performance_monitor import PerformanceMonitor


class MStarAutoInputGUI:
    """Main GUI application"""
    
    def __init__(self):
        """Initialize application"""
        self.root = tk.Tk()
        self.root.title("Club M Star AutoInput - Ultimate Edition")
        self.root.geometry("900x700")
        
        # Initialize components
        self.config_manager = ConfigManager()
        self.ml_engine = MLEngine(self.config_manager.config)
        self.game_controller = GameController(self.config_manager.config, self.ml_engine)
        self.ai_coach = AICoach()
        self.cloud_sync = CloudSync(self.config_manager.config)
        self.performance_monitor = PerformanceMonitor()
        self.mobile_server = MobileServer(
            self.config_manager.config,
            self.game_controller,
            self.performance_monitor,
            self.ai_coach
        )
        
        # State
        self.monitoring_active = False
        self.update_thread = None
        
        # Create UI
        self._create_ui()
        
        # Initialize ML model
        self._initialize_ml_model()
        
        # Start mobile server if enabled
        if self.config_manager.get('mobile.enable_remote', True):
            self.mobile_server.start()
    
    def _create_ui(self):
        """Create user interface"""
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create tabs
        self.dashboard_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)
        self.ai_coach_tab = ttk.Frame(self.notebook)
        self.cloud_sync_tab = ttk.Frame(self.notebook)
        self.mobile_control_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.dashboard_tab, text="📊 Gösterge Paneli")
        self.notebook.add(self.settings_tab, text="⚙️ Ayarlar")
        self.notebook.add(self.ai_coach_tab, text="🤖 AI Coach")
        self.notebook.add(self.cloud_sync_tab, text="☁️ Bulut Senkronizasyon")
        self.notebook.add(self.mobile_control_tab, text="📱 Mobil Kontrol")
        
        # Setup each tab
        self._setup_dashboard_tab()
        self._setup_settings_tab()
        self._setup_ai_coach_tab()
        self._setup_cloud_sync_tab()
        self._setup_mobile_control_tab()
    
    def _setup_dashboard_tab(self):
        """Setup dashboard tab"""
        # Control frame
        control_frame = ttk.LabelFrame(self.dashboard_tab, text="Kontroller", padding=10)
        control_frame.pack(fill='x', padx=10, pady=5)
        
        # Buttons
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(fill='x')
        
        self.start_btn = ttk.Button(
            btn_frame,
            text="▶️ Başlat",
            command=self._start_automation,
            width=15
        )
        self.start_btn.pack(side='left', padx=5)
        
        self.pause_btn = ttk.Button(
            btn_frame,
            text="⏸️ Duraklat",
            command=self._pause_automation,
            state='disabled',
            width=15
        )
        self.pause_btn.pack(side='left', padx=5)
        
        self.stop_btn = ttk.Button(
            btn_frame,
            text="⏹️ Durdur",
            command=self._stop_automation,
            state='disabled',
            width=15
        )
        self.stop_btn.pack(side='left', padx=5)
        
        # Status frame
        status_frame = ttk.LabelFrame(self.dashboard_tab, text="Durum", padding=10)
        status_frame.pack(fill='x', padx=10, pady=5)
        
        self.status_label = ttk.Label(status_frame, text="Durum: Hazır", font=('Arial', 10))
        self.status_label.pack(anchor='w')
        
        # Statistics frame
        stats_frame = ttk.LabelFrame(self.dashboard_tab, text="İstatistikler", padding=10)
        stats_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Stats labels
        self.accuracy_label = ttk.Label(stats_frame, text="Doğruluk: 0%")
        self.accuracy_label.pack(anchor='w', pady=2)
        
        self.notes_label = ttk.Label(stats_frame, text="Toplam Not: 0")
        self.notes_label.pack(anchor='w', pady=2)
        
        self.fps_label = ttk.Label(stats_frame, text="FPS: 0")
        self.fps_label.pack(anchor='w', pady=2)
        
        self.cpu_label = ttk.Label(stats_frame, text="CPU: 0%")
        self.cpu_label.pack(anchor='w', pady=2)
        
        self.ram_label = ttk.Label(stats_frame, text="RAM: 0 MB")
        self.ram_label.pack(anchor='w', pady=2)
    
    def _setup_settings_tab(self):
        """Setup settings tab"""
        # ML Settings
        ml_frame = ttk.LabelFrame(self.settings_tab, text="ML Ayarları", padding=10)
        ml_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(ml_frame, text="Cihaz:").grid(row=0, column=0, sticky='w', pady=2)
        self.device_var = tk.StringVar(value=self.config_manager.get('ml.device', 'cpu'))
        device_combo = ttk.Combobox(ml_frame, textvariable=self.device_var, 
                                     values=['cpu', 'cuda'], state='readonly', width=20)
        device_combo.grid(row=0, column=1, sticky='w', pady=2, padx=5)
        
        ttk.Label(ml_frame, text="Quantization:").grid(row=1, column=0, sticky='w', pady=2)
        self.quant_var = tk.BooleanVar(value=self.config_manager.get('ml.quantization', True))
        ttk.Checkbutton(ml_frame, variable=self.quant_var).grid(row=1, column=1, sticky='w', pady=2, padx=5)
        
        # Game Settings
        game_frame = ttk.LabelFrame(self.settings_tab, text="Oyun Ayarları", padding=10)
        game_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(game_frame, text="Şerit Sayısı:").grid(row=0, column=0, sticky='w', pady=2)
        self.lanes_var = tk.IntVar(value=self.config_manager.get('game.lanes', 9))
        lanes_spin = ttk.Spinbox(game_frame, from_=4, to=9, textvariable=self.lanes_var, width=20)
        lanes_spin.grid(row=0, column=1, sticky='w', pady=2, padx=5)
        
        ttk.Label(game_frame, text="Zamanlama Offset (ms):").grid(row=1, column=0, sticky='w', pady=2)
        self.offset_var = tk.IntVar(value=self.config_manager.get('game.timing_offset_ms', 50))
        offset_spin = ttk.Spinbox(game_frame, from_=0, to=200, textvariable=self.offset_var, width=20)
        offset_spin.grid(row=1, column=1, sticky='w', pady=2, padx=5)
        
        # Calibrate button
        calibrate_btn = ttk.Button(
            game_frame,
            text="Kalibre Et",
            command=self._calibrate_timing
        )
        calibrate_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Save button
        save_btn = ttk.Button(
            self.settings_tab,
            text="💾 Ayarları Kaydet",
            command=self._save_settings
        )
        save_btn.pack(pady=10)
    
    def _setup_ai_coach_tab(self):
        """Setup AI Coach tab"""
        # Progress frame
        progress_frame = ttk.LabelFrame(self.ai_coach_tab, text="İlerleme", padding=10)
        progress_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.progress_text = scrolledtext.ScrolledText(
            progress_frame,
            height=15,
            width=70,
            font=('Courier', 9)
        )
        self.progress_text.pack(fill='both', expand=True)
        
        # Recommendations frame
        rec_frame = ttk.LabelFrame(self.ai_coach_tab, text="Öneriler", padding=10)
        rec_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.recommendations_text = scrolledtext.ScrolledText(
            rec_frame,
            height=10,
            width=70,
            font=('Arial', 9)
        )
        self.recommendations_text.pack(fill='both', expand=True)
        
        # Update button
        update_btn = ttk.Button(
            self.ai_coach_tab,
            text="🔄 Güncelle",
            command=self._update_ai_coach_info
        )
        update_btn.pack(pady=5)
    
    def _setup_cloud_sync_tab(self):
        """Setup cloud sync tab"""
        # Status frame
        status_frame = ttk.LabelFrame(self.cloud_sync_tab, text="Durum", padding=10)
        status_frame.pack(fill='x', padx=10, pady=5)
        
        self.sync_status_label = ttk.Label(status_frame, text="Bağlantı durumu: Çevrimdışı")
        self.sync_status_label.pack(anchor='w', pady=2)
        
        # Controls
        control_frame = ttk.LabelFrame(self.cloud_sync_tab, text="İşlemler", padding=10)
        control_frame.pack(fill='x', padx=10, pady=5)
        
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack()
        
        ttk.Button(
            btn_frame,
            text="⬆️ Ayarları Yedekle",
            command=self._backup_settings
        ).pack(side='left', padx=5, pady=5)
        
        ttk.Button(
            btn_frame,
            text="⬇️ Ayarları Geri Yükle",
            command=self._restore_settings
        ).pack(side='left', padx=5, pady=5)
        
        ttk.Button(
            btn_frame,
            text="🔄 Skorları Senkronize Et",
            command=self._sync_scores
        ).pack(side='left', padx=5, pady=5)
        
        # Log
        log_frame = ttk.LabelFrame(self.cloud_sync_tab, text="Log", padding=10)
        log_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.sync_log_text = scrolledtext.ScrolledText(
            log_frame,
            height=20,
            width=70,
            font=('Courier', 9)
        )
        self.sync_log_text.pack(fill='both', expand=True)
    
    def _setup_mobile_control_tab(self):
        """Setup mobile control tab"""
        # Server info
        info_frame = ttk.LabelFrame(self.mobile_control_tab, text="Sunucu Bilgisi", padding=10)
        info_frame.pack(fill='x', padx=10, pady=5)
        
        server_info = self.mobile_server.get_server_info()
        
        self.mobile_status_label = ttk.Label(
            info_frame,
            text=f"Durum: {'Çalışıyor' if server_info['running'] else 'Durduruldu'}"
        )
        self.mobile_status_label.pack(anchor='w', pady=2)
        
        if server_info['url']:
            self.mobile_url_label = ttk.Label(
                info_frame,
                text=f"URL: {server_info['url']}",
                foreground='blue'
            )
            self.mobile_url_label.pack(anchor='w', pady=2)
        
        # API endpoints
        api_frame = ttk.LabelFrame(self.mobile_control_tab, text="API Endpoints", padding=10)
        api_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        api_text = scrolledtext.ScrolledText(
            api_frame,
            height=20,
            width=70,
            font=('Courier', 9)
        )
        api_text.pack(fill='both', expand=True)
        
        # Add API documentation
        api_docs = """
API Endpoints:

GET  /api/status             - Sistem durumu
POST /api/start              - Otomasyonu başlat
POST /api/stop               - Otomasyonu durdur
POST /api/pause              - Otomasyonu duraklat
POST /api/resume             - Otomasyonu devam ettir
GET  /api/statistics         - Tüm istatistikler
GET  /api/performance        - Performans metrikleri
GET  /api/coach/analysis     - AI Coach analizi
GET  /api/coach/recommendations - Öneriler
GET  /api/coach/training     - Antrenman önerileri
GET  /api/config             - Yapılandırma
POST /api/config             - Yapılandırma güncelle
GET  /api/health             - Sağlık kontrolü

Kullanım:
- Mobil cihazınızdan bu IP adresine bağlanın
- API endpoint'lerini kullanarak kontrol edin
- JSON formatında veri alışverişi yapın
        """
        api_text.insert('1.0', api_docs)
        api_text.config(state='disabled')
    
    def _initialize_ml_model(self):
        """Initialize ML model"""
        try:
            success = self.ml_engine.load_model()
            if success:
                self._log_message("ML modeli yüklendi")
            else:
                self._log_message("ML modeli yüklenemedi (yeni model oluşturuldu)")
        except Exception as e:
            self._log_message(f"ML model hatası: {e}")
    
    def _start_automation(self):
        """Start automation"""
        try:
            self.game_controller.start_automation()
            self.monitoring_active = True
            
            # Update UI
            self.start_btn.config(state='disabled')
            self.pause_btn.config(state='normal')
            self.stop_btn.config(state='normal')
            self.status_label.config(text="Durum: Çalışıyor ▶️")
            
            # Start monitoring thread
            self.update_thread = threading.Thread(target=self._update_loop, daemon=True)
            self.update_thread.start()
            
            self._log_message("Otomasyon başlatıldı")
            
        except Exception as e:
            messagebox.showerror("Hata", f"Otomasyon başlatılamadı: {e}")
    
    def _pause_automation(self):
        """Pause automation"""
        try:
            self.game_controller.pause_automation()
            self.status_label.config(text="Durum: Duraklatıldı ⏸️")
            self._log_message("Otomasyon duraklatıldı")
        except Exception as e:
            messagebox.showerror("Hata", f"Duraklama hatası: {e}")
    
    def _stop_automation(self):
        """Stop automation"""
        try:
            self.game_controller.stop_automation()
            self.monitoring_active = False
            
            # Update UI
            self.start_btn.config(state='normal')
            self.pause_btn.config(state='disabled')
            self.stop_btn.config(state='disabled')
            self.status_label.config(text="Durum: Durduruldu ⏹️")
            
            self._log_message("Otomasyon durduruldu")
            
        except Exception as e:
            messagebox.showerror("Hata", f"Durdurma hatası: {e}")
    
    def _update_loop(self):
        """Background update loop"""
        while self.monitoring_active:
            try:
                # Update statistics
                self._update_statistics()
                time.sleep(1)
            except Exception as e:
                print(f"Güncelleme hatası: {e}")
    
    def _update_statistics(self):
        """Update statistics display"""
        try:
            # Game statistics
            game_stats = self.game_controller.get_statistics()
            
            # Performance statistics
            perf_stats = self.performance_monitor.get_current_stats()
            
            # Update labels
            self.root.after(0, lambda: self.accuracy_label.config(
                text=f"Doğruluk: {game_stats.get('accuracy', 0):.1f}%"
            ))
            self.root.after(0, lambda: self.notes_label.config(
                text=f"Toplam Not: {game_stats.get('notes_hit', 0)}"
            ))
            self.root.after(0, lambda: self.fps_label.config(
                text=f"FPS: {game_stats.get('fps', 0):.1f}"
            ))
            self.root.after(0, lambda: self.cpu_label.config(
                text=f"CPU: {perf_stats.get('process_cpu', 0):.1f}%"
            ))
            self.root.after(0, lambda: self.ram_label.config(
                text=f"RAM: {perf_stats.get('process_ram_mb', 0):.1f} MB"
            ))
            
        except Exception as e:
            print(f"İstatistik güncelleme hatası: {e}")
    
    def _save_settings(self):
        """Save settings"""
        try:
            # Update config
            self.config_manager.set('ml.device', self.device_var.get())
            self.config_manager.set('ml.quantization', self.quant_var.get())
            self.config_manager.set('game.lanes', self.lanes_var.get())
            self.config_manager.set('game.timing_offset_ms', self.offset_var.get())
            
            # Save to file
            if self.config_manager.save_config():
                messagebox.showinfo("Başarılı", "Ayarlar kaydedildi")
                self._log_message("Ayarlar kaydedildi")
            else:
                messagebox.showerror("Hata", "Ayarlar kaydedilemedi")
                
        except Exception as e:
            messagebox.showerror("Hata", f"Kayıt hatası: {e}")
    
    def _calibrate_timing(self):
        """Calibrate timing"""
        try:
            messagebox.showinfo("Kalibrasyon", "Zamanlama kalibrasyonu başlatılıyor...\n10 saniye sürecek.")
            offset = self.game_controller.calibrate_timing(10)
            self.offset_var.set(int(offset))
            messagebox.showinfo("Başarılı", f"Önerilen offset: {offset:.0f} ms")
            self._log_message(f"Kalibrasyon tamamlandı: {offset:.0f} ms")
        except Exception as e:
            messagebox.showerror("Hata", f"Kalibrasyon hatası: {e}")
    
    def _update_ai_coach_info(self):
        """Update AI Coach information"""
        try:
            # Get progress report
            report = self.ai_coach.get_formatted_report()
            self.progress_text.delete('1.0', tk.END)
            self.progress_text.insert('1.0', report)
            
            # Get recommendations
            if self.ai_coach.performance_history:
                last_session = list(self.ai_coach.performance_history)[-1]
                analysis = self.ai_coach.analyze_performance(last_session)
                recommendations = self.ai_coach.get_recommendations(analysis)
                
                rec_text = "\n".join(recommendations)
                self.recommendations_text.delete('1.0', tk.END)
                self.recommendations_text.insert('1.0', rec_text)
            else:
                self.recommendations_text.delete('1.0', tk.END)
                self.recommendations_text.insert('1.0', "Henüz yeterli veri yok.\nOtomasyon çalıştırın ve performans verileri toplayın.")
            
            self._log_message("AI Coach bilgileri güncellendi")
            
        except Exception as e:
            messagebox.showerror("Hata", f"Güncelleme hatası: {e}")
    
    def _backup_settings(self):
        """Backup settings to cloud"""
        try:
            success = self.cloud_sync.backup_settings(self.config_manager.config)
            if success:
                self._log_sync("Ayarlar yedeklendi")
                messagebox.showinfo("Başarılı", "Ayarlar buluta yedeklendi")
            else:
                messagebox.showwarning("Uyarı", "Ayarlar sadece yerel olarak kaydedildi")
        except Exception as e:
            messagebox.showerror("Hata", f"Yedekleme hatası: {e}")
    
    def _restore_settings(self):
        """Restore settings from cloud"""
        try:
            settings = self.cloud_sync.restore_settings()
            if settings:
                self.config_manager.config = settings
                self.config_manager.save_config()
                self._log_sync("Ayarlar geri yüklendi")
                messagebox.showinfo("Başarılı", "Ayarlar geri yüklendi. Uygulamayı yeniden başlatın.")
            else:
                messagebox.showwarning("Uyarı", "Yedek bulunamadı")
        except Exception as e:
            messagebox.showerror("Hata", f"Geri yükleme hatası: {e}")
    
    def _sync_scores(self):
        """Sync scores"""
        try:
            # Get scores from game controller
            scores = []  # Would be populated from game data
            success = self.cloud_sync.sync_scores(scores)
            if success:
                self._log_sync("Skorlar senkronize edildi")
                messagebox.showinfo("Başarılı", "Skorlar senkronize edildi")
            else:
                messagebox.showwarning("Uyarı", "Skorlar sadece yerel olarak kaydedildi")
        except Exception as e:
            messagebox.showerror("Hata", f"Senkronizasyon hatası: {e}")
    
    def _log_message(self, message: str):
        """Log message to console"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def _log_sync(self, message: str):
        """Log message to sync tab"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.sync_log_text.insert(tk.END, log_entry)
        self.sync_log_text.see(tk.END)
    
    def run(self):
        """Run the application"""
        self.root.mainloop()
    
    def cleanup(self):
        """Cleanup on exit"""
        self.monitoring_active = False
        if self.game_controller.running:
            self.game_controller.stop_automation()
        if self.mobile_server.running:
            self.mobile_server.stop()


def main():
    """Main entry point"""
    try:
        app = MStarAutoInputGUI()
        app.run()
    except KeyboardInterrupt:
        print("\nUygulama kapatılıyor...")
    except Exception as e:
        print(f"Hata: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
