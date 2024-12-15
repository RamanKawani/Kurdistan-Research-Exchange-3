import streamlit as st
import os
from data import load_paper_data  # Ensure the load_paper_data function is correctly imported

# Function to display papers
def display_papers():
    # Load the paper data using the load_paper_data function from data.py
    paper_df = load_paper_data()

    st.title("View Research Papers")

    # Display the data as a table
    st.dataframe(paper_df)

    # Loop through the DataFrame and display each paper
    for index, row in paper_df.iterrows():
        st.subheader(f"Title: {row['Title']}")
        st.write(f"Author: {row['Author']}")
        st.write(f"University: {row['University']}")
        st.write(f"Year: {row['Year']}")
        st.write(f"Category: {row['Category']}")

        # Check if the PDF file exists in the 'uploads' folder
        paper_pdf = row['PDF']
        if os.path.isfile(os.path.join('uploads', paper_pdf)):  # Ensure that this check is correct
            with open(os.path.join('uploads', paper_pdf), 'rb') as file:
                st.download_button(label=f"Download {row['Title']} PDF", data=file, file_name=paper_pdf, mime='application/pdf')
        else:
            st.warning(f"PDF not found for {row['Title']}")
