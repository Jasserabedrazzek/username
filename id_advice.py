import streamlit as st
from PIL import Image
import pytesseract

# Define video_recorder variable and set its initial value to None
video_recorder = None

# Title of the app
st.title("Image to Text Conversion")

# Add a sidebar with instructions
st.sidebar.header("Instructions")
st.sidebar.markdown("1. Upload an image or capture from the camera.")
st.sidebar.markdown("2. Click the 'Convert' button to convert image to text.")

# Use st.file_uploader to allow user to upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Use st_camera to capture an image from camera
if st.button("Capture"):
    st_camera = st.beta_container()
    with st_camera:
        # Update the value of video_recorder if the button is clicked
        video_recorder = st.camera()

# Use pytesseract to convert image to text
if uploaded_file or video_recorder is not None:
    if uploaded_file:
        # Open and display the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    elif video_recorder is not None:
        # Get the latest frame from the camera recorder
        image = video_recorder.read()
        st.image(image, caption="Captured Image", use_column_width=True)

    # Convert image to text using pytesseract
    text = pytesseract.image_to_string(image)

    # Display the extracted text
    st.header("Extracted Text")
    st.write(text)

