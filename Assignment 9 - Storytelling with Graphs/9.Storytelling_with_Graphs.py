# Assignment: Storytelling with Graphs
# Date: 28/02/2026
# Name: Yashaswi N

import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("=== Storytelling with Graphs ===\n")
    input("Press Enter to start...") 

    # Load dataset
    dataset_file = "8Choco.csv"
    try:
        df = pd.read_csv(dataset_file)
    except FileNotFoundError:
        print(f"File '{dataset_file}' not found! Make sure it exists in the same folder.")
        input("\nPress Enter to exit...")
        return

    # --------------------------
    # 1. Bar chart: Chocolate vs Customers
    # --------------------------
    plt.figure(figsize=(8,5))
    plt.bar(df['Chocolate'].str.title(), df['Customers'])
    plt.title("Customers per Chocolate")
    plt.xlabel("Chocolate")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # --------------------------
    # 2. Pie chart: Revenue Percentage
    # --------------------------
    plt.figure(figsize=(6,6))
    plt.pie(df['RevenuePercentage'], labels=df['Chocolate'].str.title(), autopct="%1.1f%%")
    plt.title("Revenue Percentage per Chocolate")
    plt.tight_layout()
    plt.show()

    # --------------------------
    # 3. Histogram: Employees
    # --------------------------
    plt.figure(figsize=(8,5))
    plt.hist(df['Employees'], bins=5, color='skyblue', edgecolor='black')
    plt.title("Distribution of Employees")
    plt.xlabel("Number of Employees")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # --------------------------
    # 4. Data Story (VTU-friendly)
    # --------------------------
    print("\n=== Data Story ===")
    print("1. Chocolate products with higher customers generally contribute more to revenue.")
    print("2. Revenue distribution shows some chocolates dominate the business share.")
    print("3. Employee distribution is relatively balanced across products, with some outliers.")
    print("4. Bar chart, pie chart, and histogram together reveal key business trends and opportunities.")
    print("5. Visualizations simplify analysis for decision-making and trend observation.\n")

    input("Press Enter to exit...")  

if __name__ == "__main__":
    main()