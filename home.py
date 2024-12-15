import streamlit as st

def display_papers(df):
    st.title("View Research Papers")
    
    st.markdown(
        """
        Here, you can explore all the research papers available in the Kurdistan Research Exchange platform. 
        Use the filter options below to narrow down your search.
        """
    )

    # If you want to add more filters (but not categories)
    author_filter = st.text_input("Filter by Author:")
    year_filter = st.number_input("Filter by Year:", min_value=2000, max_value=2024, value=2024)
    
    # Apply filters
    filtered_df = df
    if author_filter:
        filtered_df = filtered_df[filtered_df['Author'].str.contains(author_filter, case=False, na=False)]
    if year_filter:
        filtered_df = filtered_df[filtered_df['Year'] == year_filter]

    # Show filtered papers
    if not filtered_df.empty:
        for idx, row in filtered_df.iterrows():
            st.subheader(f"Title: {row['Title']}")
            st.write(f"Author(s): {row['Author']}")
            st.write(f"Year: {row['Year']}")
            st.write(f"Abstract: {row['Abstract']}")
            st.download_button(
                label="Download PDF",
                data=row['PDF'],
                file_name=f"{row['Title']}.pdf",
                mime="application/pdf"
            )
            st.markdown("---")
    else:
        st.write("No papers found based on the applied filters.")
