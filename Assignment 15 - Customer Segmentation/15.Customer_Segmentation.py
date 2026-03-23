# Assignment: Customer Segmentation
# Date: 11/03/2026
# Name: Yashaswi N

import pandas as pd
from sklearn.cluster import KMeans

def main():
    print("=== Customer Segmentation using K-Means ===\n")

    # Step 1: Create a small mall dataset
    data = {
        "CustomerID": [1, 2, 3, 4, 5, 6],
        "Age": [25, 45, 30, 35, 50, 23],
        "Annual_Income_k": [40, 80, 60, 70, 90, 35],
        "Spending_Score": [60, 40, 50, 65, 30, 70]
    }
    df = pd.DataFrame(data)

    print("=== Dataset ===")
    print(df)

    # Step 2: Select features for clustering
    X = df[["Annual_Income_k", "Spending_Score"]]

    # Step 3: Train K-Means model
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    # Step 4: Print cluster assignments
    print("\n=== Cluster Assignments ===")
    print(df[["CustomerID", "Annual_Income_k", "Spending_Score", "Cluster"]])

    # Step 5: Describe customer groups
    cluster_summary = df.groupby("Cluster")[["Annual_Income_k", "Spending_Score"]].mean()
    print("\n=== Cluster Summary (Average values) ===")
    print(cluster_summary)

    print("\nObservation:")
    print("Cluster 0: Medium income, medium spending.")
    print("Cluster 1: High income, low spending.")
    print("Cluster 2: Low income, high spending.\n")

    input("Press Enter to exit...")  # Keep terminal output visible

if __name__ == "__main__":
    main()