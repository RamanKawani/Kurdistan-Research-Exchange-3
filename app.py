import streamlit as st
import os
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Kurdistan Research Exchange", layout="wide")

# Home Page (Landing Page)
def home_page():
    st.title("Welcome to Kurdistan Research Exchange")
    st.write("""
        A platform to upload and access social science research papers from universities in Kurdistan.
    """)
    
    # Search Bar
    query = st.text_input("Search for research papers:")
    if query:
        st.write(f"Search results for: {query}")
        # Implement search functionality here (example: search from a database or CSV)
        
    # Featured Papers (Can be fetched dynamically from a dataset)
    st.header("Featured Papers")
    st.write("Here are some of the featured research papers:")
    # Example research listing
    papers = [
        {"title": "Research Paper 1", "author": "Author 1", "university": "University A"},
        {"title": "Research Paper 2", "author": "Author 2", "university": "University B"}
    ]
    for paper in papers:
        st.write(f"- **{paper['title']}** by {paper['author']} from {paper['university']}")

# Upload Research Page
def upload_page():
    st.title("Upload Your Research")
    st.write("""
        Please fill out the form to upload your research paper.
    """)
    
    # Research paper upload form
    with st.form(key='upload_form'):
        title = st.text_input("Title of Paper")
        authors = st.text_input("Author(s)")
        university = st.text_input("University")
        department = st.text_input("Department")
        keywords = st.text_input("Keywords (comma separated)")
        abstract = st.text_area("Abstract")
        paper_file = st.file_uploader("Upload your research paper", type=['pdf', 'docx'])
        
        submit_button = st.form_submit_button(label="Upload Paper")
        
        if submit_button and paper_file is not None:
            # Save the paper to a folder (this is a simple placeholder, modify with actual backend)
            paper_path = os.path.join("uploaded_papers", paper_file.name)
            with open(paper_path, "wb") as f:
                f.write(paper_file.getbuffer())
            st.success(f"Paper '{title}' uploaded successfully!")

# Browse Research Page
def browse_page():
    st.title("Browse Research Papers")
    
    # Filters
    university_filter = st.selectbox("Select University", ["University A", "University B", "All"])
    department_filter = st.selectbox("Select Department", ["Political Science", "Sociology", "All"])
    
    st.write(f"Showing research from: {university_filter}, {department_filter}")
    
    # Display research papers (This could be dynamic from a database or CSV)
    research_papers = pd.DataFrame({
        "Title": ["Research Paper 1", "Research Paper 2"],
        "Author": ["Author 1", "Author 2"],
        "University": ["University A", "University B"],
        "Department": ["Political Science", "Sociology"]
    })
    
    # Filter papers based on selections
    filtered_papers = research_papers[
        (research_papers['University'].str.contains(university_filter) | (university_filter == "All")) &
        (research_papers['Department'].str.contains(department_filter) | (department_filter == "All"))
    ]
    
    for index, row in filtered_papers.iterrows():
        st.write(f"**{row['Title']}** by {row['Author']} ({row['University']}, {row['Department']})")

# User Profile Page
def profile_page():
    st.title("User Profile")
    st.write("Manage your account and uploaded research here.")
    # You can add functionality to manage user accounts, view uploaded papers, etc.

# Main Function to Navigate Between Pages
def main():
    pages = {
        "Home": home_page,
        "Upload Research": upload_page,
        "Browse Research": browse_page,
        "Profile": profile_page
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    # Call the function corresponding to the selected page
    pages[selection]()

if __name__ == "__main__":
    main()
