import streamlit as st
from data import load_paper_data, get_paper_file_path, check_paper_exists

def display_papers():
    st.title("View Research Papers")
    
    paper_df = load_paper_data()
    
    if paper_df.empty:
        st.write("No papers available.")
        return
    
    for _, row in paper_df.iterrows():
        paper_title = row['Title']
        paper_author = row['Author']
        paper_university = row['University']
        paper_year = row['Year']
        paper_category = row['Category']
        paper_pdf = row['PDF']
        
        if check_paper_exists(paper_pdf):
            st.write(f"### {paper_title}")
            st.write(f"**Author**: {paper_author}")
            st.write(f"**University**: {paper_university}")
            st.write(f"**Year**: {paper_year}")
            st.write(f"**Category**: {paper_category}")
            st.write(f"[Download PDF](/{get_paper_file_path(paper_pdf)})")
        else:
            st.write(f"### {paper_title}")
            st.write("**PDF not found**")
