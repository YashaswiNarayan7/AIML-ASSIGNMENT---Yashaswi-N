import pandas as pd

print("----- STUDENT DATA ANALYSIS -----\n")

# 1. Read CSV file
try:
    df = pd.read_csv("student.csv")
    print("Dataset Loaded Successfully!\n")
except:
    print("Error: File not found. Make sure student.csv is in same folder.")
    exit()

print("Original Data:\n", df)

# 2. Add Total column
df["Total"] = df["Math"] + df["Science"]

# 3. Add Average column
df["Average"] = df["Total"] / 2

print("\nData with Total & Average:\n", df)

# 4. Top 3 students based on Total
top3 = df.sort_values(by="Total", ascending=False).head(3)
print("\nTop 3 Students:\n", top3)

# 5. Department-wise average marks
dept_avg = df.groupby("Department")[["Math", "Science", "Total", "Average"]].mean()
print("\nDepartment-wise Average:\n", dept_avg)

# 6. Students scoring above 75 in all subjects
above_75 = df[(df["Math"] > 75) & (df["Science"] > 75)]
print("\nStudents scoring above 75 in all subjects:\n", above_75)

# 7. Missing values check
print("\nMissing Values:\n", df.isnull().sum())

# Bonus message
if df.isnull().values.any():
    print("\nMissing values found in dataset")
else:
    print("\nNo missing values in dataset")