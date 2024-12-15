import streamlit as st

# Simulated function to fetch user data dynamically (replace with your database logic)
def get_user_data():
    # Replace this with actual logic to fetch user data from a database or API
    return {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "institution": "University of Kurdistan",
    }

# Simulated function to save updated profile information
def save_user_data(updated_data):
    # Replace this with actual logic to save data to a database or API
    st.write("Debug: Updated user data saved!", updated_data)

# User Profile Section
def user_profile_section():
    st.title("User Profile")
    st.write("Manage your account details below.")
    
    # Fetch user data
    user_data = get_user_data()
    st.write("Debug: Retrieved User Data", user_data)  # Debugging information

    # User profile editing form
    with st.form("edit_profile_form"):
        st.subheader("Edit Profile Information")
        
        # Prefill user data in form inputs
        name = st.text_input("Name", user_data["name"])
        email = st.text_input("Email", user_data["email"])
        institution = st.text_input("Institution", user_data["institution"])
        
        # Submit button
        submitted = st.form_submit_button("Save Changes")
        if submitted:
            # Logic to handle form submission
            updated_data = {
                "name": name,
                "email": email,
                "institution": institution,
            }
            save_user_data(updated_data)
            st.success("Profile updated successfully!")
            st.experimental_rerun()  # Rerun app to reflect changes

    # Change Password Section
    st.subheader("Change Password")
    with st.form("change_password_form"):
        old_password = st.text_input("Old Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        password_submitted = st.form_submit_button("Change Password")
        
        if password_submitted:
            if new_password != confirm_password:
                st.error("New password and confirmation do not match.")
            elif len(new_password) < 6:
                st.error("Password must be at least 6 characters long.")
            else:
                # Simulate password change logic
                st.success("Password changed successfully!")

    # Logout Button
    if st.button("Logout"):
        st.info("You have been logged out.")
        # Implement your logout logic here
        st.stop()
