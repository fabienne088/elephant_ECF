import streamlit as st

# Sample data with LinkedIn links
NGO_DATA = [
    {
        "region": "Asia",
        "country": "India",
        "type": "Health",
        "keywords": ["healthcare"],
        "contact": "Dr. A. Singh",
        "linkedin": "https://www.linkedin.com/in/example-profile-singh"
    },
    {
        "region": "Europe",
        "country": "Germany",
        "type": "Education",
        "keywords": ["education", "youth"],
        "contact": "Ms. B. Meyer",
        "linkedin": "https://www.linkedin.com/in/example-profile-meyer"
    },
    {
        "region": "Africa",
        "country": "Kenya",
        "type": "Environment",
        "keywords": ["conservation"],
        "contact": "Mr. C. Otieno",
        "linkedin": "https://www.linkedin.com/in/example-profile-otieno"
    },
]

st.image('./source/logo-ecfwhite.png')

# Title and description with custom colors (blue, light gray)
st.markdown("<h1 style='color: #0f8798;'>NGO Search Page</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: gray;'>Filter your search by region, country, type, and keywords to find contact persons at NGOs.</p>", unsafe_allow_html=True)

# Filter input fields
region = st.selectbox("**Region**", options=["", "Asia", "Europe", "Africa"])
country = st.text_input("**Country**")
ngo_type = st.text_input("**Type of NGO**")
keywords = st.text_input("**Keywords** (comma-separated)")

# Title and styling for Streamlit button
st.markdown("""
    <style>
        .stButton>button {
            background-color: #0f8798;  /* Blue background */
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #cdeef2;  /* Light blue on hover */
            border: 2px solid #0f8798;  /* Border added on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Search button and filtering functionality
if st.button("**Search**"):
    keyword_list = [kw.strip().lower() for kw in keywords.split(",") if kw.strip()]

    filtered_data = [
        ngo for ngo in NGO_DATA
        if (not region or ngo["region"] == region)
        and (not country or ngo["country"].lower() == country.lower())
        and (not ngo_type or ngo["type"].lower() == ngo_type.lower())
        and (not keyword_list or any(keyword in ngo["keywords"] for keyword in keyword_list))
    ]


    # Display results
    if filtered_data:
        for ngo in filtered_data:
            st.write(
                f"**Contact Person:** {ngo['contact']} - "
                f"**NGO Type:** {ngo['type']} - "
                f"**Country:** {ngo['country']} - "
                f"[LinkedIn Profile]({ngo['linkedin']})"
            )
    else:
        st.write("No results found.")
