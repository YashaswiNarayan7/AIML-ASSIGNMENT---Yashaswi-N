import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("----- MALL CUSTOMER SEGMENTATION -----\n")

# 1. Create Dataset
data = {
    "Age": [19, 21, 20, 23, 31, 22, 35, 40, 60, 45],
    "Annual_Income": [15000, 16000, 17000, 18000, 50000, 55000, 60000, 65000, 70000, 75000],
    "Spending_Score": [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# 2. Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(df)

# 3. Plot Clusters
plt.figure()
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

# Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 1], centroids[:, 2], marker='X', s=200)

plt.show()

# 4. Display Centroids
print("\nCluster Centroids:\n", centroids)