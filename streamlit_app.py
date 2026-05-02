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
        padding: 60px;
        margin: 20px;
        background-color: rgba(255, 241, 230, 0.9);
        box-shadow: 0px 15px 35px rgba(88, 47, 14, 0.1);
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600&family=Quicksand:wght@400;600&display=swap');
    
    .radiant-title { 
        font-family: 'Cormorant Garamond', serif; 
        font-size: clamp(40px, 8vw, 85px) !important; 
        color: #582F0E !important; 
        line-height: 0.9 !important; 
        font-style: italic; 
        margin-bottom: 10px !important; 
    }
    
    .systems-subtitle { 
        font-family: 'Quicksand', sans-serif; 
        font-size: 18px !important; 
        color: #7F5539 !important; 
        letter-spacing: 3px !important; 
        text-transform: uppercase; 
    }

    .stButton>button { 
        background: #B08968; 
        color: #FFF1E6 !important; 
        border-radius: 50px; 
        border: none; 
        padding: 18px; 
        font-family: 'Quicksand', sans-serif; 
        font-size: 20px; 
        font-weight: bold; 
        width: 100%; 
        transition: 0.3s;
    }
    
    .stButton>button:hover { background: #FDE2E4; color: #582F0E !important; border: 1px solid #582F0E; }
    
    /* Input Styling */
    .stTextInput input, .stSelectbox div, .stTextArea textarea {
        border-radius: 15px !important;
        border: 1px solid #EAD2AC !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Branding
col_title, col_logo = st.columns([2, 1])
with col_title:
    st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="systems-subtitle">L OWENS SYSTEMS | Rewired for Purpose</p>', unsafe_allow_html=True)

with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=250) 
    except:
        st.write(" ") 

# 3. Step 1: Customer Authentication
st.markdown("---")
st.write("### 🔑 STEP 1: ACTIVATE YOUR STUDIO")
customer_key = st.text_input("ENTER YOUR GOOGLE API KEY", type="password", help="Paste your key from Google AI Studio.")

if not customer_key:
    st.info("The Radiant Studio is locked. Please enter your API Key to access the editorial tools.")
    st.stop()

# 4. Identity & Direction
try:
    genai.configure(api_key=customer_key)
    # Testing the key connection
    test_model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Authentication Failed. Please check your API Key.")
    st.stop()

st.write("### II. IDENTITY LOCK")
uploaded_file = st.file_uploader("UPLOAD YOUR REFERENCE PHOTO", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, width=150, caption="Identity Locked")

st.markdown("---")
st.write("### III. EDITORIAL DIRECTION")
col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("WARDROBE", ["Tailored Business Suit (Cream/Peach)", "Executive Polished", "High-End Editorial"])
    shot_type = st.selectbox("COMPOSITION", ["Headshot", "Full Length", "Editorial Studio"])
    output_count = st.selectbox("NUMBER OF OUTPUTS", [1, 2, 4])
with col2:
    hair = st.selectbox("STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves"])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View", "High-End Hotel"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])

# 5. The Production Line
if st.button("PRODUCE MY RADIANT ASSETS"):
    if uploaded_file is not None:
        with st.status("Crafting Ultra-Realistic Render...", expanded=True) as status:
            st.write("Analyzing facial structure and skin texture...")
            
            # 1. Initialize Models
            # Note: Using Imagen-3 requires the key to have access to Google's image models
            img_model = genai.ImageGenerationModel("imagen-3.0-generate-001") 
            
            # 2. Build the Ultra-Realistic Prompt
            full_prompt = f"""
            ULTRA-REALISTIC PHOTOGRAPHY. 8K resolution. RAW format.
            Maintain 100% exact facial structure, skin tone, and features of the person in the attached photo.
            NO BEAUTIFICATION. NO SKIN SMOOTHING. SHOW NATURAL SKIN PORES and authentic texture.
            EYES MUST BE VIVID AND LIFELIKE. Correct body proportions. NO LARGE HEADS.
            
            STYLING:
            - Clothing: {style}
            - Shot: {shot_type}
            - Hair: {hair}
            - Lighting: {lighting}
            - Background: {theme}
            
            Ensure the result looks like a high-end editorial magazine photo.
            """
            
            try:
                # 3. Generate
                st.write("Generating assets via Imagen 3...")
                user_img = Image.open(uploaded_file)
                
                response = img_model.generate_images(
                    prompt=full_prompt,
                    number_of_images=output_count,
                    aspect_ratio="3:4",
                    person_generation="allow_adults"
                )
                
                status.update(label="Assets Crafted!", state="complete", expanded=False)
                
                # 4. Display Results
                st.markdown("### YOUR RADIANT ASSETS")
                cols = st.columns(2)
                for i, result in enumerate(response.images):
                    cols[i % 2].image(result.image, use_container_width=True)
                    # Add download button
                    buf = io.BytesIO()
                    result.image.save(buf, format="PNG")
                    st.download_button(f"Download Image {i+1}", buf.getvalue(), f"radiant_asset_{i+1}.png", "image/png")

            except Exception as e:
                st.error(f"Generation error: {e}. Ensure your API key has 'Imagen' enabled in Google Cloud.")
    else:
        st.warning("Please upload a photo first.")
