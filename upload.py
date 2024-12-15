import streamlit as st
import pandas as pd
from io import StringIO

# Global DataFrame for research papers (this can be replaced with a database or CSV handling)
df = pd.DataFrame(columns=["Title", "Author", "University", "PDF"])

def display_upload():
    st.title("Upload Your Research Paper")

    # Add a brief description
    st.write(
        """
        Welcome to the upload section! Here you can submit your research paper.
        Please provide the details and upload the PDF file.
        """
    )

    st.markdown("### Paper Details")

    # Create form for paper details
    with st.form(key="upload_form"):
        title = st.text_input("Paper Title")
        author = st.text_input("Author Name")
        university = st.text_input("University Name")

        # File uploader for PDF
        pdf_file = st.file_uploader("Upload Your Research Paper (PDF)", type="pdf")

        # Submit button for the form
        submit_button = st.form_submit_button("Submit Paper")

    # Handling the file upload and data processing
    if submit_button:
        if not title or not author or not university or not pdf_file:
            st.error("Please fill in all fields and upload a PDF file.")
        else:
            # Store paper metadata in DataFrame (could be a database in production)
            new_data = {
                "Title": title,
                "Author": author,
                "University": university,
                "PDF": pdf_file
            }

            # Append data to the global DataFrame
            global df
            df = df.append(new_data, ignore_index=True)

            # Provide download link for the uploaded PDF
            st.success("Your paper has been uploaded successfully!")
            st.write(f"Title: {title}")
            st.write(f"Author: {author}")
            st.write(f"University: {university}")

            # Display a button to download the PDF
            pdf_file.seek(0)  # Rewind to the start of the file
            st.download_button(
                label="Download Your Paper",
                data=pdf_file,
                file_name=f"{title}.pdf",
                mime="application/pdf",
                key=f"download_{title}"  # Unique key to avoid duplication
            )

    st.markdown("### Instructions for Uploading:")
    st.write(
        """
        - Please make sure that your PDF file is less than 10MB.
        - Fill in all fields with accurate information to help others find your research.
        - If you face any issues, feel free to contact the admin for support.
        """
    )
