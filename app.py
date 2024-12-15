import pandas as pd
import streamlit as st

# Function to load data
def load_data():
    try:
        # Load the CSV file
        df = pd.read_csv('data/research_papers.csv')
        return df
    except FileNotFoundError:
        st.error("CSV file not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        st.error("CSV file is empty. Please check the file contents.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Function to display the research papers
def display_papers(df):
    if df is not None and 'PDF' in df.columns:
        # Display the papers
        st.title("Kurdistan Research Papers")
        for idx, row in df.iterrows():
            st.subheader(f"Title: {row['Title']}")
            st.write(f"Author: {row['Author']}")
            st.write(f"University: {row['University']}")
            st.write(f"Year: {row['Year']}")
            st.write(f"Category: {row['Category']}")
            st.write(f"Link: {row['Link']}")

            # Display the download button for PDF
            pdf_link = row['PDF']
            if pd.notna(pdf_link):  # Check if there's a PDF link
                st.download_button(
                    label="Download PDF",
                    data=pdf_link,
                    file_name=f"{row['Title']}.pdf",
                    mime="application/pdf"
                )
            else:
                st.write("No PDF available for this paper.")
    else:
        st.write("No data available or 'PDF' column is missing.")

# Main function to run the app
def main():
    # Load data
    df = load_data()
    
    if df is not None:
        # Display papers
        display_papers(df)

# Run the app
if __name__ == "__main__":
    main()
