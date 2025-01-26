import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data (if not already downloaded)
try:
    nltk.data.find('corpora/stopwords')
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('punkt_tab') 
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('punkt_tab')

# Set of stopwords
def clean_text(text, language="english"):
    """
    Function to clean text by:
    - Removing non-alphanumeric characters except spaces
    - Removing stopwords
    - Retaining only alphabets, numbers, and single spaces
    """
    try:
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r"[^A-Za-z0-9 ]", "", text)
    
        # Tokenize text
        tokens = word_tokenize(text)

        # Load stopwords based on the language
        STOPWORDS = set(stopwords.words(language))

        # Remove stopwords
        tokens = [word for word in tokens if word.lower() not in STOPWORDS]

        # Join tokens back to string
        cleaned_text = " ".join(tokens)

        return cleaned_text
    except Exception as e:
        raise ValueError(f"An error occurred during text cleaning: {str(e)}")
