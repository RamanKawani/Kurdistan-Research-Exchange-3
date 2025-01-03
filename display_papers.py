import streamlit as st
import os
from math import ceil
from data import load_paper_data
from database import add_record, update_record, delete_record  # Import database functions

# Function to display papers with pagination
def display_papers():
    # Load paper data from the CSV
    paper_df = load_paper_data()

    if paper_df.empty:
        st.warning("No papers available to display.")
        return

    # Display papers header
    st.title("View Research Papers")

    # Pagination logic
    papers_per_page = 5  # Number of papers per page
    total_papers = len(paper_df)
    total_pages = ceil(total_papers / papers_per_page)

    # Sidebar pagination controls
    st.sidebar.header("Pagination Controls")
    page_number = st.sidebar.slider(
        "Select Page", min_value=1, max_value=total_pages, value=1, step=1
    )

    # Calculate the start and end index for the current page
    start_idx = (page_number - 1) * papers_per_page
    end_idx = min(start_idx + papers_per_page, total_papers)

    # Display papers for the current page
    st.subheader(f"Page {page_number} of {total_pages}")
    for index, row in paper_df.iloc[start_idx:end_idx].iterrows():
        paper_pdf = row['PDF']
        file_path = os.path.join('uploads', paper_pdf)

        # Display paper details
        st.write(f"### {row['Title']}")
        st.write(f"- **Author**: {row['Author']}")
        st.write(f"- **University**: {row['University']}")
        st.write(f"- **Year**: {row['Year']}")
        st.write(f"- **Category**: {row['Category']}")
        st.write(f"- **Link**: [View Paper]({row['Link']})")

        # Check if the PDF file exists
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                st.download_button(
                    "Download PDF", data=file.read(), file_name=paper_pdf, key=f"download_{index}"
                )
        else:
            st.warning(f"PDF not found for {row['Title']}")

    # Display page navigation buttons
    col1, col2, col3 = st.sidebar.columns([1, 2, 1])
    with col1:
        if page_number > 1:
            if st.button("Previous Page"):
                st.experimental_set_query_params(page=page_number - 1)

    with col3:
        if page_number < total_pages:
            if st.button("Next Page"):
                st.experimental_set_query_params(page=page_number + 1)

    # Add new paper (example)
    st.sidebar.header("Add New Paper")
    if st.sidebar.button("Add New Paper"):
        new_paper = {
            "Title": "New Research Paper",
            "Author": "New Author",
            "University": "New University",
            "Year": 2025,
            "Category": "New Category",
            "Link": "http://example.com/newpaper",
            "PDF": "newpaper.pdf",
        }
        add_record(new_paper)
        st.sidebar.success("New paper added successfully.")

# Run this function in the main code
if __name__ == "__main__":
    display_papers()

