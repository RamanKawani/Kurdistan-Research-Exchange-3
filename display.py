import streamlit as st
from streamlit import components

def display_papers(df):
    st.title("View Research Papers")

    # Display all papers
    for idx, row in df.iterrows():
        st.subheader(f"{row['Title']} (by {row['Author']})")
        st.write(f"University: {row['University']}")
        st.write(f"Year: {row['Year']}")
        st.write(f"Category: {row['Category']}")
        st.write(f"Link: [View Paper]({row['Link']})")

        # Display the current rating and review (if any)
        st.write(f"Rating: {row['Rating']} / 5")
        st.write(f"Review: {row['Reviews']}")

        # Create a star rating system
        stars = st.slider(f"Rate this paper (out of 5)", 1, 5, 3, step=1)
        st.write("Your Rating:", "⭐" * stars)

        # Create a review box
        review = st.text_area(f"Write a review for {row['Title']}")

        # Add submit button
        if st.button(f"Submit Review for {row['Title']}", key=f"submit_{idx}"):
            df.at[idx, 'Rating'] = stars
            df.at[idx, 'Reviews'] = review
            st.success("Review submitted successfully!")

    # Display updated DataFrame with ratings and reviews
    st.dataframe(df)


