import pandas as pd

# Sample data for the papers
data = {
    "Title": ["Paper 1", "Paper 2", "Paper 3"],
    "Author": ["Author 1", "Author 2", "Author 3"],
    "University": ["University A", "University B", "University C"],
    "Year": [2020, 2021, 2022],
    "Category": ["Category A", "Category B", "Category C"],
    "Link": ["paper1.pdf", "paper2.pdf", "paper3.pdf"],
    "PDF": ["paper1.pdf", "paper2.pdf", "paper3.pdf"]
}

# Function to load paper data
def load_paper_data():
    return pd.DataFrame(data)
