import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Page Config & Professional Branding
st.set_page_config(page_title="Radiant Image AI", page_icon="✨", layout="wide")

# --- HIGH-END EDITORIAL CSS (Modern, Classy, Brown Font) ---
st.markdown("""
    <style>
    /* 1. Classy Gradient Background (Cream to softer Peach) */
    .stApp {
        background: linear-gradient(180deg, #FFF5E1 0%, #FAE9D1 100%);
    }

    /* 2. Professional BROWN Font Color for everything */
    html, body, [data-testid="stHeader"], p, h1, h2, h3, h4, li, .stSelectbox label, .stTextArea label {
        color: #8B4513 !important; /* Saddle Brown */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* 3. Classy, Subtle Dividers */
    hr {
        border-top: 1px solid #D2B48C !important;
    }

    /* 4. MODERN Button Styling (Brown background, Cream text) */
    .stButton>button {
        background-color: #8B4513; 
        color: #FFF5E1 !important;
        border-radius: 25px; /* Rounded, modern */
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #A0522D; /* Lighter brown on hover */
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }

    /* 5. Inputs Styling (Classy cream boxes) */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        color: #8B4513 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Advanced Branding: Top Right Logo + Left Titles
col_title, col_logo = st.columns([3, 1]) # 3 parts left, 1 part right

with col_title:
    st.markdown("## L Owens Systems")
    st.markdown("#### Radiant Image AI™")
    st.markdown("*Rewired for Purpose*")

with col_logo:
    # This automatically pulls "logo.png" from your GitHub and places it RIGHT
    try:
        logo = Image.open("logo.png")
        st.image(logo, use_column_width=True) # Fills the right column
    except:
        st.write("(Upload logo.png to GitHub)") # Message if logo is missing

st.markdown("---")

# 3. Secure API Connection (The background machinery)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Missing API Key in the Secrets Vault!")

# 4. Identity Lock Interface (Structured for a modern look)
st.write("### 📸 STEP 1: Identity Lock")
st.markdown("*(Upload your professional base photo)*")
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"]) # Blank label for modern look

st.markdown("---")
st.write("### 🎨 STEP 2: Editorial Customization")

# Freestyle Prompt Area
custom_prompt = st.text_area("Custom Editorial Instructions (Optional)", 
                             placeholder="e.g., 'Wearing gold framed glasses' or 'holding a leather portfolio'...")

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

# 5. The "Leadership" Launch Button
st.markdown("---")
# We place this in a container and column to help center and elevate it
with st.container():
    c_left, c_mid, c_right = st.columns([1,1,1])
    with c_mid:
        if st.button("Generate My Radiant Image", key="generate_button"):
            if uploaded_file is not None:
                st.success("Identity Locked. Merging your leadership energy with editorial excellence...")
            else:
                st.warning("Please upload a photo to lock your identity.")
