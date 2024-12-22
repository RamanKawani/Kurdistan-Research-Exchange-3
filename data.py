import pandas as pd

# Function to load paper data from a CSV file
def load_paper_data():
    # Specify the path to your CSV file (update if necessary)
    file_path = "research_papers.csv"
    # Load the data from CSV
    paper_df = pd.read_csv(file_path)

    # Optionally, you can perform any data processing here if needed
    return paper_df
