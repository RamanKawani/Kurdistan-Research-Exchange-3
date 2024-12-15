import streamlit as st
from home import home_section
from upload import upload_papers
from display import display_papers
from user_profile import user_profile_section
from guidelines import display_guidelines
from collaborative_project import collaborative_project_section

# Function to manage the navigation between different sections
def app_navigation(df):
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines", "Collaborative Projects"]
    choice = st.sidebar.selectbox("Select a section", options)

    # Navigate based on user selection
    if choice == "Home":
        home_section()
    elif choice == "Upload Papers":
        upload_papers(df)
    elif choice == "View Papers":
        display_papers(df)
    elif choice == "User Profile":
        user_profile_section()
    elif choice == "Submission Guidelines":
        display_guidelines()
    elif choice == "Collaborative Projects":
        collaborative_project_section(user_email="user@example.com")  # Pass the user email for interaction
