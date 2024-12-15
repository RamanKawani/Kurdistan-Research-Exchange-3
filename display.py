import streamlit as st
import pandas as pd

def display_papers(df):
    st.title("View Papers")
    
    # Sidebar filters for categories and authors
    st.sidebar.header("Filter Papers")
    categories = df["Category"].unique()
    selected_category = st.sidebar.selectbox("Select Category", options=["All"] + list(categories), index=0)
    
    authors = df["Author"].unique()
    selected_author = st.sidebar.selectbox("Select Author", options=["All"] + list(authors), index=0)

    # Filter based on user selections
    filtered_df = df.copy()
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df["Category"] == selected_category]
    if selected_author != "All":
        filtered_df = filtered_df[filtered_df["Author"] == selected_author]

    # Sorting options
    sort_options = ["Title", "Author", "Category", "Year"]
    sort_by = st.sidebar.selectbox("Sort By", options=sort_options, index=0)
    sort_order = st.sidebar.radio("Sort Order", options=["Ascending", "Descending"], index=0)
    filtered_df = filtered_df.sort_values(by=sort_by, ascending=(sort_order == "Ascending"))

    # Display filtered and sorted data in an elegant table
    st.subheader("Filtered Papers")
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            st.markdown(f"""
                ### {row['Title']}
                - **Author:** {row['Author']}
                - **Category:** {row['Category']}
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
        "Author": ["Author 1", "Author 2", "Author 3"],
        "Category": ["History", "Sociology", "Political Science"],
        "Year": [2021, 2020, 2022],
        "PDF": ["PDF content A", "PDF content B", "PDF content C"],  # Placeholder PDF content
    }
    df = pd.DataFrame(data)
    display_papers(df)
