import streamlit as st

def home_section():
    st.title("Welcome to Kurdistan Research Exchange")
    
    # Main Introduction
    st.write("Welcome to the **Kurdistan Research Exchange** platform! This is a space where academic researchers, institutions, and scholars come together to share, access, and collaborate on research related to the Kurdistan Region and beyond.")
    
    # Add an image or logo
    st.image("path/to/logo_or_image.jpg", width=200)  # Replace with your actual image path or URL

    # About the Platform
    st.subheader("What is Kurdistan Research Exchange?")
    st.write("""
    Kurdistan Research Exchange is an open platform for universities, scholars, and institutions to share their research papers, collaborate on projects, and engage in academic dialogues. The platform encourages the free exchange of knowledge and aims to contribute to the academic community, particularly in fields like Political Science, History, International Relations, and more.
    """)

    # Key Features Section with Icons or Highlights
    st.subheader("Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("path/to/upload_icon.png", width=50)  # Replace with your icon path or URL
        st.write("**Upload Papers**")
        st.write("Easily upload your research papers for others to access.")
    
    with col2:
        st.image("path/to/view_icon.png", width=50)  # Replace with your icon path or URL
        st.write("**View Papers**")
        st.write("Browse a collection of research papers from various institutions.")
    
    with col3:
        st.image("path/to/collaborate_icon.png", width=50)  # Replace with your icon path or URL
        st.write("**Collaborate**")
        st.write("Engage in academic collaborations and propose joint projects.")

    # Call to Action Buttons
    st.subheader("Get Involved")
    st.write("Join us in the journey to advance research in the Kurdistan Region and beyond. Choose an action below to get started!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Upload Your Paper"):
            st.write("Redirecting to the Upload Papers section...")
            # Add the logic to redirect to the Upload Papers section
    
    with col2:
        if st.button("View Research Papers"):
            st.write("Redirecting to the View Papers section...")
            # Add the logic to redirect to the View Papers section
    
    # Recent Updates Section
    st.subheader("Recent Updates")
    st.write("Stay updated with the latest research and collaborations.")
    
    # Display recent papers dynamically or placeholders (replace with actual logic if needed)
    st.write("1. Paper A - *Research on Political Dynamics in the Kurdistan Region*")
    st.write("2. Paper B - *Economic Trends in the Middle East*")
    st.write("3. Paper C - *The Impact of International Relations on Kurdistan*")

    # Footer or Contact Information
    st.subheader("Contact Us")
    st.write("""
    For inquiries or additional information, please reach out to us at:
    - Email: [info@kurdistanresearch.org](mailto:info@kurdistanresearch.org)
    - Website: [www.kurdistanresearch.org](http://www.kurdistanresearch.org)
    """)


