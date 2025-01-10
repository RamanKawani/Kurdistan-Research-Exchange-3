import streamlit as st
from navigation import app_navigation  # Import the updated navigation handler
from config import GITHUB_TOKEN

def main():
    # Initialize the app with navigation
    app_navigation()  # This is the main navigation handler

# Run the main function when the script is executed
if __name__ == "__main__":
    main() 


