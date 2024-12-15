import streamlit as st
import pandas as pd
from display_papers import display_papers

# Load the data (assuming you have data loaded as a pandas DataFrame)
def load_data():
    # Example: Load your data here
    data = {
        "title": ["Paper 1", "Paper 2", "Paper 3"],
        "author": ["Author A", "Author B", "Author C"],
        "university": ["University X", "University Y", "University Z"],
        "pdf_file": ["pdf_data_1", "pdf_data_2", "pdf_data_3"]  # This should contain actual file data
    }
    return pd.DataFrame(data)

def main():
    # Load data
    df = load_data()

    # Call display_papers function from display_papers.py
    display_papers(df)

if __name__ == "__main__":
    main()
