import pandas as pd

# Load dataset
df = pd.read_csv("../data/company_complaints.csv")

print("===== DATASET INFO =====")

# Total rows
print("Total complaints:", len(df))

# Columns
print("\nColumns:")
print(df.columns.tolist())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate complaints
print("\nDuplicate complaints:", df["complaint"].duplicated().sum())

# Category distribution
print("\nCategory distribution:")
print(df["category"].value_counts())

# Unique categories
print("\nUnique categories:")
print(df["category"].unique())
