import streamlit as st

def display_home():
    st.title("Welcome to Kurdistan Research Exchange")
    st.header("A platform for sharing research papers from universities in Kurdistan and beyond.")
    
    st.write(
        """
        This platform allows users to upload and share research papers related to various fields. 
        Whether you're a student, researcher, or educator, you can contribute and gain access to valuable resources.
        """
    )
    
    st.subheader("How to Use:")
    st.write(
        """
        1. Upload your research paper by filling out the 'Upload Paper' form.
        2. Search for research papers using the search bar.
        3. Download research papers for your reference.
        """
    )

    st.image("https://via.placeholder.com/800x400", caption="Research and Collaboration", use_column_width=True)

    st.write("Start by exploring the app through the sidebar!")
