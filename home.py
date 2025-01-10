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
        - **Discover Research**: Browse through a wide collection of research papers from various fields.
        - **Access Resources**: Gain access to valuable resources for academic and professional growth.
    """)

    # Additional instructions or call to actions
    st.subheader("Get Started")
    st.write("""
        To contribute, simply upload your research paper using the 'Upload Research Paper' section. 
        You can also explore research papers from other scholars in the 'View Research Papers' section. 
        Together, we can build a strong knowledge base for the Kurdistan Region.
    """)

    st.subheader("Contact Us")
    st.write("""
        Have questions or suggestions? Feel free to reach out to us via our contact page.
    """)
