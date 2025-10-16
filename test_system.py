"""
System Validation Test Script
Tests all core components of Club M Star AutoInput - Ultimate Edition
"""

import sys
import traceback


def test_module_imports():
    """Test that all modules can be imported"""
    print("=" * 60)
    print("TEST 1: Module Imports")
    print("=" * 60)
    
    modules = [
        'config_manager',
        'performance_monitor',
        'ml_engine',
        'ai_coach',
        'cloud_sync',
        'mobile_server',
    ]
    
    for module in modules:
        try:
            __import__(module)
            print(f"✓ {module}")
        except Exception as e:
            print(f"✗ {module}: {e}")
            return False
    
    print("\n✅ All modules imported successfully!\n")
    return True


def test_config_manager():
    """Test configuration manager"""
    print("=" * 60)
    print("TEST 2: Configuration Manager")
    print("=" * 60)
    
    try:
        from config_manager import ConfigManager
        
        config = ConfigManager()
        print(f"✓ ConfigManager initialized")
        
        # Test getting values
        language = config.get('language')
        print(f"✓ Language: {language}")
        
        device = config.get('ml.device')
        print(f"✓ ML Device: {device}")
        
        lanes = config.get('game.lanes')
        print(f"✓ Game Lanes: {lanes}")
        
        # Test hardware detection
        hw_info = config.detect_hardware()
        print(f"✓ Hardware detected: CPU={hw_info.get('cpu_threads')} threads, RAM={hw_info.get('ram_gb')}GB")
        
        print("\n✅ Configuration Manager working!\n")
        return True
        
    except Exception as e:
        print(f"\n✗ Configuration Manager failed: {e}\n")
        traceback.print_exc()
        return False


def test_ml_engine():
    """Test ML engine"""
    print("=" * 60)
    print("TEST 3: ML Engine")
    print("=" * 60)
    
    try:
        from ml_engine import MLEngine
        from config_manager import ConfigManager
        
        config = ConfigManager()
        engine = MLEngine(config.config)
        print(f"✓ ML Engine initialized")
        
        # Load model
        success = engine.load_model()
        print(f"✓ Model loaded: {success}")
        
        # Get stats
        stats = engine.get_stats()
        print(f"✓ Model stats:")
        print(f"  - Loaded: {stats['model_loaded']}")
        print(f"  - Device: {stats['device']}")
        print(f"  - Predictions: {stats['predictions_count']}")
        
        # Test difficulty prediction
        test_notes = [
            {'lane': 0, 'time': 0},
            {'lane': 1, 'time': 100},
            {'lane': 2, 'time': 200},
        ]
        difficulty = engine.predict_difficulty(test_notes)
        print(f"✓ Difficulty prediction: {difficulty:.1f}/10")
        
        print("\n✅ ML Engine working!\n")
        return True
        
    except Exception as e:
        print(f"\n✗ ML Engine failed: {e}\n")
        traceback.print_exc()
        return False


def test_ai_coach():
    """Test AI Coach"""
    print("=" * 60)
    print("TEST 4: AI Coach")
    print("=" * 60)
    
    try:
        from ai_coach import AICoach
        
        coach = AICoach()
        print(f"✓ AI Coach initialized")
        
        # Simulate sessions
        test_session = {
            'accuracy': 0.85,
            'timing_error_ms': 25,
            'total_notes': 200,
            'hits': 170
        }
        
        analysis = coach.analyze_performance(test_session)
        print(f"✓ Performance analyzed:")
        print(f"  - Accuracy: {analysis['accuracy']*100:.1f}%")
        print(f"  - Skill Level: {analysis['skill_level']}")
        print(f"  - Trend: {analysis['improvement_trend']}")
        
        # Get recommendations
        recommendations = coach.get_recommendations(analysis)
        print(f"✓ Generated {len(recommendations)} recommendations")
        
        # Get skill level
        skill_level = coach.assess_skill_level()
        print(f"✓ Skill Level: {skill_level}")
        
        print("\n✅ AI Coach working!\n")
        return True
        
    except Exception as e:
        print(f"\n✗ AI Coach failed: {e}\n")
        traceback.print_exc()
        return False


