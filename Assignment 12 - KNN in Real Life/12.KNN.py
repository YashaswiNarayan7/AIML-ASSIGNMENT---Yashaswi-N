# Assignment: KNN in Real Life
# Date: 07/03/2026
# Name: Yashaswi N

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def main():
    print("=== KNN in Real Life: Netflix Recommendations ===\n")

    # Step 1: Explain in text
    print("KNN can recommend movies to a user based on similarity with other users' ratings.\n")

    # Step 2: dataset (Users vs Movies ratings)
    data = {
        "Movie_A": [5, 4, 1, 2],
        "Movie_B": [3, 2, 5, 4],
        "Movie_C": [4, 5, 2, 3],
        "Movie_D": [1, 2, 5, 4]
    }

    users = ["User1", "User2", "User3", "User4"]
    df = pd.DataFrame(data, index=users)

    print("=== User Ratings ===")
    print(df)

    # Step 3: Calculate similarity between users using cosine similarity
    similarity = cosine_similarity(df)
    sim_df = pd.DataFrame(similarity, index=users, columns=users)

    print("\n=== User Similarity (Cosine) ===")
    print(sim_df)

    print("\nObservation: Users with higher similarity scores have similar movie preferences.")
    print("Netflix can recommend movies liked by similar users to the target user.\n")

if __name__ == "__main__":
    main()