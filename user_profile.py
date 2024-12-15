import streamlit as st

# Simulating a simple database for user profiles
# In a real scenario, you could store profiles in a database
user_profiles = {}

# Function to handle user profile creation
def create_user_profile():
    st.title("Create Your Profile")

    # Form for user details
    with st.form("profile_form", clear_on_submit=True):
        username = st.text_input("Username")
        email = st.text_input("Email")
        bio = st.text_area("Bio", height=100)
        submit_button = st.form_submit_button("Create Profile")
        
        if submit_button:
            if username and email:
                user_profiles[username] = {
                    "Email": email,
                    "Bio": bio
                }
                st.success("Profile created successfully!")
            else:
                st.error("Please fill in all required fields.")
                
# Function to view and update user profiles
def view_and_update_profiles():
    st.title("Your Profile")

    username = st.selectbox("Select your username", options=list(user_profiles.keys()))

    if username:
        profile = user_profiles[username]
        st.write(f"**Email:** {profile['Email']}")
        st.write(f"**Bio:** {profile['Bio']}")

        # Update profile
        with st.form("update_form", clear_on_submit=True):
            new_email = st.text_input("Update Email", value=profile['Email'])
            new_bio = st.text_area("Update Bio", value=profile['Bio'], height=100)
            update_button = st.form_submit_button("Update Profile")
            
            if update_button:
                user_profiles[username] = {
                    "Email": new_email,
                    "Bio": new_bio
                }
                st.success("Profile updated successfully!")
    
    else:
        st.error("No profiles available.")
