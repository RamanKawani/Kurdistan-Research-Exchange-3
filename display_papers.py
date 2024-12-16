import os
import streamlit as st
import pandas as pd

def display_papers():
    # Load paper data (Make sure you have your load_paper_data function set up)
    # For this example, let's assume you have a DataFrame `paper_df`
    paper_df = pd.DataFrame({
        "Title": ["Paper 1", "Paper 2", "Paper 3"],
        "Author": ["Author 1", "Author 2", "Author 3"],
        "University": ["University A", "University B", "University C"],
        "Year": [2020, 2021, 2022],
        "Category": ["Category A", "Category B", "Category C"],
        "PDF": ["paper1.pdf", "paper2.pdf", "paper3.pdf"]
    })

    # Title of the page
    st.title("View Research Papers")
    
    # Columns layout for mobile responsiveness
    # Create two columns for desktop and single column for mobile
    col1, col2 = st.columns([1, 1])

    # Debugging: Show files in uploads directory
    try:
        st.write("Files in 'uploads' directory:", os.listdir('uploads'))
    except FileNotFoundError:
        st.error("Uploads directory not found. Please check your folder structure.")
        return

    # Iterate through the paper DataFrame and display content
    for index, row in paper_df.iterrows():
        paper_pdf = row['PDF']
        file_path = os.path.join('uploads', paper_pdf)
        
        # If screen width is small (mobile view), reduce the content width
        with col1:
            st.write(f"**{row['Title']}**")
            st.write(f"Author: {row['Author']}")
            st.write(f"University: {row['University']}")
            st.write(f"Year: {row['Year']}")
            st.write(f"Category: {row['Category']}")

        with col2:
            if os.path.isfile(file_path):
                st.write(f"Link: [Download PDF]({file_path})")
                st.download_button("Download PDF", data=open(file_path, 'rb').read(), file_name=paper_pdf)
            else:
                st.warning(f"PDF not found for {row['Title']}")
        
        # Add spacing for readability
        st.markdown("---")

    # Optionally, add some responsive CSS styling for buttons and text
    st.markdown("""
        <style>
            .css-18e3th9 {  /* Adjust button size for mobile */
                width: 100% !important;
                padding: 15px 10px;
            }
            .css-1v3fvcr { /* Adjust spacing between elements */
                margin-bottom: 10px;
            }
            @media (max-width: 600px) {
                .css-1v3fvcr {
                    margin-bottom: 5px;
                }
                .css-18e3th9 {
                    width: 100%;
                    padding: 10px 0;
                }
            }
        </style>
    """, unsafe_allow_html=True)

