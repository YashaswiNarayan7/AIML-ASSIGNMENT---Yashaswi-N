import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("----- SALES ANALYSIS REPORT -----\n")

# 1. Create Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [20000, 25000, 30000, 28000, 35000, 40000],
    "Marketing_Spend": [5000, 7000, 8000, 7500, 9000, 10000],
    "Profit": [15000, 18000, 22000, 20500, 26000, 30000]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# 2. Line Plot (Revenue Trend)
plt.figure()
plt.plot(df["Month"], df["Revenue"], marker='o')
plt.title("Revenue Trend Over Months")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# 3. Scatter Plot (Marketing vs Profit)
plt.figure()
plt.scatter(df["Marketing_Spend"], df["Profit"])
plt.title("Marketing Spend vs Profit")
plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.show()

# 4. Correlation Heatmap
plt.figure()
sns.heatmap(df[["Revenue", "Marketing_Spend", "Profit"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 5. Insights
print("\n----- INSIGHTS -----")
print("1. Revenue shows an overall increasing trend over months.")
print("2. Higher marketing spend generally leads to higher profit.")
print("3. Strong positive correlation between Revenue and Profit.")
print("4. Marketing spend and Profit are positively correlated.")