import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

print("----- SENTIMENT VECTORIZATION -----\n")

# 1. Dataset
documents = [
    "I love this movie",
    "This movie is terrible",
    "Amazing acting",
    "Worst film ever"
]

# 2. Bag of Words
bow = CountVectorizer()
bow_matrix = bow.fit_transform(documents)

print("Bag of Words Matrix:\n")
print(bow_matrix.toarray())
print("\nFeature Names:\n", bow.get_feature_names_out())

# Convert to DataFrame (Visualization)
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=bow.get_feature_names_out())
print("\nBag of Words DataFrame:\n", bow_df)

# 3. TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

print("\nTF-IDF Matrix:\n")
print(tfidf_matrix.toarray())
print("\nFeature Names:\n", tfidf.get_feature_names_out())

# Convert to DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())
print("\nTF-IDF DataFrame:\n", tfidf_df)

# 4. Comparison
print("\n----- COMPARISON -----")
print("Bag of Words: Counts frequency of words")
print("TF-IDF: Gives importance to rare words and reduces importance of common words")