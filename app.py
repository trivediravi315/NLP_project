import streamlit as st
import pandas as pd
from text_cleaner import clean_text

st.title("Welcome to TidyText!")
st.write("Clean and refine your text")

st.write("Upload a `.txt` or `.csv` file for text cleaning.")

# File upload
uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".txt"):
        # Process TXT file
        content = uploaded_file.read().decode("utf-8")
        data = pd.DataFrame({"Content": [content]})
        st.subheader("Original File Content")
        st.write(data)

        # Add submit button to trigger cleaning
        if st.button("Submit"):
            # Apply cleaning
            st.subheader("Cleaned File Content")
            data["Cleaned_Content"] = data["Content"].apply(clean_text)
            st.write(data)

            # Download cleaned data
            cleaned_txt = data["Cleaned_Content"].iloc[0]
            st.download_button(
                label="Download Cleaned Text",
                data=cleaned_txt,
                file_name="cleaned_file.txt",
                mime="text/plain",
            )

    elif uploaded_file.name.endswith(".csv"):
        # Process CSV file
        data = pd.read_csv(uploaded_file)
        st.subheader("Original File Content")
        st.write(data)

        # Select columns to process
        selected_columns = st.multiselect("Select columns to clean", data.columns)
        if selected_columns:
            # Merge selected columns
            data["Merged_Content"] = data[selected_columns].astype(str).agg(" ".join, axis=1)

            st.subheader("Merged Content")
            st.write(data[["Merged_Content"]])

            # Add submit button to trigger cleaning
            if st.button("Submit"):
                # Apply cleaning
                st.subheader("Cleaned File Content")
                data["Cleaned_Content"] = data["Merged_Content"].apply(clean_text)
                st.write(data[["Merged_Content", "Cleaned_Content"]])

                # Option to download cleaned data
                cleaned_csv = data.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download Cleaned CSV",
                    data=cleaned_csv,
                    file_name="cleaned_file.csv",
                    mime="text/csv",
                )
        else:
            st.warning("Please select at least one column to clean.")
