import streamlit as st
from home import home_section  # Ensure home_section is imported
from user_profile import user_profile_section  # Ensure user_profile_section is imported
from collaborative_projects import collaborative_project_section  # Ensure the section is imported
from upload import upload_papers  # Assuming this function exists for file upload
from view_papers import display_papers  # Assuming this function exists for displaying papers
from guidelines import display_guidelines  # Assuming this function exists for guidelines
from institutional_partnerships import institutional_partnership_section  # Assuming this function exists

def app_navigation():
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines", "Collaborative Projects", "Institutional Partnerships"]
    choice = st.sidebar.selectbox("Select a section", options)
    
    # Navigate based on user selection
    if choice == "Home":
        home_section()  # This should call the function defined in home.py
    elif choice == "Upload Papers":
        upload_papers()  # Ensure this function is defined and imported
    elif choice == "View Papers":
        display_papers()  # Ensure this function is defined and imported
    elif choice == "User Profile":
        user_profile_section()  # This should be imported correctly
    elif choice == "Submission Guidelines":
        display_guidelines()  # This should be imported correctly
    elif choice == "Collaborative Projects":
        collaborative_project_section()  # This should be imported correctly
    elif choice == "Institutional Partnerships":
        institutional_partnership_section()  # This should be imported correctly
