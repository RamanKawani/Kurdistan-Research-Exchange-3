import pandas as pd

def load_sample_data():
    """Load sample data for demonstration."""
    data = {
        "Title": ["Research on AI in Kurdistan", "Sociology of Kurdish Communities"],
        "Author": ["Dr. A", "Dr. B"],
        "Institution": ["Erbil University", "Sulaymaniyah University"],
        "Year": [2023, 2024],
    }
    return pd.DataFrame(data)
