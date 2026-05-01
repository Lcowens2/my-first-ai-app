import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Page Config
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# --- EDITORIAL CSS (Hierarchy, Border, Brown Palette) ---
st.markdown("""
    <style>
    /* 1. Main Background */
    .stApp {
        background: linear-gradient(180deg, #FFF5E1 0%, #FAE9D1 100%);
    }

    /* 2. The Brown Border Frame */
    section.main > div {
        border: 2px solid #8B4513; 
        border-radius: 15px;
        padding: 50px;
        margin: 20px;
        background-color: rgba(255, 255, 255, 0.15);
        box-shadow: 0px 10px 30px rgba(139, 69, 19, 0.05);
    }

    /* 3. Global Brown Typography */
    html, body, [data-testid="stHeader"], p, h1, h2, h3, h4, li, .stSelectbox label, .stTextArea label {
        color: #8B4513 !important; 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* 4. Specific Hierarchy Scaling */
    .radiant-title {
        font-size: 64px !important; /* The Largest Element */
        font-weight: 700 !important;
        line-height: 1.1 !important;
        margin-bottom: 0px !important;
    }
    
    .systems-subtitle {
        font-size: 22px !important; /* Medium/Supporting */
        font-weight: 400 !important;
        letter-spacing: 1px !important;
        margin-bottom: 0px !important;
    }
    
    .purpose-tagline {
        font-size: 18px !important; /* Smallest/Elegant */
        font-style: italic !important;
        opacity: 0.8;
    }

    hr {
        border-top: 1px solid #D2B48C !important;
    }

    /* 5. Modern Button Styling */
    .stButton>button {
        background-color: #8B4513; 
        color: #FFF5E1 !important;
        border-radius: 25px;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 18px;
    }

    /* Input cleaning */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.5);
        border: 1px solid #D2B48C;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Top Right Logo + Refined Typography Layout
col_title, col_logo = st.columns([3, 1])

with col_title:
    # We use custom classes to control exact sizing
    st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="systems-subtitle">L Owens Systems</p>', unsafe_allow_html=True)
    st.markdown('<p class="purpose-tagline">Rewired for Purpose</p>', unsafe_allow_html=True)

with col_logo:
    try:
        # Pulls 'logo.png' from your GitHub folder
        logo = Image.open("logo.png")
        st.image(logo, use_column_width=True)
    except:
        st.write(" ") 

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# 3. Secure API Connection
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.write(" ")

# 4. Identity Lock Interface
st.write("### STEP 1: Identity Lock")
st.write("Upload your professional base photo")
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

st.markdown("---")
st.write("### STEP 2: Editorial Customization")

custom_prompt = st.text_area("Custom Editorial Instructions (Optional)", 
                             placeholder="Add specific brand details here...")

st.write("#### Brand Vibe Selection")
col1, col2 = st.columns(2)

with col1:
    style = st.selectbox("Clothing Aesthetic", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("Shot Composition", ["Headshot", "Full Length", "Freestyle", "Studio"])
    lighting = st.selectbox("Lighting Environment", ["Golden Hour", "Studio Softbox", "Dramatic Cinematic", "Natural Daylight"])

with col2:
    makeup = st.selectbox("Beauty Profile", ["Soft Glam", "Full Glam", "Natural Glow"])
    hair = st.selectbox("Hair Presentation", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("Setting/Theme", ["Modern Office", "High-End Hotel Lobby", "Luxury Yacht", "Penthouse Office"])

# 5. Launch Button
st.markdown("---")
c_left, c_mid, c_right = st.columns([1,1,1])
with c_mid:
    if st.button("Generate My Radiant Image"):
        if uploaded_file is not None:
            st.success("Identity Locked. Processing editorial excellence...")
        else:
            st.warning("Please upload a photo.")
