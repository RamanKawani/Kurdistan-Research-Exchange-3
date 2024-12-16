import streamlit as st

def institutional_partnership_section():
    # Title for the section
    st.title("Institutional Partnership")

    # Introduction about institutional partnerships
    st.markdown("""
        The **Institutional Partnership** section is dedicated to fostering collaborations 
        between academic institutions, research organizations, and the Kurdistan Region. 
        These partnerships are vital for promoting research, academic exchange, and the 
        development of new ideas that benefit both local and international communities.
    """)

    # Key areas of institutional partnerships
    st.subheader("Key Areas of Partnership")
    st.markdown("""
        Institutional partnerships can focus on various fields, including but not limited to:
        - Research collaboration
        - Student and faculty exchange programs
        - Joint workshops and conferences
        - Development of new academic programs
        - Knowledge sharing and capacity building
    """)

    # Types of Partners
    st.subheader("Types of Partners")
    st.markdown("""
        Institutional partnerships may involve a variety of partners:
        - **Universities and Colleges**: Higher education institutions seeking collaboration on research or student exchange programs.
        - **Research Institutes**: Organizations focused on scientific or social research in various fields.
        - **Government and NGOs**: Bodies involved in public policy or development initiatives.
        - **Private Sector**: Businesses that support research through funding or collaboration.
    """)

    # Benefits of Partnerships
    st.subheader("Benefits of Institutional Partnerships")
    st.markdown("""
        The benefits of building institutional partnerships include:
        - Enhanced academic and research opportunities
        - Increased access to funding and resources
        - Collaboration on solving regional and global challenges
        - Opportunities for students to engage in international research projects
        - Strengthened ties between the Kurdistan Region and global academic communities
    """)

    # Call to Action - Encouraging partnerships
    st.subheader("Become a Partner")
    st.markdown("""
        If your institution is interested in partnering with organizations in the Kurdistan 
        Region, please reach out to us to discuss potential collaborations.
    """)

    # Contact form or information
    st.markdown("For more information on institutional partnerships, please contact us:")
    st.markdown("[info@kurdistan-research.org](mailto:info@kurdistan-research.org)")

    # Optional: You can add a contact form or button for users to get in touch
    with st.form(key='partnership_form'):
        st.text_input("Your Name")
        st.text_input("Your Institution")
        st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.success("Thank you for your interest! We will get back to you shortly.")
