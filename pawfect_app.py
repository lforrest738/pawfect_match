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
    /* This replaces the 'mobile-simulator' to work natively on web & mobile */
    .responsive-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 2rem;
        background: white;
        border-radius: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    
    /* For smaller screens, remove radius and margin */
    @media (max-width: 500px) {
        .responsive-container {
            padding: 1rem;
            border-radius: 0;
            box-shadow: none;
            background: transparent;
        }
        /* Make Streamlit's default padding smaller on mobile */
        .block-container {
            padding-top: 1rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }
    }

    /* Modern Inputs */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        padding: 10px 15px;
    }

    /* Custom Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.2em;
        font-weight: 700;
        transition: transform 0.1s ease;
        border: none;
    }
    .stButton>button:active {
        transform: scale(0.98);
    }
    
    /* Action Buttons */
    .pass-btn > button {
        background-color: #fee2e2;
        color: #ef4444;
    }
    .pass-btn > button:hover {
        background-color: #fecaca;
    }
    
    .like-btn > button {
        background: linear-gradient(135deg, #ec4899 0%, #f97316 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3);
    }
    .like-btn > button:hover {
        opacity: 0.9;
        box-shadow: 0 6px 16px rgba(236, 72, 153, 0.4);
    }

    /* Badges */
    .badge {
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8em;
        font-weight: 600;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 8px;
        background: #f3f4f6;
        color: #374151;
    }
    .badge-highlight {
        background: #e0f2fe;
        color: #0284c7;
    }
    
    /* Card Styling */
    .pet-card {
        border-radius: 24px;
        overflow: hidden;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #f3f4f6;
        border-radius: 20px;
        padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        border-radius: 16px;
        white-space: pre-wrap;
        background-color: transparent;
        border: none;
        color: #6b7280;
    }
    .stTabs [aria-selected="true"] {
        background-color: white;
        color: #0d9488;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'pets_data' not in st.session_state:
    st.session_state.pets_data = [
        {
            "id": 1, "name": "Barnaby", "age": "2 yrs", "species": "Dog", "breed": "Golden Retriever Mix",
            "distance": 2, "location": "Belfast City Center",
            "tags": ["High Energy", "Good with Kids", "Hiker"],
            "bio": "I'm a goofy ball of fluff looking for a hiking buddy for Cave Hill! Verified medical history.",
            "image": "https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Vaccinated, Neutered"
        },
        {
            "id": 2, "name": "Luna", "age": "4 months", "species": "Cat", "breed": "Domestic Shorthair",
            "distance": 12, "location": "Bangor, Co. Down",
            "tags": ["Cuddly", "Indoor only", "Playful"],
            "bio": "Tiny tiger looking for a warm lap. I purr louder than a passing bus on the Newtownards Road!",
            "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Vaccinated"
        },
        {
            "id": 3, "name": "Seamus", "age": "5 yrs", "species": "Dog", "breed": "Irish Wolfhound Mix",
            "distance": 45, "location": "Derry/Londonderry",
            "tags": ["Gentle Giant", "Sofa Potato", "Cat Friendly"],
            "bio": "Don't let my size fool you, I'm a big softie. Loves a slow walk along the Peace Bridge.",
            "image": "https://images.unsplash.com/photo-1554693190-b894d53759cd?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Arthritis managed"
        },
        {
            "id": 4, "name": "Guinness", "age": "1 yr", "species": "Dog", "breed": "Black Lab",
            "distance": 8, "location": "Lisburn",
            "tags": ["Water Lover", "Fetch Champion", "High Energy"],
            "bio": "Named after the good stuff. I will retrieve anything you throw, even into the Lagan!",
            "image": "https://images.unsplash.com/photo-1561037404-61cd46aa615b?auto=format&fit=crop&w=800&q=80",
            "verified": False, "medical": "Vaccinated"
        },
        {
            "id": 5, "name": "Potato", "age": "3 yrs", "species": "Dog", "breed": "Corgi",
            "distance": 60, "location": "Portrush",
            "tags": ["Beach Bum", "Short Legs", "Sassy"],
            "bio": "Living my best life on the North Coast. Looking for someone to share a Poke Bowl with.",
            "image": "https://images.unsplash.com/photo-1519098901909-b1553a1190af?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Healthy"
        }
    ]

# Global State
if 'user' not in st.session_state: st.session_state.user = None
if 'view' not in st.session_state: st.session_state.view = 'auth'
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
    # Mock authentication
    if username and password:
        st.session_state.user = {
            "name": username,
            "email": f"{username}@example.com",
            "joined": "Nov 2025",
            "verified": True
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
            "verified": False # New users aren't verified yet
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

# --- VIEWS ---

def render_auth():
    # Centered Logo
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
        if st.button("Log In", type="primary"):
            login_user(username, password)

    with tab_signup:
        st.markdown("<br>", unsafe_allow_html=True)
        new_user = st.text_input("Choose a Username", key="signup_user")
        new_email = st.text_input("Email Address", key="signup_email")
        new_pass = st.text_input("Choose Password", type="password", key="signup_pass")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Create Account", type="primary"):
            signup_user(new_user, new_email, new_pass)
            
    st.markdown("""
        <div style='text-align: center; margin-top: 2rem; color: #9ca3af; font-size: 0.8rem;'>
            By continuing, you agree to our Terms of Service and Privacy Policy.
        </div>
    """, unsafe_allow_html=True)

def render_swipe_deck(filters):
    all_pets = st.session_state.pets_data
    filtered_pets = [
        p for p in all_pets 
        if (filters['species'] == 'All' or p['species'] == filters['species'])
        and (p['distance'] <= filters['distance'])
    ]

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

    # Card
    with st.container():
        st.image(pet['image'], use_container_width=True, output_format="JPEG")
        
        st.markdown(f"### {pet['name']}, {pet['age']} { '🛡️' if pet['verified'] else ''}")
        st.caption(f"📍 {pet['location']} ({pet['distance']} miles away)")
        
        badge_html = "".join([f'<span class="badge { "badge-highlight" if i==0 else "" }">{t}</span>' for i, t in enumerate(pet['tags'])])
        st.markdown(badge_html, unsafe_allow_html=True)
        
        st.write(pet['bio'])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Action Buttons
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.markdown('<div class="pass-btn">', unsafe_allow_html=True)
            if st.button("❌", key=f"pass_{pet['id']}"):
                handle_swipe(False, pet)
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if st.button("ℹ️", key=f"info_{pet['id']}"):
                st.info("Medical: " + pet['medical'])
        with col3:
            st.markdown('<div class="like-btn">', unsafe_allow_html=True)
            if st.button("❤️ Like", key=f"like_{pet['id']}"):
                handle_swipe(True, pet)
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def render_care():
    lvl, prog = get_level_progress(st.session_state.xp)
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #0d9488 0%, #115e59 100%); padding: 25px; border-radius: 20px; color: white; margin-bottom: 20px;">
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
                st.markdown(f"<div style='font-size:24px;'>{details['icon']}</div>", unsafe_allow_html=True)
            with col_text:
                st.markdown(f"**{task_name}**")
                st.caption(f"+{details['xp']} XP")
            with col_check:
                st.checkbox("Done", value=details['completed'], key=task_name, on_change=toggle_task, args=(task_name,), label_visibility="collapsed")
            st.divider()

def render_profile():
    user = st.session_state.user
    if not user: return

    st.markdown(f"## Hello, {user['name']}!")
    st.caption(f"Member since {user['joined']}")
    
    if user['verified']:
        st.success("Verified Adopter Status Active 🛡️")
    else:
        st.warning("Verification Pending ⏳")
        if st.button("Complete Verification"):
            st.info("Verification docs submitted!")

    st.markdown("### Account Settings")
    st.text_input("Email", value=user['email'], disabled=True)
    st.slider("Search Radius (miles)", 5, 100, 25)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Log Out", type="secondary"):
        logout()

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
        responses = ["Woof!", "I'd love that!", "When are we meeting?", "Do you have snacks?"]
        history.append({"role": "assistant", "content": random.choice(responses)})
        st.rerun()

def render_ar():
    st.header("AR Preview 📸")
    st.image("https://images.unsplash.com/photo-1593413941325-1e43b82756f7?auto=format&fit=crop&w=800&q=80", caption="Living Room Preview", use_container_width=True)
    st.info("AR functionality requires mobile app permissions. This is a web preview.")

# --- MAIN APP ROUTER ---

# Use a centered responsive container logic
col_spacer1, col_main, col_spacer2 = st.columns([1, 6, 1])

# On larger screens, this limits width. On mobile, it takes full width (see CSS).
with col_main:
    st.markdown('<div class="responsive-container">', unsafe_allow_html=True)
    
    if st.session_state.view == 'auth' or st.session_state.user is None:
        render_auth()
    else:
        # App Navigation
        tab1, tab2, tab3, tab4 = st.tabs(["🔥 Match", "🦴 Care", "💬 Chat", "👤 Profile"])
        
        with tab1:
            # Filters in an expander for cleaner UI
            with st.expander("Filter Settings"):
                species = st.radio("Species", ["All", "Dog", "Cat"], horizontal=True)
                dist = st.slider("Distance", 1, 100, 50)
            render_swipe_deck({"species": species, "distance": dist})
        
        with tab2:
            render_care()
            
        with tab3:
            render_chat()
            
        with tab4:
            render_profile()
            
    st.markdown('</div>', unsafe_allow_html=True)
