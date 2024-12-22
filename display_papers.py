import streamlit as st
import os
from math import ceil
from data import load_paper_data  # Import the load_paper_data function

# Function to display papers with pagination
def display_papers():
    # Load paper data from the CSV
    paper_df = load_paper_data()

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
        file_path = os.path.join('uploads', paper_pdf)

        # Display paper details
        st.write(f"**{row['Title']}**")
        st.write(f"Author: {row['Author']}")
        st.write(f"University: {row['University']}")
        st.write(f"Year: {row['Year']}")
        st.write(f"Category: {row['Category']}")
        st.write(f"Link: {row['Link']}")

        # Check if the PDF file exists
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                st.download_button("Download PDF", data=file.read(), file_name=paper_pdf)
        else:
            st.warning(f"PDF not found for {row['Title']}")

    # Display pagination controls at the bottom
    st.sidebar.write(f"Page {page_number} of {total_pages}")
    if total_pages > 1:
        if page_number < total_pages:
            next_page = st.sidebar.button("Next Page")
            if next_page:
                page_number += 1
        if page_number > 1:
            prev_page = st.sidebar.button("Previous Page")
            if prev_page:
                page_number -= 1

# Run this function in the main code
if __name__ == "__main__":
    display_papers()

