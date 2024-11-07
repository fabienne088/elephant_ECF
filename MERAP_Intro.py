import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.markdown("<h1 style='color: #0f8798;'>Make ECF Reports a PowerPool</h1>", unsafe_allow_html=True)

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Pour your knowledge into our **PowerPool**, and let it help you **grow** and create a bigger **impact**.
"""
)