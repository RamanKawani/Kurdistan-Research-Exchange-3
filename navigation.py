# navigation.py
import streamlit as st
from institutional_partnership import institutional_partnership_section  # Ensure correct import

def app_navigation():
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines", "Collaborative Projects", "Institutional Partnerships"]
    choice = st.sidebar.selectbox("Select a section", options)
    
    # Handling the navigation logic for each section
    if choice == "Home":
        home_section()
    elif choice == "Upload Papers":
        upload_papers()  # Ensure you have this function in your app
    elif choice == "View Papers":
        display_papers()  # Ensure you have this function in your app
    elif choice == "User Profile":
        user_profile_section()  # Ensure you have this function in your app
    elif choice == "Submission Guidelines":
        display_guidelines()  # Ensure you have this function in your app
    elif choice == "Collaborative Projects":
        collaborative_project_section()  # Ensure you have this function in your app
    elif choice == "Institutional Partnerships":
        institutional_partnership_section()  # Navigate to the institutional partnership section

def home_section():
    st.title("Welcome to Kurdistan Research Exchange")
    st.write("This platform allows users to upload, view, and share research papers related to the Kurdistan Region.")
