import pandas as pd

def process_txt_file(uploaded_file):
    """Process a .txt file."""
    content = uploaded_file.read().decode("utf-8")
    if not content.strip():  # Check if content is empty
        raise ValueError("The uploaded `.txt` file is empty.")
    return pd.DataFrame({"Content": [content]})

def process_csv_file(uploaded_file):
    """Process a .csv file."""
    data = pd.read_csv(uploaded_file)
    if data.empty:
        raise ValueError("The uploaded `.csv` file is empty.")
    return data
