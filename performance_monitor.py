"""
Performance Monitor for Club M Star AutoInput System
Tracks CPU/RAM usage, FPS, latency, and resource optimization
"""

import psutil
import time
from typing import Dict, List, Optional
from collections import deque


class PerformanceMonitor:
    """Monitor system performance and resource usage"""
    
    def __init__(self, history_size: int = 100):
        """Initialize performance monitor"""
        self.history_size = history_size
        self.cpu_history = deque(maxlen=history_size)
        self.ram_history = deque(maxlen=history_size)
        self.fps_history = deque(maxlen=history_size)
        self.latency_history = deque(maxlen=history_size)
        
        self.process = psutil.Process()
        self.last_frame_time = time.time()
        self.frame_count = 0
        
        # Alert thresholds
        self.cpu_threshold = 80  # percent
        self.ram_threshold = 2048  # MB
        
    def update(self):
        """Update all performance metrics"""
        try:
            # CPU usage
            cpu_percent = self.process.cpu_percent(interval=0.1)
            self.cpu_history.append(cpu_percent)
            
            # RAM usage
            memory_info = self.process.memory_info()
            ram_mb = memory_info.rss / (1024 * 1024)
            self.ram_history.append(ram_mb)
            
            # System-wide metrics
            system_cpu = psutil.cpu_percent(interval=0.1)
            system_memory = psutil.virtual_memory()
            
            return {
                'process_cpu': cpu_percent,
                'process_ram_mb': ram_mb,
                'system_cpu': system_cpu,
                'system_ram_percent': system_memory.percent,
                'system_ram_available_gb': system_memory.available / (1024**3)
            }
        except Exception as e:
            print(f"Performans güncellenirken hata: {e}")
            return {}
    
    def record_frame(self):
        """Record frame timing for FPS calculation"""
        current_time = time.time()
        frame_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        
        if frame_time > 0:
            fps = 1.0 / frame_time
            self.fps_history.append(fps)
        
        self.frame_count += 1
    
    def record_latency(self, latency_ms: float):
        """Record latency measurement"""
        self.latency_history.append(latency_ms)
    
    def get_average_fps(self) -> float:
        """Get average FPS from history"""
        if not self.fps_history:
            return 0.0
        return sum(self.fps_history) / len(self.fps_history)
    
    def get_average_latency(self) -> float:
        """Get average latency from history"""
        if not self.latency_history:
            return 0.0
        return sum(self.latency_history) / len(self.latency_history)
    
    def get_current_stats(self) -> Dict[str, float]:
        """Get current performance statistics"""
        stats = self.update()
        
        stats.update({
            'avg_fps': self.get_average_fps(),
            'avg_latency_ms': self.get_average_latency(),
            'frame_count': self.frame_count
        })
        
        return stats
    
    def get_alerts(self) -> List[str]:
        """Check for performance issues and return alerts"""
        alerts = []
        
        if self.cpu_history:
            avg_cpu = sum(self.cpu_history) / len(self.cpu_history)
            if avg_cpu > self.cpu_threshold:
                alerts.append(f"Yüksek CPU kullanımı: {avg_cpu:.1f}%")
        
        if self.ram_history:
            avg_ram = sum(self.ram_history) / len(self.ram_history)
            if avg_ram > self.ram_threshold:
                alerts.append(f"Yüksek RAM kullanımı: {avg_ram:.1f} MB")
        
        if self.fps_history and len(self.fps_history) > 10:
            avg_fps = self.get_average_fps()
            if avg_fps < 30:
                alerts.append(f"Düşük FPS: {avg_fps:.1f}")
        
        if self.latency_history and len(self.latency_history) > 10:
            avg_latency = self.get_average_latency()
            if avg_latency > 50:
                alerts.append(f"Yüksek gecikme: {avg_latency:.1f} ms")
        
        return alerts
    
    def get_optimization_suggestions(self) -> List[str]:
        """Get optimization suggestions based on metrics"""
        suggestions = []
        
        if self.cpu_history:
            avg_cpu = sum(self.cpu_history) / len(self.cpu_history)
            if avg_cpu > 70:
                suggestions.append("CPU kullanımını azaltmak için batch size'ı düşürmeyi deneyin")
                suggestions.append("Diğer uygulamaları kapatmayı deneyin")
        
        if self.ram_history:
            avg_ram = sum(self.ram_history) / len(self.ram_history)
            if avg_ram > 1500:
                suggestions.append("RAM kullanımını azaltmak için cache boyutunu düşürmeyi deneyin")
        
        return suggestions
    
    def reset_stats(self):
        """Reset all statistics"""
        self.cpu_history.clear()
        self.ram_history.clear()
        self.fps_history.clear()
        self.latency_history.clear()
        self.frame_count = 0
        self.last_frame_time = time.time()
    
    def get_summary_report(self) -> str:
        """Generate a summary report of performance metrics"""
        stats = self.get_current_stats()
        alerts = self.get_alerts()
        suggestions = self.get_optimization_suggestions()
        
        report = "=== Performans Raporu ===\n\n"
        report += f"CPU Kullanımı: {stats.get('process_cpu', 0):.1f}%\n"
        report += f"RAM Kullanımı: {stats.get('process_ram_mb', 0):.1f} MB\n"
        report += f"Ortalama FPS: {stats.get('avg_fps', 0):.1f}\n"
        report += f"Ortalama Gecikme: {stats.get('avg_latency_ms', 0):.1f} ms\n"
        report += f"Toplam Kare: {stats.get('frame_count', 0)}\n\n"
        
        if alerts:
            report += "Uyarılar:\n"
            for alert in alerts:
                report += f"  - {alert}\n"
            report += "\n"
        
        if suggestions:
            report += "Optimizasyon Önerileri:\n"
            for suggestion in suggestions:
                report += f"  - {suggestion}\n"
        
        return report


if __name__ == "__main__":
    # Test performance monitor
    monitor = PerformanceMonitor()
    
    for i in range(5):
        stats = monitor.update()
        print(f"Test {i+1}:", stats)
        monitor.record_frame()
        time.sleep(0.1)
    
    print("\n" + monitor.get_summary_report())
