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

    # Define the navigation menu options
    menu = ["Home", "Upload Paper", "View Papers", "User Profile", "Guidelines", "Collaborative Projects"]
    
    # Add menu to sidebar
    choice = st.sidebar.radio("Select an Option", menu)

    # Display the appropriate section based on user's choice
    if choice == "Home":
        home_section()
    elif choice == "Upload Paper":
        upload_papers()
    elif choice == "View Papers":
        display_papers()
    elif choice == "User Profile":
        user_profile_section()
    elif choice == "Guidelines":
        display_guidelines()
    elif choice == "Collaborative Projects":
        collaborative_project_section()


