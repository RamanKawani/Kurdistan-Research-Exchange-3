import streamlit as st
import pandas as pd
from home import home  # Ensure the function is correctly imported
from display import display_papers
from upload import upload_papers

def main():
    # Initialize session state to keep track of the current page
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Page routing logic
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "view_papers":
        df = pd.DataFrame()  # Replace with actual DataFrame for papers
        display_papers(df)
    elif st.session_state.page == "upload_papers":
        upload_papers()

if __name__ == "__main__":
    main()
