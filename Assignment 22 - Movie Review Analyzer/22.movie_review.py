# Assignment: Movie Review Analyzer
# Date: 26/03/2026
# Name: Yashaswi N

positive_words = ["good", "great", "amazing", "excellent", "love"]
negative_words = ["bad", "worst", "boring", "poor", "hate"]

def analyze_sentiment(review):
    review = review.lower()
    score = 0

    for word in positive_words:
        if word in review:
            score += 1

    for word in negative_words:
        if word in review:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# 5 sample reviews
reviews = [
    "The movie was amazing and I love it",
    "It was the worst movie ever",
    "The story was okay not bad",
    "Excellent acting and great direction",
    "Very boring and poor script"
]

# Output
for i, review in enumerate(reviews, 1):
    print(f"Review {i}: {review}")
    print("Sentiment:", analyze_sentiment(review))
    print()