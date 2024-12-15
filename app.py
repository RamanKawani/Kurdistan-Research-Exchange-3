import os
import pandas as pd
import streamlit as st
from utils.data_utils import load_sample_data

# App configuration
st.set_page_config(
    page_title="Kurdistan Research Exchange",
    page_icon="📚",
    layout="wide",
)

# Sidebar with logo handling
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_container_width=True)
else:
    st.sidebar.write("🌍 **Kurdistan Research Exchange**")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Upload Research", "Explore Research"])

# Main content
if page == "Home":
    st.title("📚 Welcome to the Kurdistan Research Exchange")
    st.markdown("""
    This platform enables researchers and institutions in Kurdistan to share and access academic research. 
    Upload your research or explore contributions by others to advance knowledge across various fields.
    """)
    st.image("https://via.placeholder.com/800x400", use_container_width=True)

elif page == "Upload Research":
    st.title("📤 Upload Your Research Paper")
    st.markdown("Share your academic research with the community.")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload Your Research Paper (PDF)", type=["pdf"])
    if uploaded_file:
        st.success("File uploaded successfully!")
        st.write("File Name:", uploaded_file.name)
    
    # Metadata form
    with st.form("upload_form"):
        title = st.text_input("Title of the Paper", placeholder="Enter the research title")
        author = st.text_input("Author(s)", placeholder="Enter the author(s) name(s)")
        institution = st.text_input("Institution", placeholder="Enter your institution")
        year = st.number_input("Year of Publication", min_value=1900, max_value=2100, step=1)
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.success("Research metadata submitted!")
            st.write("**Title:**", title)
            st.write("**Author(s):**", author)
            st.write("**Institution:**", institution)
            st.write("**Year:**", int(year))

elif page == "Explore Research":
    st.title("🔍 Explore Research Papers")
    st.markdown("Browse the research papers uploaded by the community.")
    
    # Display sample data
    sample_data = load_sample_data()
    st.dataframe(sample_data)
    st.markdown("### Filter Research Papers")
    filter_year = st.slider("Filter by Year", min_value=2000, max_value=2024, value=(2010, 2024))
    filtered_data = sample_data[
        (sample_data["Year"] >= filter_year[0]) & (sample_data["Year"] <= filter_year[1])
    ]
    st.dataframe(filtered_data)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by [Your Name]. Powered by Streamlit.")

