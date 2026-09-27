import os
from google import genai
from PIL import Image
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

st.set_page_config(page_title="Food Freshness Analyzer", page_icon="🍎", layout="centered")

st.title("🍎 Smart Food Freshness & Expiry Analyzer")
st.write("Upload an image of a food item (raw, cooked, or packaged) to check its condition, edibility, and expected shelf-life.")

uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Food Image", use_container_width=True)
    
    if st.button("Analyze Food Item"):
        with st.spinner("Analyzing food condition with Gemini..."):
            try:
                api_key = os.environ.get("GEMINI_API_KEY")
                if not api_key:
                    st.error("GEMINI_API_KEY is missing from your .env file!")
                else:
                    client = genai.Client(api_key=api_key)

                    prompt = """
                    Analyze this food image (it could be a raw ingredient or a packaged food item). 
                    Provide the response strictly in the following format:
                    
                    1. Food Item Name: [Name of the object, state whether raw, cooked, or packaged]
                    2. Condition: [Detailed breakdown of freshness, visual appearance, presence of blemishes, mold, or intact packaging seals]
                    3. Edibility: [Can be eaten or Not - answer strictly with 'Yes' or 'No' followed by a short reason]
                    4. Expected Expiry/Shelf-life Estimation: [Estimated remaining safe window or visible expiry context if visible on packaging]
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=[image, prompt]
                    )

                    st.success("Analysis Complete!")
                    st.markdown("### 📋 Analysis Report")
                    st.markdown(response.text)

            except Exception as e:
                st.error(f"An error occurred: {e}")