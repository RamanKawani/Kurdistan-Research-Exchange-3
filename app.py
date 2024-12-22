import streamlit as st
from navigation import app_navigation  # Import the updated navigation handler

def main():
    # Access GitHub token and repository URL from Streamlit's secrets
    github_token = st.secrets["GITHUB_TOKEN"]
    github_repo = st.secrets["GITHUB_REPO"]

    # Example of using the GitHub token and repository
    st.write(f"GitHub Repository: {github_repo}")
    st.write(f"GitHub Token: {github_token[:5]}...")  # Show part of the token for security

    # Initialize the app with navigation
    app_navigation()  # This is the main navigation handler

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
