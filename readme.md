# Tide Text

## Overview
This project provides a simple application to clean text files or CSV files containing textual data. It removes unwanted characters, stopwords, and retains only meaningful content. The application is built using Python and Streamlit for an intuitive and user-friendly interface.


## Features
1. **Text Cleaning**:
   - Removes non-alphanumeric characters (except spaces).
   - Removes stopwords (using NLTK's English stopword corpus).
   - Retains only words, numbers, and single spaces.
2. **File Upload**:
   - Supports `.txt` and `.csv` files.
   - Displays original and cleaned content side-by-side.
3. **Download Cleaned Data**:
   - Allows users to download the cleaned content in a CSV format.
     

## Setup Instructions

### Prerequisites
- Python 3.7 or higher.
- Ensure you have `pip` installed for package management.

### Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv my_venv
   source my_venv/bin/activate       # On Linux/Mac
   my_venv\Scripts\activate          # On Windows

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

5. Run the Streamlit app:
   ```bash
   streamlit run app.py

### Usage
Upload a File:
- Upload a .txt file for cleaning single blocks of text.
- Upload a .csv file to clean one or more text-based columns.

Select Columns (for CSV files):
- Choose the columns you want to process.
- Merge selected columns into a unified text column.
  
Clean the Text:
- Click the "Submit" button to clean the text using the built-in cleaning rules.
  
Download Processed Data:
- For .txt files: Download the cleaned text as a .txt file.
- For .csv files: Download the cleaned dataset as a .csv file.
  
### Sample Data
Use the sample .txt and .csv files in the testing_files/ folder to test the app.
