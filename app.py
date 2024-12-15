import streamlit as st
from navigation import app_navigation
from data_loading import load_sample_data

# Main function to handle app navigation and sections
def main():
    df = load_sample_data()
    
    # Call navigation function to render sections based on the user's choice
    app_navigation(df)

if __name__ == "__main__":
    main()
