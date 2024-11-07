import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="PowerPool",
    page_icon="🌊",
)

st.image('./source/logo-ecfwhite.png')

st.markdown("<h1 style='color: #0f8798;'>A PowerPool of ECF Knowledge</h1>", unsafe_allow_html=True)

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Pour your knowledge into our **PowerPool**, and let it help you **grow** and create a bigger **impact**.
"""
)

# Open and rotate the image
image = Image.open('./source/IMG_4833.JPG')
rotated_image = image.rotate(180)  # Rotate 180 degrees

# Display the rotated image
st.image(rotated_image)