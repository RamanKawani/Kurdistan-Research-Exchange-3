import os
import streamlit as st  # Import streamlit

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

            # Ensure correct file path handling
            file_path = os.path.join('uploads', row['Link'])
            if os.path.isfile(file_path):  # Check if it's a valid file
                st.download_button(
                    label="Download Paper",
                    data=open(file_path, 'rb').read(),
                    file_name=row['Link'],
                    mime="application/pdf"
                )
            else:
                st.warning(f"File for '{row['Title']}' not found or is not a valid file.")
            
            st.markdown("---")
    else:
        st.warning("No papers found matching your criteria.")
