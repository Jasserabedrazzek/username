import streamlit as st
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Replace with the path to your Tesseract executable

pytesseract.pytesseract.tesseract_cmd = r"/home/appuser/venv/lib/python3.9/site-packages/pytesseract/pytesseract.py" 
# Title of the app
st.title("Image to Text Conversion")

# Add a sidebar with instructions
st.sidebar.header("Instructions")
st.sidebar.markdown("1. Upload an image or capture from the camera.")
st.sidebar.markdown("2. Click the 'Convert' button to convert image to text.")

# Use st.file_uploader to allow user to upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    text = pytesseract.image_to_string(image)
    txt = st.text_area("Enter some text", text)
