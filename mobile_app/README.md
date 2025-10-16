# Mobile App Connection Guide 📱

This guide explains how to connect mobile devices to Club M Star AutoInput for remote control.

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Connection Methods](#connection-methods)
- [Web Interface](#web-interface)
- [API Usage](#api-usage)
- [Mobile App (Future)](#mobile-app-future)
- [Troubleshooting](#troubleshooting)

## 🌟 Overview

Control Club M Star AutoInput from your mobile device:

- **Start/Stop/Pause** automation remotely
- **View real-time statistics** and performance metrics
- **Get AI Coach recommendations** on the go
- **Monitor system status** from anywhere on your network

## 🚀 Quick Start

### Step 1: Start the Server

1. Open Club M Star AutoInput on your computer
2. The mobile server starts automatically
3. Note the server URL displayed in the **📱 Mobil Kontrol** tab

### Step 2: Connect from Mobile

1. Ensure mobile device is on the **same WiFi network**
2. Open a web browser on your mobile device
3. Enter the server URL (e.g., `http://192.168.1.100:5000`)
4. You'll see the API documentation page

### Step 3: Control Remotely

Use the API endpoints to control the system:

```bash
# Start automation
http://192.168.1.100:5000/api/start

# Get statistics
http://192.168.1.100:5000/api/statistics

# Stop automation
http://192.168.1.100:5000/api/stop
```

## 🔌 Connection Methods

### 1. Same WiFi Network (Recommended)

**Requirements**:
- Computer and mobile device on same WiFi
- No firewall blocking port 5000

**Advantages**:
- Fast connection
- Low latency
- No internet required

**Setup**:
1. Connect both devices to same WiFi
2. Find computer's local IP:
   ```bash
   # Windows
   ipconfig
   
   # Look for "IPv4 Address" (e.g., 192.168.1.100)
   ```
3. Use IP in mobile browser

### 2. Hotspot Connection

**Requirements**:
- Computer creates WiFi hotspot
- Mobile connects to hotspot

**Setup**:
1. Enable hotspot on computer (Windows Settings > Network & Internet > Mobile hotspot)
2. Connect mobile device to hotspot
3. Use hotspot IP (usually `192.168.137.1`)

### 3. VPN Connection (Advanced)

For remote access outside local network:

**Requirements**:
- VPN service (e.g., ZeroTier, Tailscale)
- Both devices on same VPN

**Setup**:
1. Install VPN on both devices
2. Connect to VPN
3. Use VPN IP address

## 🌐 Web Interface

### Browser-Based Control

Access the API through any mobile browser:

**URL**: `http://<server-ip>:5000`

**Recommended Browsers**:
- Safari (iOS)
- Chrome (Android)
- Firefox (Any)
- Edge (Windows Phone)

### Bookmarkable Actions

Create browser bookmarks for quick actions:

```
Bookmark: Start Automation
URL: http://192.168.1.100:5000/api/start

Bookmark: Stop Automation
URL: http://192.168.1.100:5000/api/stop

Bookmark: View Stats
URL: http://192.168.1.100:5000/api/statistics
```

### Mobile-Friendly Tips

1. **Add to Home Screen**: Save as app icon
2. **Use Request Method**: POST requests via JavaScript
3. **Auto-refresh**: Set timer for live updates

## 📱 API Usage

### Simple JavaScript Client

Create a simple HTML page for mobile control:

```html
<!DOCTYPE html>
<html>
<head>
    <title>M Star Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
        }
        button {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .start { background-color: #4CAF50; color: white; }
        .stop { background-color: #f44336; color: white; }
        .pause { background-color: #ff9800; color: white; }
        #stats {
            margin-top: 20px;
            padding: 15px;
            background-color: #f5f5f5;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>🎮 M Star Control</h1>
    
    <button class="start" onclick="startAutomation()">▶️ Start</button>
    <button class="pause" onclick="pauseAutomation()">⏸️ Pause</button>
    <button class="stop" onclick="stopAutomation()">⏹️ Stop</button>
    
    <div id="stats">
        <h3>Statistics</h3>
        <div id="statsContent">Loading...</div>
    </div>
    
    <script>
        const API_URL = 'http://192.168.1.100:5000';
        
        async function startAutomation() {
            const response = await fetch(`${API_URL}/api/start`, {
                method: 'POST'
            });
            const data = await response.json();
            alert(data.message || 'Started!');
        }
        
        async function pauseAutomation() {
            const response = await fetch(`${API_URL}/api/pause`, {
                method: 'POST'
            });
            const data = await response.json();
            alert(data.message || 'Paused!');
        }
        
        async function stopAutomation() {
            const response = await fetch(`${API_URL}/api/stop`, {
                method: 'POST'
            });
            const data = await response.json();
            alert(data.message || 'Stopped!');
        }
        
        async function updateStats() {
            try {
                const response = await fetch(`${API_URL}/api/statistics`);
                const stats = await response.json();
                
                document.getElementById('statsContent').innerHTML = `
                    <p>Accuracy: ${stats.game?.accuracy?.toFixed(1) || 0}%</p>
                    <p>Notes Hit: ${stats.game?.notes_hit || 0}</p>
                    <p>FPS: ${stats.game?.fps?.toFixed(1) || 0}</p>
                `;
            } catch (error) {
                document.getElementById('statsContent').innerHTML = 
                    '<p>Error loading stats</p>';
            }
        }
        
        // Update stats every 2 seconds
        setInterval(updateStats, 2000);
        updateStats();
    </script>
</body>
</html>
```

Save this as `mobile_control.html` and open in mobile browser.

### iOS Shortcuts

Create iOS shortcuts for quick control:

1. Open Shortcuts app
2. Create new shortcut
3. Add "Get Contents of URL" action
4. Set URL to API endpoint
5. Set method to POST
6. Add to Home Screen

### Android Tasker Integration

Use Tasker for automation:

1. Create new task
2. Add "HTTP Request" action
3. Configure API endpoint
4. Create widget for home screen

## 📱 Mobile App (Future)

A dedicated mobile app is planned with these features:

### Planned Features

- ✅ **Native UI**: Optimized for mobile
- ✅ **Push Notifications**: Get alerts
- ✅ **Live Dashboard**: Real-time stats
- ✅ **Quick Controls**: One-tap actions
- ✅ **Offline Mode**: Queue commands
- ✅ **Multiple Devices**: Control multiple computers

### Platforms

- **iOS**: iPhone, iPad
- **Android**: Phones, Tablets
- **Cross-platform**: React Native or Flutter

### Release Timeline

- **Q1 2024**: Android Beta
- **Q2 2024**: iOS Beta
- **Q3 2024**: Stable Release

### Join Beta Testing

Interested in beta testing? Contact:
- Email: yusufyilmazz@outlook.com.tr
- GitHub: [@yusufyImz](https://github.com/yusufyImz)

## 🔧 Troubleshooting

### Cannot Connect

**Problem**: Mobile device can't reach server

**Solutions**:
1. Check WiFi connection (same network?)
2. Verify IP address (use `ipconfig`)
3. Check firewall settings
4. Try port forwarding
5. Restart mobile server

### Slow Response

**Problem**: API responses are slow

**Solutions**:
1. Check network speed
2. Reduce update frequency
3. Use WiFi instead of mobile data
4. Close background apps

### CORS Errors

**Problem**: Browser shows CORS errors

**Solutions**:
1. Server has CORS enabled by default
2. Try different browser
3. Clear browser cache
4. Check server logs

### Connection Drops

**Problem**: Connection keeps dropping

**Solutions**:
1. Keep computer awake
2. Disable power saving on WiFi
3. Use static IP
4. Check router settings

## 🔒 Security Considerations

### Current Setup
- ⚠️ No authentication (local network only)
- ⚠️ HTTP only (not encrypted)
- ⚠️ Open to all devices on network

### Recommendations
1. **Use only on trusted networks**
2. **Enable Windows Firewall**
3. **Don't expose to internet**
4. **Consider VPN for remote access**

### Future Security
- 🔐 API Key authentication
- 🔐 HTTPS encryption
- 🔐 User accounts
- 🔐 Rate limiting

## 📞 Support

Need help with mobile connection?

- **GitHub Issues**: [Report a problem](https://github.com/yusufyImz/mstar-autoinput-ultimate/issues)
- **Email**: yusufyilmazz@outlook.com.tr
- **Documentation**: [API_DOCUMENTATION.md](../API_DOCUMENTATION.md)

## 📚 Additional Resources

- [API Documentation](../API_DOCUMENTATION.md)
- [User Guide](../USER_GUIDE_TR.md)
- [GitHub Repository](https://github.com/yusufyImz/mstar-autoinput-ultimate)

---

**Enjoy remote control! 🎮📱**
