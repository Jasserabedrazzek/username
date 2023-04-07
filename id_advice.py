import streamlit as st
import pytesseract
from PIL import Image
from tempfile import TemporaryDirectory
import os

# Replace '/usr/local/bin' with the actual path to the Tesseract OCR executable
tesseract_path = '/home/appuser/venv/lib/python3.9/site-packages/pytesseract/pytesseract.py'
os.environ['PATH'] = tesseract_path + os.pathsep + os.environ['PATH']
with TemporaryDirectory() as temp_dir:
    pytesseract.pytesseract.tesseract_cmd = f'{tesseract_path}/tesseract'
    
st.title("Image to Text Converter")

# Display file uploader widget
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# If user has uploaded a file
if uploaded_file is not None:
    # Load image from file
    img = Image.open(uploaded_file)
    # Convert image to text using PyTesseract
    text = pytesseract.image_to_string(img)
    # Display text in Streamlit app
    st.text_area("enter some text",text)

