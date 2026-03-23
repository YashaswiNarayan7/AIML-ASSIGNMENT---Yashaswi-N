# Assignment: House Price Predictor
# Date: 09/03/2026
# Name: Yashaswi N

import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    print("=== House Price Predictor ===\n")

    # Step 1: Create dataset (House Size vs Price)
    data = {
        "Size_sqft": [500, 700, 1000, 1200, 1500],
        "Price_lakh": [30, 45, 60, 70, 90]
    }
    df = pd.DataFrame(data)

    # Step 2: Separate features and labels
    X = df[["Size_sqft"]]  # Feature
    y = df["Price_lakh"]   # Label

    # Step 3: Train Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Step 4: Display dataset and model info
    print("=== Dataset ===")
    print(df)
    print("\nModel Coefficient:", model.coef_[0])
    print("Model Intercept:", model.intercept_)

    # Step 5: Predict prices for new inputs
    new_sizes = pd.DataFrame({"Size_sqft": [800, 1100, 1600]})
    predicted_prices = model.predict(new_sizes)

    print("\n=== Predictions for New House Sizes ===")
    for size, price in zip(new_sizes["Size_sqft"], predicted_prices):
        print(f"Size: {size} sqft --> Predicted Price: {price:.2f} lakh")

    # Keep terminal open until user checks output
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()