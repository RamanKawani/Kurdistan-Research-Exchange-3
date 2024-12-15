import pandas as pd
import streamlit as st

# Function to display the research papers with a category filter
def display_papers(df):
    if df is not None:
        # Title of the section
        st.title("Kurdistan Research Papers")

        # Displaying available categories for filtering
        st.subheader("Filter Papers by Category")
        categories = df["Category"].unique().tolist()  # Extract unique categories
        selected_category = st.selectbox("Select a Category", ["All"] + categories)

        # Filter papers based on the selected category
        if selected_category != "All":
            filtered_df = df[df["Category"] == selected_category]
        else:
            filtered_df = df

        # Display the filtered DataFrame or show a message if no papers are available
        if not filtered_df.empty:
            st.write(f"Showing papers in the category: **{selected_category}**")
            for idx, row in filtered_df.iterrows():
                with st.expander(f"**{row['Title']}**", expanded=False):
                    col1, col2 = st.columns([3, 1])  # Two columns for better layout

                    with col1:
                        st.markdown(f"**Author:** {row['Author']}")
                        st.markdown(f"**University:** {row['University']}")
                        st.markdown(f"**Year:** {row['Year']}")
                        st.markdown(f"**Category:** {row['Category']}")
                        if pd.notna(row['Link']):
                            st.markdown(f"**Link:** [View Paper]({row['Link']})")

                    with col2:
                        pdf_link = row['PDF']
                        if pd.notna(pdf_link):  # Check if PDF exists
                            try:
                                st.download_button(
                                    label="Download PDF",
                                    data=pdf_link,
                                    file_name=f"{row['Title']}.pdf",
                                    mime="application/pdf"
                                )
                            except Exception as e:
                                st.error(f"Error downloading PDF for **{row['Title']}**: {e}")
                        else:
                            st.warning("No PDF available for this paper.")
                st.markdown("---")
        else:
            st.warning(f"No papers found under the category: **{selected_category}**")
    else:
        st.error("No research papers available to display.")
