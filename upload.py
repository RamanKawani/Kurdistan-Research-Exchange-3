import streamlit as st
import pandas as pd

# Function to handle paper uploads
def upload_papers(df):
    st.title("Upload Research Papers")
    st.write("Upload your research paper here.")

    # Paper details form
    with st.form("upload_form", clear_on_submit=True):
        title = st.text_input("Title")
        author = st.text_input("Author")
        university = st.text_input("University")
        year = st.number_input("Year", min_value=1900, max_value=2025)
        
        # Predefined categories dropdown
        category = st.selectbox(
            "Category",
            ["History", "Political Science", "Sociology", "International Relations", "Philosophy"]
        )
        
        link = st.text_input("Link (Optional)")
        pdf_file = st.file_uploader("Upload PDF", type="pdf")

        # Submit button
        submit_button = st.form_submit_button(label="Upload Paper")

        if submit_button:
            if pdf_file is not None:
                # Save the uploaded file to a variable or storage
                pdf_path = save_pdf(pdf_file)

                # Append new paper info to the DataFrame
                new_paper = {
                    "Title": title,
                    "Author": author,
                    "University": university,
                    "Year": year,
                    "Category": category,
                    "Link": link,
                    "PDF": pdf_path
                }
                df = df.append(new_paper, ignore_index=True)
                st.success("Paper uploaded successfully!")
            else:
                st.error("Please upload a PDF file.")
    st.dataframe(df)

# Helper function to save the uploaded PDF
def save_pdf(pdf_file):
    # Save the file to the server (or any other logic for storing files)
    pdf_path = f"./uploads/{pdf_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(pdf_file.getbuffer())
    return pdf_path
