import streamlit as st
import pandas as pd

# Load CSV file containing research papers
def load_data():
    return pd.read_csv('data/research_papers.csv')

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
        updated_data.to_csv('data/research_papers.csv', index=False)
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

