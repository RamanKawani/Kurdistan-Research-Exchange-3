import streamlit as st
import pandas as pd
import os
from math import ceil
from database import delete_record  # Import the delete function from database.py

# Define constants
DATA_FILE = 'research_papers.csv'
UPLOAD_DIR = 'uploads/'
ADMIN_EMAIL = "your_actual_email@gmail.com"  # Replace with your actual admin email

# Function to load data from the CSV file
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        st.error(f"Data file '{DATA_FILE}' not found. Please upload it to continue.")
        return pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

# Function to display papers with pagination
def display_papers(user_email="user@example.com"):
    # Load paper data from the database (CSV)
    paper_df = load_data()

    if paper_df.empty:
        st.warning("No papers available to display.")
        return

    # Display papers header
    st.title("View Research Papers")

    # Pagination logic
    papers_per_page = 5
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
        file_path = os.path.join(UPLOAD_DIR, paper_pdf)

        # Display paper details
        st.write(f"### {row['Title']}")
        st.write(f"**Author:** {row['Author']}")
        st.write(f"**University:** {row['University']}")
        st.write(f"**Year:** {row['Year']}")
        st.write(f"**Category:** {row['Category']}")
        st.write(f"[External Link]({row['Link']})")

        # Check if the PDF file exists
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                st.download_button("Download PDF", data=file.read(), file_name=paper_pdf)
        else:
            st.warning(f"PDF not found for '{row['Title']}'")

        # Admin functionality to delete papers
        if user_email == ADMIN_EMAIL:
            st.write(f"Admin Email Verified: {user_email}")
            delete_button = st.button(f"Delete Paper: {row['Title']}", key=f"delete_{index}")

            if delete_button:
                confirm_delete = st.radio(
                    f"Are you sure you want to delete '{row['Title']}'?", 
                    options=['No', 'Yes'], 
                    key=f"confirm_delete_{index}"
                )

                if confirm_delete == 'Yes':
                    success, deleted_title = delete_record(index)  # Call the function to delete the paper
                    if success:
                        st.success(f"Paper '{deleted_title}' deleted successfully!")
                        st.experimental_rerun()  # Refresh the page after deletion
                    else:
                        st.error(f"Error deleting the paper: '{row['Title']}'")
                else:
                    st.info(f"Paper '{row['Title']}' w
