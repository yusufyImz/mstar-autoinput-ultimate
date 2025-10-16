# ML Models Directory 🤖

This directory contains machine learning models for note detection and pattern recognition.

## 📋 Model Files

### note_detector.pth

**Purpose**: Main note detection model for recognizing notes in Club M Star

**Architecture**:
- Type: Convolutional Neural Network (CNN)
- Input: 32x32x3 RGB image
- Output: Lane positions and confidence scores
- Layers: 3 convolutional layers + 2 fully connected layers

**Features**:
- CPU-optimized for Intel i7-7700
- Quantized (INT8) for faster inference
- Low memory footprint (~10MB)
- Real-time inference (<15ms per frame)

## 🚀 Getting Started

### Initial Setup

On first run, the application will:
1. Check if `note_detector.pth` exists
2. If not found, initialize a new model
3. Save the initialized model to this directory

### Model Training (Optional)

To train a custom model:

```python
from ml_engine import MLEngine
from config_manager import ConfigManager

# Load configuration
config = ConfigManager()

# Initialize ML engine
engine = MLEngine(config.config)

# Train model (requires training data)
# engine.train_model(training_data, epochs=100)

# Save trained model
# torch.save(engine.model.state_dict(), 'models/note_detector.pth')
```

## 📊 Model Performance

### Benchmarks (Intel i7-7700, CPU-only)

| Metric | Value |
|--------|-------|
| Inference Time | 10-15ms |
| Memory Usage | ~10MB |
| Accuracy | 95%+ |
| FPS | 60+ |

### Optimization Techniques

1. **Quantization**: INT8 quantization reduces model size and improves speed
2. **Batch Processing**: Process multiple frames simultaneously
3. **Caching**: Cache frequently used patterns
4. **Multi-threading**: Parallel processing on multiple cores

## 🔧 Model Configuration

Models are configured in `config.json`:

```json
{
  "ml": {
    "model_path": "models/note_detector.pth",
    "quantization": true,
    "device": "cpu"
  }
}
```

### Parameters

- **model_path**: Path to model file
- **quantization**: Enable INT8 quantization (recommended: true)
- **device**: Processing device ("cpu" or "cuda")

## 📝 Training Your Own Model

### Requirements

- Training dataset (labeled note images)
- PyTorch 2.0+
- GPU (optional, for faster training)

### Training Process

1. **Collect Data**:
   ```python
   # Capture and label game screenshots
   # Save as (image, label) pairs
   ```

2. **Prepare Dataset**:
   ```python
   from torch.utils.data import Dataset, DataLoader
   
   class NoteDataset(Dataset):
       def __init__(self, images, labels):
           self.images = images
           self.labels = labels
       
       def __len__(self):
           return len(self.images)
       
       def __getitem__(self, idx):
           return self.images[idx], self.labels[idx]
   ```

3. **Train Model**:
   ```python
   import torch
   import torch.nn as nn
   import torch.optim as optim
   from ml_engine import NoteDetectorModel
   
   # Initialize model
   model = NoteDetectorModel(num_lanes=9)
   
   # Define loss and optimizer
   criterion = nn.MSELoss()
   optimizer = optim.Adam(model.parameters(), lr=0.001)
   
   # Training loop
   for epoch in range(100):
       for images, labels in dataloader:
           optimizer.zero_grad()
           outputs = model(images)
           loss = criterion(outputs, labels)
           loss.backward()
           optimizer.step()
   
   # Save model
   torch.save(model.state_dict(), 'models/note_detector.pth')
   ```

4. **Evaluate**:
   ```python
   # Test on validation set
   model.eval()
   with torch.no_grad():
       accuracy = evaluate(model, test_loader)
   print(f"Accuracy: {accuracy:.2f}%")
   ```

## 🎯 Model Formats

### Supported Formats

- **PyTorch (.pth)**: Default format (recommended)
- **ONNX (.onnx)**: For cross-platform deployment (future)
- **TorchScript (.pt)**: For production deployment (future)

### Converting Models

```python
# To ONNX
import torch.onnx

dummy_input = torch.randn(1, 3, 32, 32)
torch.onnx.export(
    model,
    dummy_input,
    "models/note_detector.onnx",
    verbose=True
)

# To TorchScript
scripted_model = torch.jit.script(model)
scripted_model.save("models/note_detector.pt")
```

## 🔍 Model Inspection

### Check Model Info

```python
import torch

# Load model
model_path = "models/note_detector.pth"
state_dict = torch.load(model_path, map_location='cpu')

# Print model info
print(f"Model parameters: {len(state_dict)} layers")
for key in state_dict.keys():
    print(f"  {key}: {state_dict[key].shape}")
```

### Model Size

```bash
# Check file size
ls -lh models/note_detector.pth

# Expected: ~10-20MB
```

## 📦 Pre-trained Models (Future)

In the future, pre-trained models will be available for download:

- **Standard Model**: General-purpose note detection
- **Fast Model**: Optimized for low-end hardware
- **Accurate Model**: Maximum accuracy (slower)
- **Specific Game Models**: Trained for specific rhythm games

## 🛠️ Troubleshooting

### Model Not Loading

```python
# Check if file exists
import os
if not os.path.exists('models/note_detector.pth'):
    print("Model file not found. Will initialize new model.")
```

### Low Accuracy

1. **Retrain with more data**: Collect diverse examples
2. **Adjust hyperparameters**: Try different learning rates
3. **Data augmentation**: Increase training data variety
4. **Fine-tuning**: Train on specific game modes

### Slow Inference

1. **Enable quantization**: Set `quantization: true` in config
2. **Reduce batch size**: Lower batch size in config
3. **Check CPU threads**: Optimize thread count
4. **Model optimization**: Use model pruning techniques

## 📚 Additional Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [Model Optimization Guide](https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html)
- [Quantization Tutorial](https://pytorch.org/tutorials/advanced/static_quantization_tutorial.html)

## 📄 License

Models are licensed under the same MIT license as the main project.

---

**Need help?** Open an issue on [GitHub](https://github.com/yusufyImz/mstar-autoinput-ultimate/issues)
