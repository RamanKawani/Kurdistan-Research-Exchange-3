import streamlit as st
import pandas as pd

def load_data():
    """Load the research data from CSV."""
    return pd.read_csv("research_data.csv")

def save_data(data):
    """Save the research data to CSV."""
    data.to_csv("research_data.csv", index=False)

def main():
    st.set_page_config(page_title="Kurdistan Research Exchange", layout="wide")
    st.sidebar.image("assets/logo.png", use_column_width=True)

    # Load data
    data = load_data()

    # Title and Description
    st.title("Kurdistan Research Exchange")
    st.write("A platform to share and discover academic research from universities in Kurdistan.")

    # Categories
    categories = ["All", "History", "Political Science", "Sociology", "Philosophy", "Economics"]
    selected_category = st.sidebar.selectbox("Select a category", categories)

    # Filter data by category
    if selected_category != "All":
        filtered_data = data[data['Category'] == selected_category]
    else:
        filtered_data = data

    # Display research
    st.subheader("Research Papers")
    for index, row in filtered_data.iterrows():
        st.markdown(f"### {row['Title']}")
        st.markdown(f"**Author(s):** {row['Author(s)']}")
        st.markdown(f"**University:** {row['University']}")
        st.markdown(f"**Category:** {row['Category']}")
        st.markdown(f"**Abstract:** {row['Abstract']}")
        st.markdown("---")

    # Upload new research
    st.sidebar.subheader("Upload New Research")
    with st.sidebar.form("upload_form"):
        title = st.text_input("Research Title")
        authors = st.text_input("Author(s)")
        university = st.text_input("University")
        category = st.selectbox("Category", categories[1:])
        abstract = st.text_area("Abstract")
        uploaded = st.form_submit_button("Submit")

        if uploaded:
            if title and authors and university and abstract:
                new_row = pd.DataFrame({
                    "Title": [title],
                    "Author(s)": [authors],
                    "University": [university],
                    "Category": [category],
                    "Abstract": [abstract]
                })
                data = pd.concat([data, new_row], ignore_index=True)
                save_data(data)
                st.sidebar.success("Research uploaded successfully!")
            else:
                st.sidebar.error("Please fill in all fields.")

if __name__ == "__main__":
    main()


