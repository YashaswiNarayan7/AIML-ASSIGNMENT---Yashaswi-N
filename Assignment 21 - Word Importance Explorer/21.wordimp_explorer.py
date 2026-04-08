# Assignment: Word Importance Explorer
# Date: 24/03/2026
# Name: Yashaswi N


print("Program Started...\n")

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError:
    print("Error: scikit-learn not installed. Run: pip install scikit-learn")
    exit()

# 5 sample documents
documents = [
    "Data science is an interdisciplinary field that uses scientific methods",
    "Machine learning is a subset of artificial intelligence",
    "Artificial intelligence enables machines to think and learn",
    "Data analysis helps extract useful information from data",
    "Deep learning is a part of machine learning"
]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

print("TF-IDF Results:\n")

# Print top 3 words for each document
for i in range(len(documents)):
    print(f"Document {i+1}:")
    
    scores = list(zip(feature_names, X[i].toarray()[0]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    top_words = sorted_scores[:3]
    
    for word, score in top_words:
        print(f"  {word} -> {round(score, 3)}")
    
    print()

print("Program Finished Successfully ✅")