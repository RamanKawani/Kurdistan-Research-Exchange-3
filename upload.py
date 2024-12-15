import streamlit as st

def upload_papers():
    st.subheader("Upload Your Research Paper")
    
    # Upload file
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
    
    if uploaded_file is not None:
        # Process the file (you can add your logic here)
        st.write(f"Uploaded file: {uploaded_file.name}")
        # For example, saving the file to the server
        with open(f"uploads/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")
