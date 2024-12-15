import streamlit as st
from home import home_section  # Import the home section
from upload import upload_papers  # Import the upload papers section
from view_papers import display_papers  # Import the view papers section
from user_profile import user_profile_section  # Import the user profile section
from guidelines import display_guidelines  # Import the guidelines section
from collaborative_projects import collaborative_project_section  # Import the collaborative projects section

def app_navigation():
    # Sidebar title and navigation options
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar menu options
    menu = ["Home", "Upload Papers", "View Papers", "User Profile", "Guidelines", "Collaborative Projects"]
    choice = st.sidebar.radio("Select a Section", menu)
    
    # Render the corresponding section based on the selected menu
    if choice == "Home":
        home_section()  # Display home section content
    elif choice == "Upload Papers":
        upload_papers()  # Display upload papers section content
    elif choice == "View Papers":
        display_papers()  # Display view papers section content
    elif choice == "User Profile":
        user_profile_section()  # Display user profile section content
    elif choice == "Guidelines":
        display_guidelines()  # Display guidelines section content
    elif choice == "Collaborative Projects":
        collaborative_project_section()  # Display collaborative projects section content
