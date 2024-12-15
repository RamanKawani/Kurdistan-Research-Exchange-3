import streamlit as st

def home_section():
    # Title of the section
    st.title("Welcome to Kurdistan Research Exchange")

    # Brief description of the platform
    st.write("Browse a collection of research papers from various institutions.")

    # About the platform
    st.subheader("What is Kurdistan Research Exchange?")
    st.write("""
        The Kurdistan Research Exchange is a platform that connects researchers and academic institutions from Kurdistan and beyond.
        It aims to provide a central place to share research, collaborate, and promote academic exchange on various topics, including politics,
        international relations, social sciences, and more. The platform allows users to upload research papers, explore existing studies,
        and connect with other researchers.
    """)

    # How to use the platform
    st.subheader("How to Use This Platform")
    st.write("""
        1. Browse through research papers by category.
        2. Upload your own research to contribute to the platform.
        3. Engage with other researchers and institutions to collaborate and share insights.
    """)

    # Call to action
    st.button("Start Exploring")
