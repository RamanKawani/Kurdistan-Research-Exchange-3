import streamlit as st

# Sample papers for demonstration (replace with your actual data)
def display_papers(df, creator_email="RamanKhalid888@gmail.com"):
    st.title("View Research Papers")
    
    # Assume the user email is stored or authenticated
    user_email = st.text_input("Enter your email to manage papers", "")
    
    # Display the papers
    st.write("### Research Papers")
    for index, row in df.iterrows():
        st.subheader(f"Title: {row['Title']}")
        st.write(f"Author: {row['Author']}")
        st.write(f"University: {row['University']}")
        st.write(f"Year: {row['Year']}")
        st.write(f"Category: {row['Category']}")
        st.write(f"Link: {row['Link']}")
        st.write(f"PDF: {row['PDF']}")
        
        # Only allow delete for the creator (admin) and when the correct email is entered
        if user_email == creator_email:
            delete_button = st.button(f"Delete {row['Title']}", key=f"delete_{index}")
            if delete_button:
                # Delete the paper from the DataFrame
                df.drop(index, inplace=True)
                st.success(f"Paper '{row['Title']}' has been deleted.")
                break  # to avoid modifying the DataFrame while iterating

    # Display the updated DataFrame
    st.dataframe(df)

