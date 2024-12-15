import streamlit as st
from home import display_home
from upload import display_upload
from display_papers import display_papers

# Set the title of the app
st.set_page_config(page_title="Kurdistan Research Exchange", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Upload Paper", "Research Papers"))

def main():
    if page == "Home":
        display_home()
    elif page == "Upload Paper":
        display_upload()
    elif page == "Research Papers":
        display_papers()

if __name__ == "__main__":
    main()
