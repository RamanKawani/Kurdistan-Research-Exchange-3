import streamlit as st
from navigation import app_navigation  # Import the updated navigation handler

def main():
    # Access the GitHub token securely from Streamlit's secrets
    github_token = st.secrets.get("GITHUB_TOKEN")
    
    # Initialize the app with navigation
    app_navigation()  # This is the main navigation handler

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

