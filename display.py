import streamlit as st
import pandas as pd

# Function to display and manage papers
def display_papers(df):
    st.title("View Research Papers")

    # Category filter (optional)
    category_filter = st.selectbox(
        "Filter by Category",
        ["All", "History", "Political Science", "Sociology", "International Relations", "Philosophy"]
    )

    # Filter papers based on the selected category
    if category_filter != "All":
        df = df[df['Category'] == category_filter]
    
    # Display papers
    if not df.empty:
        # Display the data in a more advanced layout (for example, with an editable table)
        for index, row in df.iterrows():
            # Title and other details
            st.subheader(f"Title: {row['Title']}")
            st.write(f"Author: {row['Author']}")
            st.write(f"University: {row['University']}")
            st.write(f"Year: {row['Year']}")
            st.write(f"Category: {row['Category']}")
            st.write(f"Link: {row['Link']}")
            st.write(f"PDF Path: {row['PDF']}")
            
            # Display file as a link
            st.markdown(f"[Download PDF]({row['PDF']})", unsafe_allow_html=True)

            # Add a delete button for each paper
            if st.button(f"Delete Paper: {row['Title']}", key=f"delete_{index}"):
                delete_paper(index, df)
                st.experimental_rerun()  # Rerun the app to update the paper list
    else:
        st.write("No papers available.")

# Function to delete a paper from the DataFrame
def delete_paper(index, df):
    # Remove the paper from the DataFrame
    df = df.drop(index)

    # Ideally, update the DataFrame permanently (for example, save back to a CSV or database)
    df.to_csv('papers.csv', index=False)
    st.success("Paper deleted successfully!")

# You may want to reload or refresh the DataFrame each time after deletion
# This function can be placed in the app.py file or elsewhere depending on the setup
def load_papers():
    try:
        df = pd.read_csv('papers.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Title", "Author", "University", "Year", "Category", "Link", "PDF"])
    return df

