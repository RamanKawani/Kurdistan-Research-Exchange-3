import streamlit as st
import pandas as pd
from home import home
from upload import upload
from display_papers import display_papers

# Load the data (assuming you have data loaded as a pandas DataFrame)
def load_data():
    # Example: Load your data here
    data = {
        "title": ["Paper 1", "Paper 2", "Paper 3"],
        "author": ["Author A", "Author B", "Author C"],
        "university": ["University X", "University Y", "University Z"],
        "pdf_file": [b"pdf_data_1", b"pdf_data_2", b"pdf_data_3"]  # Simulated PDF binary data
    }
    return pd.DataFrame(data)

def main():
    # Load data
    df = load_data()

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", ["Home", "Research Papers", "Upload Paper"])

    if page == "Home":
        home()
    elif page == "Research Papers":
        display_papers(df)
    elif page == "Upload Paper":
        df = upload(df)

if __name__ == "__main__":
    main()
