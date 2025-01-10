import pandas as pd

# File path for the CSV where the research papers will be saved
DATA_FILE = 'research_papers.csv'

# Function to load data from the CSV file
def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        print("Loaded Data:", df)  # Debugging line to check data loading
        return df
    except FileNotFoundError:
        # If the file doesn't exist, return an empty DataFrame with the correct columns
        return pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])

# Function to save data to the CSV file
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Function to add a new record (paper) to the CSV
def add_record(record):
    df = load_data()
    df = df.append(record, ignore_index=True)
    save_data(df)

# Function to update a paper record by title
def update_record(title, updated_record):
    df = load_data()
    # Find the row where the title matches
    index = df[df['Title'] == title].index
    if not index.empty:
        # Update the row with the new data
        df.loc[index] = updated_record
        save_data(df)
    else:
        print(f"Record with title '{title}' not found.")

# Function to delete a paper record by title
def delete_record(title):
    df = load_data()
    # Find the row where the title matches
    index = df[df['Title'] == title].index
    if not index.empty:
        df = df.drop(index)
        save_data(df)
    else:
        print(f"Record with title '{title}' not found.")

# Function to search for papers by category
def search_by_category(category):
    df = load_data()
    return df[df['Category'].str.contains(category, case=False, na=False)]

# Function to search for papers by author
def search_by_author(author):
    df = load_data()
    return df[df['Author'].str.contains(author, case=False, na=False)]

# Function to get paper by title
def get_paper_by_title(title):
    df = load_data()
    paper = df[df['Title'] == title]
    if not paper.empty:
        return paper.iloc[0]
    else:
        print(f"Paper with title '{title}' not found.")
        return None

# Function to get all papers
def get_all_papers():
    df = load_data()
    return df

# Example of how to use these functions
if __name__ == "__main__":
    # Add a new paper (example)
    new_paper = {
        "Title": "New Research Paper",
        "Author": "John Doe",
        "University": "University of Kurdistan",
        "Year": 2025,
        "Category": "Political Science",
        "Link": "http://example.com/newpaper",
        "PDF": "newpaper.pdf"
    }
    add_record(new_paper)

    # Update an existing paper (example)
    updated_paper = {
        "Title": "Updated Research Paper",
        "Author": "John Doe",
        "University": "University of Kurdistan",
        "Year": 2025,
        "Category": "International Relations",
        "Link": "http://example.com/updatedpaper",
        "PDF": "updatedpaper.pdf"
    }
    update_record("New Research Paper", updated_paper)

    # Search papers by category (example)
    category_papers = search_by_category("Political Science")
    print("Papers in Political Science:", category_papers)

    # Delete a paper (example)
    delete_record("New Research Paper")

    # Get all papers (example)
    papers = get_all_papers()
    print("All Papers:", papers)
