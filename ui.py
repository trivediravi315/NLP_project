import streamlit as st

# Display the title and welcome message
def display_title():
    try:
        st.markdown(
            "<h1 style='text-align: center; color:white;'>Tidy Text</h1>", 
            unsafe_allow_html=True
        )
        st.markdown(
            "<h3 style='text-align: center;color:grey;'>Clean and refine your text with ease</h3>", 
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Error displaying title: {str(e)}")

# File uploader for user to upload files
def file_uploader():
    try:
        return st.file_uploader("Choose a file", type=["txt", "csv"])
    except Exception as e:
        st.error(f"Error during file upload: {str(e)}")
        return None

# Language selector for stopwords
def language_selector():
    try:
        return st.selectbox("Select stopword language", options=["english", "spanish", "french", "german", "italian"], index=0)
    except Exception as e:
        st.error(f"Error selecting language: {str(e)}")
        return "english"

# Display the original data (before cleaning)
def display_data(data):
    try:
        st.subheader("Original File Content")
        st.write(data)
    except Exception as e:
        st.error(f"Error displaying data: {str(e)}")

# Display the cleaned data (after cleaning)
def display_cleaned_data(data):
    try:
        st.subheader("Cleaned File Content")
        st.write(data)
    except Exception as e:
        st.error(f"Error displaying cleaned data: {str(e)}")

# Display the download button for cleaned data
def display_download_button(data, filename, filetype):
    try:
        if filetype == "txt":
            cleaned_txt = data["Cleaned_Content"].iloc[0]
            st.download_button(
                label="Download Cleaned Text",
                data=cleaned_txt,
                file_name=filename,
                mime="text/plain",
            )
        elif filetype == "csv":
            cleaned_csv = data.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Cleaned CSV",
                data=cleaned_csv,
                file_name=filename,
                mime="text/csv",
            )
    except Exception as e:
        st.error(f"Error displaying download button: {str(e)}")
