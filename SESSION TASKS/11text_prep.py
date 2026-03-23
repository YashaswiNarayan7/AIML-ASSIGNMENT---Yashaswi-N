import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

print("----- TEXT PREPROCESSING TOOL -----\n")

# Input text
text = "I am learning NLP and it is very exciting!"

print("Original Text:", text)

# 1. Convert to lowercase
text = text.lower()

# 2. Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# 3. Tokenize
tokens = word_tokenize(text)

# 4. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# 5. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]

# Final Output
print("\nProcessed Output:\n", stemmed_words)