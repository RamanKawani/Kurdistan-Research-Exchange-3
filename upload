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
        1. **Paper Format**: Please upload your research paper in PDF or DOCX format.
        2. **Paper Title**: Ensure your paper has a clear title that reflects the content.
        3. **Author Information**: Ensure your name, institution, and contact information are included in the paper or metadata.
        4. **Abstract**: Provide a brief abstract of your research (optional, but recommended).
        
        After uploading your paper, it will be reviewed for compliance with our guidelines before being published on the platform.
        """)

    # File upload section
    st.subheader("Select a Paper to Upload")
    uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])

    # Paper title input field
    paper_title = st.text_input("Enter the title of your paper:")

    # Author information input
    author_name = st.text_input("Enter your name:")
    author_institution = st.text_input("Enter your institution:")
    author_email = st.text_input("Enter your email:")

    # Abstract input
    abstract = st.text_area("Provide a brief abstract of your paper (optional):", height=150)

    # Submit button
    if uploaded_file and paper_title and author_name and author_institution and author_email:
        if st.button("Submit Paper"):
            # Save the uploaded file in a folder (temporary or permanent based on your needs)
            save_path = os.path.join("uploads", uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Provide feedback to the user
            st.success(f"Your paper titled '{paper_title}' has been successfully uploaded!")
            st.markdown("""
                Your submission will be reviewed by our team, and we will notify you once your paper is published on the platform.
                Thank you for your contribution to the Kurdistan Research Exchange.
                """)
    else:
        # Inform the user to complete all fields before submission
        st.warning("Please fill in all the required fields and upload your paper before submitting.")

