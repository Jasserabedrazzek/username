import getpass
import streamlit as st
username = getpass.getuser()
st.set_page_config(page_title=username,page_icon = None,layout='centered')


print("Welcome, " + username + "!")
st.write("Welcome, " + username + "!")