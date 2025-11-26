"""
Pawfect Match NI - Next-Generation Pet Matching Platform
========================================================
A revolutionary AI-powered pet matching application with advanced features:
- AI-driven compatibility scoring
- Predictive matching algorithms
- Real-time analytics and insights
- Advanced gamification system
- Personalized recommendations
- Future-proof modular architecture
"""

import streamlit as st
import time
import random
import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Pawfect Match NI | AI-Powered Pet Matching",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# ============================================================================
# ADVANCED CSS & UI STYLING
# ============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Poppins:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 15%, #f093fb 30%, #4facfe 45%, #00f2fe 60%, #43e97b 75%, #fa709a 90%, #667eea 100%);
        background-size: 400% 400%;
        animation: gradientFlow 20s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .block-container {
        max-width: 450px;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(30px) saturate(180%);
        border-radius: 32px;
        box-shadow: 0 25px 80px rgba(0,0,0,0.2), 0 0 0 1px rgba(255,255,255,0.2);
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        animation: slideIn 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(30px) scale(0.95);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    /* AI Compatibility Score Badge */
    .compatibility-badge {
        position: absolute;
        top: 15px;
        right: 15px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
        z-index: 10;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4); }
        50% { transform: scale(1.05); box-shadow: 0 6px 30px rgba(102, 126, 234, 0.6); }
    }
    
    /* Pet Card with 3D Effect */
    .pet-card-3d {
        background: white;
        border-radius: 28px;
        overflow: hidden;
        box-shadow: 0 15px 50px rgba(0,0,0,0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 1.5rem;
        position: relative;
        transform-style: preserve-3d;
    }
    
    .pet-card-3d:hover {
        transform: translateY(-8px) rotateX(2deg);
        box-shadow: 0 25px 70px rgba(0,0,0,0.25);
    }
    
    .pet-image-wrapper {
        position: relative;
        width: 100%;
        height: 450px;
        overflow: hidden;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .pet-image-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,0.3) 100%);
        z-index: 1;
    }
    
    .pet-image-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .pet-card-3d:hover .pet-image-wrapper img {
        transform: scale(1.1);
    }
    
    /* AI Insights Panel */
    .ai-insights {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 2px solid rgba(102, 126, 234, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .insight-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.75rem 0;
        border-bottom: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    .insight-item:last-child {
        border-bottom: none;
    }
    
    /* Navigation Bar */
    .nav-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 0.75rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .nav-button {
        border-radius: 18px !important;
        border: none !important;
        background: transparent !important;
        color: #6b7280 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        padding: 0.7rem 0.5rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .nav-button:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3) !important;
    }
    
    /* Action Buttons with Haptic Feedback Simulation */
    .action-btn {
        width: 75px;
        height: 75px;
        border-radius: 50% !important;
        border: none !important;
        font-size: 2rem !important;
        transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.25) !important;
        cursor: pointer !important;
        position: relative;
        overflow: hidden;
    }
    
    .action-btn::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255,255,255,0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .action-btn:active::before {
        width: 300px;
        height: 300px;
    }
    
    .action-btn:hover {
        transform: scale(1.2) rotate(10deg) !important;
        box-shadow: 0 10px 35px rgba(0,0,0,0.35) !important;
    }
    
    .action-btn:active {
        transform: scale(0.9) !important;
    }
    
    .pass-btn {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%) !important;
        color: #dc2626 !important;
    }
    
    .like-btn {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        color: white !important;
    }
    
    .super-like-btn {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
        color: white !important;
        animation: superLikeGlow 2s ease-in-out infinite;
    }
    
    @keyframes superLikeGlow {
        0%, 100% { box-shadow: 0 6px 20px rgba(79, 172, 254, 0.4); }
        50% { box-shadow: 0 6px 30px rgba(79, 172, 254, 0.8); }
    }
    
    /* Stats Dashboard */
    .stat-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 24px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid rgba(102, 126, 234, 0.2);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        backdrop-filter: blur(10px);
    }
    
    .stat-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.25);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    /* Progress Ring */
    .progress-ring {
        position: relative;
        width: 120px;
        height: 120px;
        margin: 0 auto;
    }
    
    .progress-ring svg {
        transform: rotate(-90deg);
    }
    
    .progress-ring circle {
        fill: none;
        stroke-width: 8;
        transition: stroke-dashoffset 0.5s ease;
    }
    
    /* Badge System */
    .badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 4px 4px 4px 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
        transition: transform 0.2s ease;
    }
    
    .badge:hover {
        transform: scale(1.1);
    }
    
    /* Premium Badge */
    .premium-badge {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 50%, #d97706 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: 800;
        font-size: 0.9rem;
        display: inline-block;
        box-shadow: 0 6px 25px rgba(251, 191, 36, 0.5);
        animation: premiumShimmer 3s ease-in-out infinite;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    @keyframes premiumShimmer {
        0%, 100% { 
            box-shadow: 0 6px 25px rgba(251, 191, 36, 0.5);
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 8px 35px rgba(251, 191, 36, 0.7);
            transform: scale(1.02);
        }
    }
    
    /* Match Animation */
    @keyframes matchExplosion {
        0% { transform: scale(0) rotate(0deg); opacity: 0; }
        50% { transform: scale(1.3) rotate(180deg); opacity: 1; }
        100% { transform: scale(1) rotate(360deg); opacity: 1; }
    }
    
    .match-popup {
        animation: matchExplosion 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }
    
    /* Task Cards */
    .task-card {
        background: white;
        border-radius: 20px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .task-card:hover {
        transform: translateX(8px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    .task-card.completed {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.1) 100%);
        border-left-color: #10b981;
    }
    
    /* AI Recommendation Badge */
    .ai-recommended {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 700;
        margin-left: 8px;
        animation: aiPulse 2s ease-in-out infinite;
    }
    
    @keyframes aiPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* Hide Streamlit Elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 10px; }
    ::-webkit-scrollbar-thumb { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Loading Animation */
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    .loading {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(102, 126, 234, 0.3);
        border-top-color: #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA MODELS & ENUMS
# ============================================================================

class PetPersonality(Enum):
    ACTIVE = "Active"
    CALM = "Calm"
    PLAYFUL = "Playful"
    INDEPENDENT = "Independent"
    SOCIAL = "Social"
    PROTECTIVE = "Protective"

class MatchQuality(Enum):
    PERFECT = "Perfect Match"
    EXCELLENT = "Excellent"
    GOOD = "Good"
    FAIR = "Fair"

@dataclass
class PetProfile:
    id: int
    name: str
    age: str
    species: str
    breed: str
    distance: float
    location: str
    tags: List[str]
    bio: str
    image: str
    verified: bool
    medical: str
    personality: List[PetPersonality] = field(default_factory=list)
    energy_level: int = 5  # 1-10
    friendliness: int = 5  # 1-10
    trainability: int = 5  # 1-10
    compatibility_score: float = 0.0
    ai_recommended: bool = False

@dataclass
class UserPreferences:
    preferred_species: List[str] = field(default_factory=lambda: ["All"])
    max_distance: int = 50
    min_energy_level: int = 1
    max_energy_level: int = 10
    personality_preferences: List[PetPersonality] = field(default_factory=list)
    preferred_tags: List[str] = field(default_factory=list)

# ============================================================================
# AI MATCHING ENGINE
# ============================================================================

class AIMatchingEngine:
    """Advanced AI-powered matching algorithm"""
    
    @staticmethod
    def calculate_compatibility(pet: PetProfile, user_prefs: UserPreferences, user_history: Dict) -> float:
        """Calculate AI compatibility score (0-100)"""
        score = 0.0
        factors = []
        
        # Distance factor (30% weight)
        distance_score = max(0, 100 - (pet.distance / user_prefs.max_distance) * 100)
        score += distance_score * 0.3
        factors.append(("Distance", distance_score))
        
        # Species preference (20% weight)
        if "All" in user_prefs.preferred_species or pet.species in user_prefs.preferred_species:
            species_score = 100
        else:
            species_score = 50
        score += species_score * 0.2
        factors.append(("Species Match", species_score))
        
        # Energy level match (15% weight)
        if user_prefs.min_energy_level <= pet.energy_level <= user_prefs.max_energy_level:
            energy_score = 100
        else:
            energy_diff = min(abs(pet.energy_level - user_prefs.min_energy_level),
                            abs(pet.energy_level - user_prefs.max_energy_level))
            energy_score = max(0, 100 - energy_diff * 10)
        score += energy_score * 0.15
        factors.append(("Energy Match", energy_score))
        
        # Personality match (15% weight)
        if user_prefs.personality_preferences:
            personality_match = len(set(pet.personality) & set(user_prefs.personality_preferences))
            personality_score = (personality_match / len(user_prefs.personality_preferences)) * 100
        else:
            personality_score = 75  # Neutral if no preferences
        score += personality_score * 0.15
        factors.append(("Personality", personality_score))
        
        # Tag preferences (10% weight)
        if user_prefs.preferred_tags:
            tag_match = len(set(pet.tags) & set(user_prefs.preferred_tags))
            tag_score = (tag_match / len(user_prefs.preferred_tags)) * 100
        else:
            tag_score = 70
        score += tag_score * 0.1
        factors.append(("Tags", tag_score))
        
        # Verification bonus (5% weight)
        verification_score = 100 if pet.verified else 70
        score += verification_score * 0.05
        factors.append(("Verified", verification_score))
        
        # User behavior learning (5% weight) - simulate ML learning
        if user_history.get('liked_pets'):
            avg_liked_energy = sum(p.get('energy_level', 5) for p in user_history['liked_pets']) / len(user_history['liked_pets'])
            behavior_score = 100 - abs(pet.energy_level - avg_liked_energy) * 10
            behavior_score = max(0, min(100, behavior_score))
        else:
            behavior_score = 75
        score += behavior_score * 0.05
        factors.append(("Behavior Match", behavior_score))
        
        return min(100, max(0, score)), factors
    
    @staticmethod
    def get_match_quality(score: float) -> MatchQuality:
        """Determine match quality tier"""
        if score >= 90:
            return MatchQuality.PERFECT
        elif score >= 75:
            return MatchQuality.EXCELLENT
        elif score >= 60:
            return MatchQuality.GOOD
        else:
            return MatchQuality.FAIR
    
    @staticmethod
    def generate_ai_insights(pet: PetProfile, compatibility: float, factors: List[Tuple]) -> List[str]:
        """Generate AI-powered insights about the match"""
        insights = []
        
        if compatibility >= 90:
            insights.append("🌟 Perfect match! This pet aligns with all your preferences.")
        elif compatibility >= 75:
            insights.append("✨ Excellent compatibility! Strong match across multiple factors.")
        
        # Distance insight
        if pet.distance <= 5:
            insights.append(f"📍 Very close - only {pet.distance} miles away!")
        elif pet.distance <= 15:
            insights.append(f"📍 Convenient distance - {pet.distance} miles away.")
        
        # Personality insights
        if PetPersonality.ACTIVE in pet.personality:
            insights.append("🏃 High energy - perfect for active owners!")
        if PetPersonality.CALM in pet.personality:
            insights.append("🧘 Calm temperament - great for relaxed households.")
        
        # Energy level insight
        if pet.energy_level >= 8:
            insights.append("⚡ High energy - needs lots of exercise and playtime.")
        elif pet.energy_level <= 3:
            insights.append("😌 Low energy - perfect for quieter lifestyles.")
        
        # Tag-based insights
        if "Friendly" in pet.tags:
            insights.append("🤝 Very friendly - great with people and other pets!")
        if "Hypoallergenic" in pet.tags:
            insights.append("🌿 Hypoallergenic - perfect for allergy sufferers!")
        
        return insights[:3]  # Limit to 3 insights

# ============================================================================
# GAMIFICATION SYSTEM
# ============================================================================

class GamificationEngine:
    """Advanced gamification and progression system"""
    
    @staticmethod
    def calculate_level(xp: int) -> Tuple[int, float, int]:
        """Calculate level, progress, and XP needed for next level"""
        base_xp = 300
        level = int(math.sqrt(xp / base_xp)) + 1
        current_level_xp = (level - 1) ** 2 * base_xp
        next_level_xp = level ** 2 * base_xp
        progress = (xp - current_level_xp) / (next_level_xp - current_level_xp)
        xp_needed = next_level_xp - xp
        return level, progress, xp_needed
    
    @staticmethod
    def get_level_title(level: int) -> str:
        """Get title based on level"""
        titles = {
            1: "Pet Enthusiast",
            2: "Animal Lover",
            3: "Companion Seeker",
            4: "Match Master",
            5: "Pet Whisperer",
            6: "Furry Friend Expert",
            7: "Animal Advocate",
            8: "Pet Match Legend",
            9: "Companion Champion",
            10: "Ultimate Pet Matcher"
        }
        return titles.get(level, f"Level {level} Expert")
    
    @staticmethod
    def calculate_achievements(user_stats: Dict) -> List[Dict]:
        """Calculate unlocked achievements"""
        achievements = []
        
        if user_stats.get('matches', 0) >= 1:
            achievements.append({"name": "First Match", "icon": "🎯", "desc": "Found your first match!"})
        if user_stats.get('matches', 0) >= 5:
            achievements.append({"name": "Match Maker", "icon": "💕", "desc": "5 matches found!"})
        if user_stats.get('matches', 0) >= 10:
            achievements.append({"name": "Love Expert", "icon": "❤️", "desc": "10 matches found!"})
        if user_stats.get('streak', 0) >= 7:
            achievements.append({"name": "Week Warrior", "icon": "🔥", "desc": "7 day streak!"})
        if user_stats.get('streak', 0) >= 30:
            achievements.append({"name": "Monthly Master", "icon": "⭐", "desc": "30 day streak!"})
        if user_stats.get('xp', 0) >= 1000:
            achievements.append({"name": "XP Collector", "icon": "✨", "desc": "Earned 1000 XP!"})
        
        return achievements

# ============================================================================
# STATE MANAGEMENT
# ============================================================================

def initialize_session_state():
    """Initialize all session state variables"""
    
    # Pet Data with Enhanced Profiles
    if 'pets_data' not in st.session_state:
        pets_raw = [
            {"id": 1, "name": "Barnaby", "age": "2 yrs", "species": "Dog", "breed": "Golden Retriever Mix", 
             "distance": 2, "location": "Belfast City Center", "tags": ["Hiker", "Friendly"], 
             "bio": "Looking for a hiking buddy for Cave Hill!", 
             "image": "https://images.unsplash.com/photo-1552053831-71594a27632d?w=800&q=80", 
             "verified": True, "medical": "Vaccinated", "personality": [PetPersonality.ACTIVE, PetPersonality.SOCIAL],
             "energy_level": 8, "friendliness": 9, "trainability": 8},
            {"id": 2, "name": "Luna", "age": "4 mo", "species": "Cat", "breed": "Domestic Shorthair", 
             "distance": 12, "location": "Bangor", "tags": ["Indoor", "Playful"], 
             "bio": "Tiny tiger looking for a warm lap.", 
             "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80", 
             "verified": True, "medical": "Vaccinated", "personality": [PetPersonality.PLAYFUL, PetPersonality.SOCIAL],
             "energy_level": 7, "friendliness": 8, "trainability": 6},
            {"id": 3, "name": "Seamus", "age": "5 yrs", "species": "Dog", "breed": "Irish Wolfhound", 
             "distance": 45, "location": "Derry", "tags": ["Gentle", "Big"], 
             "bio": "A big softie. Loves slow walks.", 
             "image": "https://images.unsplash.com/photo-1554693190-b894d53759cd?w=800&q=80", 
             "verified": True, "medical": "Healthy", "personality": [PetPersonality.CALM, PetPersonality.SOCIAL],
             "energy_level": 3, "friendliness": 9, "trainability": 7},
            {"id": 4, "name": "Guinness", "age": "1 yr", "species": "Dog", "breed": "Black Lab", 
             "distance": 8, "location": "Lisburn", "tags": ["High Energy", "Fetch"], 
             "bio": "I will retrieve anything you throw!", 
             "image": "https://images.unsplash.com/photo-1561037404-61cd46aa615b?w=800&q=80", 
             "verified": False, "medical": "Vaccinated", "personality": [PetPersonality.ACTIVE, PetPersonality.PLAYFUL],
             "energy_level": 9, "friendliness": 8, "trainability": 9},
            {"id": 5, "name": "Potato", "age": "3 yrs", "species": "Dog", "breed": "Corgi", 
             "distance": 60, "location": "Portrush", "tags": ["Sassy", "Beach"], 
             "bio": "Short legs, big personality.", 
             "image": "https://images.unsplash.com/photo-1519098901909-b1553a1190af?w=800&q=80", 
             "verified": True, "medical": "Healthy", "personality": [PetPersonality.PLAYFUL, PetPersonality.SOCIAL],
             "energy_level": 7, "friendliness": 8, "trainability": 7},
            {"id": 6, "name": "Mittens", "age": "8 yrs", "species": "Cat", "breed": "Persian", 
             "distance": 5, "location": "Holywood", "tags": ["Chill", "Fluffy"], 
             "bio": "I judge silently but love deeply.", 
             "image": "https://images.unsplash.com/photo-1513245543132-31f507417b26?w=800&q=80", 
             "verified": True, "medical": "Special Diet", "personality": [PetPersonality.CALM, PetPersonality.INDEPENDENT],
             "energy_level": 2, "friendliness": 6, "trainability": 4},
            {"id": 7, "name": "Rocky", "age": "4 yrs", "species": "Dog", "breed": "Boxer", 
             "distance": 15, "location": "Newtownabbey", "tags": ["Goofy", "Strong"], 
             "bio": "Professional drooler and hugger.", 
             "image": "https://images.unsplash.com/photo-1543071220-6ee5bf71a54e?w=800&q=80", 
             "verified": True, "medical": "Vaccinated", "personality": [PetPersonality.PLAYFUL, PetPersonality.SOCIAL],
             "energy_level": 8, "friendliness": 9, "trainability": 7},
            {"id": 8, "name": "Thumper", "age": "1 yr", "species": "Rabbit", "breed": "Lop Eared", 
             "distance": 3, "location": "Belfast East", "tags": ["Quiet", "Hops"], 
             "bio": "Loves carrots and wires (keep them safe!).", 
             "image": "https://images.unsplash.com/photo-1585110396065-88b724108873?w=800&q=80", 
             "verified": False, "medical": "Healthy", "personality": [PetPersonality.CALM, PetPersonality.INDEPENDENT],
             "energy_level": 4, "friendliness": 5, "trainability": 3},
            {"id": 9, "name": "Bella", "age": "2 yrs", "species": "Dog", "breed": "Cockapoo", 
             "distance": 20, "location": "Antrim", "tags": ["Hypoallergenic", "Cute"], 
             "bio": "Loves everyone I meet!", 
             "image": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=800&q=80", 
             "verified": True, "medical": "Vaccinated", "personality": [PetPersonality.SOCIAL, PetPersonality.PLAYFUL],
             "energy_level": 6, "friendliness": 10, "trainability": 8},
            {"id": 10, "name": "Shadow", "age": "6 yrs", "species": "Cat", "breed": "Black Cat", 
             "distance": 10, "location": "Dundonald", "tags": ["Mysterious", "Vocal"], 
             "bio": "I am the night.", 
             "image": "https://images.unsplash.com/photo-1513360371669-4adf3dd7dff8?w=800&q=80", 
             "verified": True, "medical": "Healthy", "personality": [PetPersonality.INDEPENDENT, PetPersonality.CALM],
             "energy_level": 3, "friendliness": 5, "trainability": 5},
        ]
        
        st.session_state.pets_data = [
            PetProfile(**pet) for pet in pets_raw
        ]
    
    # User State
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'view' not in st.session_state:
        st.session_state.view = 'auth'
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = 'Match'
    
    # Matching State
    if 'current_pet_index' not in st.session_state:
        st.session_state.current_pet_index = 0
    if 'matches' not in st.session_state:
        st.session_state.matches = []
    if 'liked_pets' not in st.session_state:
        st.session_state.liked_pets = []
    if 'passed_pets' not in st.session_state:
        st.session_state.passed_pets = []
    
    # Gamification State
    if 'xp' not in st.session_state:
        st.session_state.xp = 1240
    if 'happiness' not in st.session_state:
        st.session_state.happiness = 65
    if 'streak' not in st.session_state:
        st.session_state.streak = 12
    if 'last_activity' not in st.session_state:
        st.session_state.last_activity = datetime.now().date()
    
    # User Preferences
    if 'user_preferences' not in st.session_state:
        st.session_state.user_preferences = UserPreferences()
    
    # Chat State
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = {}
    
    # Tasks
    if 'tasks' not in st.session_state:
        st.session_state.tasks = {
            "Morning Walk": {"xp": 50, "completed": False, "icon": "🚶", "desc": "Take a 20m stroll"},
            "Breakfast": {"xp": 30, "completed": False, "icon": "🦴", "desc": "Healthy mix only"},
            "Grooming": {"xp": 20, "completed": False, "icon": "✨", "desc": "Brush that coat"},
            "Health Check": {"xp": 40, "completed": False, "icon": "🩺", "desc": "Check eyes and ears"},
            "Playtime": {"xp": 35, "completed": False, "icon": "🎾", "desc": "15 min of fun"},
            "Evening Walk": {"xp": 50, "completed": False, "icon": "🌙", "desc": "Sunset stroll"},
        }

# ============================================================================
# AUTHENTICATION
# ============================================================================

def login_user(username: str, password: str):
    """Authenticate user"""
    if username and password:
        st.session_state.user = {
            "name": username,
            "email": f"{username}@example.com",
            "joined": datetime.now().strftime("%b %Y"),
            "verified": True,
            "is_premium": False
        }
        st.session_state.view = 'app'
        st.toast(f"Welcome back, {username}! 🎉", icon="👋")
        time.sleep(0.3)
        st.rerun()
    else:
        st.error("Please enter both username and password.")

def signup_user(username: str, email: str, password: str):
    """Create new user account"""
    if username and email and password:
        st.session_state.user = {
            "name": username,
            "email": email,
            "joined": datetime.now().strftime("%b %Y"),
            "verified": False,
            "is_premium": False
        }
        st.session_state.view = 'app'
        st.toast(f"Account created! Welcome, {username}! 🎉", icon="🎉")
        st.balloons()
        time.sleep(0.5)
        st.rerun()
    else:
        st.error("Please fill in all fields.")

def logout():
    """Log out user"""
    st.session_state.user = None
    st.session_state.view = 'auth'
    st.session_state.active_tab = 'Match'
    st.session_state.current_pet_index = 0
    st.toast("Logged out successfully", icon="👋")
    st.rerun()

def upgrade_premium():
    """Upgrade to premium"""
    st.session_state.user['is_premium'] = True
    st.balloons()
    st.toast("Welcome to Premium! 🌟", icon="💎")
    time.sleep(0.5)
    st.rerun()

# ============================================================================
# VIEW COMPONENTS
# ============================================================================

def render_auth():
    """Render authentication screen"""
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="font-size: 4rem; margin: 0; filter: drop-shadow(0 4px 10px rgba(0,0,0,0.3));">
                🐾
            </h1>
            <h2 style="color: white; text-shadow: 0 4px 15px rgba(0,0,0,0.4); margin-top: 0.5rem; font-size: 2.5rem; font-weight: 800;">
                Pawfect Match NI
            </h2>
            <p style="color: rgba(255,255,255,0.95); font-size: 1.2rem; font-weight: 500;">
                AI-Powered Pet Matching Platform
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    tab_login, tab_signup = st.tabs(["🔐 Log In", "✨ Sign Up"])
    
    with tab_login:
        st.markdown("<br>", unsafe_allow_html=True)
        username = st.text_input("Username", key="login_user", placeholder="Enter your username")
        password = st.text_input("Password", type="password", key="login_pass", placeholder="Enter your password")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Log In", type="primary", use_container_width=True):
            login_user(username, password)
    
    with tab_signup:
        st.markdown("<br>", unsafe_allow_html=True)
        new_user = st.text_input("Choose a Username", key="signup_user", placeholder="Pick a username")
        new_email = st.text_input("Email Address", key="signup_email", placeholder="your.email@example.com")
        new_pass = st.text_input("Choose Password", type="password", key="signup_pass", placeholder="Create a secure password")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Create Account", type="primary", use_container_width=True):
            signup_user(new_user, new_email, new_pass)

def render_swipe_deck(filters: Dict):
    """Render AI-powered swipe deck with compatibility scoring"""
    all_pets = st.session_state.pets_data
    user_prefs = st.session_state.user_preferences
    
    # Apply filters
    filtered_pets = [
        p for p in all_pets 
        if (filters['species'] == 'All' or p.species == filters['species'])
        and (p.distance <= filters['distance'])
    ]
    
    # Calculate AI compatibility scores
    user_history = {
        'liked_pets': [{'energy_level': p.energy_level} for p in st.session_state.liked_pets]
    }
    
    for pet in filtered_pets:
        score, factors = AIMatchingEngine.calculate_compatibility(pet, user_prefs, user_history)
        pet.compatibility_score = score
        pet.ai_recommended = score >= 85
    
    # Sort by compatibility score (AI recommendation)
    filtered_pets.sort(key=lambda x: x.compatibility_score, reverse=True)
    
    # Paywall
    if st.session_state.current_pet_index >= 10 and not st.session_state.user.get('is_premium', False):
        st.markdown("""
        <div class="paywall-container">
            <div style="font-size: 5rem; margin-bottom: 1rem;">💎</div>
            <h1>Premium Access</h1>
            <p style="font-size: 1.3rem; opacity: 0.95;">You've viewed your daily limit of 10 free profiles.</p>
            <p style="font-size: 1.1rem; opacity: 0.9;">Upgrade for unlimited matches, AI insights, and more!</p>
            <div style="margin-top: 2rem;">
                <h2 style="font-size: 3rem; margin: 0;">£4.99<span style="font-size: 1.2rem;">/mo</span></h2>
            </div>
        </div>
        <br>
        """, unsafe_allow_html=True)
        if st.button("✨ Upgrade to Premium", type="primary", use_container_width=True):
            upgrade_premium()
        return
    
    # End of list
    if st.session_state.current_pet_index >= len(filtered_pets):
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">🐶</div>
            <h2>You've seen all matches!</h2>
            <p>Check back later for more pets.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Reset & Start Over", type="primary", use_container_width=True):
            st.session_state.current_pet_index = 0
            st.rerun()
        return
    
    pet = filtered_pets[st.session_state.current_pet_index]
    compatibility = pet.compatibility_score
    match_quality = AIMatchingEngine.get_match_quality(compatibility)
    insights = AIMatchingEngine.generate_ai_insights(pet, compatibility, [])
    
    # Pet Card with AI Compatibility
    st.markdown(f"""
    <div class="pet-card-3d">
        <div class="pet-image-wrapper">
            <div class="compatibility-badge">
                🤖 {int(compatibility)}% Match
            </div>
            <img src="{pet.image}" alt="{pet.name}">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Pet Info
    col1, col2 = st.columns([4, 1])
    with col1:
        verified_badge = "🛡️" if pet.verified else ""
        ai_badge = '<span class="ai-recommended">AI RECOMMENDED</span>' if pet.ai_recommended else ""
        st.markdown(f"### {pet.name}, {pet.age} {verified_badge} {ai_badge}", unsafe_allow_html=True)
        st.caption(f"📍 {pet.location} • {pet.distance} miles away")
    
    # Match Quality Badge
    quality_colors = {
        MatchQuality.PERFECT: "linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%)",
        MatchQuality.EXCELLENT: "linear-gradient(135deg, #10b981 0%, #059669 100%)",
        MatchQuality.GOOD: "linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)",
        MatchQuality.FAIR: "linear-gradient(135deg, #6b7280 0%, #4b5563 100%)"
    }
    st.markdown(f"""
    <div style="background: {quality_colors[match_quality]}; color: white; padding: 0.5rem 1rem; border-radius: 15px; text-align: center; margin: 0.5rem 0; font-weight: 600;">
        {match_quality.value}
    </div>
    """, unsafe_allow_html=True)
    
    # Tags
    badge_html = "".join([f'<span class="badge">{t}</span>' for t in pet.tags])
    st.markdown(badge_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Bio
    st.markdown(f"<p style='font-size: 1rem; line-height: 1.6; color: #374151;'>{pet.bio}</p>", unsafe_allow_html=True)
    
    # AI Insights
    if insights:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🤖 AI Insights")
        insights_html = "".join([f'<div class="insight-item"><span style="font-size: 1.2rem;">{insight}</span></div>' for insight in insights])
        st.markdown(f'<div class="ai-insights">{insights_html}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Action Buttons
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        if st.button("❌", key=f"pass_{pet.id}", use_container_width=True):
            st.session_state.passed_pets.append(pet)
            st.session_state.current_pet_index += 1
            st.toast("Passed", icon="➡️")
            time.sleep(0.2)
            st.rerun()
    with col2:
        if st.button("ℹ️", key=f"info_{pet.id}", use_container_width=True):
            st.info(f"""
            **Medical:** {pet.medical}
            **Breed:** {pet.breed}
            **Energy Level:** {pet.energy_level}/10
            **Friendliness:** {pet.friendliness}/10
            **Trainability:** {pet.trainability}/10
            """)
    with col3:
        if st.button("⭐", key=f"super_{pet.id}", use_container_width=True):
            st.session_state.liked_pets.append(pet)
            st.session_state.matches.append(pet)
            st.session_state.xp += 50
            st.toast(f"Super Like! +50 XP 🎉", icon="⭐")
            st.balloons()
            time.sleep(0.5)
            st.rerun()
    with col4:
        if st.button("❤️", key=f"like_{pet.id}", use_container_width=True):
            st.session_state.liked_pets.append(pet)
            st.session_state.matches.append(pet)
            st.session_state.chat_history[pet.id] = [
                {"role": "assistant", "content": f"Woof! Thanks for swiping right on me! I'm {pet.name} 🐾"}
            ]
            st.session_state.xp += 25
            st.toast(f"🎉 Match with {pet.name}! +25 XP ❤️", icon="🎉")
            st.balloons()
            time.sleep(0.5)
            st.rerun()

def render_care():
    """Render care dashboard with gamification"""
    level, progress, xp_needed = GamificationEngine.calculate_level(st.session_state.xp)
    level_title = GamificationEngine.get_level_title(level)
    achievements = GamificationEngine.calculate_achievements({
        'matches': len(st.session_state.matches),
        'streak': st.session_state.streak,
        'xp': st.session_state.xp
    })
    
    # Hero Card
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); padding: 2rem; border-radius: 28px; color: white; margin-bottom: 2rem; box-shadow: 0 15px 50px rgba(102, 126, 234, 0.3);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 1rem;">
            <div>
                <h2 style="margin:0; color:white; font-size: 2.2rem; font-weight: 800;">Barnaby</h2>
                <p style="opacity:0.95; margin:0; font-size: 1.1rem; font-weight: 600;">{level_title} • Level {level}</p>
            </div>
            <div style="text-align:right;">
                <h1 style="margin:0; color:white; font-size: 3rem; font-weight: 900;">{int(progress*100)}%</h1>
                <small style="opacity: 0.9; font-size: 0.9rem;">{xp_needed} XP to next level</small>
            </div>
        </div>
        <div class="progress-container" style="background: rgba(255,255,255,0.2);">
            <div class="progress-bar" style="width: {progress*100}%;"></div>
        </div>
        <div style="margin-top: 1rem; text-align: center; font-size: 1rem; opacity: 0.95; font-weight: 600;">
            {st.session_state.xp} Total XP
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">😊</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #667eea;">{st.session_state.happiness}%</div>
            <div style="font-size: 0.9rem; color: #6b7280; margin-top: 0.25rem; font-weight: 600;">Happiness</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔥</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #667eea;">{st.session_state.streak}</div>
            <div style="font-size: 0.9rem; color: #6b7280; margin-top: 0.25rem; font-weight: 600;">Day Streak</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💚</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #667eea;">98%</div>
            <div style="font-size: 0.9rem; color: #6b7280; margin-top: 0.25rem; font-weight: 600;">Health</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Achievements
    if achievements:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🏆 Achievements")
        cols = st.columns(len(achievements))
        for i, ach in enumerate(achievements):
            with cols[i]:
                st.markdown(f"""
                <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(245, 158, 11, 0.1) 100%); border-radius: 16px; border: 2px solid rgba(251, 191, 36, 0.3);">
                    <div style="font-size: 2.5rem;">{ach['icon']}</div>
                    <div style="font-weight: 700; font-size: 0.9rem; margin-top: 0.5rem;">{ach['name']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📋 Daily Tasks")
    
    # Task Cards
    for task_name, details in st.session_state.tasks.items():
        completed_class = "completed" if details["completed"] else ""
        st.markdown(f"""
        <div class="task-card {completed_class}">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 1rem; flex: 1;">
                    <div style="font-size: 2.5rem;">{details['icon']}</div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1rem; color: #1f2937;">{task_name}</div>
                        <div style="font-size: 0.9rem; color: #6b7280; margin-top: 0.25rem;">{details['desc']}</div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 800; color: #667eea; font-size: 1rem;">+{details['xp']} XP</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([10, 1])
        with col2:
            st.checkbox("", value=details['completed'], key=task_name, 
                       on_change=lambda tn=task_name: toggle_task(tn), label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)

def render_chat():
    """Render chat interface"""
    st.markdown("### 💬 Messages")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if not st.session_state.matches:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">💔</div>
            <h3>No matches yet!</h3>
            <p>Start swiping to find your perfect match ❤️</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    match_names = [m.name for m in st.session_state.matches]
    selected_name = st.selectbox("Select a chat:", match_names, label_visibility="collapsed")
    selected_match = next(m for m in st.session_state.matches if m.name == selected_name)
    match_id = selected_match.id
    
    if match_id not in st.session_state.chat_history:
        st.session_state.chat_history[match_id] = []
    
    history = st.session_state.chat_history[match_id]
    
    # Chat Header
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.25rem; border-radius: 20px; margin-bottom: 1rem; color: white; box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <img src="{selected_match.image}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 3px solid white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
            <div>
                <div style="font-weight: 700; font-size: 1.2rem;">{selected_match.name}</div>
                <div style="font-size: 0.9rem; opacity: 0.95;">{selected_match.age} • {selected_match.location}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat Messages
    with st.container():
        for msg in history:
            if msg['role'] == "assistant":
                st.markdown(f"""
                <div style="display: flex; align-items: start; gap: 0.75rem; margin-bottom: 1rem;">
                    <img src="{selected_match.image}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;">
                    <div style="background: #f3f4f6; padding: 1rem 1.25rem; border-radius: 20px; max-width: 70%; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                        {msg['content']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="display: flex; align-items: start; gap: 0.75rem; margin-bottom: 1rem; justify-content: flex-end;">
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1rem 1.25rem; border-radius: 20px; max-width: 70%; box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);">
                        {msg['content']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Chat Input
    if prompt := st.chat_input("Type a message..."):
        history.append({"role": "user", "content": prompt})
        responses = [
            "Woof! That sounds amazing! 🐾",
            "I'd love that! When can we meet?",
            "Do you have any treats? I'm always hungry! 🦴",
            "Can I bring my favorite toy?",
            "That sounds pawsome! Let's do it!",
            "I'm so excited! This is going to be fun!",
            "Count me in! I'm ready for an adventure!",
        ]
        history.append({"role": "assistant", "content": random.choice(responses)})
        st.rerun()

def render_profile():
    """Render user profile"""
    user = st.session_state.user
    if not user:
        return
    
    st.markdown(f"## 👋 Hello, {user['name']}!")
    
    if user.get('is_premium'):
        st.markdown("""
        <div class="premium-badge">
            💎 Premium Member
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #e5e7eb; color: #374151; padding: 10px 20px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; display: inline-block; margin-bottom: 1rem;">
            Free Plan
        </div>
        """, unsafe_allow_html=True)
    
    st.caption(f"Member since {user['joined']}")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Account Settings")
    st.text_input("Email", value=user['email'], disabled=True, key="profile_email")
    
    search_radius = st.slider("Search Radius (miles)", 5, 100, 25, key="search_radius")
    st.session_state.user_preferences.max_distance = search_radius
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 📊 Your Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Matches", len(st.session_state.matches))
        st.metric("XP", st.session_state.xp)
    with col2:
        st.metric("Happiness", f"{st.session_state.happiness}%")
        st.metric("Streak", f"{st.session_state.streak} days")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚪 Log Out", type="primary", use_container_width=True):
        logout()

def render_nav_bar():
    """Render navigation bar"""
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🔥 Match", key="nav_match", use_container_width=True):
            st.session_state.active_tab = 'Match'
            st.rerun()
    with col2:
        if st.button("🦴 Care", key="nav_care", use_container_width=True):
            st.session_state.active_tab = 'Care'
            st.rerun()
    with col3:
        if st.button("💬 Chat", key="nav_chat", use_container_width=True):
            st.session_state.active_tab = 'Chat'
            st.rerun()
    with col4:
        if st.button("👤 Profile", key="nav_profile", use_container_width=True):
            st.session_state.active_tab = 'Profile'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def toggle_task(task_name: str):
    """Toggle task completion"""
    task = st.session_state.tasks[task_name]
    if not task["completed"]:
        task["completed"] = True
        st.session_state.xp += task["xp"]
        st.session_state.happiness = min(100, st.session_state.happiness + 15)
        st.toast(f"✅ Completed {task_name}! +{task['xp']} XP", icon="✨")
    else:
        task["completed"] = False
        st.session_state.xp -= task["xp"]
        st.session_state.happiness = max(0, st.session_state.happiness - 15)

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point"""
    initialize_session_state()
    
    if st.session_state.view == 'auth' or st.session_state.user is None:
        render_auth()
    else:
        render_nav_bar()
        
        if st.session_state.active_tab == 'Match':
            with st.expander("🔍 AI Filter Settings", expanded=False):
                species = st.radio("Species", ["All", "Dog", "Cat", "Rabbit", "Hamster"], 
                                 horizontal=True, key="filter_species")
                dist = st.slider("Max Distance (miles)", 1, 100, 50, key="filter_distance")
                energy_min = st.slider("Min Energy Level", 1, 10, 1, key="energy_min")
                energy_max = st.slider("Max Energy Level", 1, 10, 10, key="energy_max")
                
                st.session_state.user_preferences.max_distance = dist
                st.session_state.user_preferences.min_energy_level = energy_min
                st.session_state.user_preferences.max_energy_level = energy_max
                if species != "All":
                    st.session_state.user_preferences.preferred_species = [species]
                else:
                    st.session_state.user_preferences.preferred_species = ["All"]
            
            render_swipe_deck({"species": species, "distance": dist})
        
        elif st.session_state.active_tab == 'Care':
            render_care()
        
        elif st.session_state.active_tab == 'Chat':
            render_chat()
        
        elif st.session_state.active_tab == 'Profile':
            render_profile()

if __name__ == "__main__":
    main()
