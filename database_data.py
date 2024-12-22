import pandas as pd
import os

# File path for the CSV where the research papers will be saved
DATA_FILE = 'research_papers.csv'

# Predefined data to initialize the CSV if it doesn't exist
INITIAL_DATA = [
    {
        "Title": "Understanding Kurdish Politics",
        "Author": "John Doe",
        "University": "University of Erbil",
        "Year": 2023,
        "Category": "Political Science",
        "Link": "http://example.com/paper1",
        "PDF": "http://example.com/paper1.pdf",
    },
    {
        "Title": "Globalization and its Impact on the Middle East",
        "Author": "Jane Smith",
        "University": "University of Kurdistan",
        "Year": 2022,
        "Category": "International Relations",
        "Link": "http://example.com/paper2",
        "PDF": "http://example.com/paper2.pdf",
    },
    {
        "Title": "Women in the Kurdish Liberation Movement",
        "Author": "Ahmed Ali",
        "University": "University of Erbil",
        "Year": 2021,
        "Category": "Gender Studies",
        "Link": "http://example.com/paper3",
        "PDF": "http://example.com/paper3.pdf",
    },
    {
        "Title": "The Role of Technology in Modern Warfare",
        "Author": "Sara Ahmed",
        "University": "University of Kurdistan",
        "Year": 2024,
        "Category": "Military Science",
        "Link": "http://example.com/paper4",
        "PDF": "http://example.com/paper4.pdf",
    },
    {
        "Title": "Kurdish Identity and Cultural Preservation",
        "Author": "Rebaz Ameen",
        "University": "University of Erbil",
        "Year": 2020,
        "Category": "Sociology",
        "Link": "http://example.com/paper5",
        "PDF": "http://example.com/paper5.pdf",
    },
]

# Function to initialize the CSV file with predefined data if it doesn't exist
def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        print(f"{DATA_FILE} not found. Creating and initializing with default data.")
        df = pd.DataFrame(INITIAL_DATA)
        df.to_csv(DATA_FILE, index=False)

# Function to load data from the CSV file
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"File not found: {DATA_FILE}. Returning an empty DataFrame.")
        return pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

# Function to save data to the CSV file
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Function to update a record by title
def update_record(title, updates):
    df = load_data()
    if title in df['Title'].values:
        for key, value in updates.items():
            if key in df.columns:
                df.loc[df['Title'] == title, key] = value
        save_data(df)
        print(f"Record with title '{title}' updated successfully.")
    else:
        print(f"Record with title '{title}' not found.")

# Function to delete a record by title
def delete_record(title):
    df = load_data()
    if title in df['Title'].values:
        df = df[df['Title'] != title]
        save_data(df)
        print(f"Record with title '{title}' deleted successfully.")
    else:
        print(f"Record with title '{title}' not found.")

# Function to add a new record
def add_record(record):
    df = load_data()
    df = df.append(record, ignore_index=True)
    save_data(df)
    print("New record added successfully.")

# Initialize the data file when the script is run
initialize_data_file()
