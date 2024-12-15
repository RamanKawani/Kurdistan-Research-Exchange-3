import pandas as pd
import streamlit as st

# Function to display the research papers with an advanced UI
def display_papers(df):
    if df is not None:
        # Sidebar for filters
        st.sidebar.header("Filters")
        
        # Category filter
        categories = df["Category"].unique().tolist()
        selected_category = st.sidebar.selectbox("Category", ["All"] + categories)

        # Author filter
        authors = df["Author"].unique().tolist()
        selected_author = st.sidebar.selectbox("Author", ["All"] + authors)

        # University filter
        universities = df["University"].unique().tolist()
        selected_university = st.sidebar.selectbox("University", ["All"] + universities)

        # Year filter
        years = df["Year"].unique().tolist()
        selected_year = st.sidebar.selectbox("Year", ["All"] + sorted(years))

        # Search bar
        search_query = st.sidebar.text_input("Search by Title or Keywords")

        # Filter logic
        filtered_df = df.copy()
        if selected_category != "All":
            filtered_df = filtered_df[filtered_df["Category"] == selected_category]
        if selected_author != "All":
            filtered_df = filtered_df[filtered_df["Author"] == selected_author]
        if selected_university != "All":
            filtered_df = filtered_df[filtered_df["University"] == selected_university]
        if selected_year != "All":
            filtered_df = filtered_df[filtered_df["Year"] == selected_year]
        if search_query:
            filtered_df = filtered_df[
                filtered_df["Title"].str.contains(search_query, case=False, na=False)
            ]

        # Display results
        st.title("Kurdistan Research Papers")
        if not filtered_df.empty:
            # Grid display using AgGrid for better UI
            gb = GridOptionsBuilder.from_dataframe(filtered_df)
            gb.configure_pagination(paginationAutoPageSize=True)
            gb.configure_default_column(wrapText=True, autoHeight=True)
            gb.configure_column("PDF", header_name="Download PDF", cellRenderer=link_renderer)
            grid_options = gb.build()

            st.subheader("Filtered Papers")
            AgGrid(filtered_df, gridOptions=grid_options, height=400, theme="balham")

            # Expandable details section for individual papers
            st.markdown("### Paper Details")
            for idx, row in filtered_df.iterrows():
                with st.expander(f"**{row['Title']}**", expanded=False):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**Author:** {row['Author']}")
                        st.markdown(f"**University:** {row['University']}")
                        st.markdown(f"**Year:** {row['Year']}")
                        st.markdown(f"**Category:** {row['Category']}")
                        if pd.notna(row['Link']):
                            st.markdown(f"**Link:** [View Paper]({row['Link']})")
                    with col2:
                        pdf_link = row['PDF']
                        if pd.notna(pdf_link):
                            st.download_button(
                                label="Download PDF",
                                data=pdf_link,
                                file_name=f"{row['Title']}.pdf",
                                mime="application/pdf"
                            )
        else:
            st.warning("No papers match the selected filters or search query.")
    else:
        st.error("No research papers available to display.")

# Helper function for rendering links in AgGrid
def link_renderer(params):
    if params.value:
        return f"<a href='{params.value}' target='_blank'>Download PDF</a>"
    return "N/A"
