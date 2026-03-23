from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

# Download tokenizer (run once)
nltk.download('punkt')

print("----- MINI WORD2VEC MODEL -----\n")

# 1. Create Dataset (15+ sentences on college life)
sentences = [
    "college life is very exciting",
    "students attend classes daily",
    "friends make college life fun",
    "exams are stressful sometimes",
    "canteen food is tasty",
    "group study helps in exams",
    "projects improve practical knowledge",
    "college events are enjoyable",
    "sports activities keep students active",
    "late night study is common",
    "teachers guide students",
    "assignments must be submitted on time",
    "library is useful for studying",
    "internships help in career growth",
    "students learn new skills in college"
]

# 2. Tokenize sentences
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# 3. Train Word2Vec model
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=4
)

# 4. Print vector of a word
word = "college"
print(f"Vector for '{word}':\n", model.wv[word])

# 5. Find most similar words
print(f"\nTop 5 similar words to '{word}':")
similar_words = model.wv.most_similar(word, topn=5)

for w, score in similar_words:
    print(f"{w} : {score:.4f}")