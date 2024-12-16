import os
import streamlit as st
import pandas as pd

# Function to load paper data
def load_paper_data():
    # Replace with the actual path to your dataset or database
    # This is an example; you can load your data from a CSV, database, etc.
    data = {
        "Title": ["Paper 1", "Paper 2", "Paper 3", "Paper 4", "Paper 5", "Paper 6", "Paper 7"],
        "Author": ["Author 1", "Author 2", "Author 3", "Author 4", "Author 5", "Author 6", "Author 7"],
        "University": ["University A", "University B", "University C", "University D", "University E", "University F", "University G"],
        "Year": [2020, 2021, 2022, 2023, 2024, 2025, 2026],
        "Category": ["Category A", "Category B", "Category C", "Category D", "Category E", "Category F", "Category G"],
        "PDF": ["paper1.pdf", "paper2.pdf", "paper3.pdf", "paper4.pdf", "paper5.pdf", "paper6.pdf", "paper7.pdf"],
        "Link": ["#link1", "#link2", "#link3", "#link4", "#link5", "#link6", "#link7"]
    }
    return pd.DataFrame(data)

def display_papers():
    # Load paper data
    paper_df = load_paper_data()

    # Pagination settings
    papers_per_page = 3  # Number of papers to display per page
    total_papers = len(paper_df)
    total_pages = (total_papers // papers_per_page) + (1 if total_papers % papers_per_page != 0 else 0)

    # Display the current page number
    page_number = st.number_input("Page number", min_value=1, max_value=total_pages, value=1)

    # Calculate the start and end indices for the papers to display
    start_idx = (page_number - 1) * papers_per_page
    end_idx = start_idx + papers_per_page

    # Show the papers for the current page
    papers_to_display = paper_df.iloc[start_idx:end_idx]

    st.title("View Research Papers")

    for index, row in papers_to_display.iterrows():
        paper_pdf = row['PDF']
        file_path = os.path.join('uploads', paper_pdf)

        # Debugging: Show file paths
        st.write(f"Checking file path: {file_path}")
        st.write(f"Absolute file path: {os.path.abspath(file_path)}")

        if os.path.isfile(file_path):
            st.write(f"**{row['Title']}**")
            st.write(f"Author: {row['Author']}")
            st.write(f"University: {row['University']}")
            st.write(f"Year: {row['Year']}")
            st.write(f"Category: {row['Category']}")
            st.write(f"Link: {row['Link']}")
            with open(file_path, 'rb') as file:
                st.download_button("Download PDF", data=file.read(), file_name=paper_pdf)
        else:
            st.warning(f"PDF not found for {row['Title']}")

    # Show pagination controls
    if total_pages > 1:
        st.write(f"Page {page_number} of {total_pages}")

