import pandas as pd

# Sample data
def load_paper_data():
    data = {
        "Title": ["Paper 1", "Paper 2", "Paper 3"],
        "Author": ["Author 1", "Author 2", "Author 3"],
        "University": ["University A", "University B", "University C"],
        "Year": [2020, 2021, 2022],
        "Category": ["Category A", "Category B", "Category C"],
        "Link": ["http://example.com/paper1", "http://example.com/paper2", "http://example.com/paper3"],
        "PDF": ["paper1.pdf", "paper2.pdf", "paper3.pdf"]
    }
    
    # Create a DataFrame
    paper_df = pd.DataFrame(data)
    
    return paper_df
