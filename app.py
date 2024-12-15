import streamlit as st
import pandas as pd
from utils.data_utils import load_sample_data

# App configuration
st.set_page_config(
    page_title="Kurdistan Research Exchange",
    page_icon="🌐",
    layout="wide",
)

# Sidebar
st.sidebar.image("assets/logo.png", use_column_width=True)
st.sidebar.title("Kurdistan Research Exchange")
st.sidebar.markdown("A platform to share and explore university research in Kurdistan.")

# Main content
st.title("📚 Welcome to the Kurdistan Research Exchange")
st.markdown("""
This platform enables researchers and institutions in Kurdistan to share and access academic research. 
Upload your research or explore contributions by others to advance knowledge across various fields.
""")

# File uploader for research papers
uploaded_file = st.file_uploader("Upload Your Research Paper (PDF)", type=["pdf"])
if uploaded_file:
    st.success("File uploaded successfully!")
    # Add GitHub integration for saving/uploading files

# Display sample data
st.header("Sample Research Papers")
sample_data = load_sample_data()
st.dataframe(sample_data)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by [Your Name]. Powered by Streamlit.")

