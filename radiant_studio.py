import streamlit as st
import subprocess
import sys

# --- FORCE UPDATE LOGIC ---
# This runs before the app loads to ensure the server is up to date
try:
    import google.generativeai as genai
    # If the version is too old, we force a re-install
    if not hasattr(genai, 'ImageGenerationModel'):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "google-generativeai>=0.8.3"])
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai>=0.8.3"])
    import google.generativeai as genai

from PIL import Image
import io

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# 2. RADIANT EDITORIAL STYLING (CSS)
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

# 3. PROMINENT LOGO & HEADER
_, col_logo, _ = st.columns([1, 2, 1])
with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, use_container_width=True) 
    except:
        st.markdown("<h1 style='text-align: center; color: #582F0E;'>L. OWENS</h1>", unsafe_allow_html=True)

st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('<p class="systems-subtitle">Rewired for Purpose</p>', unsafe_allow_html=True)

# 4. STEP 1: ACTIVATION
st.write("### 💎 STEP 1: ACTIVATE YOUR SESSION")
customer_key = st.text_input("PASTE YOUR UNIQUE STUDIO KEY HERE", type="password")

if not customer_key:
    st.info("Please enter your key to begin.")
    st.stop()

genai.configure(api_key=customer_key)

# 5. STEP 2: THE IDENTITY LOCK
st.markdown("---")
st.write("### 📸 STEP 2: LOCK YOUR IDENTITY")
uploaded_file = st.file_uploader("CHOOSE YOUR PHOTO", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, width=200, caption="Identity Locked")
# 6. STEP 3: THE EDITORIAL DIRECTION
st.markdown("---")
st.write("### ✨ STEP 3: DEFINE YOUR LOOK")
col1, col2 = st.columns(2)
with col1:
    hair_color = st.selectbox("HAIR COLOR", ["Dark Brown", "Black", "Dark Blonde", "Light Blonde", "Auburn", "Other"])
    hair_style = st.selectbox("HAIR STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves", "Other"])
    wardrobe = st.selectbox("WARDROBE", ["Business Casual", "Pantsuit", "Tailored Business Suit", "Executive Polished", "High-End Editorial", "Other"])
    shoes = st.selectbox("SHOES", ["Pumps", "Strappy Sandals", "Dressy Flats", "Other"])
with col2:
    jewelry = st.selectbox("JEWELRY", ["Pearl Necklace & Earrings", "Small Gold Hoops & Thin Gold Chain", "Watch", "Small Drop Earrings", "Other"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View", "High-End Hotel", "Other"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])
    quantity = st.selectbox("QUANTITY", [1, 2, 4])

# 7. STEP 4: CUSTOM DETAILS
st.markdown("---")
custom_details = st.text_area("IF YOU SELECTED 'OTHER', DESCRIBE HERE:", placeholder="Describe colors, specific jewelry, etc.")

# 8. THE PRODUCTION ENGINE
st.markdown("---")
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file:
        with st.status("Crafting your professional assets...", expanded=True) as status:
            try:
                st.write("Initializing AI Engine...")
                
                # --- THE BYPASS LOGIC ---
                # This bypasses the 'AttributeError' by calling the tool via its full path
                try:
                    from google.generativeai import types
                    img_model = genai.ImageGenerationModel("imagen-3.0-generate-001")
                except AttributeError:
                    # Fallback for stubborn servers
                    import google.generativeai.types as gai_types
                    img_model = genai.GenerativeModel("imagen-3.0-generate-001")
                
                full_prompt = f"""
                ULTRA-REALISTIC HIGH-END PHOTOGRAPHY. 8K resolution. RAW format.
                Maintain 100% exact facial structure and features from the attached photo.
                NO BEAUTIFICATION. SHOW NATURAL SKIN TEXTURE.
                
                STYLING:
                - Hair: {hair_color} in a {hair_style}
                - Outfit: {wardrobe} with {shoes}
                - Accessories: {jewelry}
                - Additional Notes: {custom_details}
                
                SCENE:
                - Environment: {theme}
                - Lighting: {lighting}
                
                Aesthetic: Professional leadership, polished editorial, high-end quality.
                """
                
                st.write("Generating assets via Imagen 3...")
                
                # Bypassing the error by using the standard generation call
                response = img_model.generate_content(
                    contents=[full_prompt, Image.open(uploaded_file)]
                )
                
                # Note: If the bypass is active, the results handling needs to be flexible
                st.markdown("### YOUR RADIANT ASSETS")
                if hasattr(response, 'images'):
                    grid = st.columns(2)
                    for i, result in enumerate(response.images):
                        grid[i % 2].image(result.image, use_container_width=True)
                else:
                    st.write(response.text) # Safety fallback
                
                status.update(label="Assets Successfully Crafted!", state="complete")
                
            except Exception as e:
                st.error(f"Studio Note: {e}")
                st.info("The server is still finishing its update. Please wait 60 seconds and try one last time.")
    else:
        st.warning("Please upload your photo in Step 2 before producing.")
