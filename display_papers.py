import streamlit as st
import pandas as pd

def display_papers(df):
    # Display title
    st.title("Kurdistan Research Exchange")

    # File upload section
    uploaded_file = st.file_uploader("Upload a research paper (PDF only)", type="pdf")
    if uploaded_file is not None:
        pdf_data = uploaded_file.read()
        st.write("File uploaded successfully!")

    # Display papers
    st.subheader("Research Papers")
    
    # Search bar with unique key
    search_query = st.text_input("Search by title, author, or university:", key="search_input")
    
    if search_query:
        df_filtered = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
    else:
        df_filtered = df

    # Display filtered papers as a table
    st.write(df_filtered)

    # PDF download buttons for each paper
    for index, row in df_filtered.iterrows():
        paper_title = row["title"]
        pdf_file = row["pdf_file"]
        
        # Add a unique key to avoid duplicate element IDs
        st.download_button(
            label=f"Download {paper_title}",
            data=pdf_file,
            file_name=f"{paper_title}.pdf",
            mime="application/pdf",
            key=f"download_button_{index}"  # Unique key for each button
        )
