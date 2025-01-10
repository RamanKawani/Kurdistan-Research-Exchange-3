import pandas as pd
import streamlit as st
import os

DATA_FILE = 'research_papers.csv'

# Function to save the paper metadata to CSV
def save_to_csv(paper_details):
    # Load the existing data from the CSV file
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with the correct columns
        df = pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

    # Convert paper_details to a DataFrame
    paper_df = pd.DataFrame([paper_details])

    # Concatenate the new paper with the existing data
    df = pd.concat([df, paper_df], ignore_index=True)

    # Save the updated DataFrame to the CSV file
    df.to_csv(DATA_FILE, index=False)

# Function to handle file upload and paper details input
def upload_papers():
    st.title("Upload Research Paper")
    
    # Form for user input of paper details
    with st.form(key='upload_form'):
        title = st.text_input("Title")
        author = st.text_input("Author")
        university = st.text_input("University")
        year = st.number_input("Year", min_value=1900, max_value=2025, step=1)
        category = st.text_input("Category")
        link = st.text_input("Link")
        pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

        submit_button = st.form_submit_button(label="Upload Paper")

        if submit_button:
            if title and author and university and year and category and link and pdf_file:
                # Save the uploaded file to the 'uploads' directory
                file_path = os.path.join('uploads', pdf_file.name)
                with open(file_path, "wb") as f:
                    f.write(pdf_file.getbuffer())

                # Prepare paper details to save to CSV
                paper_details = {
                    'Title': title,
                    'Author': author,
                    'University': university,
                    'Year': year,
                    'Category': category,
                    'Link': link,
                    'PDF': pdf_file.name
                }

                # Save the paper details to CSV
                save_to_csv(paper_details)
                st.success("Paper uploaded successfully!")
            else:
                st.error("Please fill in all the fields and upload the PDF.")

# If you need to call this in your main navigation or other sections, use:
# upload_papers()
