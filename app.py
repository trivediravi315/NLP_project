import streamlit as st
import pandas as pd
from text_cleaner import clean_text
from nltk.corpus import stopwords
import nltk

# Download NLTK data (if not already downloaded)
try:
    nltk.data.find('corpora/stopwords')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

# Center-aligned Title
st.markdown(
    "<h1 style='text-align: center; color:white;'>Tidy Text</h1>", 
    unsafe_allow_html=True
)
# Welcome Message
st.markdown(
    "<h3 style='text-align: center;color:grey;'>Clean and refine your text with ease</h3>", 
    unsafe_allow_html=True
)

st.write("Upload a `.txt` or `.csv` file for text cleaning.")

# Language selection for stopwords, defaulting to English
language = st.selectbox("Select preferred language", options=["english", "spanish", "french", "german", "italian"], index=0)

# File upload
uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv"])



# Error handling for invalid file or language
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".txt"):
            # Process TXT file
            content = uploaded_file.read().decode("utf-8")
            if not content.strip():  # Check if content is empty
                raise ValueError("The uploaded `.txt` file is empty.")

            data = pd.DataFrame({"Content": [content]})
            st.subheader("Original File Content")
            st.write(data)

            # Add submit button to trigger cleaning
            if st.button("Submit"):
                # Apply cleaning
                st.subheader("Cleaned File Content")
                data["Cleaned_Content"] = data["Content"].apply(lambda x: clean_text(x, language))
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
            if data.empty:
                raise ValueError("The uploaded `.csv` file is empty.")
            
            st.subheader("Original File Content")
            st.write(data)

            # Select columns to process
            selected_columns = st.multiselect("Select columns to clean", data.columns)
            if not selected_columns:
                st.warning("Please select at least one column to clean.")
            
            if selected_columns:
                # Merge selected columns
                data["Merged_Content"] = data[selected_columns].astype(str).agg(" ".join, axis=1)

                st.subheader("Merged Content")
                st.write(data[["Merged_Content"]])

                # Add submit button to trigger cleaning
                if st.button("Submit"):
                    # Apply cleaning
                    st.subheader("Cleaned File Content")
                    data["Cleaned_Content"] = data["Merged_Content"].apply(lambda x: clean_text(x, language))
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
            st.error("Invalid file type. Please upload a `.txt` or `.csv` file.")
    
    except ValueError as ve:
        # Handling empty file or value errors
        st.error(f"Error: {ve}")
    except Exception as e:
        # Handling other exceptions
        st.error(f"An unexpected error occurred: {str(e)}")

else:
    st.info("Please upload a `.txt` or `.csv` file to get started.")
