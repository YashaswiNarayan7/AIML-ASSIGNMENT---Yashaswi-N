# Assignment: Dataset Detective
# Date: 24/02/2026
# Name: Yashaswi N

import pandas as pd

def main():
    print("=== Dataset Detective ===\n")
    input("Press Enter to start...") 

    dataset_file = "7IPL.csv"
    try:
        df = pd.read_csv(dataset_file)
    except FileNotFoundError:
        print(f"File '{dataset_file}' not found! Make sure it exists in the same folder.")
        input("\nPress Enter to exit...")
        return

    print("\n=== Top 5 Rows ===")
    print(df.head())

  
    max_col = df.max(numeric_only=True).idxmax()
    max_val = df[max_col].max()
    print(f"\nColumn with highest value: '{max_col}' → {max_val}")

   
    print("\n=== Missing Values Count ===")
    print(df.isnull().sum())

   
    print("\n=== Insights ===")
    insights = [
        "1. Virat Kohli scored the highest runs in this dataset.",
        "2. Jasprit Bumrah took the most wickets.",
        "3. Hardik Pandya has both runs and wickets contributing significantly.",
        "4. Most players played between 12–16 matches.",
        "5. DC and CSK have strong batting performance in terms of runs."
    ]
    for insight in insights:
        print(insight)

    input("\nPress Enter to exit...") 

if __name__ == "__main__":
    main()