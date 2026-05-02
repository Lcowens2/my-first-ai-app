import os
import sys
import subprocess

# --- THE ENGINE ROOM ---
try:
    import google.generativeai as genai
    if not hasattr(genai, 'ImageGenerationModel'):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "google-generativeai"])
        import google.generativeai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

import streamlit as st
from PIL import Image
import io

# 1. PAGE CONFIGURATION & REWOUND RADIANT STYLING
st.set_page_config(page_title="Radiant Image AI", layout="wide")
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FDE2E4 0%, #FFF1E6 100%); }
    section.main > div {
        border: 4px solid #EAD2AC;
        outline: 20px solid #DDB892;
        border-radius: 40px;
        padding: 60px;
        margin: 10px;
        background-color: rgba(255, 255, 255, 0.95);
        box-shadow: 0px 20px 40px rgba(0,0,0,0.1);
    }
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600&family=Quicksand:wght@400;600&display=swap');
    .radiant-title { font-family: 'Cormorant Garamond', serif; font-size: 85px !important; color: #582F0E !important; text-align: center; font-style: italic; margin-top: -20px; }
    .systems-subtitle { font-family: 'Quicksand', sans-serif; font-size: 22px !important; color: #7F5539 !important; text-align: center; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 40px; }
    .stButton>button { background: #B08968; color: white !important; border-radius: 60px; border: none; padding: 25px; font-size: 24px; font-weight: bold; width: 100%; box-shadow: 0px 10px 20px rgba(176, 137, 104, 0.3); }
    h3 { font-family: 'Cormorant Garamond', serif; font-size: 35px !important; color: #582F0E !important; border-bottom: 1px solid #EAD2AC; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGO SECTION
_, col_logo, _ = st.columns([1, 2, 1])
with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, use_container_width=True) 
    except:
        st.markdown("<h1 style='text-align: center; color: #582F0E;'>L. OWENS</h1>", unsafe_allow_html=True)

st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('<p class="systems-subtitle">Rewired for Purpose</p>', unsafe_allow_html=True)

# 3. STEP 1: KEY ACTIVATION
st.write("### 💎 STEP 1: ACTIVATE YOUR SESSION")
customer_key = st.text_input("PASTE YOUR UNIQUE STUDIO KEY HERE", type="password")

if not customer_key:
    st.info("Awaiting your professional key to unlock the studio...")
    st.stop()

genai.configure(api_key=customer_key)

# 4. STEP 2: IDENTITY LOCK
st.markdown("---")
st.write("### 📸 STEP 2: LOCK YOUR IDENTITY")
uploaded_file = st.file_uploader("CHOOSE YOUR PHOTO", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, width=250, caption="Identity Reference Locked")

# 5. STEP 3: EDITORIAL DIRECTION
st.markdown("---")
st.write("### ✨ STEP 3: DEFINE YOUR LOOK")
col1, col2 = st.columns(2)
with col1:
    hair_color = st.selectbox("HAIR COLOR", ["Dark Brown", "Black", "Dark Blonde", "Light Blonde", "Auburn", "Silver/Grey"])
    hair_style = st.selectbox("HAIR STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves", "Braided Updo"])
    wardrobe = st.selectbox("WARDROBE", ["Business Casual", "Pantsuit", "Tailored Business Suit", "Executive Polished", "High-End Editorial"])
    shoes = st.selectbox("SHOES", ["Pumps", "Strappy Sandals", "Dressy Flats", "Classic Loafers"])
with col2:
    shot_style = st.selectbox("SHOT COMPOSITION", ["Professional Headshot (Shoulders up)", "Mid-Shot (Waist up)", "Full Body Stand", "Seated Executive Pose"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View", "High-End Hotel", "Minimalist Studio Background"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])
    quantity = st.selectbox("QUANTITY", [1, 2, 4])

# 6. STEP 4: PRODUCTION
st.markdown("---")
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file:
        with st.status("Crafting your professional assets...", expanded=True) as status:
            try:
                img_model = genai.ImageGenerationModel("imagen-3.0-generate-001")
                
                full_prompt = f"""
                ULTRA-REALISTIC 8K PHOTOGRAPHY. High-end leadership editorial style. 
                Maintain 100% exact facial structure and features of the person in the photo. 
                Composition: {shot_style}.
                Hair: {hair_color}, styled in a {hair_style}. 
                Outfit: {wardrobe} with {shoes}. 
                Environment: {theme}. 
                Lighting: {lighting}.
                Aesthetic: Polished, professional, and sophisticated.
                """
                
                response = img_model.generate_images(
                    prompt=full_prompt,
                    number_of_images=quantity,
                    aspect_ratio="3:4",
                    person_generation="allow_adults"
                )
                
                st.markdown("### YOUR RADIANT ASSETS")
                grid = st.columns(2)
                for i, result in enumerate(response.images):
                    grid[i % 2].image(result.image, use_container_width=True)
                    buf = io.BytesIO()
                    result.image.save(buf, format="PNG")
                    st.download_button(f"DOWNLOAD ASSET {i+1}", buf.getvalue(), f"radiant_{i+1}.png", "image/png", key=f"dl_{i}")
                
                status.update(label="Assets Successfully Crafted!", state="complete")
                
            except Exception as e:
                st.error(f"Studio Note: {e}")
    else:
        st.warning("Please upload a photo first.")
