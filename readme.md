# Text Cleaner App

## Overview
This project provides a simple application to clean text files or CSV files containing textual data. It removes unwanted characters, stopwords, and retains only meaningful content. The application is built using Python and Streamlit for an intuitive and user-friendly interface.

---

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

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher.
- Ensure you have `pip` installed for package management.

### Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
