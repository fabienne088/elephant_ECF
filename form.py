import streamlit as st

st.image('./source/logo-ecfwhite.png')

# Title and description with custom colors (blue, light gray)
st.markdown("<h1 style='color: #0f8798;'>ECF report - Prototype</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: gray;'>Please fully complete the form</p>", unsafe_allow_html=True)

# Form fields
name = st.text_input("Grantee Name")
request_id = st.text_input("Grant Request ID")

st.divider()

objective_statement = st.text_input("Grant Objective Statement") 
reporting_period = st.text_input("Reporting period") 
progress_statement = st.selectbox(
    "Grant Progress Statement", 
    ("Good", "Acceptable", "Challenged"),
    index=None,
    placeholder="Select...",
)

#st.write("You selected:", progress_statement) 

date = st.text_input("Date") 

st.divider()

objective_statement = st.text_input("Grant Objective Statement") 
objective_statement = st.text_input("Grant Objective Statement") 

age = st.number_input("Age", min_value=0, max_value=100)