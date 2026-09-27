import os
from google import genai
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def analyze_food_image(image_path: str):
    # Initialize the Gemini client using the .env file variable
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"Error loading image: {e}"

    prompt = """
    Analyze this food image (it could be a raw ingredient or a packaged food item). 
    Provide the response strictly in the following format:
    
    1. Food Item Name: [Name of the object, state whether raw, cooked, or packaged]
    2. Condition: [Detailed breakdown of freshness, visual appearance, presence of blemishes, mold, or intact packaging seals]
    3. Edibility: [Can be eaten or Not - answer strictly with 'Yes' or 'No' followed by a short reason]
    4. Expected Expiry/Shelf-life Estimation: [Estimated remaining safe window or visible expiry context if visible on packaging]
    """

    print("Analyzing image with Gemini model...")
    
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=[image, prompt]
    )

    return response.text

if __name__ == "__main__":
    target_image = "sample_food.jpg" 
    
    if os.path.exists(target_image):
        analysis_result = analyze_food_image(target_image)
        print("\n--- Food Analysis Report ---")
        print(analysis_result)
    else:
        print(f"Please place a valid image file named '{target_image}' in the directory.")