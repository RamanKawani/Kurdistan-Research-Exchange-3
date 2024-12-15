import streamlit as st
import pandas as pd

def display_papers(df):
    st.title("View Papers")
    
    # Sidebar for filtering options
    st.sidebar.header("Filter Papers")
    
    # Category filter
    categories = df["Category"].unique()
    selected_category = st.sidebar.selectbox("Select Category", options=["All"] + list(categories), index=0)
    
    # Author filter
    authors = df["Author"].unique()
    selected_author = st.sidebar.selectbox("Select Author", options=["All"] + list(authors), index=0)
    
    # Filter papers by selected category and author
    filtered_df = df.copy()
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df["Category"] == selected_category]
    if selected_author != "All":
        filtered_df = filtered_df[filtered_df["Author"] == selected_author]

    # Sorting options
    sort_options = ["Title", "Category", "Year"]
    sort_by = st.sidebar.selectbox("Sort By", options=sort_options, index=0)
    sort_order = st.sidebar.radio("Sort Order", options=["Ascending", "Descending"], index=0)
    filtered_df = filtered_df.sort_values(by=sort_by, ascending=(sort_order == "Ascending"))

    # Display filtered and sorted data
    st.subheader("Filtered Papers")
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            st.markdown(f"""
                ### {row['Title']}
                - **Category:** {row['Category']}
                - **Author:** {row['Author']}
                - **Year:** {row['Year']}
            """)
            st.download_button(
                label="Download PDF",
                data=row["PDF"],
                file_name=f"{row['Title']}.pdf",
                mime="application/pdf",
            )
            st.markdown("---")
    else:
        st.warning("No papers match the selected filters.")

# Example DataFrame for testing
if __name__ == "__main__":
    data = {
        "Title": ["Paper A", "Paper B", "Paper C"],
        "Category": ["History", "Sociology", "Political Science"],
        "Author": ["Author 1", "Author 2", "Author 1"],
        "Year": [2021, 2020, 2022],
        "PDF": ["PDF content A", "PDF content B", "PDF content C"],  # Placeholder PDF content
    }
    df = pd.DataFrame(data)
    display_papers(df)
