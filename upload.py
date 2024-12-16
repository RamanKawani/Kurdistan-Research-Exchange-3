import streamlit as st
import os

def upload_papers():
    # Set the title for the page
    st.title("Upload Research Paper")
    st.markdown("""
        Welcome to the **Research Paper Upload** section. Please follow the steps below to upload your academic paper to the Kurdistan Research Exchange platform.
    """)

    # Instructions section
    st.subheader("Upload Instructions")
    st.markdown("""
        1. **File Format**: Upload your research paper in **PDF** format only.
        2. **File Size**: Ensure the file size does not exceed 10MB.
        3. **Paper Title**: Provide a clear and concise title.
        4. **Author Details**: Include your name, institution, and email.
        5. **Abstract**: (Optional) Add a brief abstract summarizing your research.
        
        After submission, your paper will be reviewed for compliance with our guidelines.
    """)

    # File upload section
    st.subheader("Upload Your Paper")
    uploaded_file = st.file_uploader("Select a PDF file", type=["pdf"])

    # Additional metadata input
    paper_title = st.text_input("Paper Title:")
    author_name = st.text_input("Author Name:")
    author_institution = st.text_input("Institution:")
    author_email = st.text_input("Email:")
    abstract = st.text_area("Abstract (Optional):", height=150)

    # Validation: Check if all required fields are filled
    if uploaded_file and paper_title.strip() and author_name.strip() and author_institution.strip() and author_email.strip():
        # Submit button
        if st.button("Submit Paper"):
            # Ensure the "uploads" directory exists
            os.makedirs("uploads", exist_ok=True)

            # Save the uploaded file in the "uploads" directory
            save_path = os.path.join("uploads", uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Feedback to the user
            st.success(f"Your paper titled '{paper_title}' has been successfully uploaded!")
            st.info("Your submission will be reviewed and published after approval. Thank you for contributing to the Kurdistan Research Exchange!")
            
            # Display uploaded metadata for user confirmation
            st.subheader("Submission Details")
            st.write(f"**Title**: {paper_title}")
            st.write(f"**Author**: {author_name}")
            st.write(f"**Institution**: {author_institution}")
            st.write(f"**Email**: {author_email}")
            if abstract.strip():
                st.write(f"**Abstract**: {abstract}")
            st.write(f"**File Name**: {uploaded_file.name}")
    else:
        # Warning for incomplete form
        st.warning("Please complete all required fields and upload your paper in PDF format before submitting.")

# Run the function if this file is executed directly (optional for testing)
if __name__ == "__main__":
    upload_papers()


