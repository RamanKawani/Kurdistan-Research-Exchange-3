import streamlit as st
from institutional_partnership import institutional_partnership_section  # Import the institutional partnership section

# Main function to handle app navigation and sections
def main():
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines", "Collaborative Projects", "Institutional Partnerships"]
    choice = st.sidebar.selectbox("Select a section", options)

    # Load sample data for papers
    df = load_sample_data()
    
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
    elif choice == "Institutional Partnerships":
        institutional_partnership_section()  # Add the institutional partnership section

# Function for the Home section
def home_section():
    st.title("Welcome to Kurdistan Research Exchange")
    st.write("This platform allows users to upload, view, and share research papers related to the Kurdistan Region.")
    st.write("You can upload your papers under the **'Upload Papers'** section, and view papers in the **'View Papers'** section.")
    
    # Add more sections or information here if necessary
    st.subheader("About")
    st.write("Kurdistan Research Exchange is an open platform to share and access academic research papers related to the Kurdistan Region.")

# Run the main function
if __name__ == "__main__":
    main()
