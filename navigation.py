import streamlit as st
from view_papers import display_papers  # Ensure the correct function is imported

# Navigation function to handle the app's flow
def app_navigation():
    st.sidebar.title("Kurdistan Research Exchange")

    # Sidebar options
    menu = ["Home", "Upload Research Paper", "View Research Papers"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Based on the selection, call the corresponding function
    if choice == "Home":
        st.title("Welcome to Kurdistan Research Exchange")
        st.write("This is the platform for sharing and viewing research papers related to the Kurdistan region.")
    elif choice == "Upload Research Paper":
        # Call the function for uploading papers (this should be defined in another part of your code)
        pass
    elif choice == "View Research Papers":
        display_papers()  # Display the papers viewing section

