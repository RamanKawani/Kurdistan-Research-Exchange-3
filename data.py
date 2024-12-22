import pandas as pd

# Function to load paper data from a CSV file
def load_paper_data():
    # Specify the path to your CSV file (update if necessary)
    file_path = "research_papers.csv"
    
    try:
        # Load the data from CSV
        paper_df = pd.read_csv(file_path)
    except FileNotFoundError:
        # Handle if the CSV file is not found
        paper_df = pd.DataFrame(columns=['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF'])
        print(f"File not found: {file_path}")
    
    # Return the loaded or empty DataFrame
    return paper_df
