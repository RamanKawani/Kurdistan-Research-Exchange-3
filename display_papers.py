import streamlit as st
import os
import pandas as pd
from math import ceil

# Access the GitHub token securely from Streamlit's secrets
github_token = st.secrets.get("GITHUB_TOKEN")

# Function to load your paper data (this function assumes your data is in a CSV or similar format)
def load_paper_data():
    file_path = "research_papers.csv"
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        st.error(f"CSV file not found at {file_path}. Please upload the file or check the path.")
        return pd.DataFrame()  # Return an empty DataFrame if file is not found
    
    return pd.read_csv(file_path)

# Function to display papers with pagination
def display_papers():
    # Load paper data
    paper_df = load_paper_data()

    # If the DataFrame is empty, exit early
    if paper_df.empty:
        return

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

        # If GitHub token exists, use it for API requests or other purposes
        if github_token:
            # You can use the token here for GitHub API calls (e.g., to fetch repo data, commit history, etc.)
            # Example (replace with actual GitHub API logic):
            st.sidebar.write(f"GitHub Token is available. Token preview: {github_token[:5]}...")
        else:
            st.sidebar.error("GitHub Token not found.")

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

# Optionally, add a responsive layout for mobile
def responsive_layout():
    screen_width = st.slider("Select screen width for testing", min_value=300, max_value=1200, value=600)
    
    if screen_width < 500:
        st.markdown("<style>body { font-size: 12px; }</style>", unsafe_allow_html=True)
    else:
        st.markdown("<style>body { font-size: 16px; }</style>", unsafe_allow_html=True)

# Run this function in the main code
if __name__ == "__main__":
    display_papers()
