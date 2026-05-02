import google.generativeai as genai
from PIL import Image
import io

# 1. Page Config
st.set_page_config(page_title="Radiant Image AI", layout="wide")

# --- ENHANCED EDITORIAL CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FDE2E4 0%, #FFF1E6 100%); }
    
    /* Main Container */
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
    
    /* Branding */
    .radiant-title { 
        font-family: 'Cormorant Garamond', serif; 
        font-size: 85px !important; 
        color: #582F0E !important; 
        text-align: center;
        font-style: italic;
        margin-top: -20px;
    }
    .systems-subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: 22px !important;
        color: #7F5539 !important;
        text-align: center;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 40px;
    }
    
    /* Buttons */
    .stButton>button { 
        background: #B08968; 
        color: white !important; 
        border-radius: 60px; 
        border: none; 
        padding: 25px; 
        font-size: 24px; 
        font-weight: bold; 
        width: 100%; 
        box-shadow: 0px 10px 20px rgba(176, 137, 104, 0.3);
    }
    
    /* Section Headers */
    h3 { font-family: 'Cormorant Garamond', serif; font-size: 35px !important; color: #582F0E !important; border-bottom: 1px solid #EAD2AC; }
    </style>
    """, unsafe_allow_html=True)

# 2. PROMINENT LOGO & HEADER
# Centering a larger logo
_, col_logo, _ = st.columns([1, 2, 1])
with col_logo:
    try:
        logo = Image.open("logo.png")
        st.image(logo, use_container_width=True) 
    except:
        st.markdown("<h1 style='text-align: center;'>L. OWENS</h1>", unsafe_allow_html=True)

st.markdown('<p class="radiant-title">Radiant Image AI</p>', unsafe_allow_html=True)
st.markdown('<p class="systems-subtitle">Rewired for Purpose</p>', unsafe_allow_html=True)

# 3. STEP 1: ACTIVATION
st.write("### 💎 STEP 1: ACTIVATE YOUR SESSION")
customer_key = st.text_input("PASTE YOUR UNIQUE STUDIO KEY HERE", type="password", help="Enter the key provided in your welcome guide.")

if not customer_key:
    st.info("The Studio is currently in 'View Only' mode. Please enter your key above to begin.")
    st.stop()

# Configure API
try:
    genai.configure(api_key=customer_key)
except:
    st.error("Access Key not recognized. Please verify your key.")
    st.stop()

# 4. STEP 2: THE IDENTITY LOCK
st.markdown("---")
st.write("### 📸 STEP 2: LOCK YOUR IDENTITY")
st.info("Upload a clear, well-lit photo of your face. This ensures the AI maintains your exact features.")
uploaded_file = st.file_uploader("CHOOSE YOUR PHOTO", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, width=200, caption="Identity Locked")

# 5. STEP 3: THE EDITORIAL DIRECTION
st.markdown("---")
st.write("### ✨ STEP 3: DEFINE YOUR LOOK")

col1, col2 = st.columns(2)

with col1:
    hair_color = st.selectbox("HAIR COLOR", ["Dark Brown", "Black", "Dark Blonde", "Light Blonde", "Auburn", "Other"])
    hair_style = st.selectbox("HAIR STYLING", ["Sleek Bun", "Naturally Curly", "Sleek Bob", "Hollywood Waves", "Other"])
    wardrobe = st.selectbox("WARDROBE", ["Business Casual", "Pantsuit", "Tailored Business Suit", "Executive Polished", "High-End Editorial", "Other"])
    shoes = st.selectbox("SHOES", ["Pumps", "Strappy Sandals", "Dressy Flats", "Other"])

with col2:
    jewelry = st.selectbox("JEWELRY", [
        "Pearl Necklace & Earrings", 
        "Small Gold Hoops & Thin Gold Chain", 
        "Watch", 
        "Small Drop Earrings", 
        "Other"
    ])
    theme = st.selectbox("ENVIRONMENT", ["Modern Office", "Luxury Yacht", "Penthouse View", "High-End Hotel", "Other"])
    lighting = st.selectbox("LIGHTING", ["Golden Hour", "Studio Softbox", "Cinematic Glow"])
    quantity = st.selectbox("QUANTITY", [1, 2, 4])

# 6. GLOBAL OTHER BOX
st.markdown("---")
st.write("### 📝 STEP 4: CUSTOM DETAILS")
custom_details = st.text_area(
    "IF YOU SELECTED 'OTHER' ABOVE, PLEASE DESCRIBE YOUR SPECIFIC REQUEST HERE:",
    placeholder="Example: I would like a deep emerald green pantsuit and silver hoop earrings..."
)

# 7. PRODUCTION ENGINE
st.markdown("---")
if st.button("CREATE MY RADIANT ASSETS"):
    if uploaded_file:
        with st.status("Crafting your professional assets...", expanded=True) as status:
            try:
                st.write("Analyzing facial structure...")
                img_model = genai.ImageGenerationModel("imagen-3") 
                
                # Building the prompt using all selections
                full_prompt = f"""
                ULTRA-REALISTIC HIGH-END PHOTOGRAPHY. 8K resolution.
                Maintain 100% exact facial structure and features from the photo.
                NO BEAUTIFICATION. Authentic skin texture.
                
                SUBJECT DETAILS:
                - Hair: {hair_color} in a {hair_style}
                - Outfit: {wardrobe}
                - Footwear: {shoes}
                - Accessories: {jewelry}
                - Custom Preferences: {custom_details}
                
                ENVIRONMENT & LIGHTING:
                - Setting: {theme}
                - Lighting Style: {lighting}
                
                Aesthetic: Professional, editorial, polished leadership.
                """
                
                st.write("Generating assets via Imagen 3...")
                response = img_model.generate_images(
                    prompt=full_prompt,
                    number_of_images=quantity,
                    aspect_ratio="3:4",
                    person_generation="allow_adults"
                )
                
                # RESULTS
                st.markdown("### YOUR RADIANT ASSETS")
                grid = st.columns(2)
                for i, result in enumerate(response.images):
                    grid[i % 2].image(result.image, use_container_width=True)
                    
                    # Buffer for download
                    buf = io.BytesIO()
                    result.image.save(buf, format="PNG")
                    st.download_button(f"DOWNLOAD ASSET {i+1}", buf.getvalue(), f"radiant_asset_{i}.png", "image/png", key=f"dl_{i}")
                
                status.update(label="Assets Successfully Crafted!", state="complete")
                
            except Exception as e:
                st.error(f"Studio Note: {e}")
                st.info("This usually means your key needs Image permissions or the prompt was too complex.")
    else:
        st.warning("Please upload your photo in Step 2 before producing.")
