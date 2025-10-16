# API Documentation 🔌

Complete API documentation for Club M Star AutoInput - Ultimate Edition Mobile API.

## 📋 Table of Contents

- [Overview](#overview)
- [Authentication](#authentication)
- [Base URL](#base-url)
- [Endpoints](#endpoints)
- [Response Format](#response-format)
- [Error Handling](#error-handling)
- [Examples](#examples)

## Overview

The Mobile API provides RESTful endpoints for remote control and monitoring of the Club M Star AutoInput system. The API is built with Flask and supports JSON requests and responses.

### Features

- Remote automation control (start/stop/pause/resume)
- Real-time statistics and performance metrics
- AI Coach analysis and recommendations
- Configuration management
- Health monitoring

### Base Information

- **Protocol**: HTTP/HTTPS
- **Data Format**: JSON
- **Port**: 5000 (default, configurable)
- **CORS**: Enabled for all origins

## Authentication

Currently, the API does not require authentication (designed for local network use). Future versions will include:

- API Key authentication
- OAuth 2.0 support
- Rate limiting
- IP whitelisting

## Base URL

```
http://<host-ip>:<port>
```

**Default**: `http://localhost:5000`

**Example**: `http://192.168.1.100:5000`

To find your host IP:
```bash
# Windows
ipconfig | findstr IPv4

# Linux/Mac
ifconfig | grep inet
```

## Endpoints

### 1. Root Endpoint

Get API information and available endpoints.

**Endpoint**: `GET /`

**Response**:
```json
{
  "name": "Club M Star AutoInput API",
  "version": "1.0.0",
  "endpoints": [
    "GET /api/status - Sistem durumu",
    "POST /api/start - Otomasyonu başlat",
    "..."
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/
```

---

### 2. Health Check

Check if the API server is running.

**Endpoint**: `GET /api/health`

**Response**:
```json
{
  "status": "healthy",
  "timestamp": 1699999999.123
}
```

**Example**:
```bash
curl http://localhost:5000/api/health
```

---

### 3. System Status

Get current system status.

**Endpoint**: `GET /api/status`

**Response**:
```json
{
  "server": "running",
  "timestamp": 1699999999.123,
  "automation_running": true,
  "automation_paused": false
}
```

**Fields**:
- `server`: Server status (always "running" if you get a response)
- `timestamp`: Unix timestamp
- `automation_running`: Whether automation is active
- `automation_paused`: Whether automation is paused

**Example**:
```bash
curl http://localhost:5000/api/status
```

---

### 4. Start Automation

Start the automation system.

**Endpoint**: `POST /api/start`

**Request**: No body required

**Response** (Success):
```json
{
  "success": true,
  "message": "Otomasyon başlatıldı"
}
```

**Response** (Error):
```json
{
  "error": "Game controller not available"
}
```

**Status Codes**:
- `200`: Success
- `500`: Internal server error
- `503`: Service unavailable

**Example**:
```bash
curl -X POST http://localhost:5000/api/start
```

---

### 5. Stop Automation

Stop the automation system.

**Endpoint**: `POST /api/stop`

**Request**: No body required

**Response** (Success):
```json
{
  "success": true,
  "message": "Otomasyon durduruldu"
}
```

**Example**:
```bash
curl -X POST http://localhost:5000/api/stop
```

---

### 6. Pause Automation

Pause the automation system.

**Endpoint**: `POST /api/pause`

**Request**: No body required

**Response** (Success):
```json
{
  "success": true,
  "message": "Otomasyon duraklatıldı"
}
```

**Example**:
```bash
curl -X POST http://localhost:5000/api/pause
```

---

### 7. Resume Automation

Resume paused automation.

**Endpoint**: `POST /api/resume`

**Request**: No body required

**Response** (Success):
```json
{
  "success": true,
  "message": "Otomasyon devam ettiriliyor"
}
```

**Example**:
```bash
curl -X POST http://localhost:5000/api/resume
```

---

### 8. Get Statistics

Get comprehensive statistics including game, performance, and progress data.

**Endpoint**: `GET /api/statistics`

**Response**:
```json
{
  "game": {
    "running": true,
    "paused": false,
    "notes_hit": 1234,
    "notes_missed": 56,
    "accuracy": 95.67,
    "session_duration_sec": 180.5,
    "avg_frame_time_ms": 16.7,
    "fps": 60.0
  },
  "performance": {
    "process_cpu": 18.5,
    "process_ram_mb": 856.3,
    "system_cpu": 35.2,
    "system_ram_percent": 45.6,
    "system_ram_available_gb": 12.4,
    "avg_fps": 59.8,
    "avg_latency_ms": 12.3,
    "frame_count": 10800
  },
  "progress": {
    "total_sessions": 25,
    "total_notes": 50000,
    "total_hits": 47500,
    "overall_accuracy": 95.0,
    "recent_avg_accuracy": 96.2,
    "recent_avg_timing": 11.5,
    "trend": "improving",
    "trend_emoji": "📈",
    "skill_level": "İleri"
  }
}
```

**Example**:
```bash
curl http://localhost:5000/api/statistics
```

---

### 9. Get Performance Metrics

Get detailed performance metrics.

**Endpoint**: `GET /api/performance`

**Response**:
```json
{
  "stats": {
    "process_cpu": 18.5,
    "process_ram_mb": 856.3,
    "system_cpu": 35.2,
    "system_ram_percent": 45.6,
    "system_ram_available_gb": 12.4,
    "avg_fps": 59.8,
    "avg_latency_ms": 12.3,
    "frame_count": 10800
  },
  "alerts": [
    "Yüksek CPU kullanımı: 85.2%"
  ],
  "suggestions": [
    "CPU kullanımını azaltmak için batch size'ı düşürmeyi deneyin"
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/api/performance
```

---

### 10. Get AI Coach Analysis

Get AI Coach performance analysis.

**Endpoint**: `GET /api/coach/analysis`

**Response**:
```json
{
  "total_sessions": 25,
  "total_notes": 50000,
  "total_hits": 47500,
  "overall_accuracy": 95.0,
  "recent_avg_accuracy": 96.2,
  "recent_avg_timing": 11.5,
  "trend": "improving",
  "trend_emoji": "📈",
  "skill_level": "İleri"
}
```

**Example**:
```bash
curl http://localhost:5000/api/coach/analysis
```

---

### 11. Get AI Coach Recommendations

Get personalized recommendations from AI Coach.

**Endpoint**: `GET /api/coach/recommendations`

**Response**:
```json
{
  "analysis": {
    "accuracy": 0.95,
    "timing_error": 12.5,
    "skill_level": "advanced",
    "improvement_trend": "improving",
    "weak_areas": [],
    "strong_areas": ["Yüksek doğruluk", "Mükemmel zamanlama"]
  },
  "recommendations": [
    "🌟 Mükemmel performans! Hız ve karmaşıklığı artırın.",
    "🏆 Zor modlara geçmeye hazırsınız.",
    "🎯 Mükemmel zamanlama hassasiyeti!",
    "🚀 İleri seviye: Karmaşık kombinasyonlara odaklanın."
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/api/coach/recommendations
```

---

### 12. Get Training Suggestions

Get training suggestions based on skill level.

**Endpoint**: `GET /api/coach/training`

**Response**:
```json
{
  "skill_level": "İleri",
  "suggestions": [
    "1. Hızlı tempo şarkılar (120-160 BPM)",
    "2. Karmaşık chord kombinasyonları",
    "3. Stream section'larda hız geliştirin",
    "4. Farklı zorluk seviyeleri deneyin",
    "5. 45+ dakika yoğun pratik"
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/api/coach/training
```

---

### 13. Get Configuration

Get current system configuration.

**Endpoint**: `GET /api/config`

**Response**:
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
  },
  "cloud": {
    "api_url": "https://api.mstar-sync.example.com",
    "sync_interval_sec": 300
  },
  "mobile": {
    "server_port": 5000,
    "enable_remote": true
  },
  "language": "tr"
}
```

**Example**:
```bash
curl http://localhost:5000/api/config
```

---

### 14. Update Configuration

Update system configuration (partial update supported).

**Endpoint**: `POST /api/config`

**Request**:
```json
{
  "game": {
    "timing_offset_ms": 60
  }
}
```

**Response** (Success):
```json
{
  "success": true,
  "message": "Yapılandırma güncellendi"
}
```

**Example**:
```bash
curl -X POST http://localhost:5000/api/config \
  -H "Content-Type: application/json" \
  -d '{"game": {"timing_offset_ms": 60}}'
```

---

## Response Format

### Success Response

```json
{
  "success": true,
  "message": "Operation completed",
  "data": { ... }
}
```

### Error Response

```json
{
  "error": "Error description",
  "code": "ERROR_CODE"
}
```

### Status Codes

- `200`: Success
- `400`: Bad Request
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

## Error Handling

### Common Errors

**Service Unavailable (503)**:
```json
{
  "error": "Game controller not available"
}
```

**Internal Server Error (500)**:
```json
{
  "error": "Internal processing error"
}
```

### Retry Strategy

For failed requests, implement exponential backoff:

```python
import time
import requests

def api_call_with_retry(url, max_retries=3):
    for i in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            if i < max_retries - 1:
                time.sleep(2 ** i)  # Exponential backoff
            else:
                raise
```

## Examples

### Python

```python
import requests

# Base URL
BASE_URL = "http://192.168.1.100:5000"

# Start automation
response = requests.post(f"{BASE_URL}/api/start")
print(response.json())

# Get statistics
response = requests.get(f"{BASE_URL}/api/statistics")
stats = response.json()
print(f"Accuracy: {stats['game']['accuracy']}%")

# Get recommendations
response = requests.get(f"{BASE_URL}/api/coach/recommendations")
recommendations = response.json()
for rec in recommendations.get('recommendations', []):
    print(rec)
```

### JavaScript (Browser)

```javascript
const BASE_URL = "http://192.168.1.100:5000";

// Start automation
fetch(`${BASE_URL}/api/start`, {
  method: 'POST'
})
  .then(response => response.json())
  .then(data => console.log(data));

// Get statistics
fetch(`${BASE_URL}/api/statistics`)
  .then(response => response.json())
  .then(stats => {
    console.log(`Accuracy: ${stats.game.accuracy}%`);
  });

// WebSocket for real-time updates (future feature)
// const ws = new WebSocket('ws://192.168.1.100:5000/ws');
```

### cURL

```bash
# Health check
curl http://localhost:5000/api/health

# Start automation
curl -X POST http://localhost:5000/api/start

# Get statistics
curl http://localhost:5000/api/statistics | jq '.game.accuracy'

# Update configuration
curl -X POST http://localhost:5000/api/config \
  -H "Content-Type: application/json" \
  -d '{"game": {"timing_offset_ms": 60}}'
```

### Mobile App Integration

```swift
// Swift (iOS)
func startAutomation() {
    let url = URL(string: "http://192.168.1.100:5000/api/start")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    
    URLSession.shared.dataTask(with: request) { data, response, error in
        if let data = data {
            let result = try? JSONDecoder().decode(Response.self, from: data)
            print(result?.message ?? "Success")
        }
    }.resume()
}
```

```kotlin
// Kotlin (Android)
fun getStatistics() {
    val client = OkHttpClient()
    val request = Request.Builder()
        .url("http://192.168.1.100:5000/api/statistics")
        .build()
    
    client.newCall(request).enqueue(object : Callback {
        override fun onResponse(call: Call, response: Response) {
            val json = response.body?.string()
            // Parse JSON and update UI
        }
        
        override fun onFailure(call: Call, e: IOException) {
            // Handle error
        }
    })
}
```

## Rate Limiting

Currently, there is no rate limiting. Future versions will implement:

- **Rate Limit**: 100 requests per minute per IP
- **Headers**: 
  - `X-RateLimit-Limit`: Maximum requests allowed
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Time when limit resets

## WebSocket Support (Planned)

Future versions will include WebSocket support for real-time updates:

```javascript
// Connect to WebSocket
const ws = new WebSocket('ws://192.168.1.100:5000/ws');

// Listen for updates
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Real-time update:', data);
};

// Send commands
ws.send(JSON.stringify({
  action: 'start_automation'
}));
```

## Security Considerations

### Current State
- No authentication (designed for local network)
- CORS enabled for all origins
- HTTP only (no HTTPS)

### Recommendations
- Use only on trusted local networks
- Enable firewall rules
- Consider VPN for remote access
- Future versions will add authentication

### Future Security Features
- API Key authentication
- JWT tokens
- HTTPS support
- IP whitelisting
- Rate limiting
- Request signing

## Support

For API questions or issues:

- **GitHub Issues**: [Report an issue](https://github.com/yusufyImz/mstar-autoinput-ultimate/issues)
- **Email**: yusufyilmazz@outlook.com.tr
- **Documentation**: [Main README](README.md)

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-16
