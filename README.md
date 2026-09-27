# 🍎 Smart Food Freshness & Recipe Assistant (AI-Powered)

An intelligent multimodal vision-based application designed to combat food waste. The system analyzes raw, cooked, or packaged food items from single or multiple images, evaluates their real-time condition and edibility, and dynamically generates custom chef-style recipes using only the fresh ingredients available!

---

## 👥 Team Members
* **Aarti Devgun**
* **Aryan Upadhyay**
* **Anagh Mishra**
* **Adwatiya Kulshreshtha**

---

## 🛠️ Tech Stack
* **Programming Language:** Python
* **AI Core:** Google Gemini API (`google-genai` SDK) powered by the **Gemini 3.8 Flash** multimodal model
* **Web Frontend / UI:** Streamlit (for interactive browser-based interfaces)
* **Image Processing:** Pillow (PIL)
* **Environment Management:** python-dotenv

---

## 📖 Project Explanation
This application bridges computer vision and generative AI to solve everyday kitchen management challenges. Instead of training complex, resource-heavy custom models from scratch, our software leverages zero-shot visual reasoning via Google's Gemini 3.8 Flash API. When users upload images of grocery items, fridge contents, or pantry shelves, the model inspects physical attributes such as surface blemishes, mold, or intact packaging seals. It systematically outputs item identification, a clear "Yes/No" edibility status, and shelf-life estimations. Furthermore, our multi-image assistant (`app1.py`) aggregates all available fresh inventory and acts as a smart personal chef, synthesizing creative step-by-step cooking instructions to minimize food wastage.

---

## 🚀 Setup & Installation Procedure (For a Fresh Computer)

Follow these steps to set up and run the project from scratch on a new machine:

### 1. Prerequisites
Ensure you have the following installed:
* **Python** (version 3.10 or higher) downloaded from [python.org](https://www.python.org/)
* **Visual Studio Code (VS Code)** installed as your code editor

### 2. Clone the Repository & Open Terminal
Open your terminal or command prompt and clone the project:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
*(Or open your project folder directly inside VS Code).*

### 3. Install Required Python Packages
Run the following pip command in your terminal to install all dependencies:
```bash
pip install google-genai streamlit pillow python-dotenv
```

### 4. Configure Your API Key
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `.env` in the root directory of the project folder.
3. Paste your API key inside the `.env` file like this:
```env
GEMINI_API_KEY=AIzaSyYourActualKeyHere...
```

---

## 🏃‍♂️ How to Run the Application

You can run either the web-based Streamlit applications or the command-line script:

* **To run the Multi-Image Fridge & Recipe Assistant (`app1.py`):**
  ```bash
  python -m streamlit run app1.py
  ```

* **To run the Single Image Freshness Analyzer (`app.py`):**
  ```bash
  python -m streamlit run app.py
  ```

* **To run the Command-Line Script (`food_analyzer.py`):**
  ```bash
  python food_analyzer.py