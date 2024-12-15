import streamlit as st
import os
import pandas as pd

# Sample function to simulate loading paper data from a database or file
def load_paper_data():
    # For demonstration purposes, using a CSV file to store paper metadata
    data = {
        'Title': ['Research Paper 1', 'Research Paper 2', 'Research Paper 3'],
        'Author': ['Author 1', 'Author 2', 'Author 3'],
        'Institution': ['Institution 1', 'Institution 2', 'Institution 3'],
        'Year': [2022, 2023, 2021],
        'Abstract': ['Abstract of Paper 1', 'Abstract of Paper 2', 'Abstract of Paper 3'],
        'Link': ['link1.pdf', 'link2.pdf', 'link3.pdf']
    }
    return pd.DataFrame(data)

def display_papers():
    # Set the title for the page
    st.title("View Research Papers")
    st.markdown("""
        Welcome to the **Research Papers View** section. You can explore the uploaded research papers by searching, filtering, and sorting the results.
    """)

    # Load sample paper data (could be replaced with database or cloud storage retrieval)
    paper_df = load_paper_data()

    # Search bar for filtering papers by title or author
    search_query = st.text_input("Search for a paper by title or author:")

    if search_query:
        paper_df = paper_df[paper_df['Title'].str.contains(search_query, case=False) |
                            paper_df['Author'].str.contains(search_query, case=False)]
    
    # Filter options
    st.subheader("Filter Papers")
    filter_by_year = st.selectbox("Filter by year of publication:", options=[None] + sorted(paper_df['Year'].unique().tolist()))

    if filter_by_year:
        paper_df = paper_df[paper_df['Year'] == filter_by_year]

    # Sorting options
    st.subheader("Sort Papers")
    sort_by = st.selectbox("Sort by:", options=["Title", "Author", "Year"])

    paper_df = paper_df.sort_values(by=[sort_by], ascending=True)

    # Display the filtered and sorted research papers in a table
    if not paper_df.empty:
        st.subheader("Available Research Papers")
        st.write(paper_df[['Title', 'Author', 'Institution', 'Year', 'Abstract']])

        # Show download links for papers
        for _, row in paper_df.iterrows():
            st.markdown(f"**{row['Title']}** by {row['Author']} ({row['Year']})")
            st.write(f"**Institution**: {row['Institution']}")
            st.write(f"**Abstract**: {row['Abstract']}")
            st.download_button(
                label="Download Paper",
                data=open(os.path.join('uploads', row['Link']), 'rb').read(),
                file_name=row['Link'],
                mime="application/pdf"
            )
            st.markdown("---")
    else:
        st.warning("No papers found matching your criteria.")

