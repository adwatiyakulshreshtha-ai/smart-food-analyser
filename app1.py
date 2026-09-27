import os
from google import genai
from PIL import Image
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

st.set_page_config(page_title="Smart Fridge & Recipe Assistant", page_icon="🍳", layout="centered")

st.title("🍳 Smart Fridge & Smart Chef Assistant")
st.write("Upload **multiple images** of your fridge contents, pantry, or fresh groceries. The AI will inspect their condition, check edibility, and generate a creative recipe using only what's fresh!")

uploaded_files = st.file_uploader("Choose food/fridge images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 📷 Uploaded Grocery/Fridge Items")
    cols = st.columns(len(uploaded_files))
    images = []
    
    for i, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file)
        images.append(img)
        with cols[i]:
            st.image(img, caption=f"Item {i+1}", use_container_width=True)
    
    if st.button("Analyze Fridge & Generate Recipes"):
        with st.spinner("Analyzing items and thinking of delicious recipes..."):
            try:
                api_key = os.environ.get("GEMINI_API_KEY")
                if not api_key:
                    st.error("GEMINI_API_KEY is missing from your .env file!")
                else:
                    client = genai.Client(api_key=api_key)

                    prompt = """
                    Analyze all the provided food/fridge images. 
                    Perform the following tasks:
                    1. Item Inventory & Condition Assessment: List each visible food item, state whether raw/cooked/packaged, its condition (freshness/spoilage), and its edibility (Yes/No).
                    2. Available Fresh Ingredients Summary: Filter out only the items that are marked edible and safe to eat.
                    3. Recipe Suggestion: Provide a creative, step-by-step cooking recipe that can be made primarily using the available fresh items identified in the images.
                    
                    Format your output clearly with Markdown headings.
                    """
                    
                    contents_payload = images + [prompt]
                    
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=contents_payload
                    )

                    st.success("Analysis & Recipe Generation Complete!")
                    st.markdown("---")
                    st.markdown(response.text)

            except Exception as e:
                st.error(f"An error occurred: {e}")