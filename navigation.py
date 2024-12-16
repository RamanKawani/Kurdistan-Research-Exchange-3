import streamlit as st
from home import home_section
from upload import upload_papers
from display_papers import display_papers  # Correct import of display_papers
from user_profile import user_profile_section
from guidelines import display_guidelines
from collaborative_projects import collaborative_project_section

def app_navigation():
    # Sidebar UI
    st.sidebar.title("Kurdistan Research Exchange")
    st.sidebar.markdown("Welcome to the **Kurdistan Research Exchange** platform.")

    menu = [
        "Home",
        "Upload Research Paper",
        "View Research Papers",
        "User Profile",
        "Guidelines",
        "Collaborative Projects"
    ]

    choice = st.sidebar.radio("Select an option from the menu", menu)

    # Main content area
    st.title("Kurdistan Research Exchange Platform")
    st.markdown("Please select one of the following sections to proceed.")

    if choice == "Home":
        home_section()
    elif choice == "Upload Research Paper":
        upload_papers()
    elif choice == "View Research Papers":
        display_papers()  # Correctly call the display_papers function
    elif choice == "User Profile":
        user_profile_section()
    elif choice == "Guidelines":
        display_guidelines()
    elif choice == "Collaborative Projects":
        collaborative_project_section()
