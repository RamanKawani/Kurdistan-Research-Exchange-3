import streamlit as st
from navigation import app_navigation  # Import the updated navigation handler
from config import GITHUB_TOKEN  # Import the GitHub token from config.py

def main():
    # Display the GitHub token in the Streamlit app (just for testing, remove it later for security)
    if GITHUB_TOKEN:
        st.write("GitHub Token Loaded Successfully!")
    else:
        st.error("GitHub Token Not Found!")

    # Initialize the app with navigation
    app_navigation()  # This is the main navigation handler

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
