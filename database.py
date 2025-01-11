import pandas as pd
import os

# File paths for the CSV and uploads directory
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
        # Return an empty DataFrame if the file doesn't exist
        return pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

# Function to save data to the CSV file
def save_data(df):
    try:
        df.to_csv(DATA_FILE, index=False)
        print(f"Data saved to {DATA_FILE}")
    except Exception as e:
        print(f"Error saving data: {e}")

# Function to add a new record (paper) to the CSV
def add_record(record):
    try:
        df = load_data()
        df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)  # Add the new record
        save_data(df)
        print(f"Record added: {record}")
    except Exception as e:
        print(f"Error adding record: {e}")

# Function to update a paper record by title
def update_record(title, updated_record):
    try:
        df = load_data()
        index = df[df['Title'] == title].index  # Find the index of the record to update
        if not index.empty:
            df.loc[index[0]] = updated_record  # Update the record
            save_data(df)
            print(f"Record with title '{title}' updated successfully.")
        else:
            print(f"Record with title '{title}' not found.")
    except Exception as e:
        print(f"Error updating record: {e}")

# Function to delete a paper record by index and remove the corresponding PDF
def delete_record(index):
    try:
        df = load_data()
        
        if 0 <= index < len(df):
            # Get the paper to delete
            paper_to_delete = df.iloc[index]
            
            # Get the PDF filename
            pdf_filename = paper_to_delete['PDF']
            pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
            
            # Remove the paper from the DataFrame
            df = df.drop(index).reset_index(drop=True)  # Reset index after deletion
            save_data(df)
            
            # If the PDF exists, delete it from the uploads directory
            if pdf_filename and os.path.isfile(pdf_path):
                os.remove(pdf_path)
                print(f"PDF file '{pdf_filename}' removed from {UPLOAD_DIR}")
            
            print(f"Record '{paper_to_delete['Title']}' deleted successfully.")
            return True, paper_to_delete['Title']
        else:
            print(f"Invalid index: {index}. No record deleted.")
            return False, None
    except Exception as e:
        print(f"Error deleting record: {e}")
        return False, None
