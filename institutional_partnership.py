import streamlit as st

def institutional_partnership_section():
    st.title("Institutional Partnerships")
    st.write("Welcome to the Institutional Partnerships section.")
    st.write("Here universities and academic institutions can collaborate and partner on research projects related to the Kurdistan Region.")
    st.write("This section provides an opportunity for institutions to engage in collaborative research efforts, share knowledge, and build academic partnerships.")

        "Welcome to the Institutional Partnerships section, where universities and academic institutions can collaborate."
    )
    
    # Form to register an institution partnership
    st.subheader("Register a New Partnership")
    
    institution_name = st.text_input("Institution Name")
    contact_person = st.text_input("Contact Person")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    website = st.text_input("Website")
    partnership_description = st.text_area("Partnership Description")

    if st.button("Submit Partnership"):
        # Here, you would typically save the partnership details to a database or file
        st.success("Institutional Partnership Submitted!")
        
        # Show the submitted details (for demo purposes)
        st.write(f"**Institution Name:** {institution_name}")
        st.write(f"**Contact Person:** {contact_person}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone Number:** {phone}")
        st.write(f"**Website:** {website}")
        st.write(f"**Partnership Description:** {partnership_description}")
    
    st.write("### View Existing Partnerships")
    # Display the list of existing partnerships (for demo purposes, we show mock data)
    partnerships = [
        {"Institution": "University A", "Contact Person": "John Doe", "Email": "john@universitya.edu"},
        {"Institution": "University B", "Contact Person": "Jane Smith", "Email": "jane@universityb.edu"},
    ]
    
    for partnership in partnerships:
        st.write(f"**Institution:** {partnership['Institution']}")
        st.write(f"**Contact Person:** {partnership['Contact Person']}")
        st.write(f"**Email:** {partnership['Email']}")
        st.write("---")
