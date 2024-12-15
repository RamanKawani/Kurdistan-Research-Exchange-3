import pandas as pd
import streamlit as st

# Function to display the research papers
def display_papers(df):
    if df is not None:
        # Display the title of the app
        st.title("Kurdistan Research Papers")

        # Iterate through the papers in the DataFrame
        for idx, row in df.iterrows():
            # Display paper details
            st.subheader(f"**Title:** {row['Title']}")
            st.write(f"**Author:** {row['Author']}")
            st.write(f"**University:** {row['University']}")
            st.write(f"**Year:** {row['Year']}")
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Link:** {row['Link']}")

            # Check if a PDF is available for download
            pdf_link = row['PDF']
            if pd.notna(pdf_link):  # If a valid PDF link exists
                try:
                    # Display the download button for PDF
                    st.download_button(
                        label="Download PDF",
                        data=pdf_link,
                        file_name=f"{row['Title']}.pdf",
                        mime="application/pdf"
                    )
                except Exception as e:
                    st.error(f"Error displaying PDF for '{row['Title']}': {e}")
            else:
                st.warning(f"No PDF available for **{row['Title']}**.")
            st.markdown("---")  # Add a horizontal line for separation between papers
    else:
        st.write("No research papers available to display.")
