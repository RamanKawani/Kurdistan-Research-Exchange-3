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

 
