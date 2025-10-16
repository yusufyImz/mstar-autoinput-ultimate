"""
Configuration Manager for Club M Star AutoInput System
Handles JSON-based config storage, user preferences, and hardware detection
"""

import json
import os
import platform
import psutil
from typing import Dict, Any


class ConfigManager:
    """Manages application configuration and user preferences"""
    
    DEFAULT_CONFIG = {
        "hardware": {
            "cpu_threads": 2,
            "use_gpu": False,
            "cache_size_mb": 512,
            "batch_size": 16
        },
        "ml": {
            "model_path": "models/note_detector.pth",
            "quantization": True,
            "device": "cpu"
        },
        "game": {
            "lanes": 9,
            "timing_offset_ms": 50,
            "accuracy_threshold": 0.95
        },
        "cloud": {
            "api_url": "https://api.mstar-sync.example.com",
            "sync_interval_sec": 300
        },
        "mobile": {
            "server_port": 5000,
            "enable_remote": True
        },
        "language": "tr"
    }
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize configuration manager"""
        self.config_path = config_path
        self.config = self.load_config()
        
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                # Merge with defaults to ensure all keys exist
                return self._merge_configs(self.DEFAULT_CONFIG.copy(), config)
            except Exception as e:
                print(f"Yapılandırma yüklenirken hata: {e}")
                return self.DEFAULT_CONFIG.copy()
        else:
            return self.DEFAULT_CONFIG.copy()
    
    def save_config(self) -> bool:
        """Save current configuration to file"""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Yapılandırma kaydedilirken hata: {e}")
            return False
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """Get configuration value using dot notation (e.g., 'ml.device')"""
        keys = key_path.split('.')
        value = self.config
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key_path: str, value: Any) -> bool:
        """Set configuration value using dot notation"""
        keys = key_path.split('.')
        config = self.config
        try:
            for key in keys[:-1]:
                if key not in config:
                    config[key] = {}
                config = config[key]
            config[keys[-1]] = value
            return True
        except Exception as e:
            print(f"Yapılandırma ayarlanırken hata: {e}")
            return False
    
    def detect_hardware(self) -> Dict[str, Any]:
        """Auto-detect hardware specifications"""
        try:
            cpu_count = psutil.cpu_count(logical=True)
            memory = psutil.virtual_memory()
            
            hardware_info = {
                "cpu_name": platform.processor() or "Unknown",
                "cpu_cores": psutil.cpu_count(logical=False),
                "cpu_threads": cpu_count,
                "ram_gb": round(memory.total / (1024**3), 2),
                "platform": platform.system(),
                "platform_version": platform.version()
            }
            return hardware_info
        except Exception as e:
            print(f"Donanım algılanırken hata: {e}")
            return {}
    
    def optimize_for_hardware(self):
        """Auto-optimize settings based on detected hardware"""
        hw_info = self.detect_hardware()
        
        # Adjust thread count based on CPU
        cpu_threads = hw_info.get('cpu_threads', 2)
        optimal_threads = min(2, max(1, cpu_threads // 2))
        self.set('hardware.cpu_threads', optimal_threads)
        
        # Adjust batch size based on RAM
        ram_gb = hw_info.get('ram_gb', 8)
        if ram_gb >= 24:
            batch_size = 16
        elif ram_gb >= 16:
            batch_size = 8
        else:
            batch_size = 4
        self.set('hardware.batch_size', batch_size)
        
        # Save optimized config
        self.save_config()
    
    def backup_config(self, backup_path: str = "config.backup.json") -> bool:
        """Create backup of current configuration"""
        try:
            with open(backup_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Yedekleme hatası: {e}")
            return False
    
    def restore_config(self, backup_path: str = "config.backup.json") -> bool:
        """Restore configuration from backup"""
        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            self.save_config()
            return True
        except Exception as e:
            print(f"Geri yükleme hatası: {e}")
            return False
    
    def _merge_configs(self, default: Dict, custom: Dict) -> Dict:
        """Recursively merge custom config into default"""
        result = default.copy()
        for key, value in custom.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_configs(result[key], value)
            else:
                result[key] = value
        return result


if __name__ == "__main__":
    # Test configuration manager
    config = ConfigManager()
    print("Donanım Bilgisi:", config.detect_hardware())
    print("ML Cihaz:", config.get('ml.device'))
    config.optimize_for_hardware()
