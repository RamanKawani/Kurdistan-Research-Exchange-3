import streamlit as st

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

        # Rating and review section for logged-in users
        with st.form(key=f"review_form_{idx}"):
            rating = st.slider(f"Rate this paper", 1, 5, 3)
            review = st.text_area(f"Write a review for {row['Title']}")
            submit_button = st.form_submit_button(label="Submit Review")

            if submit_button:
                # Here you can save the review and rating to the database or DataFrame
                df.at[idx, 'Rating'] = rating
                df.at[idx, 'Reviews'] = review
                st.success("Review submitted successfully!")
                
    st.dataframe(df)  # Display updated papers DataFrame with ratings and reviews

