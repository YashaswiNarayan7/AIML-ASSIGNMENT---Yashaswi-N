import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

print("----- DATA CLEANING & LINEAR REGRESSION -----\n")

# 1. Create dataset (inside Python)
data = {
    "Age": [25, 30, np.nan, 28, 35, np.nan, 40],
    "Salary": [50000, np.nan, 45000, 52000, np.nan, 48000, 60000],
    "City": ["hyderabad", "HYDERABAD", "Hyderabad", "hyderabad", "HYDERABAD", "Hyderabad", "hyderabad"],
    "Experience": [2, 5, 3, 4, 7, 3, 10]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# 2. Handle missing values (fill with mean)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# 3. Standardize city names
df["City"] = df["City"].str.lower().str.capitalize()

# 4. Apply Min-Max Scaling
scaler = MinMaxScaler()
df[["Age", "Salary"]] = scaler.fit_transform(df[["Age", "Salary"]])

# 5. Linear Regression (Predict Salary based on Age & Experience)
X = df[["Age", "Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

print("\nModel Trained Successfully!")

# 6. Show final cleaned data
print("\nFinal Cleaned Data:\n", df)

# Optional: show predictions
df["Predicted_Salary"] = model.predict(X)

print("\nData with Predictions:\n", df)