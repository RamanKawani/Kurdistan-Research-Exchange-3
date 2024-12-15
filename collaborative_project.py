import streamlit as st

# Collaborative project section
def collaborative_project_section(user_email="user@example.com"):
    st.title("Collaborative Research Projects")

    # Ask user to select a category for the project
    categories = [
        "History", "Political Science", "International Relations", 
        "Law", "Sociology", "Psychology", "Gender Studies"
    ]
    st.subheader("Select Research Category")
    selected_category = st.selectbox("Choose a category for your project:", categories)

    # Display a message based on the selected category
    st.write(f"You have selected the category: **{selected_category}**")

    # Let users propose a project
    st.subheader("Propose a Collaborative Research Project")

    project_title = st.text_input("Enter Project Title")
    project_description = st.text_area("Enter Project Description")
    project_contact = st.text_input("Your Contact Information (Email)")

    if st.button("Submit Project Proposal"):
        if project_title and project_description and project_contact:
            st.success("Your project proposal has been submitted!")
            # You can save these details into a database or file for further processing
            # For demonstration, we just display the submitted details
            st.write(f"Project Title: {project_title}")
            st.write(f"Description: {project_description}")
            st.write(f"Contact Info: {project_contact}")
        else:
            st.error("Please fill out all the fields to submit your project proposal.")

    # If user is looking for projects to collaborate on, show available categories
    st.subheader("Find a Project to Collaborate On")
    st.write("Explore collaborative projects in your chosen category:")

    # List existing categories with a simple button to indicate interest
    if selected_category:
        st.write(f"Explore collaborative projects under **{selected_category}**.")
        # In a real application, you'd load and display actual project listings for the category
        st.write(f"Currently, there are no projects listed under {selected_category}.")

    st.write("---")
    st.write("**Note**: If you'd like to suggest a project or collaborate with others, please use the above options.")

