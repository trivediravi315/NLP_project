import streamlit as st
import pandas as pd
from text_cleaner import clean_text


st.title("Text File Cleaner")
st.write("Upload a text file, and the app will clean the content for you.")

# File upload
uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv"])

if uploaded_file is not None:
    # Read file content
    if uploaded_file.name.endswith(".txt"):
        content = uploaded_file.read().decode("utf-8")
        data = pd.DataFrame({"Content": [content]})
    elif uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)

    st.subheader("Original File Content")
    st.write(data)

    # Apply cleaning
    st.subheader("Cleaned File Content")
    if "Content" in data.columns:
        data["Cleaned_Content"] = data["Content"].apply(clean_text)
        st.write(data[["Content", "Cleaned_Content"]])

        # Option to download cleaned data
        cleaned_csv = data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Cleaned Data",
            data=cleaned_csv,
            file_name="cleaned_file.csv",
            mime="text/csv",
        )
    else:
        st.error("The uploaded file must contain a 'Content' column.")

