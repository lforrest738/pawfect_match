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
# Streamlit is strictly Python, so we inject some CSS to make it look more like an "App"
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        font-weight: bold;
    }
    .badge {
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8em;
        font-weight: bold;
        display: inline-block;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    .badge-yellow { background-color: #fef3c7; color: #92400e; }
    .badge-purple { background-color: #f3e8ff; color: #6b21a8; }
    .badge-green { background-color: #dcfce7; color: #166534; }
    .badge-blue { background-color: #dbeafe; color: #1e40af; }
    .badge-red { background-color: #fee2e2; color: #991b1b; }
    
    .card-container {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 1px solid #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)

# --- MOCK DATA ---
if 'pets_data' not in st.session_state:
    st.session_state.pets_data = [
        {
            "id": 1, "name": "Barnaby", "age": "2 yrs", "breed": "Golden Retriever Mix",
            "distance": "2 miles away", "location": "Belfast City Center",
            "tags": ["High Energy", "Good with Kids", "Loves Mournes"],
            "bio": "I'm a goofy ball of fluff looking for a hiking buddy for Cave Hill! Verified medical history.",
            "image": "https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Vaccinated, Neutered", "badge_class": "badge-yellow"
        },
        {
            "id": 2, "name": "Luna", "age": "4 months", "breed": "Domestic Shorthair",
            "distance": "12 miles away", "location": "Bangor, Co. Down",
            "tags": ["Cuddly", "Indoor only", "Playful"],
            "bio": "Tiny tiger looking for a warm lap. I purr louder than a passing bus on the Newtownards Road!",
            "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Vaccinated", "badge_class": "badge-purple"
        },
        {
            "id": 3, "name": "Seamus", "age": "5 yrs", "breed": "Irish Wolfhound Mix",
            "distance": "45 miles away", "location": "Derry/Londonderry",
            "tags": ["Gentle Giant", "Sofa Potato", "Good with Cats"],
            "bio": "Don't let my size fool you, I'm a big softie. Loves a slow walk along the Peace Bridge.",
            "image": "https://images.unsplash.com/photo-1554693190-b894d53759cd?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Arthritis managed", "badge_class": "badge-green"
        },
        {
            "id": 4, "name": "Guinness", "age": "1 yr", "breed": "Black Lab",
            "distance": "8 miles away", "location": "Lisburn",
            "tags": ["Water Lover", "Fetch Champion", "High Energy"],
            "bio": "Named after the good stuff. I will retrieve anything you throw, even into the Lagan!",
            "image": "https://images.unsplash.com/photo-1561037404-61cd46aa615b?auto=format&fit=crop&w=800&q=80",
            "verified": False, "medical": "Vaccinated", "badge_class": "badge-blue"
        },
        {
            "id": 5, "name": "Potato", "age": "3 yrs", "breed": "Corgi",
            "distance": "60 miles away", "location": "Portrush",
            "tags": ["Beach Bum", "Short Legs", "Sassy"],
            "bio": "Living my best life on the North Coast. Looking for someone to share a Poke Bowl with.",
            "image": "https://images.unsplash.com/photo-1519098901909-b1553a1190af?auto=format&fit=crop&w=800&q=80",
            "verified": True, "medical": "Healthy", "badge_class": "badge-yellow"
        }
    ]

# --- STATE MANAGEMENT ---
# Streamlit needs 'session_state' to remember variables between clicks
if 'view' not in st.session_state:
    st.session_state.view = 'onboarding'
if 'current_pet_index' not in st.session_state:
    st.session_state.current_pet_index = 0
if 'matches' not in st.session_state:
    st.session_state.matches = []
if 'happiness' not in st.session_state:
    st.session_state.happiness = 65
if 'xp' not in st.session_state:
    st.session_state.xp = 1240
if 'tasks' not in st.session_state:
    st.session_state.tasks = {
        "Morning Walk": {"xp": 50, "completed": False, "icon": "📍"},
        "Breakfast": {"xp": 30, "completed": False, "icon": "🦴"},
        "Grooming": {"xp": 20, "completed": False, "icon": "✨"},
        "Health Check": {"xp": 40, "completed": False, "icon": "🩺"},
    }

# --- FUNCTIONS ---

def handle_swipe(liked):
    current_idx = st.session_state.current_pet_index
    pets = st.session_state.pets_data
    
    if liked:
        # Add to matches
        pet = pets[current_idx]
        st.session_state.matches.append(pet)
        st.balloons() # Fun Streamlit effect
        st.toast(f"It's a match with {pet['name']}! ❤️", icon="🎉")
        time.sleep(1) # Pause to let user see effect
        
    # Move to next pet
    if current_idx < len(pets) - 1:
        st.session_state.current_pet_index += 1
    else:
        st.info("That's everyone in Northern Ireland!")
        st.session_state.current_pet_index = 0 # Loop back

def toggle_task(task_name):
    task = st.session_state.tasks[task_name]
    if not task["completed"]:
        task["completed"] = True
        st.session_state.xp += task["xp"]
        st.session_state.happiness = min(100, st.session_state.happiness + 10)
        st.success(f"Completed {task_name}! +{task['xp']} XP")
    else:
        # Allow unticking for demo purposes
        task["completed"] = False
        st.session_state.xp -= task["xp"]
        st.session_state.happiness = max(0, st.session_state.happiness - 10)

# --- VIEWS ---

def show_onboarding():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=150)
        st.markdown("<h1 style='text-align: center; color: #0d9488;'>Pawfect Match NI</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Find your best friend in Northern Ireland, gamify their care, and build a happy life together.</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Start Adopting 🐾", type="primary"):
            st.session_state.view = 'app'
            st.rerun()

def show_swipe_deck():
    pets = st.session_state.pets_data
    idx = st.session_state.current_pet_index
    pet = pets[idx]

    # Location Header
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("📍"):
             st.toast("Locating you in Belfast...", icon="📡")
    with col2:
        st.markdown(f"**Near You** • Boost Active ⚡")

    # Pet Card
    with st.container():
        st.image(pet['image'], use_container_width=True)
        
        st.markdown(f"""
        <div class="card-container">
            <h2>{pet['name']}, {pet['age']} { '🛡️' if pet['verified'] else ''}</h2>
            <p style='color: gray;'>📍 {pet['location']} ({pet['distance']})</p>
            <div style='margin-bottom: 15px;'>
                {''.join([f'<span class="badge {pet["badge_class"]}">{tag}</span>' for tag in pet['tags']])}
            </div>
            <p><i>{pet['bio']}</i></p>
            <hr>
            <small>🩺 {pet['medical']}</small>
        </div>
        """, unsafe_allow_html=True)

    # Controls
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("❌", key="pass"):
            handle_swipe(False)
            st.rerun()
    with c2:
        if st.button("ℹ️"):
            st.info(f"More details about {pet['name']} coming soon!")
    with c3:
        if st.button("❤️", type="primary", key="love"):
            handle_swipe(True)
            st.rerun()

def show_care_dashboard():
    # Header
    st.markdown(f"""
    <div style="background-color: #0d9488; padding: 20px; border-radius: 20px; color: white; margin-bottom: 20px;">
        <h2>Barnaby's Care</h2>
        <p>Level 5 Companion • {st.session_state.streak if 'streak' in st.session_state else 12} Day Streak 🔥</p>
    </div>
    """, unsafe_allow_html=True)

    # Happiness
    st.subheader("Happiness Level")
    st.progress(st.session_state.happiness / 100)
    st.caption(f"Current Happiness: {st.session_state.happiness}% - { 'Fantastic!' if st.session_state.happiness > 70 else 'Needs playtime.'}")

    st.markdown("---")

    # Tasks
    st.subheader(f"Daily Checklist (XP: {st.session_state.xp})")
    
    for task_name, details in st.session_state.tasks.items():
        cols = st.columns([1, 5, 2])
        with cols[0]:
            st.write(details['icon'])
        with cols[1]:
            st.write(f"**{task_name}** (+{details['xp']} XP)")
        with cols[2]:
            # Checkbox logic
            is_checked = st.checkbox(
                "Done", 
                value=details['completed'], 
                key=task_name,
                on_change=toggle_task,
                args=(task_name,)
            )

def show_chat():
    st.header("Messages 💬")
    if not st.session_state.matches:
        st.info("No matches yet! Go swipe on some pets.")
    else:
        for match in st.session_state.matches:
            with st.expander(f"{match['name']} ({match['breed']})"):
                c1, c2 = st.columns([1,3])
                with c1:
                    st.image(match['image'], width=80)
                with c2:
                    st.write("You matched! Send a message to start the adoption process.")
                    st.text_input(f"Message {match['name']}...", key=f"msg_{match['id']}")
                    if st.button("Send", key=f"btn_{match['id']}"):
                        st.success("Message sent!")

def show_ar_preview():
    st.header("AR Preview 📸")
    st.info("Point your camera at a flat surface to place the pet.")
    
    # Mock AR using an overlaid image
    st.image("https://images.unsplash.com/photo-1593413941325-1e43b82756f7?auto=format&fit=crop&w=800&q=80", caption="Living Room Preview")
    
    st.markdown("""
    <div style="text-align: center; margin-top: -200px; margin-bottom: 100px; position: relative; z-index: 99;">
        <img src="https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=300&q=80" 
        style="width: 150px; border-radius: 10px; box-shadow: 0 10px 20px rgba(0,0,0,0.5); border: 3px solid white;">
        <br><br>
        <span style="background: white; padding: 5px 10px; border-radius: 10px; font-weight: bold;">Barnaby placed!</span>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN APP LOGIC ---

if st.session_state.view == 'onboarding':
    show_onboarding()

elif st.session_state.view == 'app':
    # Streamlit Tab Navigation acts as the "Bottom Bar"
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔥 Match", "🦴 Care", "💬 Chat", "👤 Profile", "📸 AR"])
    
    with tab1:
        show_swipe_deck()
    
    with tab2:
        show_care_dashboard()
        
    with tab3:
        show_chat()
        
    with tab4:
        st.header("My Profile")
        col1, col2 = st.columns([1,3])
        with col1:
             st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80", width=100)
        with col2:
             st.subheader("Sarah Jenkins")
             st.success("Verified Adopter 🛡️")
        
        st.info("Premium Member 💎")
        st.button("Account Settings")
        if st.button("Log Out"):
            st.session_state.view = 'onboarding'
            st.rerun()

    with tab5:
        show_ar_preview()
