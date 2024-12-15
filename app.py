import streamlit as st
import pandas as pd  # Add this import statement
from home import home_section
from upload import upload_papers
from display import display_papers
from user_profile import create_user_profile, view_and_update_profiles
from guidelines import display_guidelines  # Import the guidelines section

# Function to load sample data (or you can replace with actual data loading code)
def load_sample_data():
    data = {
        "Title": ["Paper 1", "Paper 2", "Paper 3"],
        "Author": ["Author 1", "Author 2", "Author 3"],
        "University": ["University A", "University B", "University C"],
        "Year": [2020, 2021, 2022],
        "Category": ["Category A", "Category B", "Category C"],
        "Link": ["http://example.com/paper1", "http://example.com/paper2", "http://example.com/paper3"],
        "PDF": ["http://example.com/paper1.pdf", "http://example.com/paper2.pdf", "http://example.com/paper3.pdf"]
    }
    return pd.DataFrame(data)

# Main function to handle app navigation and sections
def main():
    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines"]
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
        display_guidelines()  # Display the guidelines section

# Function for User Profile section
def user_profile_section():
    st.sidebar.title("User Profile")
    profile_option = st.sidebar.radio("Select Profile Option", ("Create Profile", "View/Update Profile"))

    if profile_option == "Create Profile":
        create_user_profile()
    elif profile_option == "View/Update Profile":
        view_and_update_profiles()

# Run the main function
if __name__ == "__main__":
    main()
