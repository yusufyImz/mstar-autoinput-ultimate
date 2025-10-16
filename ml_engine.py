"""
Machine Learning Engine for Club M Star AutoInput System
CPU-optimized PyTorch-based note detection and pattern recognition
"""

import torch
import torch.nn as nn
import numpy as np
from typing import List, Dict, Tuple, Optional
import os
import time


class NoteDetectorModel(nn.Module):
    """Simple CNN model for note detection"""
    
    def __init__(self, num_lanes: int = 9):
        super(NoteDetectorModel, self).__init__()
        self.num_lanes = num_lanes
        
        # Simple CNN architecture optimized for CPU
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        
        self.pool = nn.MaxPool2d(2, 2)
        self.relu = nn.ReLU()
        
        # Fully connected layers
        self.fc1 = nn.Linear(64 * 4 * 4, 128)
        self.fc2 = nn.Linear(128, num_lanes * 2)  # position and confidence per lane
        
    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = self.pool(self.relu(self.conv3(x)))
        
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        
        # Reshape to (batch, lanes, 2) for position and confidence
        return x.view(-1, self.num_lanes, 2)


class MLEngine:
    """Machine Learning engine for note detection and pattern recognition"""
    
    def __init__(self, config: Dict):
        """Initialize ML engine with configuration"""
        self.config = config
        self.device = torch.device('cpu')  # CPU-only for this hardware
        self.num_lanes = config.get('game', {}).get('lanes', 9)
        
        # Model
        self.model = None
        self.model_loaded = False
        
        # Performance optimization
        self.use_quantization = config.get('ml', {}).get('quantization', True)
        self.batch_size = config.get('hardware', {}).get('batch_size', 16)
        
        # Caching
        self.pattern_cache = {}
        self.cache_size_mb = config.get('hardware', {}).get('cache_size_mb', 512)
        
        # Statistics
        self.inference_times = []
        self.predictions_count = 0
        
    def load_model(self, model_path: Optional[str] = None) -> bool:
        """Load or initialize the model"""
        try:
            if model_path is None:
                model_path = self.config.get('ml', {}).get('model_path', 'models/note_detector.pth')
            
            # Initialize model
            self.model = NoteDetectorModel(num_lanes=self.num_lanes)
            
            # Load weights if file exists
            if os.path.exists(model_path):
                state_dict = torch.load(model_path, map_location=self.device)
                self.model.load_state_dict(state_dict)
                print(f"Model yüklendi: {model_path}")
            else:
                print(f"Model dosyası bulunamadı, yeni model başlatıldı: {model_path}")
                # Create models directory if it doesn't exist
                os.makedirs(os.path.dirname(model_path) if os.path.dirname(model_path) else 'models', exist_ok=True)
            
            self.model.to(self.device)
            self.model.eval()
            
            # Apply quantization for CPU optimization
            if self.use_quantization:
                self.model = torch.quantization.quantize_dynamic(
                    self.model, {nn.Linear, nn.Conv2d}, dtype=torch.qint8
                )
                print("Model quantization uygulandı (CPU optimizasyonu)")
            
            # Set thread count for CPU optimization
            torch.set_num_threads(self.config.get('hardware', {}).get('cpu_threads', 2))
            
            self.model_loaded = True
            return True
            
        except Exception as e:
            print(f"Model yüklenirken hata: {e}")
            self.model_loaded = False
            return False
    
    def detect_notes(self, frame: np.ndarray) -> List[Dict]:
        """Detect notes in a frame"""
        if not self.model_loaded:
            return []
        
        try:
            start_time = time.time()
            
            # Preprocess frame
            input_tensor = self._preprocess_frame(frame)
            
            # Run inference
            with torch.no_grad():
                output = self.model(input_tensor)
            
            # Post-process output
            detections = self._postprocess_output(output)
            
            # Record inference time
            inference_time = (time.time() - start_time) * 1000  # ms
            self.inference_times.append(inference_time)
            if len(self.inference_times) > 100:
                self.inference_times.pop(0)
            
            self.predictions_count += 1
            
            return detections
            
        except Exception as e:
            print(f"Not algılama hatası: {e}")
            return []
    
    def recognize_pattern(self, note_sequence: List[Dict]) -> Dict:
        """Recognize pattern in note sequence"""
        try:
            # Create pattern signature
            pattern_sig = self._create_pattern_signature(note_sequence)
            
            # Check cache
            if pattern_sig in self.pattern_cache:
                return self.pattern_cache[pattern_sig]
            
            # Analyze pattern
            pattern_info = {
                'type': self._classify_pattern(note_sequence),
                'difficulty': self._estimate_difficulty(note_sequence),
                'bpm': self._estimate_bpm(note_sequence),
                'density': len(note_sequence)
            }
            
            # Cache result
            self.pattern_cache[pattern_sig] = pattern_info
            
            return pattern_info
            
        except Exception as e:
            print(f"Pattern tanıma hatası: {e}")
            return {'type': 'unknown', 'difficulty': 0, 'bpm': 0, 'density': 0}
    
    def predict_difficulty(self, notes: List[Dict]) -> float:
        """Predict difficulty level (0-10)"""
        if not notes:
            return 0.0
        
        # Simple difficulty estimation based on note density and patterns
        density_score = min(len(notes) / 100.0, 1.0) * 3.0
        
        # Check for complex patterns
        pattern_score = 0.0
        for i in range(len(notes) - 1):
            if abs(notes[i]['lane'] - notes[i+1]['lane']) > 3:
                pattern_score += 0.1
        pattern_score = min(pattern_score, 4.0)
        
        # Timing complexity
        timing_score = 0.0
        if len(notes) > 1:
            avg_interval = np.mean([notes[i+1]['time'] - notes[i]['time'] 
                                   for i in range(len(notes) - 1)])
            if avg_interval < 100:  # Fast notes
                timing_score = 3.0
            elif avg_interval < 200:
                timing_score = 2.0
            else:
                timing_score = 1.0
        
        total_difficulty = density_score + pattern_score + timing_score
        return min(total_difficulty, 10.0)
    
    def analyze_performance(self, actual_hits: List[Dict], 
                          expected_notes: List[Dict]) -> Dict:
        """Analyze performance metrics"""
        if not expected_notes:
            return {'accuracy': 0, 'precision': 0, 'timing_error': 0}
        
        # Calculate accuracy
        correct_hits = 0
        timing_errors = []
        
        for expected in expected_notes:
            # Find matching hit
            matching_hit = None
            for hit in actual_hits:
                if (hit['lane'] == expected['lane'] and 
                    abs(hit['time'] - expected['time']) < 100):  # 100ms window
                    matching_hit = hit
                    break
            
            if matching_hit:
                correct_hits += 1
                timing_errors.append(abs(matching_hit['time'] - expected['time']))
        
        accuracy = correct_hits / len(expected_notes) if expected_notes else 0
        avg_timing_error = np.mean(timing_errors) if timing_errors else 0
        
        return {
            'accuracy': accuracy,
            'precision': correct_hits / len(actual_hits) if actual_hits else 0,
            'timing_error_ms': avg_timing_error,
            'total_notes': len(expected_notes),
            'hits': correct_hits,
            'misses': len(expected_notes) - correct_hits
        }
    
    def get_stats(self) -> Dict:
        """Get ML engine statistics"""
        avg_inference_time = (np.mean(self.inference_times) 
                            if self.inference_times else 0)
        
        return {
            'model_loaded': self.model_loaded,
            'predictions_count': self.predictions_count,
            'avg_inference_ms': avg_inference_time,
            'cache_size': len(self.pattern_cache),
            'device': str(self.device)
        }
    
    def _preprocess_frame(self, frame: np.ndarray) -> torch.Tensor:
        """Preprocess frame for model input"""
        # Resize to model input size (32x32)
        from PIL import Image
        img = Image.fromarray(frame)
        img = img.resize((32, 32))
        
        # Convert to tensor and normalize
        img_array = np.array(img).astype(np.float32) / 255.0
        tensor = torch.from_numpy(img_array).permute(2, 0, 1).unsqueeze(0)
        
        return tensor.to(self.device)
    
    def _postprocess_output(self, output: torch.Tensor) -> List[Dict]:
        """Post-process model output to detections"""
        detections = []
        output_np = output.cpu().numpy()[0]  # Get first batch
        
        threshold = self.config.get('game', {}).get('accuracy_threshold', 0.95)
        
        for lane_idx in range(self.num_lanes):
            position = output_np[lane_idx, 0]
            confidence = torch.sigmoid(torch.tensor(output_np[lane_idx, 1])).item()
            
            if confidence > threshold:
                detections.append({
                    'lane': lane_idx,
                    'position': float(position),
                    'confidence': float(confidence),
                    'time': time.time()
                })
        
        return detections
    
    def _create_pattern_signature(self, note_sequence: List[Dict]) -> str:
        """Create a unique signature for a note pattern"""
        if not note_sequence:
            return ""
        
        # Simple signature based on lane sequence
        lanes = [note['lane'] for note in note_sequence[:10]]  # First 10 notes
        return '-'.join(map(str, lanes))
    
    def _classify_pattern(self, note_sequence: List[Dict]) -> str:
        """Classify pattern type"""
        if len(note_sequence) < 2:
            return 'single'
        
        lanes = [note['lane'] for note in note_sequence]
        
        # Check for patterns
        if len(set(lanes)) == 1:
            return 'stream'
        elif all(lanes[i] < lanes[i+1] for i in range(len(lanes)-1)):
            return 'ascending'
        elif all(lanes[i] > lanes[i+1] for i in range(len(lanes)-1)):
            return 'descending'
        else:
            return 'mixed'
    
    def _estimate_difficulty(self, note_sequence: List[Dict]) -> float:
        """Estimate pattern difficulty"""
        return self.predict_difficulty(note_sequence)
    
    def _estimate_bpm(self, note_sequence: List[Dict]) -> float:
        """Estimate BPM from note sequence"""
        if len(note_sequence) < 2:
            return 0.0
        
        times = [note['time'] for note in note_sequence]
        intervals = [times[i+1] - times[i] for i in range(len(times)-1)]
        
        if not intervals:
            return 0.0
        
        avg_interval = np.mean(intervals)
        if avg_interval > 0:
            bpm = 60.0 / (avg_interval / 1000.0)  # Convert to BPM
            return bpm
        
        return 0.0


if __name__ == "__main__":
    # Test ML engine
    config = {
        'hardware': {'batch_size': 16, 'cpu_threads': 2, 'cache_size_mb': 512},
        'ml': {'quantization': True, 'device': 'cpu'},
        'game': {'lanes': 9, 'accuracy_threshold': 0.95}
    }
    
    engine = MLEngine(config)
    engine.load_model()
    
    print("ML Engine İstatistikleri:", engine.get_stats())
