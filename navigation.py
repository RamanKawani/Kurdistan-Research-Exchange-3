import streamlit as st
from home import home_section  # Import the home section
from upload import upload_papers  # Import the upload papers section
from view_papers import display_papers  # Import the view papers section
from user_profile import user_profile_section  # Import the user profile section
from guidelines import display_guidelines  # Import the guidelines section
from collaborative_projects import collaborative_project_section  # Import the collaborative projects section

def app_navigation():
    # Sidebar UI - formal and academic style
    st.sidebar.title("Kurdistan Research Exchange")
    st.sidebar.markdown("Welcome to the **Kurdistan Research Exchange** platform.")
    st.sidebar.markdown("This platform is dedicated to sharing and accessing academic research related to the Kurdistan Region.")
    
    # Optional logo or image in the sidebar
    # st.sidebar.image("https://example.com/logo.png", width=150)

    # Sidebar navigation menu
    menu = [
        "Home",
        "Upload Research Paper",
        "View Research Papers",
        "User Profile",
        "Guidelines",
        "Collaborative Projects"
    ]

    choice = st.sidebar.radio("Select an option from the menu", menu)

    # Main content area - formal and academic tone
    st.title("Kurdistan Research Exchange Platform")
    st.markdown("Please select one of the following sections to proceed.")

    if choice == "Home":
        home_section()  # Display the home section
    elif choice == "Upload Research Paper":
        upload_papers()  # Display the upload papers section
    elif choice == "View Research Papers":
        display_papers()  # Display the papers viewing section with advanced features
    elif choice == "User Profile":
        user_profile_section()  # Display the user profile section
    elif choice == "Guidelines":
        display_guidelines()  # Display the guidelines section
    elif choice == "Collaborative Projects":
        collaborative_project_section()  # Display collaborative projects section

