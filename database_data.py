import pandas as pd
import os

# File path for the CSV where the research papers will be saved
DATA_FILE = 'research_papers.csv'
UPLOAD_DIR = 'uploads/'

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

# Function to delete a paper record by index and remove the corresponding PDF
def delete_record(index):
    df = load_data()
    
    if index >= 0 and index < len(df):
        # Get the paper to delete
        paper_to_delete = df.iloc[index]
        
        # Get the PDF filename
        pdf_filename = paper_to_delete['PDF']
        pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
        
        # Remove the paper from the DataFrame
        df = df.drop(index)
        save_data(df)
        
        # If the PDF exists, delete it from the uploads directory
        if os.path.isfile(pdf_path):
            os.remove(pdf_path)
            print(f"PDF file '{pdf_filename}' removed from {UPLOAD_DIR}")
        
        print(f"Record '{paper_to_delete['Title']}' deleted successfully.")
        return True, paper_to_delete['Title']
    
    else:
        print(f"Record with index {index} not found.")
        return False, None


