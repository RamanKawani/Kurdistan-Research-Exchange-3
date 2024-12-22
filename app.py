import streamlit as st
from navigation import app_navigation  # Import the updated navigation handler

# Access the GitHub token securely from Streamlit's secrets
github_token = st.secrets.get("GITHUB_TOKEN")

def main():
    # Check if the token was successfully retrieved
    if github_token:
        st.sidebar.write(f"GitHub Token: {github_token[:5]}...")  # Display part of it for debugging (do not expose full token)
    else:
        st.sidebar.error("GitHub token not found.")
    
    # Initialize the app with navigation
    app_navigation()  # This is the main navigation handler

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

