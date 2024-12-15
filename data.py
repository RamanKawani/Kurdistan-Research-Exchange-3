import os
import pandas as pd

# Path to the uploads directory where the PDF files are stored
UPLOAD_FOLDER = 'uploads'

# Data to simulate your research papers database
paper_data = {
    "Title": ["Paper 1", "Paper 2", "Paper 3"],
    "Author": ["Author 1", "Author 2", "Author 3"],
    "University": ["University A", "University B", "University C"],
    "Year": [2020, 2021, 2022],
    "Category": ["Category A", "Category B", "Category C"],
    "Link": ["paper1", "paper2", "paper3"],  # Without 'http://example.com/'
    "PDF": ["paper1.pdf", "paper2.pdf", "paper3.pdf"]  # Assuming PDF file names are stored in 'uploads' folder
}

# Convert the paper data dictionary to a DataFrame
paper_df = pd.DataFrame(paper_data)

# Function to load paper data (as a DataFrame)
def load_paper_data():
    return paper_df

# Function to check if a paper file exists in the uploads directory
def check_paper_exists(paper_link):
    return os.path.isfile(os.path.join(UPLOAD_FOLDER, paper_link))

# Function to get the file path for a paper from the uploads directory
def get_paper_file_path(paper_link):
    return os.path.join(UPLOAD_FOLDER, paper_link)

# Example function that could be used to display research papers
def get_paper_details():
    # Load the paper data
    paper_df = load_paper_data()
    
    if not paper_df.empty:
        # Extract necessary details, assuming columns like 'Title', 'Link', etc.
        for _, row in paper_df.iterrows():
            paper_title = row['Title']
            paper_author = row['Author']
            paper_university = row['University']
            paper_year = row['Year']
            paper_category = row['Category']
            paper_link = row['Link']
            paper_pdf = row['PDF']
            
            # Check if the paper exists in the uploads folder
            if check_paper_exists(paper_pdf):
                print(f"Title: {paper_title}\nAuthor: {paper_author}\nUniversity: {paper_university}\nYear: {paper_year}\nCategory: {paper_category}")
                print(f"Link: {paper_link}\nPDF: {get_paper_file_path(paper_pdf)}\n")
            else:
                print(f"Warning: PDF for {paper_title} not found.\n")
    else:
        print("No paper data found.")

