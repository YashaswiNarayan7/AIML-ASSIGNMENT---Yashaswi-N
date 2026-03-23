import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

print("----- LOAN APPROVAL PREDICTOR -----\n")

# 1. Create Dataset (inside file)
data = {
    "Income": [50000, 60000, 30000, 80000, 75000, 40000, 90000, 65000],
    "Credit_Score": [700, 750, 600, 800, 780, 650, 820, 720],
    "Age": [25, 35, 28, 45, 40, 30, 50, 38],
    "Loan_Amount": [200000, 250000, 150000, 300000, 280000, 180000, 350000, 260000],
    "Employment_Years": [2, 5, 3, 10, 8, 4, 12, 6],
    "Approved": [1, 1, 0, 1, 1, 0, 1, 1]   # Target column
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# 2. Split features and target
X = df.drop("Approved", axis=1)
y = df["Approved"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)

# 5. Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)

# 6. Compare Accuracy
print("\nDecision Tree Accuracy:", dt_accuracy)
print("Random Forest Accuracy:", rf_accuracy)

# 7. Feature Importance (Random Forest)
importance = rf_model.feature_importances_
features = X.columns

print("\nFeature Importance:")
for f, imp in zip(features, importance):
    print(f"{f}: {imp:.4f}")

# 8. Save Model using pickle
with open("loan_model.pkl", "wb") as file:
    pickle.dump(rf_model, file)

print("\nModel saved as loan_model.pkl")