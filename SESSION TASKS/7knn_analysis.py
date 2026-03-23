import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("----- KNN CLASSIFIER ANALYSIS -----\n")

# 1. Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Try K values (1 to 15)
k_values = range(1, 16)
accuracy_euclidean = []
accuracy_manhattan = []

# 4. Train models for different K
for k in k_values:
    # Euclidean
    model_e = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    model_e.fit(X_train, y_train)
    y_pred_e = model_e.predict(X_test)
    accuracy_euclidean.append(accuracy_score(y_test, y_pred_e))
    
    # Manhattan
    model_m = KNeighborsClassifier(n_neighbors=k, metric='manhattan')
    model_m.fit(X_train, y_train)
    y_pred_m = model_m.predict(X_test)
    accuracy_manhattan.append(accuracy_score(y_test, y_pred_m))

# 5. Plot Accuracy vs K
plt.figure()
plt.plot(k_values, accuracy_euclidean, marker='o', label="Euclidean")
plt.plot(k_values, accuracy_manhattan, marker='s', label="Manhattan")
plt.title("Accuracy vs K")
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# 6. Show results
print("K values:", list(k_values))
print("Euclidean Accuracy:", accuracy_euclidean)
print("Manhattan Accuracy:", accuracy_manhattan)

# 7. Best K
best_k_e = k_values[np.argmax(accuracy_euclidean)]
best_k_m = k_values[np.argmax(accuracy_manhattan)]

print("\nBest K (Euclidean):", best_k_e)
print("Best Accuracy (Euclidean):", max(accuracy_euclidean))

print("\nBest K (Manhattan):", best_k_m)
print("Best Accuracy (Manhattan):", max(accuracy_manhattan))