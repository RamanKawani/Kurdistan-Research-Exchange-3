import streamlit as st

def user_profile_section():
    """Display the User Profile section."""
    st.title("User Profile")
    st.write("Welcome to your profile! Manage your account settings and preferences here.")

    # Display user information (static or dynamic example)
    st.subheader("Personal Information")
    st.write("Name: John Doe")
    st.write("Email: johndoe@example.com")
    st.write("Institution: University of Kurdistan")

    # Option to edit user information
    st.subheader("Edit Information")
    with st.form("edit_profile_form"):
        name = st.text_input("Name", value="John Doe")
        email = st.text_input("Email", value="johndoe@example.com")
        institut
