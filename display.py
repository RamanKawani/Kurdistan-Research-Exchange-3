import streamlit as st

def display_papers(df):
    st.title("View Research Papers")

    # Create a container to hold all the papers
    with st.container():
        for idx, row in df.iterrows():
            # Use columns to split the layout for paper info
            col1, col2 = st.columns([3, 1])  # Adjust the columns width
            
            with col1:
                # Display Paper Title and Author
                st.subheader(f"{row['Title']}")
                st.write(f"**Author**: {row['Author']}")
                st.write(f"**University**: {row['University']}")
                st.write(f"**Year**: {row['Year']}")
                st.write(f"**Category**: {row['Category']}")
                st.write(f"**Link**: [View Paper]({row['Link']})")
                st.write("---")  # Horizontal separator

            with col2:
                # Display Paper Rating and Review (if any)
                st.write(f"**Rating**: {row['Rating']} / 5")
                st.write(f"**Review**: {row['Reviews']}")
                st.write("---")  # Horizontal separator
            
            # Add some space for separation
            st.markdown("<br>", unsafe_allow_html=True)

            # Create a rating slider with a unique key
            stars = st.slider(f"Rate this paper (out of 5)", 1, 5, 3, step=1, key=f"stars_{idx}")
            st.write("Your Rating:", "⭐" * stars)

            # Create a review box
            review = st.text_area(f"Write a review for {row['Title']}", key=f"review_{idx}")

            # Add submit button
            if st.button(f"Submit Review for {row['Title']}", key=f"submit_{idx}"):
                df.at[idx, 'Rating'] = stars
                df.at[idx, 'Reviews'] = review
                st.success("Review submitted successfully!")

            st.write("---")  # Horizontal separator

        # Display updated DataFrame with ratings and reviews
        st.dataframe(df)
