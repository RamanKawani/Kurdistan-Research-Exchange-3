import pandas as pd
import streamlit as st

# Function to display the research papers with improved UI
def display_papers(df):
    if df is not None:
        # Title of the app
        st.title("Kurdistan Research Papers")

        # Introduction
        st.write("Explore the latest research papers from various universities in the Kurdistan Region.")
        
        # Display papers with better UI
        for idx, row in df.iterrows():
            # Display each paper with a card-like style
            with st.expander(f"**{row['Title']}**", expanded=True):
                col1, col2 = st.columns([3, 1])  # Two columns: one for the content, one for the button

                # Left column (paper details)
                with col1:
                    st.markdown(f"**Author:** {row['Author']}")
                    st.markdown(f"**University:** {row['University']}")
                    st.markdown(f"**Year:** {row['Year']}")
                    st.markdown(f"**Category:** {row['Category']}")
                    st.markdown(f"**Link:** [{row['Link']}]({row['Link']})")

                # Right column (PDF download button)
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
                        st.warning(f"No PDF available for **{row['Title']}**.")

            # Horizontal line after each paper
            st.markdown("---")
    else:
        st.write("No research papers available to display.")
