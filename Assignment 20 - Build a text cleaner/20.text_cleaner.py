# Assignment: Build a text Cleaner
# Date: 21/03/2026
# Name: Yashaswi N

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

nltk.download('punkt')
nltk.download('stopwords')

text = "I am learning NLP and it is very exciting!"

# Lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

# Stemming
stemmer = PorterStemmer()
tokens = [stemmer.stem(word) for word in tokens]

print(tokens)