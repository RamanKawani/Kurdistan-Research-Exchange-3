import pandas as pd
import streamlit as st

# Hardcoded data for research papers
data = [
    {'title': 'Sample Paper 1', 'author': 'Author A', 'university': 'University X', 'year': 2023, 'abstract': 'This is an abstract.'},
    {'title': 'Sample Paper 2', 'author': 'Author B', 'university': 'University Y', 'year': 2022, 'abstract': 'Another abstract.'},
]

# Convert the hardcoded data into a pandas DataFrame
df = pd.DataFrame(data)

# Function to display papers
def display_papers():
    st.title("Kurdistan Research Exchange")
    st.write("Welcome to the platform where you can publish and explore social science research papers related to the Kurdistan Region.")
    
    # Display the research papers
    st.subheader("Published Research Papers")
    st.dataframe(df)

# Function to allow users to upload research papers
def upload_paper():
    st.subheader("Upload Your Research Paper")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Process the uploaded CSV and append to the DataFrame
        new_data = pd.read_csv(uploaded_file)
        global df
        df = pd.concat([df, new_data], ignore_index=True)
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
