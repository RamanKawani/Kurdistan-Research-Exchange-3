import streamlit as st
import pandas as pd
from display import display_papers
from upload import upload_papers

# Function to load sample data
def load_sample_data():
    data = {
        "Title": ["History of Kurdistan", "Modern Political Theory", "Sociological Trends"],
        "Author": ["Author 1", "Author 2", "Author 3"],
        "University": ["University A", "University B", "University C"],
        "Year": [2020, 2021, 2022],
        "Category": ["History", "Political Science", "Sociology"],
        "Link": ["http://example.com/paper1", "http://example.com/paper2", "http://example.com/paper3"],
        "PDF": ["http://example.com/paper1.pdf", "http://example.com/paper2.pdf", "http://example.com/paper3.pdf"]
    }
    return pd.DataFrame(data)

# Main function to handle navigation and sections
def main():
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = ["Home", "Upload Papers", "View Papers"]
    choice = st.sidebar.selectbox("Select a section", options)

    # Load sample data for papers
    df = load_sample_data()
    
    # Navigate based on user selection
    if choice == "Home":
        home_section()
    elif choice == "Upload Papers":
        upload_papers(df)
    elif choice == "View Papers":
        display_papers(df)

# Function for the Home section
def home_section():
    st.title("Welcome to Kurdistan Research Exchange")
    st.write("This platform allows users to upload, view, and share research papers related to the Kurdistan Region.")
    st.write("You can upload your papers under the **'Upload Papers'** section, and view papers in the **'View Papers'** section.")
    st.subheader("Categories Available")
    st.write("- History")
    st.write("- Political Science")
    st.write("- Sociology")
    st.write("- International Relations")
    st.write("- Philosophy")

if __name__ == "__main__":
    main()
