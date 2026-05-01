import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Page Config
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# --- EDITORIAL CSS (Brown Font, Gradient Background, and BORDER) ---
st.markdown("""
    <style>
    /* 1. Main Background */
    .stApp {
        background: linear-gradient(180deg, #FFF5E1 0%, #FAE9D1 100%);
    }

    /* 2. The Brown Border Frame */
    /* This creates a clean line around the central content area */
    section.main > div {
        border: 2px solid #8B4513; 
        border-radius: 15px;
        padding: 40px;
        margin: 20px;
        background-color: rgba(255, 255, 255, 0.2); /* Slight lift from background */
        box-shadow: 0px 10px 30px rgba(139, 69, 19, 0.1);
    }

    /* 3. Global Brown Typography */
    html, body, [data-testid="stHeader"], p, h1, h2, h3, h4, li, .stSelectbox label, .stTextArea label {
        color: #8B4513 !important; 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    hr {
        border-top: 1px solid #D2B48C !important;
    }

    /* 4. Modern Button Styling */
    .stButton>button {
        background-color: #8B4513; 
        color: #FFF5E1 !important;
        border-radius: 25px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }

    /* Clean up the upload box label */
    .stFileUploader label {
        color: #8B4513 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Top Right Logo + Branding
col_title, col_logo = st.columns([3, 1])

with col_title:
    st.markdown("## L Owens Systems")
    st.markdown("#### Radiant Image AI")
    st.markdown("*Rewired for Purpose*")

with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, use_column_width=True)
    except:
        st.write(" ") 

st.markdown("---")

# 3. Secure API Connection
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API Key not found.")

# 4. Identity Lock Interface
st.write("### STEP 1: Identity Lock")
st.write("Upload your professional base photo")
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

st.markdown("---")
st.write("### STEP 2: Editorial Customization")

custom_prompt = st.text_area("Custom Editorial Instructions (Optional)", 
                             placeholder="Add specific details...")

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
