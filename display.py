# Instead of importing at the top:
# from display import display_papers

def load_sample_data():
    data = {
        "Title": ["Paper 1", "Paper 2", "Paper 3"],
        "Author": ["Author 1", "Author 2", "Author 3"],
        "University": ["University A", "University B", "University C"],
        "Year": [2020, 2021, 2022],
        "Category": ["Category A", "Category B", "Category C"],
        "Link": ["http://example.com/paper1", "http://example.com/paper2", "http://example.com/paper3"],
        "PDF": ["http://example.com/paper1.pdf", "http://example.com/paper2.pdf", "http://example.com/paper3.pdf"]
    }
    return pd.DataFrame(data)

def main():
    from display import display_papers  # Importing inside the function

    st.sidebar.title("Kurdistan Research Exchange")
    
    # Sidebar navigation options
    options = ["Home", "Upload Papers", "View Papers", "User Profile", "Submission Guidelines"]
    choice = st.sidebar.selectbox("Select a section", options)

    # Load sample data for papers
    df = load_sample_data()
    
    # Navigate based on user selection
    if choice == "Home":
        home_section()
    elif choice == "Upload Papers":
        upload_papers(df)
    elif choice == "View Papers":
        creator_email = "ramankhalid888@gmail.com"  # Change this to the actual creator email
        display_papers(df, creator_email)  # Pass the creator email to display_papers function
    elif choice == "User Profile":
        user_profile_section()
    elif choice == "Submission Guidelines":
        display_guidelines()  # Display the guidelines section
