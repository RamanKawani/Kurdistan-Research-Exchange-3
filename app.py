import streamlit as st
from home import display_home
from upload import display_upload

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Upload Research Paper"])

    if selection == "Home":
        display_home()
    elif selection == "Upload Research Paper":
        display_upload()

if __name__ == "__main__":
    main()
