import os
import streamlit as st
import pandas as pd
from data import load_paper_data

def display_papers():
    # Load paper data
    paper_df = load_paper_data()

    # Display papers
    st.title("View Research Papers")

    for index, row in paper_df.iterrows():
        paper_pdf = row['PDF']
        file_path = os.path.join('uploads', paper_pdf)
        st.write(f"Checking file path: {file_path}")  # Debugging line
        if os.path.isfile(file_path):  
            st.write(f"**{row['Title']}**")
            st.write(f"Author: {row['Author']}")
            st.write(f"University: {row['University']}")
            st.write(f"Year: {row['Year']}")
            st.write(f"Category: {row['Category']}")
            st.write(f"Link: {row['Link']}")
            st.download_button("Download PDF", data=open(file_path, 'rb').read(), file_name=paper_pdf)
        else:
            st.warning(f"PDF not found for {row['Title']}")

