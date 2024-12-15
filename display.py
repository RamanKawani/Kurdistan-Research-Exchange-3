import streamlit as st
import pandas as pd

def display_papers(df):
    # Search bar for filtering papers
    search_query = st.text_input("Search by title, author, or university:")
    
    if search_query:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
    
    # Display the papers
    st.write(df)
    
    # Allow download of papers
    for idx, row in df.iterrows():
        pdf_file = row['PDF']
        st.download_button(
            label="Download PDF",
            data=pdf_file,
            file_name=pdf_file,
            mime="application/pdf",
            key=f"download_{idx}"  # Unique key for each button
        )
