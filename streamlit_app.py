import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Page Config
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# --- SOFT RADIANT EDITORIAL CSS ---
st.markdown("""
    <style>
    /* 1. Background: Soft Pink to Cream Gradient */
    .stApp {
        background: linear-gradient(135deg, #FDE2E4 0%, #FFF1E6 100%);
    }

    /* 2. The Matte Frame: Soft Brown & Beige */
    section.main > div {
        border: 4px solid #EAD2AC; /* Warm Beige Inner */
        outline: 20px solid #DDB892; /* Soft Tan/Brown Outer */
        border-radius: 30px;
        padding: 70px;
        margin: 40px;
        background-color: rgba(255, 241, 230, 0.9); /* Cream Canvas */
        box-shadow: 0px 15px 35px rgba(88, 47, 14, 0.1);
    }

    /* 3. Typography: Elegant & Rounded (No Black Font) */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600&family=Quicksand:wght@400;600&display=swap');

    .radiant-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 90px !important;
        color: #582F0E !important; /* Cocoa Brown */
        line-height: 0.9 !important;
        font-style: italic;
        margin-bottom: 10px !important;
    }
    
    .systems-subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: 22px !important;
        color: #7F5539 !important; /* Medium Brown */
        letter-spacing: 3px !important;
        text-transform: uppercase;
        margin-bottom: 5px !important;
    }
    
    .purpose-tagline {
        font-family: 'Quicksand', sans-serif;
        font-size: 18px !important;
        color: #B08968 !important; /* Soft Beige-Brown */
        font-weight: 600;
    }

    /* 4. Labels & Buttons (Soft & Rounded) */
    label, p, .stSelectbox label {
        color: #582F0E !important;
        font-family: 'Quicksand', sans-serif;
        font-weight: 600;
    }

    .stButton>button {
        background: #B08968; /* Warm Brown/Tan */
        color: #FFF1E6 !important;
        border-radius: 50px; /* Fully rounded/soft */
        border: none;
        padding: 15px 50px;
        font-family: 'Quicksand', sans-serif;
        font-size: 18px;
        font-weight: bold;
        transition: 0.4s ease;
    }
    
    .stButton>button:hover {
        background: #FDE2E4;
        color: #582F0E !important;
        border: 1px solid #582F0E;
    }

    /* Softening the Input fields */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea {
        background-color: #FFF1E6;
        border-radius: 15px;
        border: 1px solid #EAD2AC;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Branding
col_title, col_logo = st.columns([2, 1])

with col_title:
    st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="systems-subtitle">L Owens Systems</p>', unsafe_allow_html=True)
    st.markdown('<p class="purpose-tagline">Rewired for Purpose</p>', unsafe_allow_html=True)

with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=280) 
    except:
        st.write(" ") 

st.markdown("<br>", unsafe_allow_html=True)

# 3. Step 1: Identity & Quantity
st.write("### I. IDENTITY LOCK")
col_file, col_qty = st.columns([2, 1])

with col_file:
    uploaded_file = st.file_uploader("UPLOAD BASE IMAGE", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

with col_qty:
    output_count = st.selectbox("NUMBER OF OUTPUTS", [1, 2, 4])

st.markdown("<hr style='border-top: 1px solid #EAD2AC;'>", unsafe_allow_html=True)

# 4. Step 2: Customization
st.write("### II. EDITORIAL DIRECTION")
custom_prompt = st.text_area("ADDITIONAL SPECIFICATIONS", placeholder="How can we refine your look today?")

col1, col2 = st.columns(2)

with col1:
    style = st.selectbox("WARDROBE", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("COMPOSITION", ["Headshot", "Full Length", "Editorial Studio"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])

with col2:
    makeup = st.selectbox("BEAUTY", ["Soft Glam", "Full Glam", "Natural Glow"])
    hair = st.selectbox("STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "High-End Hotel Lobby", "Luxury Yacht", "Penthouse View"])

# 5. Launch Button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file is not None:
        st.success(f"SUCCESS. YOUR {output_count} ASSETS ARE BEING CRAFTED.")
    else:
        st.warning("PLEASE UPLOAD A BASE IMAGE TO BEGIN.")
