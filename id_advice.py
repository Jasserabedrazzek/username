import streamlit as st

# Get the value of the username configuration key
username = st.secrets["username"]

# Show the username
st.text(f"Welcome, {username}!")

