import streamlit as st
import google.generativeai as genai
from PIL import Image

import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Page Config & CSS Branding
st.set_page_config(page_title="Radiant Image AI", page_icon="✨")

# --- CUSTOM COLORS & BACKGROUNDS ---
st.markdown("""
    <style>
    /* Sets the main background to your brand's Cream color */
    .stApp {
        background-color: #FFF5E1; 
    }
    /* Sets the text and titles to Editorial Charcoal */
    h1, h2, h3, p {
        color: #1A1A1A !important;
    }
    /* Styles the buttons in your brand's Peach color */
    .stButton>button {
        background-color: #FAD5A5;
        color: #1A1A1A;
        border-radius: 10px;
        border: 1px solid #1A1A1A;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Add your Logo (Ensure 'logo.png' is in your GitHub folder)
try:
    logo = Image.open("logo.png")
    st.image(logo, width=200) # Centers or left-aligns your logo
except:
    st.title("Radiant Image AI™") # Backup if logo isn't found

st.subheader("L Owens Systems | Rewired for Purpose")
st.markdown("---")

# Rest of your code continues here...

# 2. Secure API Connection (Using your vault key)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Connection Error: Please verify your API Key in the Secrets vault.")

# 3. The Identity Lock Interface
st.write("### 📸 Step 1: Identity Lock")
uploaded_file = st.file_uploader("Upload your base photo for identity verification", type=["jpg", "png", "jpeg"])

st.markdown("---")
st.write("### 🎨 Step 2: Editorial Customization")

# Freestyle Prompt Area
custom_prompt = st.text_area("Custom Editorial Instructions (Optional)", 
                             placeholder="Example: 'Wearing gold framed glasses' or 'holding a leather portfolio'...")

col1, col2 = st.columns(2)

with col1:
    st.write("**Wardrobe & Lighting**")
    style = st.selectbox("Clothing Style", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("Shot Choice", ["Headshot", "Full Length", "Freestyle", "Studio"])
    lighting = st.selectbox("Lighting Environment", ["Golden Hour", "Studio Softbox", "Dramatic Cinematic", "Natural Daylight"])

with col2:
    st.write("**Beauty & Location**")
    makeup = st.selectbox("Makeup Style", ["Soft Glam", "Full Glam", "Natural Glow"])
    hair = st.selectbox("Hair Style", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("Location Theme", ["Modern Office", "High-End Hotel Lobby", "Luxury Yacht", "Penthouse Office"])

# 4. Generate Button
st.markdown("---")
if st.button("Generate My Radiant Image"):
    if uploaded_file is not None:
        st.success("Identity Locked. Creating your ultra-realistic editorial portrait...")
        # The AI will now merge the 'Radiant Image AI' standards with the user's photo
    else:
        st.warning("Please upload a photo first to lock your identity!")
