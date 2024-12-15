import streamlit as st

def home():
    st.title("Kurdistan Research Exchange")

    st.markdown(
        """
        Welcome to the Kurdistan Research Exchange platform! Here, you can explore a wide range of academic papers and research from various fields such as History, Political Science, Sociology, and more.

        Our goal is to provide access to research papers and allow users to upload and share their work for the betterment of the academic community. 

        Feel free to explore the papers in different categories and sort them by author, year, or title.
        """
    )

    # Interactive buttons for navigation
    st.subheader("Navigate to Sections")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("View Papers"):
            st.session_state.page = "view_papers"
            st.experimental_rerun()

    with col2:
        if st.button("Upload Papers"):
            st.session_state.page = "upload_papers"
            st.experimental_rerun()

    st.markdown("---")
    st.subheader("About the Platform")

    st.markdown(
        """
        **Kurdistan Research Exchange** is a platform aimed at promoting research in various disciplines related to the Kurdistan region. We are committed to providing open access to academic work and fostering collaboration among researchers.

        Explore our growing repository of research papers, and feel free to upload your own work to contribute to the community.

        For any queries, contact us at: **kurdistanresearch@platform.com**
        """
    )

# Initialize session state to keep track of the current page
if "page" not in st.session_state:
    st.session_state.page = "home"

# Page routing logic
if st.session_state.page == "home":
    home()
elif st.session_state.page == "view_papers":
    # Replace this with the view papers display code
    from display import display_papers
    # Assuming you have a function to get the papers DataFrame, pass it here
    df = pd.DataFrame()  # Replace with actual DataFrame for papers
    display_papers(df)
elif st.session_state.page == "upload_papers":
    # Replace this with the upload papers section code
    from upload import upload_papers
    upload_papers()

