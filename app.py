import streamlit as st
import pandas as pd
import os
from io import StringIO

# Directory to save PDFs
PDF_DIR = 'uploaded_pdfs/'

# Ensure the directory exists
if not os.path.exists(PDF_DIR):
    os.makedirs(PDF_DIR)

# Load data from CSV (if file exists)
def load_data():
    if os.path.exists('research_papers.csv'):
        return pd.read_csv('research_papers.csv')
    else:
        return pd.DataFrame(columns=['title', 'author', 'university', 'year', 'abstract', 'pdf_file'])

# Save data to CSV
def save_data(df):
    df.to_csv('research_papers.csv', index=False)

# Function to display papers
# Function to display papers
def display_papers():
    global df
    st.title("Kurdistan Research Exchange")
    st.write("Welcome to the platform where you can publish and explore social science research papers related to the Kurdistan Region.")
    
    # Search functionality
    st.subheader("Search Research Papers")
    search_query = st.text_input("Search by title, author, or university:")
    if search_query:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)

    # Display PDF download links for each paper
    for index, row in df.iterrows():
        if row['pdf_file']:  # Check if there's a PDF file
            pdf_path = os.path.join(PDF_DIR, row['pdf_file'])
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label=f"Download PDF: {row['title']}",
                        data=pdf_file,
                        file_name=row['pdf_file'],
                        mime="application/pdf",
                        key=f"download_button_{index}"  # Unique key using the index
                    )

    st.subheader("Search Research Papers")
    search_query = st.text_input("Search by title, author, or university:")
    if search_query:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)

    # Display PDF download links for each paper
    for index, row in df.iterrows():
        if row['pdf_file']:  # Check if there's a PDF file
            pdf_path = os.path.join(PDF_DIR, row['pdf_file'])
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label=f"Download PDF: {row['title']}",
                        data=pdf_file,
                        file_name=row['pdf_file'],
                        mime="application/pdf"
                    )

# Function to allow users to add a new research paper using a form
def add_paper_form():
    global df
    st.subheader("Add a New Research Paper")

    # Option 1: Upload PDF File
    uploaded_pdf = st.file_uploader("Upload the PDF of the research paper", type="pdf")
    if uploaded_pdf is not None:
        # Save the uploaded PDF file
        pdf_path = os.path.join(PDF_DIR, uploaded_pdf.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_pdf.getbuffer())
        
        # Show success message
        st.success(f"PDF file {uploaded_pdf.name} uploaded successfully!")

    # Option 2: Manually Add Paper Details
    with st.form(key='paper_form'):
        title = st.text_input("Title")
        author = st.text_input("Author")
        university = st.text_input("University")
        year = st.number_input("Year", min_value=1900, max_value=2024, step=1)
        abstract = st.text_area("Abstract")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Create a new DataFrame for the new paper
            new_paper = {
                'title': title,
                'author': author,
                'university': university,
                'year': year,
                'abstract': abstract,
                'pdf_file': uploaded_pdf.name if uploaded_pdf else None  # Store PDF file name or None
            }

            # Append the new paper to the existing dataframe and save it
            df = pd.concat([df, pd.DataFrame([new_paper])], ignore_index=True)
            save_data(df)
            st.success("Your research paper has been successfully added!")

# Sidebar navigation
def main():
    global df
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Add Paper"])

    if selection == "Home":
        display_papers()
    elif selection == "Add Paper":
        add_paper_form()

if __name__ == '__main__':
    # Load the data
    df = load_data()  # This loads the global df
    main()

