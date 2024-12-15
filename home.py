import streamlit as st

def home_section():
    # Display a title for the home section
    st.title("Welcome to the Kurdistan Research Exchange")

    # Description or information about the app
    st.write("""
        This platform allows users to upload, view, and collaborate on research papers related to the Kurdistan Region.
        It is a hub for researchers, institutions, and organizations to collaborate and share knowledge.
    """)

    # Add more content to the homepage if needed (e.g., introducing sections or services)
    st.subheader("Explore Our Features")
    st.write("""
        - **Research Paper Upload**: Share your research papers with the community.
        - **Collaborative Projects**: Join ongoing research initiatives.
        - **User Profile**: Manage your personal information and research activities.
    """)

    # Display some static content for now (e.g., welcome message or featured content)
    st.write("This is the homepage of the Kurdistan Research Exchange. Feel free to explore the available sections!")
    
    # Optionally add buttons or navigation links for the user
    if st.button("Go to Research Papers"):
        st.write("Navigate to the research papers section here.")  # Update with actual navigation later

    if st.button("Go to Collaborative Projects"):
        st.write("Navigate to the collaborative projects section here.")  # Update with actual navigation later
