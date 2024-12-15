from user_profile import user_profile_section

def app_navigation():
    st.sidebar.title("Kurdistan Research Exchange")
    
    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines", "Collaborative Projects", "Institutional Partnerships"]
    choice = st.sidebar.selectbox("Select a section", options)
    
    if choice == "Home":
        home_section()
    elif choice == "Upload Papers":
        upload_papers()
    elif choice == "View Papers":
        display_papers()
    elif choice == "User Profile":
        user_profile_section()  # Correctly call the User Profile section
    elif choice == "Submission Guidelines":
        display_guidelines()
    elif choice == "Collaborative Projects":
        collaborative_project_section()
    elif choice == "Institutional Partnerships":
        institutional_partnership_section()