def test_cloud_sync():
    """Test cloud sync"""
    print("=" * 60)
    print("TEST 5: Cloud Sync")
    print("=" * 60)
    
    try:
        from cloud_sync import CloudSync
        from config_manager import ConfigManager
        
        config = ConfigManager()
        sync = CloudSync(config.config)
        print(f"✓ Cloud Sync initialized")
        
        # Test authentication
        success = sync.authenticate()
        print(f"✓ Authentication: {success}")
        
        # Test backup
        test_settings = {'test': 'value'}
        success = sync.backup_settings(test_settings)
        print(f"✓ Settings backup: {success}")
        
        # Get sync status
        status = sync.get_sync_status()
        print(f"✓ Sync status:")
        print(f"  - Enabled: {status['enabled']}")
        print(f"  - Offline: {status['offline_mode']}")
        print(f"  - User ID: {status['user_id']}")
        
        print("\n✅ Cloud Sync working!\n")
        return True
        
    except Exception as e:
        print(f"\n✗ Cloud Sync failed: {e}\n")
        traceback.print_exc()
        return False


def test_performance_monitor():
    """Test performance monitor"""
    print("=" * 60)
    print("TEST 6: Performance Monitor")
    print("=" * 60)
    
    try:
        from performance_monitor import PerformanceMonitor
        
        monitor = PerformanceMonitor()
        print(f"✓ Performance Monitor initialized")
        
        # Update stats
        stats = monitor.update()
        print(f"✓ Performance stats:")
        print(f"  - Process CPU: {stats.get('process_cpu', 0):.1f}%")
        print(f"  - Process RAM: {stats.get('process_ram_mb', 0):.1f} MB")
        print(f"  - System CPU: {stats.get('system_cpu', 0):.1f}%")
        
        # Record some frames
        for _ in range(5):
            monitor.record_frame()
        
        avg_fps = monitor.get_average_fps()
        print(f"✓ Average FPS: {avg_fps:.1f}")
        
        # Get alerts
        alerts = monitor.get_alerts()
        print(f"✓ Active alerts: {len(alerts)}")
        
        print("\n✅ Performance Monitor working!\n")
        return True
        
    except Exception as e:
        print(f"\n✗ Performance Monitor failed: {e}\n")
        traceback.print_exc()
        return False


def test_mobile_server():
    """Test mobile server"""
    print("=" * 60)
    print("TEST 7: Mobile Server")
    print("=" * 60)
    
    try:
        from mobile_server import MobileServer
        from config_manager import ConfigManager
        
        config = ConfigManager()
        server = MobileServer(config.config)
        print(f"✓ Mobile Server initialized")
        
        # Get server info
        info = server.get_server_info()
        print(f"✓ Server info:")
        print(f"  - Port: {info['port']}")
        print(f"  - Enabled: {info['enabled']}")
        
        print("\n✅ Mobile Server working!\n")
        return True
        
    except Exception as e:
        print(f"\n✗ Mobile Server failed: {e}\n")
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("CLUB M STAR AUTOINPUT - SYSTEM VALIDATION")
    print("=" * 60 + "\n")
    
    tests = [
        ("Module Imports", test_module_imports),
        ("Configuration Manager", test_config_manager),
        ("ML Engine", test_ml_engine),
        ("AI Coach", test_ai_coach),
        ("Cloud Sync", test_cloud_sync),
        ("Performance Monitor", test_performance_monitor),
        ("Mobile Server", test_mobile_server),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ {test_name} crashed: {e}\n")
            traceback.print_exc()
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print("\n" + "-" * 60)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 60 + "\n")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! System is ready to use!")
        return 0
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
