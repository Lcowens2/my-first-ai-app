import streamlit as st
from PIL import Image
import io
import requests
import json
import base64

# 1. RADIANT STYLING (Editorial Leadership Aesthetic)
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

# 2. BRANDING SECTION
st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('<p class="systems-subtitle">Rewired for Purpose</p>', unsafe_allow_html=True)

# 3. STEP 1: KEY ACTIVATION
st.write("### 💎 STEP 1: ACTIVATE YOUR SESSION")
raw_key = st.text_input("ENTER YOUR RADIANT ACTIVATION KEY", type="password")
if not raw_key:
    st.info("Awaiting your professional key to unlock the studio...")
    st.stop()

# Auto-strip any accidental spaces or hidden newlines from copy-paste
customer_key = raw_key.strip()

# 4. STEP 2: IDENTITY LOCK (UPLOAD PHOTO)
st.markdown("---")
st.write("### 📸 STEP 2: LOCK YOUR IDENTITY")
uploaded_file = st.file_uploader("CHOOSE YOUR REFERENCE PHOTO", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, width=250, caption="Identity Reference Locked")

# 5. STEP 3: FREESTYLE STUDIO (THE BYPASS MASTER)
st.markdown("---")
st.write("### ✍️ STEP 3: CUSTOM VISION (OPTIONAL)")
st.caption("Note: Typing here will automatically hide the standard menu options below.")
freestyle_prompt = st.text_area("INJECT YOUR CUSTOM PROMPT HERE", placeholder="e.g. Standing on a luxury balcony overlooking the Mediterranean...")

# 6. STEP 4: EDITORIAL DIRECTION (CONDITIONAL DISPLAY)
# These variables must exist even if the menu is hidden
h_color = h_style = wardrobe = shot_style = theme = lighting = ""

if not freestyle_prompt.strip():
    st.markdown("---")
    st.write("### ✨ STEP 4: DEFINE YOUR LOOK (MENU MODE)")
    col1, col2 = st.columns(2)

    with col1:
        h_color = st.selectbox("HAIR COLOR", ["Dark Brown", "Black", "Dark Blonde", "Light Blonde", "Auburn", "Silver/Grey", "Other..."])
        if h_color == "Other...": h_color = st.text_input("SPECIFY HAIR COLOR")

        h_style = st.selectbox("HAIR STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves", "Braided Updo", "Other..."])
        if h_style == "Other...": h_style = st.text_input("SPECIFY HAIR STYLE")

        wardrobe = st.selectbox("WARDROBE", ["Business Casual", "Pantsuit", "Tailored Business Suit", "Executive Polished", "High-End Editorial", "Other..."])
        if wardrobe == "Other...": wardrobe = st.text_input("SPECIFY WARDROBE")

    with col2:
        shot_style = st.selectbox("SHOT COMPOSITION", ["Professional Headshot", "Mid-Shot (Waist up)", "Full Body Stand", "Other..."])
        if shot_style == "Other...": shot_style = st.text_input("SPECIFY SHOT STYLE")

        theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View", "High-End Hotel", "Studio Background", "Other..."])
        if theme == "Other...": theme = st.text_input("SPECIFY ENVIRONMENT")

        lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow", "Other..."])
        if lighting == "Other...": lighting = st.text_input("SPECIFY LIGHTING")
else:
    st.success("🎯 Radiant Bypass Active: Studio is now prioritizing your custom vision.")

# 7. PRODUCTION SETTINGS
st.markdown("---")
quantity = st.selectbox("QUANTITY OF ASSETS", [1, 2, 4])

# 8. PRODUCTION ENGINE
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file:
        with st.status("Crafting your professional assets...", expanded=True) as status:
            try:
                # BYPASS LOGIC
                if freestyle_prompt.strip():
                    final_prompt = f"ULTRA-REALISTIC 8K PHOTOGRAPHY. High-end leadership editorial style. 100% exact facial structure. {freestyle_prompt}"
                else:
                    final_prompt = f"ULTRA-REALISTIC 8K PHOTOGRAPHY. High-end leadership editorial style. 100% exact facial structure. Composition: {shot_style}. Hair: {h_color}, {h_style}. Outfit: {wardrobe}. Environment: {theme}. Lighting: {lighting}."

                img_bytes = uploaded_file.getvalue()
                img_b64 = base64.b64encode(img_bytes).decode('utf-8')
                
                # Try v1 first (Stable), then v1beta (Experimental)
                api_versions = ["v1", "v1beta"]
                model_name = "imagen-3.0-generate-002"  # Standard high-quality Imagen 3 model string
                
                success = False
                for version in api_versions:
                    if success: break
                    st.write(f"Attempting connection via {version}...")
                    
                    url = f"https://generativelanguage.googleapis.com/{version}/models/{model_name}:predict?key={customer_key}"
                    payload = {
                        "instances": [{"prompt": final_prompt, "image": {"bytesBase64Encoded": img_b64}}],
                        "parameters": {"sampleCount": quantity, "aspectRatio": "3:4", "personGeneration": "allow_adults", "safetySetting": "BLOCK_NONE"}
                    }

                    response = requests.post(url, json=payload)
                    
                    if response.status_code == 200:
                        result = response.json()
                        success = True
                        st.markdown("### YOUR RADIANT ASSETS")
                        grid = st.columns(2)
                        predictions = result.get("predictions", [])
                        
                        for i, pred in enumerate(predictions):
                            gen_img_data = base64.b64decode(pred["bytesBase64Encoded"])
                            generated_img = Image.open(io.BytesIO(gen_img_data))
                            grid[i % 2].image(generated_img, use_container_width=True)
                            
                            buf = io.BytesIO()
                            generated_img.save(buf, format="PNG")
                            st.download_button(f"DOWNLOAD {i+1}", buf.getvalue(), f"radiant_{i+1}.png", "image/png", key=f"dl_{i}_{version}")
                        
                        status.update(label="Assets Successfully Crafted!", state="complete")
                    else:
                        try:
                            error_detail = response.json().get("error", {}).get("message", "Unknown error")
                        except Exception:
                            error_detail = response.text
                        st.write(f"Note ({version}): {error_detail}")

                if not success:
                    st.error("The Studio is still verifying your high-fidelity access.")
                    st.info("Since billing is active, this error usually clears once you have made your first $10 'credit' purchase in AI Studio Billing.")

            except Exception as e:
                st.error(f"Studio Error: {e}")
    else:
        st.warning("Please upload a photo first.")
