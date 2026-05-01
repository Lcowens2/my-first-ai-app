import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Page Config
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# --- EDITORIAL LUXE CSS (Cream, Brown, Tan, Gold) ---
st.markdown("""
    <style>
    /* 1. Layered Background (Cream & Tan Gradient) */
    .stApp {
        background: radial-gradient(circle, #FFFDF9 0%, #F3E5D8 100%);
    }

    /* 2. The Luxe Double Border Frame */
    section.main > div {
        border: 1px solid #D4AF37; /* Thin Gold Inner Line */
        outline: 15px solid #5C4033; /* Thick Espresso Outer Frame */
        border-radius: 5px;
        padding: 60px;
        margin: 30px;
        background-color: #FFFDF9; /* Solid Cream Canvas */
        box-shadow: 0px 20px 40px rgba(0,0,0,0.2);
    }

    /* 3. High-End Typography */
    /* Importing a Serif font for the Titles to look like a Magazine */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400&display=swap');

    .radiant-title {
        font-family: 'Playfair Display', serif;
        font-size: 72px !important;
        color: #5C4033 !important; /* Espresso */
        line-height: 1 !important;
        margin-bottom: 5px !important;
    }
    
    .systems-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 20px !important;
        color: #8B7355 !important; /* Muted Tan */
        letter-spacing: 4px !important;
        text-transform: uppercase;
        margin-bottom: 0px !important;
    }
    
    .purpose-tagline {
        font-family: 'Inter', sans-serif;
        font-size: 16px !important;
        color: #D4AF37 !important; /* Gold */
        font-style: italic;
        margin-top: 5px;
    }

    /* 4. Labels and Inputs */
    label, p, .stSelectbox label {
        color: #5C4033 !important;
        font-family: 'Inter', sans-serif;
        font-weight: 400;
    }

    /* 5. The Gold "Radiant" Button */
    .stButton>button {
        background: linear-gradient(145deg, #D4AF37, #B8860B); /* Metallic Gold */
        color: #FFFDF9 !important;
        border-radius: 0px; /* Sharp, modern edges */
        border: 1px solid #5C4033;
        padding: 15px 40px;
        font-family: 'Inter', sans-serif;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #5C4033;
        color: #D4AF37 !important;
    }

    /* Modernizing the Upload Box */
    .stFileUploader {
        border: 1px dashed #D4AF37;
        background-color: #FAF6F1;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Branding Header (Logo Top Right)
col_title, col_logo = st.columns([3, 1])

with col_title:
    st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="systems-subtitle">L Owens Systems</p>', unsafe_allow_html=True)
    st.markdown('<p class="purpose-tagline">Rewired for Purpose</p>', unsafe_allow_html=True)

with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=180)
    except:
        st.write(" ") 

st.markdown("<br><br>", unsafe_allow_html=True)

# 3. App Content
st.write("### I. IDENTITY LOCK")
uploaded_file = st.file_uploader("UPLOAD BASE IMAGE", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

st.markdown("<hr style='border-top: 1px solid #D4AF37;'>", unsafe_allow_html=True)

st.write("### II. EDITORIAL DIRECTION")
custom_prompt = st.text_area("ADDITIONAL SPECIFICATIONS", placeholder="Enter custom details here...")

col1, col2 = st.columns(2)

with col1:
    style = st.selectbox("WARDROBE", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("COMPOSITION", ["Headshot", "Full Length", "Studio"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic"])

with col2:
    makeup = st.selectbox("BEAUTY", ["Soft Glam", "Full Glam", "Natural Glow"])
    hair = st.selectbox("STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "High-End Hotel Lobby", "Luxury Yacht"])

# 4. Action Button
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1,1,1])
with c2:
    if st.button("PRODUCE RADIANT IMAGE"):
        if uploaded_file is not None:
            st.success("AUTHENTICATED. PREPARING EDITORIAL OUTPUT.")
        else:
            st.warning("PLEASE UPLOAD BASE IMAGE.")
