import os
import streamlit as st
import pandas as pd
from data import load_paper_data  # Assuming you have this function for loading paper data

def display_papers():
    # Load paper data
    paper_df = load_paper_data()

    # Display papers title
    st.title("View Research Papers")

    # Debugging: Show all files in uploads directory
    try:
        files_in_directory = os.listdir('uploads')
        st.write("Files in 'uploads' directory:", files_in_directory)
    except FileNotFoundError:
        st.error("Uploads directory not found. Please check your folder structure.")
        return

    # Search functionality
    search_query = st.text_input("Search papers by title or author:")

    # Filter papers based on search query
    if search_query:
        paper_df = paper_df[paper_df['Title'].str.contains(search_query, case=False) |
                            paper_df['Author'].str.contains(search_query, case=False)]

    # Filter by category
    categories = paper_df['Category'].unique()
    selected_category = st.selectbox("Select a category", options=["All"] + list(categories))

    if selected_category != "All":
        paper_df = paper_df[paper_df['Category'] == selected_category]

    # Pagination setup
    papers_per_page = 5
    total_papers = len(paper_df)
    page_num = st.slider("Select page", 1, (total_papers // papers_per_page) + 1)

    # Slice the dataframe for the selected page
    start_idx = (page_num - 1) * papers_per_page
    end_idx = page_num * papers_per_page
    paper_df_page = paper_df[start_idx:end_idx]

    # Display each paper's details in a grid
    for index, row in paper_df_page.iterrows():
        paper_pdf = row['PDF']
        file_path = os.path.join('uploads', paper_pdf)

        # Display paper information in a card-style layout
        with st.expander(f"**{row['Title']}**"):
            st.write(f"Author: {row['Author']}")
            st.write(f"University: {row['University']}")
            st.write(f"Category: {row['Category']}")
            st.write(f"Link: [Visit Link]({row['Link']})")

            # Display PDF download button
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    st.download_button("Download PDF", data=file.read(), file_name=paper_pdf)
            else:
                st.warning(f"PDF not found for '{row['Title']}'.")

    # Display pagination information
    st.write(f"Page {page_num} of {(total_papers // papers_per_page) + 1}")
