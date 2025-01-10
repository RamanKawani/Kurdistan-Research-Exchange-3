import streamlit as st
import pandas as pd
from database_data import load_data  # Ensure you're importing the correct function

def display_papers():
    # Load paper data from the database (CSV)
    paper_df = load_data()  # Use the correct function name here

    # Debugging: Check if paper_df has data
    st.write("Loaded Data:", paper_df)  # Display the entire loaded dataframe

    # Display papers header
    st.title("View Research Papers")

    # Pagination logic
    papers_per_page = 5  # Number of papers per page
    total_papers = len(paper_df)
    total_pages = ceil(total_papers / papers_per_page)

    # Sidebar pagination controls
    page_number = st.sidebar.number_input("Select Page", min_value=1, max_value=total_pages, value=1)

    # Calculate the start and end index for the current page
    start_idx = (page_number - 1) * papers_per_page
    end_idx = min(start_idx + papers_per_page, total_papers)

    # Display papers for the current page
    for index, row in paper_df.iloc[start_idx:end_idx].iterrows():
        paper_pdf = row['PDF']
        st.write(f"**{row['Title']}**")
        st.write(f"Author: {row['Author']}")
        st.write(f"University: {row['University']}")
        st.write(f"Year: {row['Year']}")
        st.write(f"Category: {row['Category']}")
        st.write(f"Link: {row['Link']}")

        # Check if the PDF file exists (you can modify this logic based on actual file structure)
        st.write(f"PDF: {row['PDF']}")  # Display the PDF link or use it for further action
