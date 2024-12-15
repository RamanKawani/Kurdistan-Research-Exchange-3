import streamlit as st

# Function to create a new user profile
def create_user_profile():
    st.title("Create User Profile")
    # Add fields for creating a profile (e.g., Name, Email, etc.)
    st.text_input("Full Name")
    st.text_input("Email Address")
    st.text_input("University")
    st.text_area("Bio")
    if st.button("Create Profile"):
        st.success("Profile Created Successfully!")

# Function to view and update user profiles
def view_and_update_profiles():
    st.title("View/Update User Profile")
    # Assuming we already have a profile data (or this can be loaded from a database)
    st.write("Your profile information:")
    st.text("Name: John Doe")
    st.text("Email: john.doe@example.com")
    st.text("University: Example University")
    st.text_area("Bio", "Short bio about yourself...")
    
    if st.button("Update Profile"):
        st.success("Profile Updated Successfully!")
