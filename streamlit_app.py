import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

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
        padding: 70px;
        margin: 40px;
        background-color: rgba(255, 241, 230, 0.9);
        box-shadow: 0px 15px 35px rgba(88, 47, 14, 0.1);
    }
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600&family=Quicksand:wght@400;600&display=swap');
    .radiant-title { font-family: 'Cormorant Garamond', serif; font-size: 90px !important; color: #582F0E !important; line-height: 0.9 !important; font-style: italic; margin-bottom: 10px !important; }
    .systems-subtitle { font-family: 'Quicksand', sans-serif; font-size: 22px !important; color: #7F5539 !important; letter-spacing: 3px !important; text-transform: uppercase; margin-bottom: 5px !important; }
    .purpose-tagline { font-family: 'Quicksand', sans-serif; font-size: 18px !important; color: #B08968 !important; font-weight: 600; }
    label, p, .stSelectbox label { color: #582F0E !important; font-family: 'Quicksand', sans-serif; font-weight: 600; }
    .stButton>button { background: #B08968; color: #FFF1E6 !important; border-radius: 50px; border: none; padding: 15px 50px; font-family: 'Quicksand', sans-serif; font-size: 18px; font-weight: bold; width: 100%; }
    .stButton>button:hover { background: #FDE2E4; color: #582F0E !important; border: 1px solid #582F0E; }
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

# 3. Connection & Logic
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash') # Using Flash for speed/cost
except:
    st.error("Authentication required. Please check your Secrets Vault.")

# 4. Step 1: Identity & Quantity
st.write("### I. IDENTITY LOCK")
col_file, col_qty = st.columns([2, 1])
with col_file:
    uploaded_file = st.file_uploader("UPLOAD BASE IMAGE", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
with col_qty:
    output_count = st.selectbox("NUMBER OF OUTPUTS", [1, 2, 4])

st.markdown("<hr style='border-top: 1px solid #EAD2AC;'>", unsafe_allow_html=True)

# 5. Step 2: Customization
st.write("### II. EDITORIAL DIRECTION")
custom_prompt = st.text_area("ADDITIONAL SPECIFICATIONS", placeholder="Refine your look...")
col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("WARDROBE", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("COMPOSITION", ["Headshot", "Full Length", "Editorial Studio"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])
with col2:
    makeup = st.selectbox("BEAUTY", ["Soft Glam", "Full Glam", "Natural Glow"])
    hair = st.selectbox("STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "High-End Hotel Lobby", "Luxury Yacht", "Penthouse View"])

# 6. The Action Button (The "Engine")
st.markdown("<br>", unsafe_allow_html=True)
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file is not None:
        with st.status("Locking Identity and Crafting Editorial Render...", expanded=True) as status:
            # Preparing the instruction for Ultra-Realism
            st.write("Analyzing facial structure and skin texture...")
            
            # This is the 'Master Prompt' that prevents "Fake AI" looks
            prompt = f"""
            ULTRA-REALISTIC PHOTOGRAPHY. 8K resolution. RAW format.
            Maintain 100% exact facial structure, skin tone, and features of the person in the image.
            NO BEAUTIFICATION. NO SKIN SMOOTHING. SHOW NATURAL SKIN PORES, fine lines, and authentic texture.
            EYES MUST BE VIVID AND LIFELIKE with natural reflections. Correct body proportions. NO LARGE HEADS.
            
            STYLING:
            - Clothing: {style}
            - Shot: {shot_type}
            - Hair: {hair}
            - Makeup: {makeup}
            - Lighting: {lighting}
            - Background: {theme}
            - Additional: {custom_prompt}
            
            Ensure the result looks like a high-end editorial magazine photo, not a digital painting.
            """
            
            # Simulated Processing for the Demo
            # (In the final version, this is where the image generation call lives)
            time.sleep(3)
            status.update(label="Assets Crafted!", state="complete", expanded=False)
            
            st.success(f"IDENTITY LOCKED. {output_count} EDITORIAL ASSETS READY.")
            st.info("NOTE: For the final launch, we will connect the direct image output stream to your account.")
    else:
        st.warning("PLEASE UPLOAD A BASE IMAGE TO BEGIN.")
