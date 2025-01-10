import streamlit as st
import pandas as pd

# Function to save a collaborative project to CSV
def save_collaborative_project(project_details):
    try:
        # Load the existing CSV file, or create one if it doesn't exist
        df = pd.read_csv('collaborative_projects.csv')
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=['Title', 'Description', 'Contact', 'Location', 'Category'])
    
    # Convert the project details to a DataFrame format and append
    project_details_df = pd.DataFrame([project_details])
    df = pd.concat([df, project_details_df], ignore_index=True)
    
    # Save the updated DataFrame back to CSV
    df.to_csv('collaborative_projects.csv', index=False)

# Main function for the Collaborative Research Projects Section
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
    st.write(f"You have selected the category: {selected_category}")

    # Navigation between proposing a project and finding a project
    section_choice = st.radio("Select a section:", ["Propose a Project", "Find a Project to Collaborate On"])

    if section_choice == "Propose a Project":
        propose_project_section(selected_category)
    elif section_choice == "Find a Project to Collaborate On":
        find_project_section(selected_category)

# Function to propose a new collaborative project
def propose_project_section(selected_category):
    st.subheader("Propose a Collaborative Research Project")

    project_title = st.text_input("Enter Project Title")
    project_description = st.text_area("Enter Project Description")
    project_contact = st.text_input("Your Contact Information (Email)")
    project_location = st.text_input("Enter Project Location")  # Added field for location

    if st.button("Submit Project Proposal"):
        if project_title and project_description and project_contact and project_location:
            # Create a dictionary for the project details
            project_details = {
                "Title": project_title,
                "Description": project_description,
                "Contact": project_contact,
                "Location": project_location,
                "Category": selected_category
            }
            # Save the project to CSV
            save_collaborative_project(project_details)
            st.success("Your project proposal has been submitted!")
            st.write(f"Project Title: {project_title}")
            st.write(f"Description: {project_description}")
            st.write(f"Contact Info: {project_contact}")
            st.write(f"Location: {project_location}")
            st.write(f"Category: {selected_category}")
        else:
            st.error("Please fill out all the fields to submit your project proposal.")

# Function to find a collaborative project to join
def find_project_section(selected_category):
    st.subheader("Find a Project to Collaborate On")
    st.write(f"Explore collaborative projects in your chosen category: {selected_category}")

    try:
        df = pd.read_csv('collaborative_projects.csv')
        filtered_projects = df[df['Category'] == selected_category]

        if not filtered_projects.empty:
            for _, project in filtered_projects.iterrows():
                st.write(f"### {project['Title']}")
                st.write(f"Location: {project['Location']}")
                st.write(f"Description: {project['Description']}")
                st.write(f"Contact: {project['Contact']}")
                st.write("---")
        else:
            st.write("Currently, there are no projects listed under this category.")
    except FileNotFoundError:
        st.write("No collaborative projects available.")
