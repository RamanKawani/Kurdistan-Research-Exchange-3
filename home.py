import streamlit as st

def home():
    st.title("Welcome to Kurdistan Research Exchange")
    st.write("This is the home page. You can navigate to view papers or upload papers.")
    
    # Add buttons for navigation
    if st.button('View Papers'):
        st.session_state.page = "view_papers"
    elif st.button('Upload Papers'):
        st.session_state.page = "upload_papers"
