import streamlit as st
from PIL import Image
import io

# 1. FORCE THE NEW LIBRARY
try:
    from google import genai
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai"])
    from google import genai

# 2. RADIANT STYLING
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
    .stButton>button { background: #B08968; color: white !important; border-radius: 60px; border: none; padding: 25px; font-size: 24px; font-weight: bold; width: 100%; box-shadow: 0px 10px 20px rgba(176, 137, 104, 0.3); margin-top: 20px; }
    h3 { font-family: 'Cormorant Garamond', serif; font-size: 35px !important; color: #582F0E !important; border-bottom: 1px solid #EAD2AC; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING
_, col_logo, _ = st.columns([1, 2, 1])
with col_logo:
    try:
        st.image(Image.open("logo.png"), use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center; color: #582F0E;'>L. OWENS</h1>", unsafe_allow_html=True)

st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('<p class="systems-subtitle">Rewired for Purpose</p>', unsafe_allow_html=True)

# 4. STEP 1: KEY ACTIVATION
st.write("### 💎 STEP 1: ACTIVATE YOUR SESSION")
customer_key = st.text_input("PASTE YOUR UNIQUE STUDIO KEY HERE", type="password")
if not customer_key:
    st.info("Awaiting your professional key to unlock the studio...")
    st.stop()

client = genai.Client(api_key=customer_key)

# 5. STEP 2: IDENTITY LOCK
st.markdown("---")
st.write("### 📸 STEP 2: LOCK YOUR IDENTITY")
uploaded_file = st.file_uploader("CHOOSE YOUR PHOTO", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, width=250, caption="Identity Reference Locked")

# 6. STEP 3: EDITORIAL DIRECTION
st.markdown("---")
st.write("### ✨ STEP 3: DEFINE YOUR LOOK")
col1, col2 = st.columns(2)

with col1:
    h_color = st.selectbox("HAIR COLOR", ["Dark Brown", "Black", "Dark Blonde", "Light Blonde", "Auburn", "Silver/Grey", "Other..."])
    if h_color == "Other...":
        h_color = st.text_input("SPECIFY HAIR COLOR")

    h_style = st.selectbox("HAIR STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves", "Braided Updo", "Other..."])
    if h_style == "Other...":
        h_style = st.text_input("SPECIFY HAIR STYLE")

    wardrobe = st.selectbox("WARDROBE", ["Business Casual", "Pantsuit", "Tailored Business Suit", "Executive Polished", "High-End Editorial", "Other..."])
    if wardrobe == "Other...":
        wardrobe = st.text_input("SPECIFY WARDROBE")

    shoes = st.selectbox("SHOES", ["Pumps", "Strappy Sandals", "Dressy Flats", "Classic Loafers", "Other..."])
    if shoes == "Other...":
        shoes = st.text_input("SPECIFY SHOES")

with col2:
    shot_style = st.selectbox("SHOT COMPOSITION", ["Professional Headshot", "Mid-Shot (Waist up)", "Full Body Stand", "Other..."])
    if shot_style == "Other...":
        shot_style = st.text_input("SPECIFY SHOT STYLE")

    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View", "High-End Hotel", "Studio Background", "Other..."])
    if theme == "Other...":
        theme = st.text_input("SPECIFY ENVIRONMENT")

    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow", "Other..."])
    if lighting == "Other...":
        lighting = st.text_input("SPECIFY LIGHTING")

    quantity = st.selectbox("QUANTITY", [1, 2, 4])

# 7. STEP 4: FREESTYLE STUDIO
st.markdown("---")
st.write("### ✍️ STEP 4: FREESTYLE STUDIO (OPTIONAL)")
freestyle_prompt = st.text_area("INJECT YOUR OWN CUSTOM PROMPT DETAILS", placeholder="e.g. 'I want to be holding a professional camera' or 'Make the background a library with velvet curtains'...")

# 8. PRODUCTION
st.markdown("---")
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file:
        with st.status("Crafting your professional assets...", expanded=True) as status:
            try:
                import requests
                import json
                import base64

                # 1. PREPARE THE PROMPT
                base_details = f"ULTRA-REALISTIC 8K PHOTOGRAPHY. High-end leadership editorial style. 100% exact facial structure. Composition: {shot_style}. Hair: {h_color}, {h_style}. Outfit: {wardrobe}, {shoes}. Environment: {theme}. Lighting: {lighting}."
                final_prompt = base_details + (f" Additional Notes: {freestyle_prompt}" if freestyle_prompt else "")

                # 2. THE DIRECT REST API CALL
                st.write("Connecting to Production Servers...")
                
                # We try the standard production path first
                # Model names can vary by account: 'imagen-3', 'imagen-3.0-generate-001', or 'image-generation-006'
                model_variants = ["imagen-3", "imagen-3.0-generate-001", "image-generation-006"]
                
                success = False
                for model_name in model_variants:
                    if success: break
                    
                    st.write(f"Testing Engine: {model_name}...")
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:predict?key={customer_key}"
                    
                    img_bytes = uploaded_file.getvalue()
                    img_b64 = base64.b64encode(img_bytes).decode('utf-8')

                    payload = {
                        "instances": [{"prompt": final_prompt, "image": {"bytesBase64Encoded": img_b64}}],
                        "parameters": {"sampleCount": quantity, "aspectRatio": "3:4"}
                    }

                    response = requests.post(url, json=payload)
                    result = response.json()

                    if response.status_code == 200:
                        success = True
                        st.markdown("### YOUR RADIANT ASSETS")
                        grid = st.columns(2)
                        predictions = result.get("predictions", [])
                        for i, pred in enumerate(predictions):
                            img_data = base64.b64decode(pred["bytesBase64Encoded"])
                            generated_img = Image.open(io.BytesIO(img_data))
                            grid[i % 2].image(generated_img, use_container_width=True)
                            
                            buf = io.BytesIO()
                            generated_img.save(buf, format="PNG")
                            st.download_button(f"DOWNLOAD {i+1}", buf.getvalue(), f"radiant_{i+1}.png", "image/png", key=f"dl_{i}_{model_name}")
                        
                        status.update(label="Assets Successfully Crafted!", state="complete")
                
                if not success:
                    st.error("Studio Note: Imagen 3 access is not yet active on this API Key.")
                    st.info("To fix this: Go to Google AI Studio, create a NEW API Key, and ensure you have accepted the latest 'Generative AI Terms of Service'.")

            except Exception as e:
                st.error(f"Studio Note: {e}")
    else:
        st.warning("Please upload a photo first.")
        
