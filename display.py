import os
import streamlit as st
import pandas as pd
from data import load_paper_data  # Assuming you have this function for loading paper data

def display_papers():
    # Load paper data
    paper_df = load_paper_data()

    # Display papers
    st.title("View Research Papers")

    # Debugging: Show all files in uploads directory
    try:
        files_in_directory = os.listdir('uploads')
        st.write("Files in 'uploads' directory:", files_in_directory)
    except FileNotFoundError:
        st.error("Uploads directory not found. Please check your folder structure.")
        return

    # Create a filter for categories
    categories = paper_df['Category'].unique()
    selected_category = st.selectbox("Select a category", options=["All"] + list(categories))

    # Filter the papers by selected category
    if selected_category != "All":
        paper_df = paper_df[paper_df['Category'] == selected_category]

    # Display each paper's details
    for index, row in paper_df.iterrows():
        paper_pdf = row['PDF']
        file_path = os.path.join('uploads', paper_pdf)

        # Debugging: Show file paths
        st.write(f"Checking file path: {file_path}")
        st.write(f"Absolute file path: {os.path.abspath(file_path)}")

        if os.path.isfile(file_path):
            # Display paper information without the Year field
            st.write(f"**{row['Title']}**")
            st.write(f"Author: {row['Author']}")
            st.write(f"University: {row['University']}")
            st.write(f"Category: {row['Category']}")
            st.write(f"Link: [Visit Link]({row['Link']})")

            # Provide PDF download button
            with open(file_path, 'rb') as file:
                st.download_button("Download PDF", data=file.read(), file_name=paper_pdf)

        else:
            st.warning(f"PDF not found for '{row['Title']}'. Please check back later.")

    # Additional Section for Category Filtering
    if selected_category == "All":
        st.markdown("""
            **Note:** You can filter papers by category using the dropdown above to find the research that interests you.
        """)
    else:
        st.markdown(f"""
            **You are viewing papers in the '{selected_category}' category.**
        """)

