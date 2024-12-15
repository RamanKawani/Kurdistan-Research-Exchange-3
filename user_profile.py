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
        institution = st.text_input("Institution", value="University of Kurdistan")
        submitted = st.form_submit_button("Save Changes")
        if submitted:
            st.success("Your profile information has been updated!")
            st.write(f"Updated Name: {name}")
            st.write(f"Updated Email: {email}")
            st.write(f"Updated Institution: {institution}")

    # Section for changing the password
    st.subheader("Change Password")
    with st.form("change_password_form"):
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        password_submitted = st.form_submit_button("Update Password")
        if password_submitted:
            if new_password == confirm_password:
                st.success("Password updated successfully!")
            else:
                st.error("Passwords do not match. Please try again.")

    # Logout option
    st.subheader("Logout")
    if st.button("Log Out"):
        st.write("You have been logged out.")
