import streamlit as st
import os
import pandas as pd

# Define file path for CSV where research papers are stored
DATA_FILE = 'research_papers.csv'
UPLOAD_DIR = 'uploads/'

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Function to save the paper metadata to CSV
def save_to_csv(paper_details):
    # Load the existing data from the CSV file
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

    # Append the new paper details to the DataFrame
    df = df.append(paper_details, ignore_index=True)

    # Save the updated DataFrame to the CSV file
    df.to_csv(DATA_FILE, index=False)

# Function to handle file upload
def upload_papers():
    st.title("Upload Research Paper")
    
    # Form to upload paper details
    with st.form(key='upload_form'):
        title = st.text_input("Title")
        author = st.text_input("Author")
        university = st.text_input("University")
        year = st.number_input("Year", min_value=1900, max_value=2025, step=1)
        category = st.text_input("Category")
        link = st.text_input("Link")
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

        # Submit button
        submit_button = st.form_submit_button(label="Upload Paper")

        if submit_button:
            if uploaded_file is not None:
                # Save the uploaded PDF to the directory
                file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Prepare the paper metadata
                paper_details = {
                    "Title": title,
                    "Author": author,
                    "University": university,
                    "Year": year,
                    "Category": category,
                    "Link": link,
                    "PDF": uploaded_file.name
                }

                # Save metadata to CSV
                save_to_csv(paper_details)

                st.success("Research paper uploaded successfully!")
            else:
                st.warning("Please upload a PDF file.")
