import streamlit as st
import os
import pandas as pd
from math import ceil
from data import load_paper_data  # Assuming you have a function to load paper data
from database import delete_record  # Function to handle the deletion of a paper record

# Function to display papers with pagination and delete option for admins
def display_papers(user_email="user@example.com"):  # Pass the email for permission check
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

        # Admin-only delete option
        if user_email == "admin@example.com":  # Check if the user is an admin
            delete_button = st.button(f"Delete {row['Title']}", key=f"delete_{index}")
            if delete_button:
                # Call the function to delete the record from the CSV/database
                delete_record(row['Title'])
                st.success(f"The paper '{row['Title']}' has been deleted.")
                break  # Refresh the page after deletion to reflect changes

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

