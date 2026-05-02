import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# 1. Page Config
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# --- SOFT RADIANT EDITORIAL CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FDE2E4 0%, #FFF1E6 100%); }
    section.main > div {
        border: 4px solid #EAD2AC;
        outline: 20px solid #DDB892;
        border-radius: 30px;
        padding: 50px;
        margin: 20px;
        background-color: rgba(255, 241, 230, 0.9);
    }
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600&family=Quicksand:wght@400;600&display=swap');
    .radiant-title { font-family: 'Cormorant Garamond', serif; font-size: 60px !important; color: #582F0E !important; font-style: italic; }
    .stButton>button { background: #B08968; color: #FFF1E6 !important; border-radius: 50px; border: none; padding: 15px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. Header
st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('**L OWENS SYSTEMS** | *Rewired for Purpose*')

# 3. STEP 1: Activation (The Gate)
st.markdown("---")
st.write("### 🔑 STEP 1: ACTIVATE YOUR STUDIO")
customer_key = st.text_input("ENTER YOUR GOOGLE API KEY", type="password")

if not customer_key:
    st.info("Please enter your API Key to unlock the Radiant Studio.")
    st.stop() # This hides everything below until the key is entered

# 4. STEP 2: Identity & Style (These were "missing")
try:
    genai.configure(api_key=customer_key)
except:
    st.error("Invalid Key.")
    st.stop()

st.write("### II. IDENTITY LOCK")
uploaded_file = st.file_uploader("UPLOAD REFERENCE PHOTO", type=["jpg", "png", "jpeg"])

st.markdown("---")
st.write("### III. EDITORIAL DIRECTION")
col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("WARDROBE", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("COMPOSITION", ["Headshot", "Full Length", "Editorial Studio"])
    output_count = st.selectbox("NUMBER OF OUTPUTS", [1, 2, 4])
with col2:
    hair = st.selectbox("STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])

# 5. STEP 3: Production
st.markdown("---")
if st.button("PRODUCE MY RADIANT ASSETS"):
    if uploaded_file:
        with st.status("Crafting...", expanded=True) as status:
            try:
                img_model = genai.ImageGenerationModel("imagen-3") 
                prompt = f"ULTRA-REALISTIC. {style}, {shot_type}, {hair}, {theme}, {lighting}. High-end editorial."
                
                response = img_model.generate_images(
                    prompt=prompt,
                    number_of_images=output_count,
                    aspect_ratio="3:4",
                    person_generation="allow_adults"
                )
                
                st.markdown("### YOUR RADIANT ASSETS")
                cols = st.columns(2)
                for i, result in enumerate(response.images):
                    cols[i % 2].image(result.image, use_container_width=True)
                    buf = io.BytesIO()
                    result.image.save(buf, format="PNG")
                    st.download_button(f"Download {i+1}", buf.getvalue(), f"img_{i}.png", "image/png", key=f"dl_{i}")
                status.update(label="Complete!", state="complete")
            except Exception as e:
                st.error(f"Note: {e}")
    else:
        st.warning("Upload a photo first.")
