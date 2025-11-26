import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Pawfect Match NI",
    page_icon="🐾",
    layout="wide", # We use wide layout so we can center the "mobile app" in the middle
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS STYLING ---
# Advanced styling to create a "Mobile App" look within the browser
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Simulate Mobile Screen */
    .mobile-container {
        background-color: white;
        padding: 2rem;
        border-radius: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border: 8px solid #1f2937;
        min-height: 800px;
    }

    /* Custom Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        font-weight: bold;
        transition: all 0.2s;
    }
    
    /* specific button colors */
    .pass-btn > button {
        border: 2px solid #ef4444;
        color: #ef4444;
        background: white;
    }
    .pass-btn > button:hover {
        background: #ef4444;
        color: white;
    }
    
    .like-btn > button {
        background: linear-gradient(45deg, #ec4899, #f97316);
        color: white;
        border: none;
    }
    .like-btn > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(236, 72, 153, 0.4);
    }

    /* Badges */
    .badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75em;
        font-weight: 700;
        display: inline-block;
        margin-right: 5px;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-yellow { background-color: #fef3c7; color: #92400e; }
    .badge-purple { background-color: #f3e8ff; color: #6b21a8; }
    .badge-green { background-color: #dcfce7; color: #166534; }
    .badge-blue { background-color: #dbeafe; color: #1e40af; }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #0d9488, #2dd4bf);
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
            "verified": True, "medical": "Vaccinated, Neutered", "badge_class": "badge-yellow"
        },
        {
            "id": 2, "name": "Luna", "age": "4 months", "species": "Cat", "breed": "Domestic Shorthair",
            "distance": 12, "location": "Bangor, Co. Down",
            "tags": ["Cuddly", "Indoor only", "Playful"],
            "bio": "Tiny tiger looking for a warm lap. I purr louder than a passing bus on the Newtownards Road!",
            "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Vaccinated", "badge_class": "badge-purple"
        },
        {
            "id": 3, "name": "Seamus", "age": "5 yrs", "species": "Dog", "breed": "Irish Wolfhound Mix",
            "distance": 45, "location": "Derry/Londonderry",
            "tags": ["Gentle Giant", "Sofa Potato", "Cat Friendly"],
            "bio": "Don't let my size fool you, I'm a big softie. Loves a slow walk along the Peace Bridge.",
            "image": "https://images.unsplash.com/photo-1554693190-b894d53759cd?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Arthritis managed", "badge_class": "badge-green"
        },
        {
            "id": 4, "name": "Guinness", "age": "1 yr", "species": "Dog", "breed": "Black Lab",
            "distance": 8, "location": "Lisburn",
            "tags": ["Water Lover", "Fetch Champion", "High Energy"],
            "bio": "Named after the good stuff. I will retrieve anything you throw, even into the Lagan!",
            "image": "https://images.unsplash.com/photo-1561037404-61cd46aa615b?auto=format&fit=crop&w=800&q=80",
            "verified": False, "medical": "Vaccinated", "badge_class": "badge-blue"
        },
        {
            "id": 5, "name": "Potato", "age": "3 yrs", "species": "Dog", "breed": "Corgi",
            "distance": 60, "location": "Portrush",
            "tags": ["Beach Bum", "Short Legs", "Sassy"],
            "bio": "Living my best life on the North Coast. Looking for someone to share a Poke Bowl with.",
            "image": "https://images.unsplash.com/photo-1519098901909-b1553a1190af?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Healthy", "badge_class": "badge-yellow"
        }
    ]

# --- APP STATE & GAMIFICATION ---
if 'view' not in st.session_state: st.session_state.view = 'onboarding'
if 'current_pet_index' not in st.session_state: st.session_state.current_pet_index = 0
if 'matches' not in st.session_state: st.session_state.matches = []
if 'happiness' not in st.session_state: st.session_state.happiness = 65
if 'xp' not in st.session_state: st.session_state.xp = 1240
if 'level' not in st.session_state: st.session_state.level = 5

# Chat History
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {} # Format: {pet_id: [{"role": "user", "content": "hi"}]}

if 'tasks' not in st.session_state:
    st.session_state.tasks = {
        "Morning Walk": {"xp": 50, "completed": False, "icon": "📍", "desc": "Take a 20m stroll"},
        "Breakfast": {"xp": 30, "completed": False, "icon": "🦴", "desc": "Healthy mix only"},
        "Grooming": {"xp": 20, "completed": False, "icon": "✨", "desc": "Brush that coat"},
        "Health Check": {"xp": 40, "completed": False, "icon": "🩺", "desc": "Check eyes and ears"},
    }

# --- FUNCTIONS ---

def get_level_progress(xp):
    # Simple logic: 300 XP per level
    level = int(xp / 300)
    progress = (xp % 300) / 300
    return level, progress

def handle_swipe(liked, pet):
    if liked:
        st.session_state.matches.append(pet)
        # Initialize chat for this match
        st.session_state.chat_history[pet['id']] = [
            {"role": "assistant", "content": f"Woof! Thanks for swiping right on me! I'm {pet['name']} 🐾"}
        ]
        st.balloons()
        st.toast(f"It's a match with {pet['name']}! ❤️", icon="🎉")
    else:
        st.toast("Pass", icon="❌")
    
    # Move to next
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

def render_onboarding():
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=120)
    st.markdown("""
        <h1 style='color: #0d9488; margin-bottom:0;'>Pawfect Match NI</h1>
        <p style='color: gray; font-size: 1.1em;'>Swipe. Match. Adopt.</p>
        <hr style='margin: 20px 0;'>
    """, unsafe_allow_html=True)
    
    st.info("👋 Welcome! Find your best friend in Northern Ireland.")
    
    col1, col2 = st.columns([1, 10])
    if st.button("Start Adopting 🐾", type="primary"):
        st.session_state.view = 'app'
        st.rerun()

def render_swipe_deck(filters):
    # Filter Logic
    all_pets = st.session_state.pets_data
    filtered_pets = [
        p for p in all_pets 
        if (filters['species'] == 'All' or p['species'] == filters['species'])
        and (p['distance'] <= filters['distance'])
    ]

    # Check if we ran out of cards
    if st.session_state.current_pet_index >= len(filtered_pets):
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.warning("🐶 No more pets match your criteria!")
        if st.button("Reset Filters"):
            st.session_state.current_pet_index = 0
            st.rerun()
        return

    pet = filtered_pets[st.session_state.current_pet_index]

    # Header
    c1, c2 = st.columns([4, 1])
    with c1:
        st.markdown(f"📍 **{pet['location']}** ({pet['distance']}m)")
    with c2:
        st.markdown("⚡ **Boost**")

    # Image Card
    st.image(pet['image'], use_container_width=True)
    
    # Info
    st.markdown(f"### {pet['name']}, {pet['age']} { '🛡️' if pet['verified'] else ''}")
    
    # Badges
    badge_html = "".join([f'<span class="badge {pet["badge_class"]}">{t}</span>' for t in pet['tags']])
    st.markdown(badge_html, unsafe_allow_html=True)
    
    st.caption(pet['bio'])
    
    # Controls
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        # Custom class for styling
        st.markdown('<div class="pass-btn">', unsafe_allow_html=True)
        if st.button("❌", key=f"pass_{pet['id']}"):
            handle_swipe(False, pet)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
         if st.button("ℹ️", key=f"info_{pet['id']}"):
            st.toast("Full profile details would open here!")

    with col3:
        st.markdown('<div class="like-btn">', unsafe_allow_html=True)
        if st.button("❤️ Like", key=f"like_{pet['id']}"):
            handle_swipe(True, pet)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

def render_care():
    # Level Calculation
    lvl, prog = get_level_progress(st.session_state.xp)
    
    # Top Card
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #0d9488 0%, #115e59 100%); padding: 25px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(13, 148, 136, 0.3);">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <h2 style="margin:0; color:white;">Barnaby</h2>
                <p style="opacity:0.8; margin:0;">Golden Retriever Mix</p>
            </div>
            <div style="text-align:right;">
                <h1 style="margin:0; color:white;">Lvl {lvl}</h1>
                <small>{int(prog*100)}% to Lvl {lvl+1}</small>
            </div>
        </div>
        <div style="margin-top:15px; background: rgba(255,255,255,0.2); height: 8px; border-radius: 4px;">
            <div style="width: {prog*100}%; background: #fbbf24; height: 100%; border-radius: 4px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Happiness Stats
    c1, c2, c3 = st.columns(3)
    c1.metric("Happiness", f"{st.session_state.happiness}%", "1.2%")
    c2.metric("Streak", "12 Days", "1")
    c3.metric("Health", "98%", "0.4%")
    
    st.divider()
    
    # Task List
    st.subheader("Daily Tasks")
    for task_name, details in st.session_state.tasks.items():
        with st.container():
            col_icon, col_text, col_check = st.columns([1, 4, 1])
            with col_icon:
                st.markdown(f"<div style='font-size:24px; text-align:center;'>{details['icon']}</div>", unsafe_allow_html=True)
            with col_text:
                st.markdown(f"**{task_name}**")
                st.caption(f"{details['desc']} • +{details['xp']} XP")
            with col_check:
                st.checkbox("Done", value=details['completed'], key=task_name, on_change=toggle_task, args=(task_name,), label_visibility="collapsed")
            st.markdown("<hr style='margin: 5px 0; opacity: 0.1;'>", unsafe_allow_html=True)

def render_chat():
    st.header("Messages 💬")
    
    if not st.session_state.matches:
        st.markdown("""
            <div style="text-align: center; padding: 40px; color: gray;">
                <h2>No matches yet 😢</h2>
                <p>Start swiping to find your pawfect match!</p>
            </div>
        """, unsafe_allow_html=True)
        return

    # Select a match
    match_names = [m['name'] for m in st.session_state.matches]
    selected_name = st.selectbox("Conversation with:", match_names)
    
    # Find selected match object
    selected_match = next(m for m in st.session_state.matches if m['name'] == selected_name)
    match_id = selected_match['id']
    
    # Ensure history exists
    if match_id not in st.session_state.chat_history:
        st.session_state.chat_history[match_id] = []

    # Display Chat History
    history = st.session_state.chat_history[match_id]
    
    chat_container = st.container()
    with chat_container:
        for msg in history:
            avatar = selected_match['image'] if msg['role'] == "assistant" else None
            with st.chat_message(msg['role'], avatar=avatar):
                st.write(msg['content'])
    
    # Chat Input
    if prompt := st.chat_input(f"Message {selected_name}..."):
        # Add user message
        history.append({"role": "user", "content": prompt})
        
        # Simulate bot response
        responses = [
            "Woof! That sounds great!", 
            "I'd love to go for a walk there.", 
            "Do you have treats?", 
            "Can I bring my favorite toy?"
        ]
        history.append({"role": "assistant", "content": random.choice(responses)})
        st.rerun()

def render_ar():
    st.header("AR Preview 📸")
    st.info("Point your camera at a flat surface.")
    
    # Camera "Viewfinder"
    st.markdown("""
    <div style="position: relative; width: 100%; height: 400px; overflow: hidden; border-radius: 20px;">
        <img src="https://images.unsplash.com/photo-1593413941325-1e43b82756f7?auto=format&fit=crop&w=800&q=80" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
             <img src="https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=300&q=80" style="width: 180px; filter: drop-shadow(0 20px 15px rgba(0,0,0,0.4)); border: 3px solid white; border-radius: 10px;">
        </div>
        <div style="position: absolute; bottom: 20px; width: 100%; text-align: center;">
            <div style="width: 60px; height: 60px; background: white; border-radius: 50%; display: inline-block; border: 4px solid rgba(0,0,0,0.2);"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1: st.button("Switch Pet")
    with c2: st.button("Take Photo")

# --- MAIN LAYOUT ---

# Sidebar for "System" Controls
with st.sidebar:
    st.header("⚙️ Preferences")
    
    species_filter = st.radio("I'm looking for:", ["All", "Dog", "Cat"])
    distance_filter = st.slider("Max Distance (miles)", 1, 100, 50)
    
    st.divider()
    st.caption("Pawfect Match v2.0")

# Mobile Container Layout
# This creates the "Phone" box in the center of the screen
col_left, col_center, col_right = st.columns([1, 1.5, 1])

with col_center:
    # Everything happens inside this "Mobile Container"
    # Note: We can't strictly nest st.markdown divs around st.tabs easily, 
    # so we apply the styling globally to the column content via CSS previously.
    
    if st.session_state.view == 'onboarding':
        render_onboarding()
    else:
        # Main App Navigation
        tab_match, tab_care, tab_chat, tab_ar = st.tabs(["🔥 Match", "🦴 Care", "💬 Chat", "📸 AR"])
        
        with tab_match:
            render_swipe_deck({"species": species_filter, "distance": distance_filter})
        
        with tab_care:
            render_care()
            
        with tab_chat:
            render_chat()
            
        with tab_ar:
            render_ar()
