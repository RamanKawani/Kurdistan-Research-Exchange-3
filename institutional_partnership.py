# institutional_partnership.py
import streamlit as st

def institutional_partnership_section():
    # Title and Introduction
    st.title("Institutional Partnerships")
    st.write("Welcome to the **Institutional Partnerships** section of the Kurdistan Research Exchange platform.")
    
    # Description of the Section
    st.write("This section provides an opportunity for universities and academic institutions to collaborate on research projects related to the Kurdistan Region.")
    st.write("Universities, research centers, and academic institutions can use this space to engage in joint research efforts, exchange knowledge, and form valuable academic partnerships.")

    # Provide a space for institutions to propose collaborations
    st.subheader("Propose a Collaboration")
    st.write("If your institution is interested in proposing a collaboration or project, please fill out the form below with details of your proposed partnership.")

    # Form for collaboration proposal
    with st.form(key='collaboration_form'):
        institution_name = st.text_input("Institution Name")
        project_title = st.text_input("Project Title")
        project_description = st.text_area("Project Description")
        contact_email = st.text_input("Contact Email")
        submit_button = st.form_submit_button("Submit Proposal")
        
        if submit_button:
            if institution_name and project_title and project_description and contact_email:
                st.success(f"Thank you! Your proposal for '{project_title}' has been submitted successfully. We will contact you soon at {contact_email}.")
            else:
                st.error("Please fill in all fields to submit the proposal.")

    # Additional Information for Universities and Academic Institutions
    st.subheader("Why Collaborate?")
    st.write("Collaborating with universities and academic institutions is crucial for advancing research in the Kurdistan Region.")
    st.write("By working together, we can achieve greater impact and foster innovation in various academic fields such as Political Science, History, International Relations, and more.")

    # Examples of previous or potential collaborations (can be added dynamically)
    st.subheader("Previous Collaborations")
    st.write("We have seen successful partnerships in the past. Below are some examples:")
    
    st.write("1. **Project A**: A joint project between University A and University B focused on Political Science research in the Kurdistan Region.")
    st.write("2. **Project B**: A collaboration between University C and University D exploring regional economic growth patterns.")
    st.write("3. **Project C**: A partnership between multiple institutions for a comparative study of Middle Eastern geopolitics.")

    # Footer with contact information
    st.subheader("Contact Information")
    st.write("For more information or to inquire about institutional partnerships, please contact us at: info@kurdistanresearch.org")
