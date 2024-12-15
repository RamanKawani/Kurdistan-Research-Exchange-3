import streamlit as st
from home import display_home
from upload import display_upload
from display import display_papers

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Upload Research Paper", "View Papers"])

    if selection == "Home":
        display_home()
    elif selection == "Upload Research Paper":
        display_upload()
    elif selection == "View Papers":
        display_papers()  # Show the papers to the user

if __name__ == "__main__":
    main()

