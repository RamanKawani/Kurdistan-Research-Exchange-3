import streamlit as st
import pandas as pd
from io import StringIO
import os

# Load data from CSV (if file exists)
def load_data():
    if os.path.exists('research_papers.csv'):
        return pd.read_csv('research_papers.csv')
    else:
        return pd.DataFrame(columns=['title', 'author', 'university', 'year', 'abstract'])

# Save data to CSV
def save_data(df):
    df.to_csv('research_papers.csv', index=False)

# Function to display papers
def display_papers():
    global df  # Declare global df here
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

# Function to allow users to add a new research paper using a form
def add_paper_form():
    global df  # Declare global df here
    st.subheader("Add a New Research Paper")

    # Option 1: Upload CSV File
    uploaded_file = st.file_uploader("Upload a CSV file with research paper details", type="csv")

    if uploaded_file is not None:
        # Read the uploaded CSV file into a DataFrame
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        uploaded_df = pd.read_csv(stringio)
        
        # Ensure the uploaded CSV has the correct columns
        required_columns = ['title', 'author', 'university', 'year', 'abstract']
        if all(col in uploaded_df.columns for col in required_columns):
            # Append the new papers to the existing DataFrame and save it
            df = pd.concat([df, uploaded_df], ignore_index=True)
            save_data(df)
            st.success("Your research papers have been successfully added!")
        else:
            st.error("The uploaded CSV file must contain the following columns: title, author, university, year, abstract.")
    
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
            new_paper = pd.DataFrame({
                'title': [title],
                'author': [author],
                'university': [university],
                'year': [year],
                'abstract': [abstract]
            })

            # Append the new paper to the existing dataframe and save it
            df = pd.concat([df, new_paper], ignore_index=True)
            save_data(df)
            st.success("Your research paper has been successfully added!")

# Sidebar navigation
def main():
    global df  # Declare global df here
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

