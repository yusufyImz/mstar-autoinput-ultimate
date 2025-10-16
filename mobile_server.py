"""
Mobile Server for Club M Star AutoInput System
Flask-based RESTful API for mobile control and monitoring
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
from typing import Dict, Optional
import time


class MobileServer:
    """Flask server for mobile control"""
    
    def __init__(self, config: Dict, game_controller=None, 
                 performance_monitor=None, ai_coach=None):
        """Initialize mobile server"""
        self.config = config
        self.game_controller = game_controller
        self.performance_monitor = performance_monitor
        self.ai_coach = ai_coach
        
        self.port = config.get('mobile', {}).get('server_port', 5000)
        self.enabled = config.get('mobile', {}).get('enable_remote', True)
        
        # Flask app
        self.app = Flask(__name__)
        CORS(self.app)  # Enable CORS for mobile apps
        
        # Server state
        self.running = False
        self.server_thread = None
        
        # Setup routes
        self._setup_routes()
    
    def _setup_routes(self):
        """Setup API routes"""
        
        @self.app.route('/api/status', methods=['GET'])
        def get_status():
            """Get system status"""
            status = {
                'server': 'running',
                'timestamp': time.time(),
                'automation_running': False,
                'automation_paused': False
            }
            
            if self.game_controller:
                stats = self.game_controller.get_statistics()
                status['automation_running'] = stats.get('running', False)
                status['automation_paused'] = stats.get('paused', False)
            
            return jsonify(status)
        
        @self.app.route('/api/start', methods=['POST'])
        def start_automation():
            """Start automation"""
            if not self.game_controller:
                return jsonify({'error': 'Game controller not available'}), 503
            
            try:
                self.game_controller.start_automation()
                return jsonify({
                    'success': True,
                    'message': 'Otomasyon başlatıldı'
                })
            except Exception as e:
                return jsonify({
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/stop', methods=['POST'])
        def stop_automation():
            """Stop automation"""
            if not self.game_controller:
                return jsonify({'error': 'Game controller not available'}), 503
            
            try:
                self.game_controller.stop_automation()
                return jsonify({
                    'success': True,
                    'message': 'Otomasyon durduruldu'
                })
            except Exception as e:
                return jsonify({
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/pause', methods=['POST'])
        def pause_automation():
            """Pause automation"""
            if not self.game_controller:
                return jsonify({'error': 'Game controller not available'}), 503
            
            try:
                self.game_controller.pause_automation()
                return jsonify({
                    'success': True,
                    'message': 'Otomasyon duraklatıldı'
                })
            except Exception as e:
                return jsonify({
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/resume', methods=['POST'])
        def resume_automation():
            """Resume automation"""
            if not self.game_controller:
                return jsonify({'error': 'Game controller not available'}), 503
            
            try:
                self.game_controller.resume_automation()
                return jsonify({
                    'success': True,
                    'message': 'Otomasyon devam ettiriliyor'
                })
            except Exception as e:
                return jsonify({
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/statistics', methods=['GET'])
        def get_statistics():
            """Get automation statistics"""
            stats = {}
            
            if self.game_controller:
                stats['game'] = self.game_controller.get_statistics()
            
            if self.performance_monitor:
                stats['performance'] = self.performance_monitor.get_current_stats()
            
            if self.ai_coach:
                stats['progress'] = self.ai_coach.get_progress_report()
            
            return jsonify(stats)
        
        @self.app.route('/api/performance', methods=['GET'])
        def get_performance():
            """Get performance metrics"""
            if not self.performance_monitor:
                return jsonify({'error': 'Performance monitor not available'}), 503
            
            stats = self.performance_monitor.get_current_stats()
            alerts = self.performance_monitor.get_alerts()
            suggestions = self.performance_monitor.get_optimization_suggestions()
            
            return jsonify({
                'stats': stats,
                'alerts': alerts,
                'suggestions': suggestions
            })
        
        @self.app.route('/api/coach/analysis', methods=['GET'])
        def get_coach_analysis():
            """Get AI coach analysis"""
            if not self.ai_coach:
                return jsonify({'error': 'AI coach not available'}), 503
            
            report = self.ai_coach.get_progress_report()
            
            return jsonify(report)
        
        @self.app.route('/api/coach/recommendations', methods=['GET'])
        def get_recommendations():
            """Get AI coach recommendations"""
            if not self.ai_coach:
                return jsonify({'error': 'AI coach not available'}), 503
            
            # Get recent analysis
            if self.ai_coach.performance_history:
                last_session = self.ai_coach.performance_history[-1]
                analysis = self.ai_coach.analyze_performance(last_session)
                recommendations = self.ai_coach.get_recommendations(analysis)
                
                return jsonify({
                    'analysis': analysis,
                    'recommendations': recommendations
                })
            else:
                return jsonify({
                    'message': 'Henüz yeterli veri yok'
                })
        
        @self.app.route('/api/coach/training', methods=['GET'])
        def get_training_suggestions():
            """Get training suggestions"""
            if not self.ai_coach:
                return jsonify({'error': 'AI coach not available'}), 503
            
            skill_level = self.ai_coach.assess_skill_level()
            suggestions = self.ai_coach.get_training_suggestions(skill_level)
            
            return jsonify({
                'skill_level': skill_level,
                'suggestions': suggestions
            })
        
        @self.app.route('/api/config', methods=['GET'])
        def get_config():
            """Get current configuration"""
            return jsonify(self.config)
        
        @self.app.route('/api/config', methods=['POST'])
        def update_config():
            """Update configuration (partial)"""
            try:
                new_config = request.get_json()
                # In production, would update config_manager
                return jsonify({
                    'success': True,
                    'message': 'Yapılandırma güncellendi'
                })
            except Exception as e:
                return jsonify({
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/health', methods=['GET'])
        def health_check():
            """Health check endpoint"""
            return jsonify({
                'status': 'healthy',
                'timestamp': time.time()
            })
        
        @self.app.route('/', methods=['GET'])
        def index():
            """API information"""
            return jsonify({
                'name': 'Club M Star AutoInput API',
                'version': '1.0.0',
                'endpoints': [
                    'GET /api/status - Sistem durumu',
                    'POST /api/start - Otomasyonu başlat',
                    'POST /api/stop - Otomasyonu durdur',
                    'POST /api/pause - Otomasyonu duraklat',
                    'POST /api/resume - Otomasyonu devam ettir',
                    'GET /api/statistics - İstatistikler',
                    'GET /api/performance - Performans metrikleri',
                    'GET /api/coach/analysis - AI Coach analizi',
                    'GET /api/coach/recommendations - Öneriler',
                    'GET /api/coach/training - Antrenman önerileri',
                    'GET /api/config - Yapılandırma',
                    'POST /api/config - Yapılandırma güncelle',
                    'GET /api/health - Sağlık kontrolü'
                ]
            })
    
    def start(self):
        """Start mobile server"""
        if self.running:
            print("Mobil sunucu zaten çalışıyor")
            return
        
        if not self.enabled:
            print("Mobil sunucu devre dışı")
            return
        
        self.running = True
        
        # Start server in separate thread
        self.server_thread = threading.Thread(
            target=self._run_server,
            daemon=True
        )
        self.server_thread.start()
        
        print(f"Mobil sunucu başlatıldı: http://0.0.0.0:{self.port}")
        print(f"API dokümantasyonu: http://localhost:{self.port}/")
    
    def stop(self):
        """Stop mobile server"""
        self.running = False
        print("Mobil sunucu durduruluyor...")
    
    def _run_server(self):
        """Run Flask server"""
        try:
            self.app.run(
                host='0.0.0.0',
                port=self.port,
                debug=False,
                use_reloader=False
            )
        except Exception as e:
            print(f"Sunucu hatası: {e}")
            self.running = False
    
    def get_server_info(self) -> Dict:
        """Get server information"""
        return {
            'running': self.running,
            'enabled': self.enabled,
            'port': self.port,
            'url': f'http://localhost:{self.port}' if self.running else None
        }


def create_standalone_server(port: int = 5000):
    """Create standalone server for testing"""
    config = {
        'mobile': {
            'server_port': port,
            'enable_remote': True
        }
    }
    
    server = MobileServer(config)
    return server


if __name__ == "__main__":
    # Test server
    server = create_standalone_server(5000)
    server.start()
    
    print("\nSunucu bilgisi:", server.get_server_info())
    print("\nTest için: http://localhost:5000/")
    print("Durdurmak için Ctrl+C basın\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSunucu kapatılıyor...")
        server.stop()
