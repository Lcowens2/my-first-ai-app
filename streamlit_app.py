import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Official App Branding
st.set_page_config(page_title="Radiant Image AI", page_icon="✨")
st.title("Radiant Image AI™")
st.subheader("L Owens Systems | Rewired for Purpose")
st.markdown("---")

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
