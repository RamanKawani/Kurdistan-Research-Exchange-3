import streamlit as st
import pandas as pd
import os
from math import ceil

# Define file path for the CSV where research papers are stored
DATA_FILE = 'research_papers.csv'
UPLOAD_DIR = 'uploads/'

# Function to load data from the CSV file
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
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

        # Admin functionality to delete papers
        if user_email == "RamanKhalid888@gmail.com":  # Check if the user is an admin
            if st.button(f"Delete Paper: {row['Title']}", key=f"delete_{index}"):
                delete_paper(index, paper_df)

    # Display pagination controls at the bottom
    st.sidebar.write(f"Page {page_number} of {total_pages}")

# Function to delete paper
def delete_paper(index, df):
    # Get paper details to be deleted
    paper_to_delete = df.iloc[index]

    # Ask for confirmation before deletion
    confirm_delete = st.radio(f"Are you sure you want to delete '{paper_to_delete['Title']}'?", ('No', 'Yes'))

    if confirm_delete == 'Yes':
        # Drop the paper from the DataFrame and save the updated DataFrame
        df = df.drop(index)
        df.to_csv(DATA_FILE, index=False)
        st.success(f"Paper '{paper_to_delete['Title']}' deleted successfully!")
        display_papers(user_email)  # Refresh the papers list after deletion
    else:
        st.info(f"Paper '{paper_to_delete['Title']}' was not deleted.")
