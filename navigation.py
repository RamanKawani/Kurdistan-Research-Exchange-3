import streamlit as st
from home import home_section
from upload import upload_papers
from display import display_papers
from user_profile import create_user_profile, view_and_update_profiles
from guidelines import display_guidelines
from collaborative_project import collaborative_project_section
from institutional_partnership import institutional_partnership_section  # Assuming you added this section

# Function to handle navigation between sections
def app_navigation():
    # Sidebar for navigation
    st.sidebar.title("Kurdistan Research Exchange")

    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines", "Collaborative Projects", "Institutional Partnerships"]
    choice = st.sidebar.selectbox("Select a section", options)

    # Based on the user's selection, navigate to the appropriate section
    if choice == "Home":
        home_section()
    elif choice == "Upload Papers":
        upload_papers()
    elif choice == "View Papers":
        display_papers()
    elif choice == "User Profile":
        user_profile_section()
    elif choice == "Submission Guidelines":
        display_guidelines()
    elif choice == "Collaborative Projects":
        collaborative_project_section(user_email="user@example.com")
    elif choice == "Institutional Partnerships":
        institutional_partnership_section()  # Added the institutional partnership section here

