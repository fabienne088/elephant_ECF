import pandas as pd
import streamlit as st
import io
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

st.image('./source/logo-ecfwhite.png')

# Title and description with custom colors (blue, light gray)
st.markdown("<h1 style='color: #0f8798;'>ECF Report</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: gray;'>Please fully complete the form</p>", unsafe_allow_html=True)

# Load the Excel file specifying the header location (adjust sheet_name or header row)
df = pd.read_excel('source/empty_form.xlsx', header=None)

# Extract headers from rows B3, B4, B6 to B10 and B13 to J13
headers_part_1 = df.iloc[[2, 3, 5, 6, 7, 8, 9], 1].dropna().tolist()  # B3, B4, B6 to B10
headers_part_2 = df.iloc[12, 1:10].dropna().tolist()  # B13 to J13

# Combine the headers
headers = headers_part_1 + headers_part_2

# Create a form dynamically using headers as labels
with st.form(key="dynamic_form"):
    form_inputs = {}
    for i, header in enumerate(headers):
        if i == 0:
            form_inputs[header] = st.text_input(header)
        elif i == 1:
            form_inputs[header] = st.text_input(header)
        elif i == 2:
            st.markdown("---")  # Divider (horizontal line)
        elif i == 3:
            options = [1,2,3,4]
            form_inputs[header] = st.selectbox(header, options)
        elif i == 4:
            options = ["Good", "Acceptable", "Challenged"]  # Replace with actual options
            form_inputs[header] = st.selectbox(header, options)
        elif i == 5:
            form_inputs[header] = st.text_input(header)
        elif i == 6:
            form_inputs[header] = st.date_input(
                header, 
                value=pd.to_datetime('today').date(),  # Default to today's date
                format="YYYY/MM/DD"
            )
            st.markdown("---")  # Divider (horizontal line)

        elif i == 7:
            options = [
                "Analysis (policy options)",
                "Analysis (implementation options)",
                "Analysis (risk & opportunities)",
                "Campaigning (advocacy)",
                "Campaigning (public)",
                "Coalition Building",
                "Education & Training",
                "Joint Projects",
                "Provide technical expertise on specific subjects"
                ]
            form_inputs[header] = st.selectbox(header, options)
        elif i == 8:
            options = ["Type A", "Type B"]
            form_inputs[header] = st.selectbox(header, options)
        elif 8 < i < 14:
            form_inputs[header] = st.text_input(header)
        elif i == 14: 
            options = ["Good", "Acceptable", "Challenged"]
            form_inputs[header] = st.selectbox(header, options)
        elif i == 15:
            # if form_inputs.get(headers[14]) == "Challenged":
            form_inputs[header] = st.text_input("Explanation (only required when challenged)") 


    submit_button = st.form_submit_button("Submit")

if submit_button:
    df = pd.DataFrame([form_inputs])
    csv = df.to_csv(index=False, sep=";", encoding="utf-8")
    csv_bytes = io.BytesIO(csv.encode('utf-8'))  # Convert to bytes for download
    
    st.download_button(
        label="Download CSV",
        data=csv_bytes,
        file_name="form_data.csv",
        mime="text/csv"
    )