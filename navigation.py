import streamlit as st
from home import home_section  # Import the home section
from upload import upload_papers  # Import the upload papers section
from view_papers import display_papers  # Import the view papers section
from user_profile import user_profile_section  # Import the user profile section
from guidelines import display_guidelines  # Import the guidelines section
from collaborative_projects import collaborative_project_section  # Import the collaborative projects section

def app_navigation():
    # Sidebar UI enhancements
    st.sidebar.title("Kurdistan Research Exchange")  # Main title for sidebar
    st.sidebar.markdown("Welcome to the **Kurdistan Research Exchange** platform!")
    st.sidebar.markdown("Choose a section from the options below.")
    
    # Add an image to the sidebar (optional)
    st.sidebar.image("https://example.com/logo.png", width=150)

    # Define the navigation menu with icons (Streamlit's icon support)
    menu = [
        "🏠 Home",
        "📤 Upload Paper",
        "📚 View Papers",
        "👤 User Profile",
        "📄 Guidelines",
        "🤝 Collaborative Projects"
    ]

    # Sidebar menu radio button
    choice = st.sidebar.radio("Select an Option", menu)

    # Main content area
    st.title("Kurdistan Research Exchange Platform")  # Main title for body content

    if choice == "🏠 Home":
        home_section()  # Display the home section
    elif choice == "📤 Upload Paper":
        upload_papers()  # Display the upload paper section
    elif choice == "📚 View Papers":
        display_papers()  # Display the papers viewing section
    elif choice == "👤 User Profile":
        user_profile_section()  # Display the user profile section
    elif choice == "📄 Guidelines":
        display_guidelines()  # Display the guidelines section
    elif choice == "🤝 Collaborative Projects":
        collaborative_project_section()  # Display collaborative projects section

# Additional customization options can be added here (e.g., footer, info, etc.)


