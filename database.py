import pandas as pd

# File path for the CSV where the research papers will be saved
DATA_FILE = 'research_papers.csv'

# Function to load data from the CSV file
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty DataFrame with the correct columns
        return pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

# Function to save data to the CSV file
def save_data(df):
    df.to_csv(DATA_FILE, index=False)
