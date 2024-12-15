def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Upload Research Paper"])

    if selection == "Home":
        display_home()
    elif selection == "Upload Research Paper":
        display_upload()  # Use display_upload here

if __name__ == "__main__":
    main()
