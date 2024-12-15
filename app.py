import streamlit as st
import pandas as pd
from display import display_papers  # Import the function

def load_data():
    # Load your CSV or data here
    df = pd.read_csv('data/research_papers.csv')
    return df

def main():
    # Load data
    df = load_data()

    # Display papers using the imported function
    display_papers(df)

if __name__ == "__main__":
    main()
