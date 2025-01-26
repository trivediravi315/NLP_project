import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data (if not already downloaded)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download('punkt_tab')


# Set of stopwords
STOPWORDS = set(stopwords.words("english"))
#print(STOPWORDS)

def clean_text(text):
    """
    Function to clean text by:
    - Removing non-alphanumeric characters except spaces
    - Removing stopwords
    - Retaining only alphabets, numbers, and single spaces
    """
    # Remove non-alphanumeric characters except spaces
    text = re.sub(r"[^A-Za-z0-9 ]", "", text)
    
    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word.lower() not in STOPWORDS]

    # Join tokens back to string
    cleaned_text = " ".join(tokens)

    return cleaned_text
