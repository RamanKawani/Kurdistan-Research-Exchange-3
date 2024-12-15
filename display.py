import streamlit as st

# Sample papers for demonstration (replace with your actual data)
def display_papers(df, creator_email="creator@example.com"):
    st.title("View Research Papers")
    
    # Ask user to enter their email to manage papers
    user_email = st.text_input("Enter your email to manage papers (admin only)", "")
    
    # Display the papers
    st.write("### Research Papers")
    for index, row in df.iterrows():
        # Create a styled card for each paper
        with st.expander(f"Paper: {row['Title']}"):
            # Display paper details
            st.subheader(f"Title: {row['Title']}")
            st.write(f"**Author**: {row['Author']}")
            st.write(f"**University**: {row['University']}")
            st.write(f"**Year**: {row['Year']}")
            st.write(f"**Category**: {row['Category']}")
            st.write(f"**Link**: [View Paper]({row['Link']})")
            st.write(f"**PDF**: [Download PDF]({row['PDF']})")
            
            # Display rating and review functionality
            rating = st.slider(f"Rate this paper (out of 5)", 1, 5, 3, step=1, key=f"rate_{index}")
            review = st.text_area(f"Write your review for '{row['Title']}'", key=f"review_{index}")
            st.write(f"Your rating: {rating} stars")
            st.write(f"Your review: {review}")
            
            # Display admin options if the user is the creator
            if user_email == creator_email:
                delete_button = st.button(f"Delete Paper: {row['Title']}", key=f"delete_{index}")
                edit_button = st.button(f"Edit Paper: {row['Title']}", key=f"edit_{index}")
                
                if delete_button:
                    # Confirm the deletion action
                    confirm_deletion = st.selectbox(
                        "Are you sure you want to delete this paper?", ["No", "Yes"]
                    )
                    if confirm_deletion == "Yes":
                        df.drop(index, inplace=True)
                        st.success(f"Paper '{row['Title']}' has been deleted.")
                        break  # To avoid modifying DataFrame while iterating
                    else:
                        st.info(f"Paper '{row['Title']}' was not deleted.")
                
                if edit_button:
                    # Allow for editing paper details
                    new_title = st.text_input(f"Edit Title of {row['Title']}", row['Title'], key=f"edit_title_{index}")
                    new_author = st.text_input(f"Edit Author of {row['Title']}", row['Author'], key=f"edit_author_{index}")
                    new_university = st.text_input(f"Edit University of {row['Title']}", row['University'], key=f"edit_university_{index}")
                    new_year = st.number_input(f"Edit Year of {row['Title']}", min_value=1900, max_value=2100, value=row['Year'], key=f"edit_year_{index}")
                    new_category = st.text_input(f"Edit Category of {row['Title']}", row['Category'], key=f"edit_category_{index}")
                    new_link = st.text_input(f"Edit Link of {row['Title']}", row['Link'], key=f"edit_link_{index}")
                    new_pdf = st.text_input(f"Edit PDF of {row['Title']}", row['PDF'], key=f"edit_pdf_{index}")
                    
                    update_button = st.button(f"Update Paper: {row['Title']}", key=f"update_{index}")
                    if update_button:
                        # Apply changes to the DataFrame
                        df.at[index, 'Title'] = new_title
                        df.at[index, 'Author'] = new_author
                        df.at[index, 'University'] = new_university
                        df.at[index, 'Year'] = new_year
                        df.at[index, 'Category'] = new_category
                        df.at[index, 'Link'] = new_link
                        df.at[index, 'PDF'] = new_pdf
                        st.success(f"Paper '{row['Title']}' has been updated.")
                    
    # Display the updated DataFrame after all actions
    st.write("### Updated Research Papers")
    st.dataframe(df)
