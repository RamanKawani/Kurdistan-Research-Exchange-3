import pandas as pd
import streamlit as st

# Function to load the data
def load_data():
    try:
        return pd.read_csv("database.csv")
    except FileNotFoundError:
        st.error("Error: database.csv file not found!")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

# Main application
def main():
    # Load data
    data = load_data()

    # Sidebar logo
    st.sidebar.image("logo.png", use_column_width=True)

    # Title and description
    st.title("Kurdistan Research Exchange")
    st.write("A platform to explore research about the Kurdistan Region.")

    # Filter options
    st.sidebar.header("Filters")
    categories = data["category"].unique() if not data.empty else []
    selected_category = st.sidebar.selectbox("Select a Category", options=["All"] + list(categories))

    # Filter data
    if selected_category != "All" and not data.empty:
        data = data[data["category"] == selected_category]

    # Display data
    if not data.empty:
        st.write(f"Showing {len(data)} research papers:")
        for _, row in data.iterrows():
            st.subheader(row["title"])
            st.write(f"**Author:** {row['author']}")
            st.write(f"**Date:** {row['date']}")
            st.write(row["abstract"])
            st.markdown("---")
    else:
        st.write("No research papers available.")

if __name__ == "__main__":
    main()



