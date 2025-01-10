import pandas as pd
import os

# File path for the CSV where the research papers will be saved
DATA_FILE = 'research_papers.csv'

# Ensure the CSV file exists or create one with proper columns
if not os.path.isfile(DATA_FILE):
    df = pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])
    df.to_csv(DATA_FILE, index=False)

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
    print(f"Data saved to {DATA_FILE}")

# Function to add a new record (paper) to the CSV
def add_record(record):
    df = load_data()
    df = df.append(record, ignore_index=True)
    save_data(df)
    print(f"Record added: {record}")

# Function to update a paper record by title
def update_record(title, updated_record):
    df = load_data()
    index = df[df['Title'] == title].index
    if not index.empty:
        df.loc[index] = updated_record
        save_data(df)
    else:
        print(f"Record with title '{title}' not found.")

# Function to delete a paper record by title
def delete_record(title):
    df = load_data()
    index = df[df['Title'] == title].index
    if not index.empty:
        df = df.drop(index)
        save_data(df)
    else:
        print(f"Record with title '{title}' not found.")
