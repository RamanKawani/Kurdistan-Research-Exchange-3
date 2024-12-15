# guidelines.py
import streamlit as st

def display_guidelines():
    st.title("Submission Guidelines")
    
    st.header("Welcome to the Kurdistan Research Exchange Submission Guidelines")
    st.write("This section provides guidelines for submitting your research papers to our platform.")
    
    st.subheader("1. Paper Format")
    st.write("""
        - All papers must be in PDF format.
        - Use standard font (Times New Roman or Arial), size 12.
        - Include your title, author, university, and year on the first page.
        - Ensure your research is properly cited using MLA or APA citation styles.
    """)
    
    st.subheader("2. Categories")
    st.write("""
        Choose an appropriate category for your research. Categories include:
        - History
        - Political Science
        - Sociology
        - International Relations
        - Philosophy
    """)
    
    st.subheader("3. Uploading Process")
    st.write("""
        - Use the **'Upload Papers'** section to submit your research.
        - Fill in the required fields: Title, Author, University, Year, and Category.
        - If applicable, include a link to the paper, and upload the PDF file.
        - Once submitted, your paper will be available for viewing by others.
    """)
    
    st.subheader("4. Review and Approval")
    st.write("""
        - All papers will undergo a review process before being made public.
        - Authors will be notified once their papers are approved.
        - If there are any issues with the submission, we will contact you.
    """)
    
    st.subheader("5. Contact Information")
    st.write("""
        If you need assistance, feel free to reach out to us:
        - Email: RamanKhalid888@gmail.com
        - Phone: 07507427976
    """)
