import streamlit as st
from view_papers import display_papers  # Import function to display papers
from database_data import add_record  # Import function to add records

def main():
    # Sidebar navigation options
    page = st.sidebar.radio("Select a page", ["Home", "View Papers", "Add Paper"])

    if page == "Home":
        st.title("Welcome to the Research Papers App")
        st.write("Use the navigation on the left to explore the app.")

    elif page == "View Papers":
        display_papers()  # Display papers from the CSV with pagination

    elif page == "Add Paper":
        st.title("Add a New Paper")

        # Form to add a new paper
        title = st.text_input("Title")
        author = st.text_input("Author")
        university = st.text_input("University")
        year = st.number_input("Year", min_value=1900, max_value=2100, value=2023)
        category = st.text_input("Category")
        link = st.text_input("Link")
        pdf = st.text_input("PDF file name (must be uploaded in 'uploads' folder)")

        if st.button("Add Paper"):
            if title and author and university and category and link and pdf:
                new_paper = {
                    "Title": title,
                    "Author": author,
                    "University": university,
                    "Year": year,
                    "Category": category,
                    "Link": link,
                    "PDF": pdf
                }
                add_record(new_paper)  # Add the paper record to CSV
                st.success("Paper added successfully!")
                st.experimental_rerun()  # Refresh the page to show updated data

if __name__ == "__main__":
    main()
