import pandas as pd

# File path for the CSV where the research papers will be saved
DATA_FILE = 'research_papers.csv'

# Function to load data from the CSV file
def load_data():
    try:
        # Load the data from CSV
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty DataFrame with the correct columns
        print(f"File not found: {DATA_FILE}. Returning an empty DataFrame.")
        return pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

# Function to save data to the CSV file
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Function to load paper data (alias of load_data for compatibility)
def load_paper_data():
    return load_data()
