### Tidy Text - Text Cleaning Application
Tidy Text is a simple and easy-to-use Streamlit app for cleaning text files. It allows users to upload a .txt or .csv file, select specific columns for cleaning (for .csv files), and then clean the text by removing stopwords and unwanted characters. The app then provides a cleaned version of the file for download.

### Features
- Supports both .txt and .csv file formats.
- Allows users to select the language of stopwords (default is English).
- Users can clean specific columns of a .csv file by merging them before cleaning.
- Provides cleaned text for .txt and .csv files.
- Option to download the cleaned data in the original file format.

Installation
Follow these steps to run the app locally:

1. Clone the repository:
bash
git clone <repository_url>
cd <repository_folder>

2. Create a virtual environment (optional, but recommended):
bash
python -m venv myenv
3. Activate the virtual environment:
Windows:
bash
myenv\Scripts\activate
macOS/Linux:
bash
source myenv/bin/activate
4. Install the required dependencies:
bash
pip install -r requirements.txt
5. Run the app:
bash
streamlit run app.py
This will open the app in your default web browser.

### App Usage

**Upload File:**

You can upload a .txt or .csv file. The app will automatically detect the file type.
Select Language for Stopwords:

By default, the app uses English stopwords. You can select other languages (e.g., Spanish, French, German, Italian) from a dropdown menu.

**Select Columns for CSV Files:**

If you upload a .csv file, the app allows you to select which columns you want to clean. These columns will be merged and cleaned as a single string.

**Clean and Download**:

Once you've uploaded the file and selected the columns to clean, click the Submit button to process the text.
After cleaning, you can view the cleaned text and download the cleaned file.

**File Format Details:**
.txt Files
Upload a text file, and the app will clean the entire text, removing stopwords and unwanted characters. The cleaned text will be available for download.
.csv Files
Upload a CSV file. The app allows you to select columns to clean. If multiple columns are selected, they will be merged into a single text column before cleaning.
After cleaning, the app will provide an option to download the cleaned CSV file.