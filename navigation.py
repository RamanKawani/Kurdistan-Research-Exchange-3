import streamlit as st
from home import home_section  # Import the home section
from upload import upload_papers  # Import the upload papers section
from view_papers import display_papers  # Import the view papers section
from guidelines import display_guidelines  # Import the guidelines section
from collaborative_projects import collaborative_project_section  # Import the collaborative projects section

def app_navigation():
    # Access GitHub token from Streamlit's secrets
    github_token = st.secrets.get("GITHUB_TOKEN", "Token not found")
    
    # Display part of the token for security reasons (Never expose the full token)
    st.sidebar.write(f"GitHub Token (hidden part): {github_token[:5]}...")  # Display part of the token

    # Sidebar UI - formal and academic style
    st.sidebar.title("Kurdistan Research Exchange")
    st.sidebar.markdown("Welcome to the **Kurdistan Research Exchange** platform.")
    st.sidebar.markdown("This platform is dedicated to sharing and accessing academic research related to the Kurdistan Region.")

    # Sidebar navigation menu
    menu = [
        "Home",
        "Upload Research Paper",
        "View Research Papers",
        "Guidelines",
        "Collaborative Projects",
    ]

    choice = st.sidebar.radio("Select an option from the menu", menu)

    # Main content area - formal and academic tone
    st.title("Kurdistan Research Exchange Platform")
    st.markdown("Please select one of the following sections to proceed.")

    # Conditional display of content based on selected menu option
    if choice == "Home":
        home_section()  # Display the home section
    elif choice == "Upload Research Paper":
        upload_papers()  # Display the upload papers section
    elif choice == "View Research Papers":
        display_papers()  # Display the papers viewing section
    elif choice == "Guidelines":
        display_guidelines()  # Display the guidelines section
    elif choice == "Collaborative Projects":
        # Update this section to pass the user email (admin or regular) for proper access
        collaborative_project_section(user_email="admin@example.com")  # Replace with actual user email

    # Footer Section - Academic and Formal
    st.markdown("---")
    st.markdown("## About the Platform")
    st.markdown("The **Kurdistan Research Exchange** is an open platform aimed at promoting academic research related to the Kurdistan Region. It serves as a space for researchers, students, and academics to share their work and collaborate with others.")
    
    st.markdown("### Contact Us")
    st.markdown("For more information, please contact us at: [info@kurdistan-research.org](mailto:info@kurdistan-research.org)")

    st.markdown("### Acknowledgments")
    st.markdown("We acknowledge the efforts of the Kurdistan Regional Government (KRG) and academic institutions in facilitating research and collaboration.")
