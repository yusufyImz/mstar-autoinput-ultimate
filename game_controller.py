"""
Game Controller for Club M Star AutoInput System
Handles screen capture, note detection, and input automation
"""

import cv2
import numpy as np
import mss
import time
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
from typing import Dict, List, Optional, Tuple
import threading


class GameController:
    """Controls game automation including screen capture and input"""
    
    # Key mappings for lanes (customizable)
    DEFAULT_LANE_KEYS = ['s', 'd', 'f', 'space', 'j', 'k', 'l', ';', "'"]
    
    def __init__(self, config: Dict, ml_engine=None):
        """Initialize game controller"""
        self.config = config
        self.ml_engine = ml_engine
        
        # Input controllers
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        
        # Screen capture
        self.sct = mss.mss()
        self.capture_region = None
        
        # Game settings
        self.num_lanes = config.get('game', {}).get('lanes', 9)
        self.timing_offset = config.get('game', {}).get('timing_offset_ms', 50)
        self.lane_keys = self.DEFAULT_LANE_KEYS[:self.num_lanes]
        
        # State
        self.running = False
        self.paused = False
        self.automation_thread = None
        
        # Statistics
        self.notes_hit = 0
        self.notes_missed = 0
        self.total_timing_error = 0.0
        self.session_start_time = None
        
        # Performance
        self.frame_times = []
        self.last_frame = None
        
    def set_capture_region(self, x: int, y: int, width: int, height: int):
        """Set screen capture region"""
        self.capture_region = {
            'left': x,
            'top': y,
            'width': width,
            'height': height
        }
    
    def auto_detect_game_window(self) -> bool:
        """Auto-detect game window (placeholder - needs window detection)"""
        # Default to full screen for now
        monitor = self.sct.monitors[1]  # Primary monitor
        self.capture_region = {
            'left': monitor['left'],
            'top': monitor['top'],
            'width': monitor['width'],
            'height': monitor['height']
        }
        print(f"Oyun penceresi algılandı: {self.capture_region}")
        return True
    
    def capture_screen(self) -> Optional[np.ndarray]:
        """Capture screen region"""
        if not self.capture_region:
            self.auto_detect_game_window()
        
        try:
            start_time = time.time()
            
            # Capture screen
            screenshot = self.sct.grab(self.capture_region)
            frame = np.array(screenshot)
            
            # Convert BGRA to BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            
            # Record frame time
            frame_time = (time.time() - start_time) * 1000
            self.frame_times.append(frame_time)
            if len(self.frame_times) > 100:
                self.frame_times.pop(0)
            
            self.last_frame = frame
            return frame
            
        except Exception as e:
            print(f"Ekran yakalama hatası: {e}")
            return None
    
    def detect_notes_in_frame(self, frame: np.ndarray) -> List[Dict]:
        """Detect notes in captured frame"""
        if self.ml_engine:
            return self.ml_engine.detect_notes(frame)
        else:
            # Fallback: simple color-based detection
            return self._simple_note_detection(frame)
    
    def _simple_note_detection(self, frame: np.ndarray) -> List[Dict]:
        """Simple color-based note detection (fallback)"""
        detections = []
        
        # This is a placeholder - actual implementation would analyze
        # specific regions of the frame for note indicators
        height, width = frame.shape[:2]
        lane_width = width // self.num_lanes
        
        for lane in range(self.num_lanes):
            # Check specific region for each lane
            x_start = lane * lane_width
            x_end = (lane + 1) * lane_width
            
            # Check top portion for notes (where they typically appear)
            region = frame[0:height//3, x_start:x_end]
            
            # Simple brightness check (notes are usually bright)
            avg_brightness = np.mean(region)
            
            if avg_brightness > 150:  # Threshold
                detections.append({
                    'lane': lane,
                    'position': 0.0,
                    'confidence': avg_brightness / 255.0,
                    'time': time.time()
                })
        
        return detections
    
    def press_key(self, lane: int, duration_ms: int = 50):
        """Press key for specific lane"""
        if 0 <= lane < len(self.lane_keys):
            key = self.lane_keys[lane]
            try:
                self.keyboard.press(key)
                time.sleep(duration_ms / 1000.0)
                self.keyboard.release(key)
            except Exception as e:
                print(f"Tuş basma hatası (lane {lane}): {e}")
    
    def press_multiple_keys(self, lanes: List[int], duration_ms: int = 50):
        """Press multiple keys simultaneously (for chords)"""
        keys = [self.lane_keys[lane] for lane in lanes if 0 <= lane < len(self.lane_keys)]
        
        try:
            # Press all keys
            for key in keys:
                self.keyboard.press(key)
            
            # Hold
            time.sleep(duration_ms / 1000.0)
            
            # Release all keys
            for key in keys:
                self.keyboard.release(key)
                
        except Exception as e:
            print(f"Çoklu tuş basma hatası: {e}")
    
    def calibrate_timing(self, test_duration_sec: int = 10) -> float:
        """Calibrate timing offset by measuring system latency"""
        print(f"Zamanlama kalibrasyonu başlatılıyor ({test_duration_sec} saniye)...")
        
        latencies = []
        start_time = time.time()
        
        while time.time() - start_time < test_duration_sec:
            # Measure capture latency
            capture_start = time.time()
            frame = self.capture_screen()
            if frame is not None:
                capture_time = (time.time() - capture_start) * 1000
                latencies.append(capture_time)
            
            time.sleep(0.1)
        
        if latencies:
            avg_latency = np.mean(latencies)
            # Add some buffer for processing
            recommended_offset = avg_latency + 20
            print(f"Önerilen timing offset: {recommended_offset:.1f} ms")
            return recommended_offset
        else:
            print("Kalibrasyon başarısız, varsayılan değer kullanılıyor")
            return self.timing_offset
    
    def start_automation(self):
        """Start automation loop"""
        if self.running:
            print("Otomasyon zaten çalışıyor")
            return
        
        self.running = True
        self.session_start_time = time.time()
        self.notes_hit = 0
        self.notes_missed = 0
        self.total_timing_error = 0.0
        
        # Start automation in separate thread
        self.automation_thread = threading.Thread(target=self._automation_loop, daemon=True)
        self.automation_thread.start()
        
        print("Otomasyon başlatıldı")
    
    def stop_automation(self):
        """Stop automation loop"""
        self.running = False
        if self.automation_thread:
            self.automation_thread.join(timeout=2.0)
        print("Otomasyon durduruldu")
    
    def pause_automation(self):
        """Pause automation"""
        self.paused = True
        print("Otomasyon duraklatıldı")
    
    def resume_automation(self):
        """Resume automation"""
        self.paused = False
        print("Otomasyon devam ettiriliyor")
    
    def _automation_loop(self):
        """Main automation loop"""
        while self.running:
            if self.paused:
                time.sleep(0.1)
                continue
            
            try:
                # Capture frame
                frame = self.capture_screen()
                if frame is None:
                    continue
                
                # Detect notes
                notes = self.detect_notes_in_frame(frame)
                
                # Process detected notes
                for note in notes:
                    # Apply timing offset
                    timing_adjustment = self.timing_offset / 1000.0
                    time.sleep(timing_adjustment)
                    
                    # Press corresponding key
                    self.press_key(note['lane'])
                    self.notes_hit += 1
                
                # Small delay to prevent excessive CPU usage
                time.sleep(0.01)
                
            except Exception as e:
                print(f"Otomasyon döngüsü hatası: {e}")
                time.sleep(0.1)
    
    def get_statistics(self) -> Dict:
        """Get automation statistics"""
        total_notes = self.notes_hit + self.notes_missed
        accuracy = (self.notes_hit / total_notes * 100) if total_notes > 0 else 0
        
        session_duration = 0
        if self.session_start_time:
            session_duration = time.time() - self.session_start_time
        
        avg_frame_time = np.mean(self.frame_times) if self.frame_times else 0
        fps = 1000.0 / avg_frame_time if avg_frame_time > 0 else 0
        
        return {
            'running': self.running,
            'paused': self.paused,
            'notes_hit': self.notes_hit,
            'notes_missed': self.notes_missed,
            'accuracy': accuracy,
            'session_duration_sec': session_duration,
            'avg_frame_time_ms': avg_frame_time,
            'fps': fps
        }
    
    def get_accuracy(self) -> float:
        """Get current accuracy percentage"""
        stats = self.get_statistics()
        return stats['accuracy']
    
    def reset_statistics(self):
        """Reset all statistics"""
        self.notes_hit = 0
        self.notes_missed = 0
        self.total_timing_error = 0.0
        self.session_start_time = time.time() if self.running else None
        self.frame_times.clear()


if __name__ == "__main__":
    # Test game controller
    config = {
        'game': {
            'lanes': 9,
            'timing_offset_ms': 50,
            'accuracy_threshold': 0.95
        }
    }
    
    controller = GameController(config)
    print("Oyun kontrolcüsü başlatıldı")
    
    # Test screen capture
    frame = controller.capture_screen()
    if frame is not None:
        print(f"Ekran yakalandı: {frame.shape}")
    
    print("İstatistikler:", controller.get_statistics())
