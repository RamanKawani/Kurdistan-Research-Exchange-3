import streamlit as st
from home import home_section  # Ensure home_section is imported here
from upload import upload_papers  # Ensure upload_papers is imported
from view_papers import display_papers  # Ensure display_papers is imported
from user_profile import user_profile_section  # Ensure user_profile_section is imported
from guidelines import display_guidelines  # Ensure display_guidelines is imported
from collaborative_projects import collaborative_project_section  # Ensure collaborative_project_section is imported
from institutional_partnerships import institutional_partnership_section  # Ensure institutional_partnership_section is imported

def app_navigation():
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = [
        "Home", 
        "Upload Papers", 
        "View Papers", 
        "User Profile", 
        "Submission Guidelines", 
        "Collaborative Projects", 
        "Institutional Partnerships"
    ]
    choice = st.sidebar.selectbox("Select a section", options)
    
    # Navigate based on user selection
    if choice == "Home":
        home_section()  # Ensure home_section is being called
    elif choice == "Upload Papers":
        upload_papers()
    elif choice == "View Papers":
        display_papers()
    elif choice == "User Profile":
        user_profile_section()
    elif choice == "Submission Guidelines":
        display_guidelines()
    elif choice == "Collaborative Projects":
        collaborative_project_section()
    elif choice == "Institutional Partnerships":
        institutional_partnership_section()

