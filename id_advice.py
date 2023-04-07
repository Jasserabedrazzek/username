import streamlit as st
import pytesseract
from PIL import Image

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

