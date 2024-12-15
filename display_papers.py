import streamlit as st
import pandas as pd

# Sample Data: Replace this with actual data or load from CSV/database
papers = [
    {"title": "Research on Kurdish Identity", "author": "Author 1", "university": "University A", "file": "file1.pdf"},
    {"title": "Kurdistan Economy Trends", "author": "Author 2", "university": "University B", "file": "file2.pdf"},
    # Add more papers here
]

# Display Papers
def display_papers():
    st.title("Research Papers")

    # Displaying research paper details in a table format
    df = pd.DataFrame(papers)
    st.write(df)

    # Display download button for each paper
    for paper in papers:
        st.subheader(paper["title"])
        st.write(f"Author: {paper['author']}")
        st.write(f"University: {paper['university']}")
        
        # Check if the file exists and is accessible (replace this with the correct path to the PDF files)
        file_path = f"files/{paper['file']}"
        
        try:
            with open(file_path, "rb") as pdf_file:
                st.download_button(
                    label="Download PDF",
                    data=pdf_file,
                    file_name=paper["file"],
                    mime="application/pdf",
                    key=paper["file"]  # Unique key for each download button
                )
        except FileNotFoundError:
            st.error(f"File {paper['file']} not found.")
