import os
import pandas as pd
import streamlit as st

# Get the absolute path of the data folder
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# Load CSV file containing research papers
def load_data():
    # Check if the 'data' directory exists, if not, create it
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Check if the CSV file exists, if not, create it with default columns
    file_path = os.path.join(DATA_DIR, 'research_papers.csv')
    if not os.path.exists(file_path):
        columns = ['title', 'author', 'university', 'year', 'abstract']
        df = pd.DataFrame(columns=columns)
        df.to_csv(file_path, index=False)
    
    # Read and return the CSV data
    return pd.read_csv(file_path)

# Function to display papers
def display_papers():
    data = load_data()
    st.title("Kurdistan Research Exchange")
    st.write("Welcome to the platform where you can publish and explore social science research papers related to the Kurdistan Region.")
    
    # Display the research papers
    st.subheader("Published Research Papers")
    st.dataframe(data)

# Function to allow users to upload research papers
def upload_paper():
    st.subheader("Upload Your Research Paper")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Process the uploaded CSV and append to the main CSV
        new_data = pd.read_csv(uploaded_file)
        existing_data = load_data()
        updated_data = existing_data.append(new_data, ignore_index=True)
        updated_data.to_csv(os.path.join(DATA_DIR, 'research_papers.csv'), index=False)
        st.success("Your research paper has been successfully uploaded.")

# Sidebar navigation
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Upload Paper"])
    
    if selection == "Home":
        display_papers()
    elif selection == "Upload Paper":
        upload_paper()

if __name__ == '__main__':
    main()
