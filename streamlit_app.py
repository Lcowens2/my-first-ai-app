import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Page Config
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# --- IMMERSIVE BRANDING CSS ---
st.markdown("""
    <style>
    /* 1. Background with Watermark Logo Effect */
    .stApp {
        background: linear-gradient(rgba(255, 253, 249, 0.9), rgba(243, 229, 216, 0.9)), 
                    url("app/static/logo.png"); /* This attempts to pull your logo as a background */
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-size: 60%; /* Large but contained */
    }

    /* 2. Heavy Editorial Border (The Frame) */
    section.main > div {
        border: 2px solid #D4AF37; /* Inner Gold */
        outline: 25px solid #5C4033; /* Extra Thick Espresso Frame */
        border-radius: 0px;
        padding: 80px;
        margin: 50px;
        background-color: rgba(255, 253, 249, 0.85); /* Semi-transparent to let background logo show through */
        box-shadow: 0px 30px 60px rgba(0,0,0,0.3);
    }

    /* 3. Typography Hierarchy */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');

    .radiant-title {
        font-family: 'Playfair Display', serif;
        font-size: 85px !important;
        color: #5C4033 !important;
        line-height: 1 !important;
        margin-bottom: 10px !important;
    }
    
    .systems-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 24px !important;
        color: #8B7355 !important;
        letter-spacing: 6px !important;
        text-transform: uppercase;
        margin-bottom: 5px !important;
    }
    
    .purpose-tagline {
        font-family: 'Inter', sans-serif;
        font-size: 20px !important;
        color: #D4AF37 !important;
        font-style: italic;
    }

    /* 4. Inputs & Modern Styling */
    label, p, .stSelectbox label {
        color: #5C4033 !important;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
    }

    .stButton>button {
        background: linear-gradient(145deg, #D4AF37, #B8860B);
        color: #FFFDF9 !important;
        border-radius: 0px;
        border: 1px solid #5C4033;
        padding: 20px 60px;
        font-family: 'Inter', sans-serif;
        font-size: 20px;
        letter-spacing: 3px;
        text-transform: uppercase;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header: Double Logo Presence
col_title, col_logo = st.columns([2, 1])

with col_title:
    st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="systems-subtitle">L Owens Systems</p>', unsafe_allow_html=True)
    st.markdown('<p class="purpose-tagline">Rewired for Purpose</p>', unsafe_allow_html=True)

with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=300) # Significantly larger logo in the corner
    except:
        st.write(" ") 

st.markdown("<br><br>", unsafe_allow_html=True)

# 3. Step 1: Image & Quantity
st.write("### I. IDENTITY LOCK")
col_file, col_qty = st.columns([2, 1])

with col_file:
    uploaded_file = st.file_uploader("UPLOAD BASE IMAGE", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

with col_qty:
    # NEW: Photo output options
    output_count = st.selectbox("NUMBER OF OUTPUTS", [1, 2, 4])

st.markdown("<hr style='border-top: 2px solid #5C4033;'>", unsafe_allow_html=True)

# 4. Step 2: Customization
st.write("### II. EDITORIAL DIRECTION")
custom_prompt = st.text_area("ADDITIONAL SPECIFICATIONS", placeholder="Detail your specific brand requirements...")

col1, col2 = st.columns(2)

with col1:
    style = st.selectbox("WARDROBE", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("COMPOSITION", ["Headshot", "Full Length", "Editorial Studio"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])

with col2:
    makeup = st.selectbox("BEAUTY", ["Soft Glam", "Full Glam", "Natural Glow"])
    hair = st.selectbox("STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "High-End Hotel Lobby", "Luxury Yacht", "Penthouse View"])

# 5. Execute
st.markdown("<br>", unsafe_allow_html=True)
if st.button("PRODUCE RADIANT ASSETS"):
    if uploaded_file is not None:
        st.success(f"AUTHENTICATED. GENERATING {output_count} PREMIUM ASSETS.")
    else:
        st.warning("PLEASE UPLOAD BASE IMAGE.")
