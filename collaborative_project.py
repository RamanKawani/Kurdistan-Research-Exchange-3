import streamlit as st

def collaborative_project_section():
    st.title("Collaborative Projects")
    st.write("This section will feature collaborative research projects.")
    # Ask user to select a category for the project
    categories = [
        "History", "Political Science", "International Relations", 
        "Law", "Sociology", "Psychology", "Gender Studies"
    ]
    st.subheader("Select Research Category")
    selected_category = st.selectbox("Choose a category for your project:", categories)

    # Display a message based on the selected category
    st.write(f"You have selected the category: **{selected_category}**")

    # Navigation between proposing a project and finding a project
    section_choice = st.radio("Select a section:", ["Propose a Project", "Find a Project to Collaborate On"])

    if section_choice == "Propose a Project":
        propose_project_section()
    elif section_choice == "Find a Project to Collaborate On":
        find_project_section(selected_category)

def propose_project_section():
    st.subheader("Propose a Collaborative Research Project")

    project_title = st.text_input("Enter Project Title")
    project_description = st.text_area("Enter Project Description")
    project_contact = st.text_input("Your Contact Information (Email)")
    project_location = st.text_input("Enter Project Location")  # Added field for location

    if st.button("Submit Project Proposal"):
        if project_title and project_description and project_contact and project_location:
            st.success("Your project proposal has been submitted!")
            st.write(f"Project Title: {project_title}")
            st.write(f"Description: {project_description}")
            st.write(f"Contact Info: {project_contact}")
            st.write(f"Location: {project_location}")  # Display location of the project
        else:
            st.error("Please fill out all the fields to submit your project proposal.")

def find_project_section(selected_category):
    st.subheader("Find a Project to Collaborate On")
    st.write(f"Explore collaborative projects in your chosen category: **{selected_category}**")

    # Sample project data (You can replace it with a list of actual projects from a database or data structure)
    sample_projects = [
        {"title": "History of Kurdistan", "location": "Erbil, Kurdistan", "description": "A deep dive into the history of Kurdistan.", "contact": "user1@example.com"},
        {"title": "Political Science Research", "location": "Baghdad, Iraq", "description": "Analyzing political trends in Iraq.", "contact": "user2@example.com"}
    ]

    # Display the sample projects
    if sample_projects:
        for project in sample_projects:
            st.write(f"### {project['title']}")
            st.write(f"**Location:** {project['location']}")
            st.write(f"**Description:** {project['description']}")
            st.write(f"**Contact:** {project['contact']}")
            st.write("---")
    else:
        st.write("Currently, there are no projects listed under this category.")


