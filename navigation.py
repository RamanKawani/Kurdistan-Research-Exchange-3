import streamlit as st
from home import home_section  # Ensure home_section is properly imported

# Ensure other functions are imported or implemented
# If these are defined in other modules, adjust imports accordingly
try:
    from home import upload_papers, display_papers, user_profile_section, display_guidelines
    from home import collaborative_project_section, institutional_partnership_section
except ImportError:
    # Placeholder imports in case the functions are not yet defined
    def upload_papers():
        st.error("The 'Upload Papers' functionality is not yet implemented.")
    
    def display_papers():
        st.error("The 'View Papers' functionality is not yet implemented.")
    
    def user_profile_section():
        st.error("The 'User Profile' section is not yet implemented.")
    
    def display_guidelines():
        st.error("The 'Submission Guidelines' functionality is not yet implemented.")
    
    def collaborative_project_section():
        st.error("The 'Collaborative Projects' section is not yet implemented.")
    
    def institutional_partnership_section():
        st.error("The 'Institutional Partnerships' section is not yet implemented.")

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
        home_section()  # Ensure home_section is implemented in home.py
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

# Ensure the navigation script can run standalone if needed
if __name__ == "__main__":
    app_navigation()

