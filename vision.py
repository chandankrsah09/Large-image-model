from dotenv import load_dotenv
# loading all the environment variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the Generative AI API with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Updated function to load Gemini 1.5 Flash model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")  # Switch to Gemini 1.5 Flash

def get_gemini_response(input_text, image):
    # Ensure text parameter is always present
    if input_text.strip() == "":
        input_text = "Describe this image."
    
    if image:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content([input_text])
    
    return response.text

## Initialize the Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Application")
input_text = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)  # Updated parameter

submit = st.button("Tell me about the image")

# If the submit button is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("The Response is")
    st.write(response)
