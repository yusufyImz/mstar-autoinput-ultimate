"""
AI Coach for Club M Star AutoInput System
Provides performance analysis, skill assessment, and personalized recommendations in Turkish
"""

import time
from typing import Dict, List, Tuple
import numpy as np
from collections import deque


class AICoach:
    """AI-powered coaching system for performance improvement"""
    
    # Skill levels in Turkish
    SKILL_LEVELS = {
        'beginner': 'Başlangıç',
        'intermediate': 'Orta',
        'advanced': 'İleri',
        'expert': 'Uzman',
        'master': 'Usta'
    }
    
    def __init__(self):
        """Initialize AI Coach"""
        self.performance_history = deque(maxlen=100)
        self.session_data = []
        self.weak_points = {}
        self.strengths = {}
        
        # Tracking metrics
        self.total_sessions = 0
        self.total_notes = 0
        self.total_hits = 0
        
    def analyze_performance(self, session_stats: Dict) -> Dict:
        """Analyze a play session and provide insights"""
        # Store session data
        self.performance_history.append(session_stats)
        self.session_data.append({
            'timestamp': time.time(),
            'stats': session_stats
        })
        
        self.total_sessions += 1
        self.total_notes += session_stats.get('total_notes', 0)
        self.total_hits += session_stats.get('hits', 0)
        
        # Calculate metrics
        analysis = {
            'accuracy': session_stats.get('accuracy', 0),
            'timing_error': session_stats.get('timing_error_ms', 0),
            'skill_level': self._assess_skill_level(session_stats),
            'improvement_trend': self._calculate_trend(),
            'weak_areas': self._identify_weak_areas(session_stats),
            'strong_areas': self._identify_strong_areas(session_stats)
        }
        
        return analysis
    
    def get_recommendations(self, analysis: Dict) -> List[str]:
        """Get personalized recommendations in Turkish"""
        recommendations = []
        
        accuracy = analysis.get('accuracy', 0)
        timing_error = analysis.get('timing_error', 0)
        skill_level = analysis.get('skill_level', 'beginner')
        
        # Accuracy-based recommendations
        if accuracy < 0.5:
            recommendations.append("🎯 Doğruluk çok düşük. Daha yavaş parçalarla başlayın ve odaklanın.")
            recommendations.append("💡 Not pozisyonlarını ezberlemek için önce sadece izleyin.")
        elif accuracy < 0.7:
            recommendations.append("📈 Doğruluğu artırmak için pratik yapın. Hedef: %70+")
            recommendations.append("⏱️ Timing offset ayarını kontrol edin.")
        elif accuracy < 0.85:
            recommendations.append("✨ İyi ilerleme! Daha zorlu parçaları deneyebilirsiniz.")
            recommendations.append("🎵 Combo'ları korumaya odaklanın.")
        elif accuracy < 0.95:
            recommendations.append("🌟 Mükemmel performans! Hız ve karmaşıklığı artırın.")
            recommendations.append("🏆 Zor modlara geçmeye hazırsınız.")
        else:
            recommendations.append("👑 Harika! Usta seviyesindesiniz!")
            recommendations.append("💪 Expert modlarda kendinizi test edin.")
        
        # Timing-based recommendations
        if timing_error > 50:
            recommendations.append("⏰ Zamanlama hatası yüksek. Kalibrasyon yapın.")
            recommendations.append("🔧 Sistem gecikmesini azaltmak için ayarları optimize edin.")
        elif timing_error > 30:
            recommendations.append("⚡ Zamanlama biraz geç. Offset değerini ayarlayın.")
        elif timing_error < 10:
            recommendations.append("🎯 Mükemmel zamanlama hassasiyeti!")
        
        # Skill level recommendations
        if skill_level == 'beginner':
            recommendations.append("🎮 Başlangıç seviyesi: Temel ritim egzersizleri yapın.")
            recommendations.append("📚 Kolay şarkılarla başlayın ve tempo artırın.")
        elif skill_level == 'intermediate':
            recommendations.append("📊 Orta seviye: Farklı pattern türlerini deneyin.")
            recommendations.append("🎼 Çeşitli BPM'lerde pratik yapın.")
        elif skill_level == 'advanced':
            recommendations.append("🚀 İleri seviye: Karmaşık kombinasyonlara odaklanın.")
            recommendations.append("💎 Mükemmellik için detaylara dikkat edin.")
        elif skill_level in ['expert', 'master']:
            recommendations.append("👑 Usta seviye: Her gün en az 30 dakika pratik yapın.")
            recommendations.append("🎯 Turnuvalara katılmayı düşünün!")
        
        # Weak areas
        weak_areas = analysis.get('weak_areas', [])
        if weak_areas:
            recommendations.append(f"⚠️ Zayıf alanlar: {', '.join(weak_areas)}")
            recommendations.append("💪 Bu alanlarda özel pratik yapın.")
        
        return recommendations
    
    def assess_skill_level(self, recent_sessions: int = 10) -> str:
        """Assess current skill level"""
        if not self.performance_history:
            return self.SKILL_LEVELS['beginner']
        
        # Get recent sessions
        recent = list(self.performance_history)[-recent_sessions:]
        
        # Calculate average metrics
        avg_accuracy = np.mean([s.get('accuracy', 0) for s in recent])
        avg_timing = np.mean([s.get('timing_error_ms', 100) for s in recent])
        
        # Determine skill level
        skill_key = self._assess_skill_level({'accuracy': avg_accuracy, 'timing_error_ms': avg_timing})
        return self.SKILL_LEVELS.get(skill_key, self.SKILL_LEVELS['beginner'])
    
    def _assess_skill_level(self, stats: Dict) -> str:
        """Internal skill level assessment"""
        accuracy = stats.get('accuracy', 0)
        timing = stats.get('timing_error_ms', 100)
        
        if accuracy >= 0.95 and timing < 10:
            return 'master'
        elif accuracy >= 0.90 and timing < 15:
            return 'expert'
        elif accuracy >= 0.80 and timing < 25:
            return 'advanced'
        elif accuracy >= 0.65 and timing < 40:
            return 'intermediate'
        else:
            return 'beginner'
    
    def _calculate_trend(self) -> str:
        """Calculate performance trend"""
        if len(self.performance_history) < 3:
            return 'stable'
        
        recent = list(self.performance_history)[-10:]
        accuracies = [s.get('accuracy', 0) for s in recent]
        
        # Simple linear trend
        if len(accuracies) >= 3:
            first_half = np.mean(accuracies[:len(accuracies)//2])
            second_half = np.mean(accuracies[len(accuracies)//2:])
            
            diff = second_half - first_half
            if diff > 0.05:
                return 'improving'
            elif diff < -0.05:
                return 'declining'
        
        return 'stable'
    
    def _identify_weak_areas(self, stats: Dict) -> List[str]:
        """Identify weak areas based on statistics"""
        weak_areas = []
        
        accuracy = stats.get('accuracy', 0)
        timing_error = stats.get('timing_error_ms', 0)
        
        if accuracy < 0.7:
            weak_areas.append('Not tanıma')
        
        if timing_error > 40:
            weak_areas.append('Zamanlama')
        
        # Check for specific pattern issues (if available)
        if 'pattern_accuracy' in stats:
            pattern_acc = stats['pattern_accuracy']
            if pattern_acc.get('stream', 1.0) < 0.7:
                weak_areas.append('Stream notları')
            if pattern_acc.get('mixed', 1.0) < 0.7:
                weak_areas.append('Karışık pattern\'ler')
        
        return weak_areas
    
    def _identify_strong_areas(self, stats: Dict) -> List[str]:
        """Identify strong areas based on statistics"""
        strong_areas = []
        
        accuracy = stats.get('accuracy', 0)
        timing_error = stats.get('timing_error_ms', 0)
        
        if accuracy >= 0.9:
            strong_areas.append('Yüksek doğruluk')
        
        if timing_error < 15:
            strong_areas.append('Mükemmel zamanlama')
        
        if stats.get('combo', 0) > 100:
            strong_areas.append('Uzun combo')
        
        return strong_areas
    
    def get_training_suggestions(self, skill_level: str) -> List[str]:
        """Get training suggestions based on skill level"""
        suggestions = []
        
        if skill_level == self.SKILL_LEVELS['beginner']:
            suggestions.extend([
                "1. Yavaş tempo şarkılarla başlayın (60-80 BPM)",
                "2. Her gün 15-20 dakika pratik yapın",
                "3. Tek sütun notlarına odaklanın",
                "4. Not pozisyonlarını görsel olarak öğrenin",
                "5. Metronom kullanarak ritim hissini geliştirin"
            ])
        elif skill_level == self.SKILL_LEVELS['intermediate']:
            suggestions.extend([
                "1. Orta tempo şarkılar deneyin (80-120 BPM)",
                "2. İki notlu kombinasyonları çalışın",
                "3. Farklı pattern türlerini öğrenin",
                "4. Combo'ları korumaya odaklanın",
                "5. Günlük 30 dakika pratik yapın"
            ])
        elif skill_level == self.SKILL_LEVELS['advanced']:
            suggestions.extend([
                "1. Hızlı tempo şarkılar (120-160 BPM)",
                "2. Karmaşık chord kombinasyonları",
                "3. Stream section'larda hız geliştirin",
                "4. Farklı zorluk seviyeleri deneyin",
                "5. 45+ dakika yoğun pratik"
            ])
        else:  # Expert/Master
            suggestions.extend([
                "1. En zorlu şarkıları tamamlayın",
                "2. Full combo hedefleyin",
                "3. Turnuva modunda yarışın",
                "4. Kendi record'larınızı kırın",
                "5. Topluluk etkinliklerine katılın"
            ])
        
        return suggestions
    
    def get_progress_report(self) -> Dict:
        """Generate comprehensive progress report"""
        if not self.performance_history:
            return {
                'message': 'Henüz yeterli veri yok. Daha fazla oturum tamamlayın.',
                'sessions': 0
            }
        
        recent = list(self.performance_history)[-20:]
        
        avg_accuracy = np.mean([s.get('accuracy', 0) for s in recent])
        avg_timing = np.mean([s.get('timing_error_ms', 0) for s in recent])
        
        overall_accuracy = (self.total_hits / self.total_notes * 100) if self.total_notes > 0 else 0
        
        trend = self._calculate_trend()
        trend_emoji = {
            'improving': '📈',
            'stable': '➡️',
            'declining': '📉'
        }.get(trend, '➡️')
        
        return {
            'total_sessions': self.total_sessions,
            'total_notes': self.total_notes,
            'total_hits': self.total_hits,
            'overall_accuracy': overall_accuracy,
            'recent_avg_accuracy': avg_accuracy * 100,
            'recent_avg_timing': avg_timing,
            'trend': trend,
            'trend_emoji': trend_emoji,
            'skill_level': self.assess_skill_level()
        }
    
    def get_formatted_report(self) -> str:
        """Get formatted progress report in Turkish"""
        report = self.get_progress_report()
        
        if report.get('sessions', 0) == 0:
            return report.get('message', 'Veri yok')
        
        text = "=== İLERLEME RAPORU ===\n\n"
        text += f"📊 Toplam Oturum: {report['total_sessions']}\n"
        text += f"🎵 Toplam Not: {report['total_notes']}\n"
        text += f"✅ Başarılı Hit: {report['total_hits']}\n"
        text += f"🎯 Genel Doğruluk: {report['overall_accuracy']:.1f}%\n\n"
        text += f"Son 20 Oturum:\n"
        text += f"  • Ortalama Doğruluk: {report['recent_avg_accuracy']:.1f}%\n"
        text += f"  • Ortalama Timing: {report['recent_avg_timing']:.1f} ms\n"
        text += f"  • Trend: {report['trend_emoji']} {report['trend']}\n\n"
        text += f"🏆 Seviye: {report['skill_level']}\n"
        
        return text


if __name__ == "__main__":
    # Test AI Coach
    coach = AICoach()
    
    # Simulate some sessions
    test_sessions = [
        {'accuracy': 0.65, 'timing_error_ms': 45, 'total_notes': 100, 'hits': 65},
        {'accuracy': 0.72, 'timing_error_ms': 38, 'total_notes': 100, 'hits': 72},
        {'accuracy': 0.78, 'timing_error_ms': 32, 'total_notes': 100, 'hits': 78},
    ]
    
    for session in test_sessions:
        analysis = coach.analyze_performance(session)
        print("\nAnaliz:", analysis)
        recommendations = coach.get_recommendations(analysis)
        print("\nÖneriler:")
        for rec in recommendations:
            print(f"  {rec}")
    
    print("\n" + coach.get_formatted_report())
