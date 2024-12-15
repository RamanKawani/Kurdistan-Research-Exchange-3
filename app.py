import streamlit as st
import subprocess
import sys
import os

# Function to check installed package version
def get_installed_version(package_name):
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "show", package_name], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if line.startswith("Version:"):
                return line.split(" ")[1]
        return None
    except Exception as e:
        return None

# Function to modify requirements.txt based on version conflict
def resolve_conflict():
    # Get current versions of Streamlit and pandas
    streamlit_version = get_installed_version('streamlit')
    pandas_version = get_installed_version('pandas')

    # Display the current versions
    st.write(f"Installed Streamlit version: {streamlit_version}")
    st.write(f"Installed pandas version: {pandas_version}")

    if streamlit_version and pandas_version:
        # If Streamlit 1.21.0 and pandas 2.x
        if streamlit_version == '1.21.0' and pandas_version.startswith('2'):
            st.warning("Conflict detected: Streamlit 1.21.0 is incompatible with pandas 2.x.")
            st.info("Downgrading pandas to 1.5.3 (compatible with Streamlit 1.21.0).")
            
            # Modify requirements.txt to downgrade pandas
            with open('requirements.txt', 'w') as f:
                f.write('streamlit==1.21.0\n')
                f.write('pandas==1.5.3\n')
            
            st.success("requirements.txt has been updated. Run `pip install -r requirements.txt` to resolve the conflict.")
        
        # If Streamlit is 2.x and pandas is compatible
        elif streamlit_version.startswith('2') and pandas_version.startswith('2'):
            st.success("Streamlit and pandas versions are compatible. No changes needed.")
        
        # If Streamlit 1.21.0 and pandas < 2
        elif streamlit_version == '1.21.0' and not pandas_version.startswith('2'):
            st.success("Streamlit 1.21.0 is compatible with pandas < 2.x. No changes needed.")
        
        # If Streamlit is 2.x and pandas < 2
        elif streamlit_version.startswith('2') and not pandas_version.startswith('2'):
            st.success("Streamlit version is compatible with pandas versions < 2 and >= 2.x. No changes needed.")
        
        else:
            st.error("Could not detect appropriate versions. Please check manually.")
    else:
        st.error("Required packages (Streamlit or pandas) are not installed.")

# Streamlit App Layout
st.title('Streamlit Dependency Conflict Resolver')
st.write(
    """
    This app helps resolve version conflicts between Streamlit and pandas.
    It checks installed versions of Streamlit and pandas, and automatically updates 
    the `requirements.txt` file if there is a conflict.
    """
)

# Button to resolve dependency issues
if st.button('Check & Resolve Dependency Conflicts'):
    resolve_conflict()

