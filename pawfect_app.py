import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Pawfect Match NI",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #f3f4f6;
    }
    
    /* Responsive Main Container */
    .responsive-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 2rem;
        background: white;
        border-radius: 24px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        min-height: 80vh;
        display: flex;
        flex-direction: column;
    }
    
    @media (max-width: 500px) {
        .responsive-container {
            padding: 1rem;
            border-radius: 0;
            box-shadow: none;
            background: transparent;
        }
    }

    /* Custom Navigation Bar */
    .nav-button {
        border-radius: 15px;
        border: none;
        background: transparent;
        color: #6b7280;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s;
    }
    /* Streamlit button override for nav */
    div[data-testid="column"] > div > div > div > div > .stButton > button {
        border-radius: 12px;
        border: none;
        box-shadow: none;
        background: #f9fafb;
        color: #6b7280;
        font-size: 0.9rem;
        padding: 0.5rem;
    }
    div[data-testid="column"] > div > div > div > div > .stButton > button:hover {
        background: #f3f4f6;
        color: #0d9488;
    }
    div[data-testid="column"] > div > div > div > div > .stButton > button:focus {
        border: none;
        outline: none;
        color: #0d9488;
        background: #ccfbf1;
    }

    /* Action Buttons (Like/Pass) */
    .action-btn > button {
        border-radius: 50px !important;
        height: 3.5rem !important;
        font-size: 1.2rem !important;
        transition: transform 0.2s !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    .pass-btn > button {
        background: white !important;
        border: 2px solid #fee2e2 !important;
        color: #ef4444 !important;
    }
    .pass-btn > button:hover {
        background: #fee2e2 !important;
        transform: scale(1.05);
    }
    
    .like-btn > button {
        background: linear-gradient(135deg, #ec4899 0%, #f97316 100%) !important;
        color: white !important;
        border: none !important;
    }
    .like-btn > button:hover {
        opacity: 0.9;
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(236, 72, 153, 0.3) !important;
    }

    /* Primary Actions */
    .stButton > button {
        border-radius: 12px;
        font-weight: bold;
    }

    /* Badges */
    .badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
        margin-right: 4px;
        margin-bottom: 6px;
        background: #f3f4f6;
        color: #4b5563;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Paywall Styling */
    .paywall-container {
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(79, 70, 229, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---

# Expanded Data Set (20 Animals)
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
        {"id": 10, "name": "Shadow", "age": "6 yrs", "species": "Cat", "breed": "Bombay", "distance": 10, "location": "Dundonald", "tags": ["Mysterious", "Vocal"], "bio": "I am the night.", "image": "https://images.unsplash.com/photo-1513360371669-4adf3dd7dff8?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 11, "name": "Max", "age": "5 mo", "species": "Dog", "breed": "German Shepherd", "distance": 25, "location": "Larne", "tags": ["Smart", "Puppy"], "bio": "Training to be the best boy.", "image": "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=800&q=80", "verified": False, "medical": "Vaccinated"},
        {"id": 12, "name": "Daisy", "age": "3 yrs", "species": "Dog", "breed": "Beagle", "distance": 30, "location": "Ballymena", "tags": ["Howler", "Foodie"], "bio": "Will follow nose to food.", "image": "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 13, "name": "Simba", "age": "2 yrs", "species": "Cat", "breed": "Ginger Tabby", "distance": 4, "location": "Belfast South", "tags": ["King", "Orange"], "bio": "One brain cell, lots of love.", "image": "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=800&q=80", "verified": True, "medical": "Neutered"},
        {"id": 14, "name": "Cooper", "age": "7 yrs", "species": "Dog", "breed": "Spaniel", "distance": 50, "location": "Coleraine", "tags": ["Water Dog", "Loyal"], "bio": "Beach days are my favorite.", "image": "https://images.unsplash.com/photo-1529429612779-c8e40df2b54c?w=800&q=80", "verified": True, "medical": "Arthritis managed"},
        {"id": 15, "name": "Pip", "age": "1 yr", "species": "Hamster", "breed": "Syrian", "distance": 1, "location": "Belfast West", "tags": ["Tiny", "Runner"], "bio": "Night owl. Loves my wheel.", "image": "https://images.unsplash.com/photo-1425082661705-1834bfd09dca?w=800&q=80", "verified": False, "medical": "Healthy"},
        {"id": 16, "name": "Nala", "age": "4 yrs", "species": "Dog", "breed": "Pitbull Mix", "distance": 8, "location": "Castlereagh", "tags": ["Sweet", "Smile"], "bio": "Misunderstood velvet hippo.", "image": "https://images.unsplash.com/photo-1570824104453-508955ab713e?w=800&q=80", "verified": True, "medical": "Vaccinated"},
        {"id": 17, "name": "Oliver", "age": "2 mo", "species": "Cat", "breed": "Siamese Mix", "distance": 18, "location": "Carrickfergus", "tags": ["Baby", "Blue Eyes"], "bio": "Need constant attention.", "image": "https://images.unsplash.com/photo-1513245543132-31f507417b26?w=800&q=80", "verified": True, "medical": "First shots"},
        {"id": 18, "name": "Bear", "age": "9 yrs", "species": "Dog", "breed": "Newfoundland", "distance": 40, "location": "Omagh", "tags": ["Huge", "Fluffy"], "bio": "I'm basically a rug that eats.", "image": "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?w=800&q=80", "verified": True, "medical": "Healthy"},
        {"id": 19, "name": "Cleo", "age": "3 yrs", "species": "Cat", "breed": "Sphynx", "distance": 6, "location": "Belfast City", "tags": ["Hairless", "Warm"], "bio": "I feel like warm suede. Cuddle me.", "image": "https://images.unsplash.com/photo-1516280030429-27679b3dc9cf?w=800&q=80", "verified": True, "medical": "Skin care needed"},
        {"id": 20, "name": "Buster", "age": "5 yrs", "species": "Dog", "breed": "Jack Russell", "distance": 14, "location": "Comber", "tags": ["Fast", "Digging"], "bio": "Ball is life.", "image": "https://images.unsplash.com/photo-1596492784531-6e6eb5ea9205?w=800&q=80", "verified": True, "medical": "Vaccinated"},
    ]

# Global State
if 'user' not in st.session_state: st.session_state.user = None
if 'view' not in st.session_state: st.session_state.view = 'auth'
if 'active_tab' not in st.session_state: st.session_state.active_tab = 'Match' # NAVIGATION STATE
if 'current_pet_index' not in st.session_state: st.session_state.current_pet_index = 0
if 'matches' not in st.session_state: st.session_state.matches = []
if 'happiness' not in st.session_state: st.session_state.happiness = 65
if 'xp' not in st.session_state: st.session_state.xp = 1240
if 'chat_history' not in st.session_state: st.session_state.chat_history = {}
if 'tasks' not in st.session_state:
    st.session_state.tasks = {
        "Morning Walk": {"xp": 50, "completed": False, "icon": "📍", "desc": "Take a 20m stroll"},
        "Breakfast": {"xp": 30, "completed": False, "icon": "🦴", "desc": "Healthy mix only"},
        "Grooming": {"xp": 20, "completed": False, "icon": "✨", "desc": "Brush that coat"},
        "Health Check": {"xp": 40, "completed": False, "icon": "🩺", "desc": "Check eyes and ears"},
    }

# --- AUTH FUNCTIONS ---

def login_user(username, password):
    if username and password:
        st.session_state.user = {
            "name": username,
            "email": f"{username}@example.com",
            "joined": "Nov 2025",
            "verified": True,
            "is_premium": False # Default to Free Tier
        }
        st.session_state.view = 'app'
        st.toast(f"Welcome back, {username}!", icon="👋")
        st.rerun()
    else:
        st.error("Please enter both username and password.")

def signup_user(username, email, password):
    if username and email and password:
        st.session_state.user = {
            "name": username,
            "email": email,
            "joined": "Nov 2025",
            "verified": False,
            "is_premium": False
        }
        st.session_state.view = 'app'
        st.toast(f"Account created! Welcome, {username}!", icon="🎉")
        st.balloons()
        st.rerun()
    else:
        st.error("Please fill in all fields.")

def logout():
    st.session_state.user = None
    st.session_state.view = 'auth'
    st.session_state.active_tab = 'Match'
    st.rerun()

def upgrade_premium():
    st.session_state.user['is_premium'] = True
    st.balloons()
    st.toast("Welcome to Premium! 🌟", icon="💎")
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
        st.toast(f"It's a match with {pet['name']}! ❤️", icon="🎉")
    else:
        st.toast("Pass", icon="❌")
    
    st.session_state.current_pet_index += 1

def toggle_task(task_name):
    task = st.session_state.tasks[task_name]
    if not task["completed"]:
        task["completed"] = True
        st.session_state.xp += task["xp"]
        st.session_state.happiness = min(100, st.session_state.happiness + 15)
        st.success(f"Completed {task_name}! +{task['xp']} XP")
    else:
        task["completed"] = False
        st.session_state.xp -= task["xp"]
        st.session_state.happiness = max(0, st.session_state.happiness - 15)

def change_tab(tab_name):
    st.session_state.active_tab = tab_name

# --- VIEWS ---

def render_auth():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=100)
        st.markdown("<h2 style='text-align: center; color: #0d9488;'>Pawfect Match NI</h2>", unsafe_allow_html=True)

    tab_login, tab_signup = st.tabs(["Log In", "Sign Up"])
    with tab_login:
        st.markdown("<br>", unsafe_allow_html=True)
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Log In", type="primary"): login_user(username, password)
    with tab_signup:
        st.markdown("<br>", unsafe_allow_html=True)
        new_user = st.text_input("Choose a Username", key="signup_user")
        new_email = st.text_input("Email Address", key="signup_email")
        new_pass = st.text_input("Choose Password", type="password", key="signup_pass")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Create Account", type="primary"): signup_user(new_user, new_email, new_pass)

def render_swipe_deck(filters):
    all_pets = st.session_state.pets_data
    filtered_pets = [
        p for p in all_pets 
        if (filters['species'] == 'All' or p['species'] == filters['species'])
        and (p['distance'] <= filters['distance'])
    ]

    # PAYWALL LOGIC
    # Limit to 10 profiles if not premium
    if st.session_state.current_pet_index >= 10 and not st.session_state.user.get('is_premium', False):
        st.markdown("""
        <div class="paywall-container">
            <h1>💎 Premium Access</h1>
            <p>You've viewed your daily limit of 10 free profiles.</p>
            <p>Upgrade to see <b>unlimited pets</b>, see who liked you, and more!</p>
        </div>
        <br>
        """, unsafe_allow_html=True)
        if st.button("Upgrade to Premium (£4.99/mo)", type="primary"):
            upgrade_premium()
        return

    # End of List
    if st.session_state.current_pet_index >= len(filtered_pets):
        st.markdown("""
        <div style="text-align:center; padding: 40px;">
            <h2>You've reached the end! 🐶</h2>
            <p>Check back later for more pets.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Reset Filters"):
            st.session_state.current_pet_index = 0
            st.rerun()
        return

    pet = filtered_pets[st.session_state.current_pet_index]

    with st.container():
        # Card Header
        c1, c2 = st.columns([3, 1])
        with c1: st.caption(f"📍 {pet['location']} ({pet['distance']} mi)")
        with c2: st.markdown(f"**#{pet['id']}**")

        st.image(pet['image'], use_container_width=True, output_format="JPEG")
        
        st.markdown(f"### {pet['name']}, {pet['age']} { '🛡️' if pet['verified'] else ''}")
        
        badge_html = "".join([f'<span class="badge">{t}</span>' for t in pet['tags']])
        st.markdown(badge_html, unsafe_allow_html=True)
        
        st.write(pet['bio'])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Nicer Action Buttons
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.markdown('<div class="action-btn pass-btn">', unsafe_allow_html=True)
            if st.button("❌", key=f"pass_{pet['id']}"):
                handle_swipe(False, pet)
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div style="text-align:center; padding-top:10px;">', unsafe_allow_html=True)
            if st.button("ℹ️", key=f"info_{pet['id']}"):
                st.info("Medical: " + pet['medical'])
            st.markdown('</div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="action-btn like-btn">', unsafe_allow_html=True)
            if st.button("❤️ Match", key=f"like_{pet['id']}"):
                handle_swipe(True, pet)
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def render_care():
    lvl, prog = get_level_progress(st.session_state.xp)
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #0d9488 0%, #115e59 100%); padding: 25px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 5px 15px rgba(13, 148, 136, 0.4);">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <h2 style="margin:0; color:white;">Barnaby</h2>
                <p style="opacity:0.8; margin:0;">Level {lvl} Companion</p>
            </div>
            <div style="text-align:right;">
                <h1 style="margin:0; color:white;">{int(prog*100)}%</h1>
                <small>XP to Lvl {lvl+1}</small>
            </div>
        </div>
        <div style="margin-top:15px; background: rgba(255,255,255,0.2); height: 8px; border-radius: 4px;">
            <div style="width: {prog*100}%; background: #fbbf24; height: 100%; border-radius: 4px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Happiness", f"{st.session_state.happiness}%", "1.2%")
    c2.metric("Streak", "12 Days", "1")
    c3.metric("Health", "98%", "0.4%")
    
    st.subheader("Daily Tasks")
    for task_name, details in st.session_state.tasks.items():
        with st.container():
            col_icon, col_text, col_check = st.columns([1, 5, 1])
            with col_icon:
                st.markdown(f"<div style='font-size:24px; padding-top:5px;'>{details['icon']}</div>", unsafe_allow_html=True)
            with col_text:
                st.markdown(f"**{task_name}**")
                st.caption(f"+{details['xp']} XP")
            with col_check:
                st.checkbox("Done", value=details['completed'], key=task_name, on_change=toggle_task, args=(task_name,), label_visibility="collapsed")
            st.divider()

def render_chat():
    st.header("Messages 💬")
    
    if not st.session_state.matches:
        st.markdown("<div style='text-align:center; padding:2rem; color:gray;'>No matches yet! Go swipe ❤️</div>", unsafe_allow_html=True)
        return

    match_names = [m['name'] for m in st.session_state.matches]
    selected_name = st.selectbox("Select Chat:", match_names)
    selected_match = next(m for m in st.session_state.matches if m['name'] == selected_name)
    match_id = selected_match['id']
    
    if match_id not in st.session_state.chat_history:
        st.session_state.chat_history[match_id] = []

    history = st.session_state.chat_history[match_id]
    
    with st.container():
        for msg in history:
            avatar = selected_match['image'] if msg['role'] == "assistant" else None
            with st.chat_message(msg['role'], avatar=avatar):
                st.write(msg['content'])
    
    if prompt := st.chat_input("Type a message..."):
        history.append({"role": "user", "content": prompt})
        responses = ["Woof!", "I'd love that!", "When are we meeting?", "Do you have snacks?", "Can I bring my toy?", "That sounds pawsome!"]
        history.append({"role": "assistant", "content": random.choice(responses)})
        st.rerun()

def render_profile():
    user = st.session_state.user
    if not user: return

    st.markdown(f"## Hello, {user['name']}!")
    
    # Premium Badge
    if user.get('is_premium'):
        st.markdown("""
        <div style="background: linear-gradient(45deg, #4f46e5, #9333ea); color: white; padding: 10px 20px; border-radius: 10px; display: inline-block; font-weight: bold; margin-bottom: 15px;">
            💎 Premium Member
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: #e5e7eb; color: #374151; padding: 10px 20px; border-radius: 10px; display: inline-block; font-weight: bold; margin-bottom: 15px;">
            Free Plan
        </div>
        """, unsafe_allow_html=True)

    st.caption(f"Member since {user['joined']}")
    
    st.markdown("### Account Settings")
    st.text_input("Email", value=user['email'], disabled=True)
    st.slider("Search Radius (miles)", 5, 100, 25)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Log Out"):
        logout()

def render_nav_bar():
    # This replaces st.tabs for state persistence
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    # Simple logic to highlight active tab could be added via CSS if we passed 'key' args differently
    # But for now, simple buttons work robustly.
    with col1:
        if st.button("🔥 Match", key="nav_match", use_container_width=True): change_tab('Match')
    with col2:
        if st.button("🦴 Care", key="nav_care", use_container_width=True): change_tab('Care')
    with col3:
        if st.button("💬 Chat", key="nav_chat", use_container_width=True): change_tab('Chat')
    with col4:
        if st.button("👤 Profile", key="nav_profile", use_container_width=True): change_tab('Profile')

# --- MAIN APP ROUTER ---

col_spacer1, col_main, col_spacer2 = st.columns([1, 6, 1])

with col_main:
    st.markdown('<div class="responsive-container">', unsafe_allow_html=True)
    
    if st.session_state.view == 'auth' or st.session_state.user is None:
        render_auth()
    else:
        # 1. Custom Navigation Bar (Top)
        # We put it at top or bottom. Mobile apps often have bottom nav, but top is cleaner in Streamlit web view.
        # Let's try top for clarity.
        render_nav_bar()
        
        # 2. Content Area
        if st.session_state.active_tab == 'Match':
            with st.expander("Filter Settings"):
                species = st.radio("Species", ["All", "Dog", "Cat", "Rabbit", "Hamster"], horizontal=True)
                dist = st.slider("Distance", 1, 100, 50)
            render_swipe_deck({"species": species, "distance": dist})
        
        elif st.session_state.active_tab == 'Care':
            render_care()
            
        elif st.session_state.active_tab == 'Chat':
            render_chat()
            
        elif st.session_state.active_tab == 'Profile':
            render_profile()
            
    st.markdown('</div>', unsafe_allow_html=True)
