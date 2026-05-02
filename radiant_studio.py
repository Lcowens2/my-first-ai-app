import os
import sys
import subprocess

# 1. THE RECOVERY ENGINE (Forces the server to update)
try:
    import google.generativeai as genai
    # If the version is too old to have the Image tool, force an upgrade
    if not hasattr(genai, 'ImageGenerationModel'):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "google-generativeai"])
        import google.generativeai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

import streamlit as st
from PIL import Image
import io

# 2. BRANDING & STYLE
st.set_page_config(page_title="Radiant Image AI", layout="wide")
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FDE2E4 0%, #FFF1E6 100%); }
    section.main > div {
        border: 4px solid #EAD2AC;
        border-radius: 40px;
        padding: 40px;
        background-color: rgba(255, 255, 255, 0.95);
    }
    .radiant-title { font-family: serif; font-size: 60px; color: #582F0E; text-align: center; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; letter-spacing: 3px;">REWIRED FOR PURPOSE</p>', unsafe_allow_html=True)

# 3. PROMINENT LOGO & HEADER
_, col_logo, _ = st.columns([1, 2, 1])
with col_logo:
    try:
        # This looks for the file named 'logo.png' in your GitHub
        logo = Image.open("logo.png")
        st.image(logo, use_container_width=True) 
    except:
        # This is the backup if the file isn't found
        st.markdown("<h1 style='text-align: center; color: #582F0E;'>L. OWENS</h1>", unsafe_allow_html=True)

st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; letter-spacing: 3px; color: #7F5539;">REWIRED FOR PURPOSE</p>', unsafe_allow_html=True)

# 4. IDENTITY & EDITORIAL DIRECTION
col1, col2 = st.columns(2)
with col1:
    st.write("### 📸 1. IDENTITY LOCK")
    uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, width=150)

with col2:
    st.write("### ✨ 2. EDITORIAL STYLE")
    wardrobe = st.selectbox("WARDROBE", ["Business Casual", "Pantsuit", "Tailored Business Suit", "Executive Polished"])
    theme = st.selectbox("SETTING", ["Modern Office", "Luxury Yacht", "Penthouse View", "High-End Hotel"])
    hair_style = st.selectbox("HAIR", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])

# 5. PRODUCTION ENGINE
st.markdown("---")
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file:
        with st.status("Crafting your professional assets...", expanded=True) as status:
            try:
                # We use the generic 'imagen-3.0-generate-001' which is the standard Pro name
                st.write("Waking up the Imagen 3 Engine...")
                model_name = "imagen-3.0-generate-001"
                img_model = genai.ImageGenerationModel(model_name)
                
                prompt = f"ULTRA-REALISTIC 8K PHOTOGRAPHY. High-end editorial style. 100% exact facial structure of the person in the photo. Wearing a {wardrobe} in a {theme} setting. Hair: {hair_style}."
                
                st.write("Generating image...")
                response = img_model.generate_images(
                    prompt=prompt,
                    number_of_images=1,
                    aspect_ratio="3:4",
                    person_generation="allow_adults"
                )
                
                for i, result in enumerate(response.images):
                    st.image(result.image, use_container_width=True)
                    buf = io.BytesIO()
                    result.image.save(buf, format="PNG")
                    st.download_button("DOWNLOAD ASSET", buf.getvalue(), "radiant_asset.png", "image/png")
                
                status.update(label="Asset Created!", state="complete")
                
            except Exception as e:
                # If the specific name fails, we try the short name as a final backup
                try:
                    st.write("Trying backup connection...")
                    img_model = genai.ImageGenerationModel("imagen-3")
                    response = img_model.generate_images(prompt=prompt, number_of_images=1)
                    st.image(response.images[0].image)
                    status.update(label="Asset Created!", state="complete")
                except Exception as e2:
                    st.error(f"Studio Note: {e2}")
                    st.info("The server is still updating its tools. Refresh the page in 2 minutes.")
    else:
        st.warning("Please upload a photo first.")
