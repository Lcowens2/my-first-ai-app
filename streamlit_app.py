import streamlit as st
import google.generativeai as genai
from PIL import Image

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
    }
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600&family=Quicksand:wght@400;600&display=swap');
    .radiant-title { font-family: 'Cormorant Garamond', serif; font-size: 80px !important; color: #582F0E !important; font-style: italic; }
    .stButton>button { background: #B08968; color: #FFF1E6 !important; border-radius: 50px; border: none; padding: 15px 50px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Branding
col_title, col_logo = st.columns([2, 1])
with col_title:
    st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
    st.markdown('**L OWENS SYSTEMS** | *Rewired for Purpose*')

with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=250) 
    except:
        st.write(" ") 

# 3. CUSTOMER ACTIVATION BOX
st.markdown("---")
st.write("### 🔑 STEP 1: ACTIVATE YOUR STUDIO")
customer_key = st.text_input("ENTER YOUR GOOGLE API KEY TO BEGIN", type="password", help="Paste your unique key from Google AI Studio here to power your session.")

if not customer_key:
    st.info("Please enter your API Key to unlock the Radiant Studio features.")
    st.stop() # Stops the app here until a key is entered

# 4. Identity & Selection (Only shows if key is entered)
try:
    genai.configure(api_key=customer_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.success("STUDIO ACTIVATED. WELCOME TO RADIANT IMAGE AI.")
except:
    st.error("Invalid Key. Please check your Google API settings.")

# 5. App Content
st.write("### II. IDENTITY LOCK")
uploaded_file = st.file_uploader("UPLOAD BASE IMAGE", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

st.markdown("---")
st.write("### III. EDITORIAL DIRECTION")
col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("WARDROBE", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("COMPOSITION", ["Headshot", "Full Length", "Editorial Studio"])
with col2:
    hair = st.selectbox("STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View"])

if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file:
        st.write("CRAFTING...")
        # Imagine processing logic here
    else:
        st.warning("Please upload a photo.")
        st.warning("PLEASE UPLOAD A BASE IMAGE TO BEGIN.")
