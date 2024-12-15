import streamlit as st

def home():
    st.title("Welcome to the Kurdistan Research Exchange")
    st.write("""
        This platform allows users to upload, share, and download research papers related to Kurdistan and the surrounding region.
        Use the sections below to interact with the platform.
    """)
import streamlit as st

def upload(df):
    # File upload section
    uploaded_file = st.file_uploader("Upload a research paper (PDF only)", type="pdf")
    if uploaded_file is not None:
        pdf_data = uploaded_file.read()
        st.write("File uploaded successfully!")

        # Add the paper to the database (append to df)
        title = st.text_input("Enter the title of the paper:", key="title_input")
        author = st.text_input("Enter the author(s) of the paper:", key="author_input")
        university = st.text_input("Enter the university associated with the paper:", key="university_input")

        if st.button("Add Paper"):
            if title and author and university:
                # Assuming df is a global data storage (in-memory or database)
                new_paper = {
                    "title": title,
                    "author": author,
                    "university": university,
                    "pdf_file": pdf_data
                }
                df = df.append(new_paper, ignore_index=True)
                st.success(f"Paper '{title}' added successfully!")
            else:
                st.warning("Please fill in all fields.")
    return df
