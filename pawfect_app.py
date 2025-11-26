import streamlit as st
import time
import random
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Pawfect Match NI",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# --- ENHANCED CUSTOM CSS STYLING ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Main Content Container */
    .block-container {
        max-width: 420px;
        padding: 1.5rem 1.5rem 3rem 1.5rem;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border-radius: 32px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,255,255,0.1);
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        animation: slideUp 0.5s ease-out;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @media (max-width: 500px) {
        .block-container {
            padding: 1rem;
            margin-top: 0.5rem;
            border-radius: 24px 24px 0 0;
        }
    }
    
    /* Navigation Bar */
    .nav-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 0.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    
    .nav-button {
        border-radius: 16px !important;
        border: none !important;
        background: transparent !important;
        color: #6b7280 !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 0.6rem 0.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    .nav-button:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
    }
    
    .nav-button.active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
    }
    
    /* Pet Card Styling */
    .pet-card {
        background: white;
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 1.5rem;
    }
    
    .pet-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0,0,0,0.15);
    }
    
    .pet-image-container {
        position: relative;
        width: 100%;
        height: 400px;
        overflow: hidden;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .pet-image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }
    
    .pet-image-container:hover img {
        transform: scale(1.05);
    }
    
    /* Action Buttons */
    .action-button-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        padding: 1.5rem 0;
    }
    
    .action-btn {
        width: 70px;
        height: 70px;
        border-radius: 50% !important;
        border: none !important;
        font-size: 1.8rem !important;
        transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
        cursor: pointer !important;
    }
    
    .action-btn:hover {
        transform: scale(1.15) rotate(5deg) !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important;
    }
    
    .action-btn:active {
        transform: scale(0.95) !important;
    }
    
    .pass-btn {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%) !important;
        color: #dc2626 !important;
    }
    
    .like-btn {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        color: white !important;
    }
    
    .info-btn {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
        color: white !important;
    }
    
    /* Badges */
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
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
    }
    
    /* Premium Paywall */
    .paywall-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .paywall-container h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid rgba(102, 126, 234, 0.2);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    /* Task Cards */
    .task-card {
        background: white;
        border-radius: 16px;
        padding: 1rem;
        margin-bottom: 0.75rem;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .task-card:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .task-card.completed {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.1) 100%);
        border-left-color: #10b981;
    }
    
    /* Chat Messages */
    .chat-message {
        padding: 1rem;
        border-radius: 18px;
        margin-bottom: 1rem;
        animation: fadeIn 0.3s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Premium Badge */
    .premium-badge {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(251, 191, 36, 0.4);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0%, 100% { box-shadow: 0 4px 15px rgba(251, 191, 36, 0.4); }
        50% { box-shadow: 0 4px 25px rgba(251, 191, 36, 0.6); }
    }
    
    /* Progress Bar */
    .progress-container {
        background: rgba(102, 126, 234, 0.1);
        border-radius: 10px;
        height: 12px;
        overflow: hidden;
        margin-top: 0.5rem;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
        box-shadow: 0 2px 10px rgba(102, 126, 234, 0.4);
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        border: 2px solid #e5e7eb !important;
        padding: 0.75rem 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Button Styling */
    .stButton > button {
        border-radius: 12px !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
        border: none !important;
    }
    
    .stButton > button[type="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stButton > button[type="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Empty State */
    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
        color: #6b7280;
    }
    
    .empty-state-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }
    
    /* Match Animation */
    @keyframes matchPop {
        0% { transform: scale(0); opacity: 0; }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .match-popup {
        animation: matchPop 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }
    
    /* Hide Streamlit default elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---

# Expanded Data Set (20 Animals) with Fixed Images
if 'pets_data' not in st.session_state:
    st.session_state.pets_data = [
        {"id": 1, "name": "Barnaby", "age": "2 yrs", "species": "Dog", "breed": "Golden Retriever Mix", "distance": 2, "location": "Belfast City Center", "tags": ["Hiker", "Friendly"], "bio": "Looking for a hiking buddy for Cave Hill!", "image": "https://images.unsplash.com/photo-1552053831-71594a27632d?w=800&q=80", "verified": True, "medical": "Vaccinated"},
        {"id": 2, "name": "Luna", "age": "4 mo", "species": "Cat", "breed": "Domestic Shorthair", "distance": 12, "location": "Bangor", "tags": ["Indoor", "Playful"], "bio": "Tiny tiger looking for a warm lap.", "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80", "verified": True, "medical": "Vaccinated"},
        {"id": 3, "name": "Seamus", "age": "5 yrs", "species": "Dog", "breed": "Irish Wolfhound", "distance": 45, "location": "Derry", "tags": ["Gentle", "Big"], "bio": "A big softie. Loves slow walks.", "image": "https://images.unsplash.com/photo-1554693190-b894d53759cd?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 4, "name": "Guinness", "age": "1 yr", "species": "Dog", "breed": "Black Lab", "distance": 8, "location": "Lisburn", "tags": ["High Energy", "Fetch"], "bio": "I will retrieve anything you throw!", "image": "https://images.unsplash.com/photo-1561037404-61cd46aa615b?w=800&q=80", "verified": False, "medical": "Vaccinated"},
        {"id": 5, "name": "Potato", "age": "3 yrs", "species": "Dog", "breed": "Corgi", "distance": 60, "location": "Portrush", "tags": ["Sassy", "Beach"], "bio": "Short legs, big personality.", "image": "https://images.unsplash.com/photo-1519098901909-b1553a1190af?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 6, "name": "Mittens", "age": "8 yrs", "species": "Cat", "breed": "Persian", "distance": 5, "location": "Holywood", "tags": ["Chill", "Fluffy"], "bio": "I judge silently but love deeply.", "image": "https://images.unsplash.com/photo-1513245543132-31f507417b26?w=800&q=80", "verified": True, "medical": "Special Diet"},
        {"id": 7, "name": "Rocky", "age": "4 yrs", "species": "Dog", "breed": "Boxer", "distance": 15, "location": "Newtownabbey", "tags": ["Goofy", "Strong"], "bio": "Professional drooler and hugger.", "image": "https://images.unsplash.com/photo-1543071220-6ee5bf71a54e?w=800&q=80", "verified": True, "medical": "Vaccinated"},
        {"id": 8, "name": "Thumper", "age": "1 yr", "species": "Rabbit", "breed": "Lop Eared", "distance": 3, "location": "Belfast East", "tags": ["Quiet", "Hops"], "bio": "Loves carrots and wires (keep them safe!).", "image": "https://images.unsplash.com/photo-1585110396065-88b724108873?w=800&q=80", "verified": False, "medical": "Healthy"},
        {"id": 9, "name": "Bella", "age": "2 yrs", "species": "Dog", "breed": "Cockapoo", "distance": 20, "location": "Antrim", "tags": ["Hypoallergenic", "Cute"], "bio": "Loves everyone I meet!", "image": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=800&q=80", "verified": True, "medical": "Vaccinated"},
        {"id": 10, "name": "Shadow", "age": "6 yrs", "species": "Cat", "breed": "Black Cat", "distance": 10, "location": "Dundonald", "tags": ["Mysterious", "Vocal"], "bio": "I am the night.", "image": "https://images.unsplash.com/photo-1513360371669-4adf3dd7dff8?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 11, "name": "Max", "age": "5 mo", "species": "Dog", "breed": "German Shepherd", "distance": 25, "location": "Larne", "tags": ["Smart", "Puppy"], "bio": "Training to be the best boy.", "image": "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=800&q=80", "verified": False, "medical": "Vaccinated"},
        {"id": 12, "name": "Daisy", "age": "3 yrs", "species": "Dog", "breed": "Beagle", "distance": 30, "location": "Ballymena", "tags": ["Howler", "Foodie"], "bio": "Will follow nose to food.", "image": "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 13, "name": "Simba", "age": "2 yrs", "species": "Cat", "breed": "Ginger Tabby", "distance": 4, "location": "Belfast South", "tags": ["King", "Orange"], "bio": "One brain cell, lots of love.", "image": "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=800&q=80", "verified": True, "medical": "Neutered"},
        {"id": 14, "name": "Cooper", "age": "7 yrs", "species": "Dog", "breed": "Spaniel", "distance": 50, "location": "Coleraine", "tags": ["Water Dog", "Loyal"], "bio": "Beach days are my favorite.", "image": "https://images.unsplash.com/photo-1529429612779-c8e40df2b54c?w=800&q=80", "verified": True, "medical": "Arthritis managed"},
        {"id": 15, "name": "Pip", "age": "1 yr", "species": "Hamster", "breed": "Syrian", "distance": 1, "location": "Belfast West", "tags": ["Tiny", "Runner"], "bio": "Night owl. Loves my wheel.", "image": "https://images.unsplash.com/photo-1425082661705-1834bfd09dca?w=800&q=80", "verified": False, "medical": "Healthy"},
        {"id": 16, "name": "Nala", "age": "4 yrs", "species": "Dog", "breed": "Staffy Mix", "distance": 8, "location": "Castlereagh", "tags": ["Sweet", "Smile"], "bio": "Misunderstood velvet hippo.", "image": "https://images.unsplash.com/photo-1570824104453-508955ab713e?w=800&q=80", "verified": True, "medical": "Vaccinated"},
        {"id": 17, "name": "Oliver", "age": "2 mo", "species": "Cat", "breed": "Siamese Mix", "distance": 18, "location": "Carrickfergus", "tags": ["Baby", "Blue Eyes"], "bio": "Need constant attention.", "image": "https://images.unsplash.com/photo-1513245543132-31f507417b26?w=800&q=80", "verified": True, "medical": "First shots"},
        {"id": 18, "name": "Bear", "age": "9 yrs", "species": "Dog", "breed": "Newfoundland", "distance": 40, "location": "Omagh", "tags": ["Huge", "Fluffy"], "bio": "I'm basically a rug that eats.", "image": "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 19, "name": "Cleo", "age": "3 yrs", "species": "Cat", "breed": "Sphynx", "distance": 6, "location": "Belfast City", "tags": ["Hairless", "Warm"], "bio": "I feel like warm suede. Cuddle me.", "image": "https://images.unsplash.com/photo-1516280030429-27679b3dc9cf?w=800&q=80", "verified": True, "medical": "Skin care needed"},
        {"id": 20, "name": "Buster", "age": "5 yrs", "species": "Dog", "breed": "Jack Russell", "distance": 14, "location": "Comber", "tags": ["Petite", "Energetic"], "bio": "Ball is life.", "image": "https://images.unsplash.com/photo-1596492784531-6e6eb5ea9205?w=800&q=80", "verified": True, "medical": "Vaccinated"},
    ]

# Global State
if 'user' not in st.session_state: 
    st.session_state.user = None
if 'view' not in st.session_state: 
    st.session_state.view = 'auth'
if 'active_tab' not in st.session_state: 
    st.session_state.active_tab = 'Match'
if 'current_pet_index' not in st.session_state: 
    st.session_state.current_pet_index = 0
if 'matches' not in st.session_state: 
    st.session_state.matches = []
if 'happiness' not in st.session_state: 
    st.session_state.happiness = 65
if 'xp' not in st.session_state: 
    st.session_state.xp = 1240
if 'chat_history' not in st.session_state: 
    st.session_state.chat_history = {}
if 'tasks' not in st.session_state:
    st.session_state.tasks = {
        "Morning Walk": {"xp": 50, "completed": False, "icon": "🚶", "desc": "Take a 20m stroll"},
        "Breakfast": {"xp": 30, "completed": False, "icon": "🦴", "desc": "Healthy mix only"},
        "Grooming": {"xp": 20, "completed": False, "icon": "✨", "desc": "Brush that coat"},
        "Health Check": {"xp": 40, "completed": False, "icon": "🩺", "desc": "Check eyes and ears"},
        "Playtime": {"xp": 35, "completed": False, "icon": "🎾", "desc": "15 min of fun"},
        "Evening Walk": {"xp": 50, "completed": False, "icon": "🌙", "desc": "Sunset stroll"},
    }
if 'streak' not in st.session_state:
    st.session_state.streak = 12
if 'last_activity' not in st.session_state:
    st.session_state.last_activity = datetime.now().date()

# --- AUTH FUNCTIONS ---

def login_user(username, password):
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

def signup_user(username, email, password):
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
    st.session_state.user = None
    st.session_state.view = 'auth'
    st.session_state.active_tab = 'Match'
    st.session_state.current_pet_index = 0
    st.toast("Logged out successfully", icon="👋")
    st.rerun()

def upgrade_premium():
    st.session_state.user['is_premium'] = True
    st.balloons()
    st.toast("Welcome to Premium! 🌟", icon="💎")
    time.sleep(0.5)
    st.rerun()

# --- HELPER FUNCTIONS ---

def get_level_progress(xp):
    level = int(xp / 300)
    progress = (xp % 300) / 300
    return level, progress

def handle_swipe(liked, pet):
    if liked:
        st.session_state.matches.append(pet)
        st.session_state.chat_history[pet['id']] = [
            {"role": "assistant", "content": f"Woof! Thanks for swiping right on me! I'm {pet['name']} 🐾"}
        ]
        st.session_state.xp += 25
        st.toast(f"🎉 It's a match with {pet['name']}! ❤️", icon="🎉")
        st.balloons()
    else:
        st.toast("Passed", icon="➡️")
    
    st.session_state.current_pet_index += 1

def toggle_task(task_name):
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

def change_tab(tab_name):
    st.session_state.active_tab = tab_name
    st.rerun()

# --- VIEWS ---

def render_auth():
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="font-size: 3rem; margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                🐾
            </h1>
            <h2 style="color: white; text-shadow: 0 2px 10px rgba(0,0,0,0.3); margin-top: 0.5rem;">
                Pawfect Match NI
            </h2>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem;">
                Find your perfect pet companion
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

def render_swipe_deck(filters):
    all_pets = st.session_state.pets_data
    filtered_pets = [
        p for p in all_pets 
        if (filters['species'] == 'All' or p['species'] == filters['species'])
        and (p['distance'] <= filters['distance'])
    ]

    # PAYWALL LOGIC
    if st.session_state.current_pet_index >= 10 and not st.session_state.user.get('is_premium', False):
        st.markdown("""
        <div class="paywall-container">
            <div style="font-size: 4rem; margin-bottom: 1rem;">💎</div>
            <h1>Premium Access</h1>
            <p style="font-size: 1.2rem; opacity: 0.95;">You've viewed your daily limit of 10 free profiles.</p>
            <p style="font-size: 1.1rem; opacity: 0.9;">Upgrade to see <b>unlimited pets</b>, see who liked you, and more!</p>
            <div style="margin-top: 2rem;">
                <h2 style="font-size: 2.5rem; margin: 0;">£4.99<span style="font-size: 1rem;">/mo</span></h2>
            </div>
        </div>
        <br>
        """, unsafe_allow_html=True)
        if st.button("✨ Upgrade to Premium", type="primary", use_container_width=True):
            upgrade_premium()
        return

    # End of List
    if st.session_state.current_pet_index >= len(filtered_pets):
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">🐶</div>
            <h2>You've reached the end!</h2>
            <p>Check back later for more pets.</p>
            <p style="font-size: 0.9rem; opacity: 0.7;">You've seen all available matches in your area.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Reset & Start Over", type="primary", use_container_width=True):
            st.session_state.current_pet_index = 0
            st.rerun()
        return

    pet = filtered_pets[st.session_state.current_pet_index]
    
    # Enhanced Pet Card
    st.markdown(f"""
    <div class="pet-card">
        <div class="pet-image-container">
            <img src="{pet['image']}" alt="{pet['name']}">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Pet Info Section
    col1, col2 = st.columns([4, 1])
    with col1:
        verified_badge = "🛡️" if pet['verified'] else ""
        st.markdown(f"### {pet['name']}, {pet['age']} {verified_badge}")
        st.caption(f"📍 {pet['location']} • {pet['distance']} miles away")
    
    with col2:
        st.markdown(f"<div style='text-align: right; color: #6b7280; font-size: 0.9rem;'>#{pet['id']}</div>", unsafe_allow_html=True)
    
    # Tags
    badge_html = "".join([f'<span class="badge">{t}</span>' for t in pet['tags']])
    st.markdown(badge_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Bio
    st.markdown(f"<p style='font-size: 1rem; line-height: 1.6; color: #374151;'>{pet['bio']}</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Action Buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("❌", key=f"pass_{pet['id']}", use_container_width=True):
            handle_swipe(False, pet)
            time.sleep(0.2)
            st.rerun()
    with col2:
        if st.button("ℹ️", key=f"info_{pet['id']}", use_container_width=True):
            st.info(f"""
            **Medical Information:**
            {pet['medical']}
            
            **Breed:** {pet['breed']}
            **Species:** {pet['species']}
            """)
    with col3:
        if st.button("❤️", key=f"like_{pet['id']}", use_container_width=True):
            handle_swipe(True, pet)
            time.sleep(0.5)
            st.rerun()

def render_care():
    lvl, prog = get_level_progress(st.session_state.xp)
    
    # Hero Stats Card
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); padding: 2rem; border-radius: 24px; color: white; margin-bottom: 2rem; box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 1rem;">
            <div>
                <h2 style="margin:0; color:white; font-size: 2rem;">Barnaby</h2>
                <p style="opacity:0.9; margin:0; font-size: 1rem;">Level {lvl} Companion 🐾</p>
            </div>
            <div style="text-align:right;">
                <h1 style="margin:0; color:white; font-size: 2.5rem;">{int(prog*100)}%</h1>
                <small style="opacity: 0.8;">XP to Level {lvl+1}</small>
            </div>
        </div>
        <div class="progress-container" style="background: rgba(255,255,255,0.2);">
            <div class="progress-bar" style="width: {prog*100}%;"></div>
        </div>
        <div style="margin-top: 1rem; text-align: center; font-size: 0.9rem; opacity: 0.9;">
            {st.session_state.xp} / {(lvl+1)*300} XP
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">😊</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: #667eea;">{st.session_state.happiness}%</div>
            <div style="font-size: 0.85rem; color: #6b7280; margin-top: 0.25rem;">Happiness</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔥</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: #667eea;">{st.session_state.streak}</div>
            <div style="font-size: 0.85rem; color: #6b7280; margin-top: 0.25rem;">Day Streak</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💚</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: #667eea;">98%</div>
            <div style="font-size: 0.85rem; color: #6b7280; margin-top: 0.25rem;">Health</div>
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
                    <div style="font-size: 2rem;">{details['icon']}</div>
                    <div>
                        <div style="font-weight: 600; font-size: 1rem; color: #1f2937;">{task_name}</div>
                        <div style="font-size: 0.85rem; color: #6b7280; margin-top: 0.25rem;">{details['desc']}</div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 700; color: #667eea; font-size: 0.9rem;">+{details['xp']} XP</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([10, 1])
        with col2:
            st.checkbox("", value=details['completed'], key=task_name, on_change=toggle_task, args=(task_name,), label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)

def render_chat():
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
    
    # Match Selector
    match_names = [m['name'] for m in st.session_state.matches]
    selected_name = st.selectbox("Select a chat:", match_names, label_visibility="collapsed")
    selected_match = next(m for m in st.session_state.matches if m['name'] == selected_name)
    match_id = selected_match['id']
    
    if match_id not in st.session_state.chat_history:
        st.session_state.chat_history[match_id] = []
    
    history = st.session_state.chat_history[match_id]
    
    # Chat Header
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 16px; margin-bottom: 1rem; color: white;">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <img src="{selected_match['image']}" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; border: 2px solid white;">
            <div>
                <div style="font-weight: 600; font-size: 1.1rem;">{selected_match['name']}</div>
                <div style="font-size: 0.85rem; opacity: 0.9;">{selected_match['age']} • {selected_match['location']}</div>
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
                    <img src="{selected_match['image']}" style="width: 35px; height: 35px; border-radius: 50%; object-fit: cover;">
                    <div style="background: #f3f4f6; padding: 0.75rem 1rem; border-radius: 18px; max-width: 70%;">
                        {msg['content']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="display: flex; align-items: start; gap: 0.75rem; margin-bottom: 1rem; justify-content: flex-end;">
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.75rem 1rem; border-radius: 18px; max-width: 70%;">
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
    user = st.session_state.user
    if not user:
        return
    
    st.markdown(f"## 👋 Hello, {user['name']}!")
    
    # Premium Badge
    if user.get('is_premium'):
        st.markdown("""
        <div class="premium-badge">
            💎 Premium Member
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #e5e7eb; color: #374151; padding: 8px 16px; border-radius: 20px; font-weight: 600; font-size: 0.85rem; display: inline-block; margin-bottom: 1rem;">
            Free Plan
        </div>
        """, unsafe_allow_html=True)
    
    st.caption(f"Member since {user['joined']}")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Account Settings
    st.markdown("### ⚙️ Account Settings")
    st.text_input("Email", value=user['email'], disabled=True, key="profile_email")
    
    search_radius = st.slider("Search Radius (miles)", 5, 100, 25, key="search_radius")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Stats Summary
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
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    tabs = {
        'Match': ('🔥', 'Match'),
        'Care': ('🦴', 'Care'),
        'Chat': ('💬', 'Chat'),
        'Profile': ('👤', 'Profile')
    }
    
    with col1:
        active = "active" if st.session_state.active_tab == 'Match' else ""
        if st.button("🔥 Match", key="nav_match", use_container_width=True):
            change_tab('Match')
    with col2:
        if st.button("🦴 Care", key="nav_care", use_container_width=True):
            change_tab('Care')
    with col3:
        if st.button("💬 Chat", key="nav_chat", use_container_width=True):
            change_tab('Chat')
    with col4:
        if st.button("👤 Profile", key="nav_profile", use_container_width=True):
            change_tab('Profile')
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN APP ROUTER ---

if st.session_state.view == 'auth' or st.session_state.user is None:
    render_auth()
else:
    render_nav_bar()
    
    if st.session_state.active_tab == 'Match':
        with st.expander("🔍 Filter Settings", expanded=False):
            species = st.radio("Species", ["All", "Dog", "Cat", "Rabbit", "Hamster"], horizontal=True, key="filter_species")
            dist = st.slider("Max Distance (miles)", 1, 100, 50, key="filter_distance")
        render_swipe_deck({"species": species, "distance": dist})
    
    elif st.session_state.active_tab == 'Care':
        render_care()
    
    elif st.session_state.active_tab == 'Chat':
        render_chat()
    
    elif st.session_state.active_tab == 'Profile':
        render_profile()
