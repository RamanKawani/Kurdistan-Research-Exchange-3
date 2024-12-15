import streamlit as st
import pandas as pd

# Initialize a DataFrame to store project proposals (replace with actual database if necessary)
def initialize_projects():
    # Sample data structure for demonstration
    data = {
        "Title": ["Climate Change Research", "Kurdistan Economic Development"],
        "Description": ["Research on the impact of climate change in Kurdistan", 
                        "Study the impact of economic growth in the Kurdistan Region"],
        "Category": ["Environment", "Economics"],
        "Proposed By": ["creator@example.com", "creator@example.com"],
        "Interested": [["user1@example.com", "user2@example.com"], []]  # List of interested users
    }
    return pd.DataFrame(data)

# Function to propose a new project
def propose_project(df, user_email):
    st.title("Propose a Collaborative Research Project")
    
    title = st.text_input("Project Title")
    description = st.text_area("Project Description")
    category = st.selectbox("Category", ["Environment", "Economics", "Health", "Politics", "Technology"])
    
    if st.button("Submit Project Proposal"):
        if title and description:
            new_project = {
                "Title": title,
                "Description": description,
                "Category": category,
                "Proposed By": user_email,
                "Interested": []
            }
            df = df.append(new_project, ignore_index=True)
            st.success("Project proposed successfully!")
        else:
            st.error("Please fill in all fields.")

# Function to show available projects
def show_projects(df, user_email):
    st.title("Available Collaborative Research Projects")
    
    for index, row in df.iterrows():
        with st.expander(f"{row['Title']}"):
            st.write(f"**Description**: {row['Description']}")
            st.write(f"**Category**: {row['Category']}")
            st.write(f"**Proposed By**: {row['Proposed By']}")
            st.write(f"**Interested Users**: {', '.join(row['Interested'])}")
            
            if user_email not in row['Interested'] and user_email != row['Proposed By']:
                if st.button(f"Express Interest in {row['Title']}", key=f"interest_{index}"):
                    df.at[index, 'Interested'].append(user_email)
                    st.success(f"You are now interested in collaborating on {row['Title']}.")
            elif user_email == row['Proposed By']:
                st.write("You are the proposer of this project. You can manage the collaborators here.")
                
    # Display the updated projects after interaction
    st.write("### Updated Projects")
    st.dataframe(df)

# Main function for the collaborative section
def collaborative_project_section(user_email="user@example.com"):
    df = initialize_projects()  # Initialize projects (replace with your data source)
    
    # Sidebar options for the collaborative section
    option = st.sidebar.selectbox("Choose an action", ["Propose a Project", "View Available Projects"])
    
    if option == "Propose a Project":
        propose_project(df, user_email)
    elif option == "View Available Projects":
        show_projects(df, user_email)

