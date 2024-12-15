import pandas as pd
import streamlit as st

# Function to load data
def load_data():
    try:
        # Attempt to load the CSV file containing research papers
        df = pd.read_csv('data/research_papers.csv')
        # Ensure the necessary columns are present in the dataframe
        required_columns = ['Title', 'Author', 'University', 'Year', 'Category', 'Link', 'PDF']
        for col in required_columns:
            if col not in df.columns:
                st.warning(f"Warning: Column '{col}' is missing in the dataset.")
        return df
    except FileNotFoundError:
        st.error("Error: The data file could not be found. Please ensure the file is present in the correct path.")
        return None
    except pd.errors.EmptyDataError:
        st.error("Error: The data file is empty. Please ensure the file contains data.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Function to display the research papers
def display_papers(df):
    if df is not None:
        # Display the title of the app
        st.title("Kurdistan Research Papers")

        # Iterate through the papers in the DataFrame
        for idx, row in df.iterrows():
            # Display paper details
            st.subheader(f"**Title:** {row['Title']}")
            st.write(f"**Author:** {row['Author']}")
            st.write(f"**University:** {row['University']}")
            st.write(f"**Year:** {row['Year']}")
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Link:** {row['Link']}")

            # Check if a PDF is available for download
            pdf_link = row['PDF']
            if pd.notna(pdf_link):  # If a valid PDF link exists
                try:
                    # Display the download button for PDF
                    st.download_button(
                        label="Download PDF",
                        data=pdf_link,
                        file_name=f"{row['Title']}.pdf",
                        mime="application/pdf"
                    )
                except Exception as e:
                    st.error(f"Error displaying PDF for '{row['Title']}': {e}")
            else:
                st.warning(f"No PDF available for **{row['Title']}**.")
            st.markdown("---")  # Add a horizontal line for separation between papers
    else:
        st.write("No research papers available to display.")

# Main function to run the app
def main():
    # Load the data from the CSV file
    df = load_data()

    # Display papers if data is successfully loaded
    display_papers(df)

# Run the Streamlit app
if __name__ == "__main__":
    main()
