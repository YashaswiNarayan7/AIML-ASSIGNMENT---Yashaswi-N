# Assignment: Data Doctor
# Date: 26/02/2026
# Name: Yashaswi N

import pandas as pd

def main():
    print("=== Data Doctor: Cleaning Business Dataset ===\n")
    input("Press Enter to start...")  

 
    dataset_file = "8Choco.csv"
    try:
        df = pd.read_csv(dataset_file)
    except FileNotFoundError:
        print(f"File '{dataset_file}' not found! Make sure it exists in the same folder.")
        input("\nPress Enter to exit...")
        return

    print("\n=== Original Data (Top 5 Rows) ===")
    print(df.head())

    # --------------------------
    # 1. Handle missing values
    # --------------------------
    df.fillna({
        'Customers': 0,
        'Affiliates': 0,
        'Employees': 0,
        'RevenuePercentage': 0.0,
        'Chocolate': 'Unknown'
    }, inplace=True)

    # --------------------------
    # 2. Remove duplicate rows
    # --------------------------
    df.drop_duplicates(inplace=True)

    # --------------------------
    # 3. Standardize text columns
    # --------------------------
    df['Chocolate'] = df['Chocolate'].str.title().str.strip()

    print("\n=== Cleaned Data (Top 5 Rows) ===")
    print(df.head())

    # --------------------------
    # 4. Explanation
    # --------------------------
    print("\n=== Why Data Cleaning Matters ===")
    explanations = [
        "1. Filling missing values ensures accurate calculations and analysis.",
        "2. Removing duplicates prevents overcounting and misleading statistics.",
        "3. Standardizing text ensures consistency for filtering and grouping.",
        "4. Clean data improves reliability for reporting and business decisions.",
        "5. Data hygiene is essential for professional and reproducible analytics."
    ]
    for explanation in explanations:
        print(explanation)

    input("\nPress Enter to exit...")  

if __name__ == "__main__":
    main()