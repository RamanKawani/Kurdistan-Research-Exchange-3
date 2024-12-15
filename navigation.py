import streamlit as st
from view_papers import display_papers  # Import the function to display research papers
from upload_paper import upload_paper  # Import the function for uploading research papers

# Navigation function to handle the app's flow
def app_navigation():
    st.sidebar.title("Kurdistan Research Exchange")

    # Sidebar options
    menu = ["Home", "Upload Research Paper", "View Research Papers"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Based on the selection, call the corresponding function
    if choice == "Home":
        st.title("Welcome to Kurdistan Research Exchange")
        st.write("This platform allows you to upload, view, and share research papers related to the Kurdistan Region.")
        st.write("Browse and explore the work of researchers.")
    elif choice == "Upload Research Paper":
        upload_paper()  # Function for uploading research papers (you need to define this function in your 'upload_paper.py')
    elif choice == "View Research Papers":
        display_papers()  # Display the papers viewing section
