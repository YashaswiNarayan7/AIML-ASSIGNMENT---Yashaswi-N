# Assignment: Build Your First Dataset
# Date: 03/03/2026
# Name: Yashaswi N

import pandas as pd

def main():
    print("=== Build Your First Dataset ===\n")

    # Step 1: Create dataset 
    data = {
        "Student": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Study_Hours": [2, 5, 3, 8, 6],
        "Marks": [50, 80, 60, 90, 85]
    }

    df = pd.DataFrame(data)

    # Step 2: Show the dataset
    print("=== Dataset ===")
    print(df)

    # Step 3: Identify Features & Labels
    print("\n=== Features & Labels ===")
    features = df["Study_Hours"]
    labels = df["Marks"]
    print(f"Features (Study Hours):\n{features}")
    print(f"\nLabels (Marks):\n{labels}")

    # Step 4: Predict relationship (simple observation)
    print("\n=== Predicted Relationship ===")
    print("Observation: More study hours generally lead to higher marks.")
    print("This shows a positive correlation between study hours and marks.\n")

if __name__ == "__main__":
    main()