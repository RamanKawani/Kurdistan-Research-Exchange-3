import streamlit as st
from home import home_section
from user_profile import user_profile_section  # Importing from a separate module
# Define placeholders for other sections if needed
def upload_papers():
    st.title("Upload Papers")
    st.write("Upload your research papers.")

def display_papers():
    st.title("View Papers")
    st.write("Browse through available research papers.")

def display_guidelines():
    st.title("Submission Guidelines")
    st.write("Follow these steps to submit your research.")

def collaborative_project_section():
    st.title("Collaborative Projects")
    st.write("Join or create collaborative research initiatives.")

def institutional_partnership_section():
    st.title("Institutional Partnerships")
    st.write("Learn about partnerships with institutions.")

# Navigation handler
def app_navigation():
    st.sidebar.title("Kurdistan Research Exchange")
    
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
        collaborative_project_section()
    elif choice == "Institutional Partnerships":
        institutional_partnership_section()

if __name__ == "__main__":
    app_navigation()

