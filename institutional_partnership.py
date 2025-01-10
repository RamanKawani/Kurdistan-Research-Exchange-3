import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send the email
def send_email(name, institution, message):
    # Sender and receiver details
    sender_email = "your_email@example.com"  # Your email address
    receiver_email = "RamanKhalid888@gmail.com"  # Your email address where you want to receive the message
    password = "KA4323CKK4082"  # Your email password (consider using app password or environment variable for security)

    # Create the email content
    subject = "Institutional Partnership Inquiry"
    body = f"Name: {name}\nInstitution: {institution}\nMessage: {message}"

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            st.success("Your message has been sent successfully!")
    except Exception as e:
        st.error(f"An error occurred while sending the email: {e}")

# Function to save partnership inquiry to CSV
def save_institutional_partnership(inquiry_details):
    try:
        # Load the existing CSV file, or create one if it doesn't exist
        df = pd.read_csv('institutional_partnerships.csv')
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=['Name', 'Institution', 'Message'])
    
    # Convert the inquiry details to a DataFrame format and append
    inquiry_details_df = pd.DataFrame([inquiry_details])
    df = pd.concat([df, inquiry_details_df], ignore_index=True)
    
    # Save the updated DataFrame back to CSV
    df.to_csv('institutional_partnerships.csv', index=False)

# Main function for the Institutional Partnership Section
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

    # Optional: You can add a contact form for users to get in touch
    with st.form(key='partnership_form'):
        name = st.text_input("Your Name")
        institution = st.text_input("Your Institution")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if name and institution and message:
                # Create a dictionary for the inquiry details
                inquiry_details = {
                    "Name": name,
                    "Institution": institution,
                    "Message": message
                }
                # Save the inquiry to CSV
                save_institutional_partnership(inquiry_details)
                # Send the email with the partnership details
                send_email(name, institution, message)
            else:
                st.error("Please fill out all fields before submitting.")
