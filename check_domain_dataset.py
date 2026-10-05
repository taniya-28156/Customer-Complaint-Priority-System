import pandas as pd

df = pd.read_csv("data/domain_complaints.csv")

print("===== DOMAIN DATASET INFO =====")

print("Total complaints:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate complaints:")
print(df["complaint"].duplicated().sum())

print("\nDomain distribution:")
print(df["domain"].value_counts())

print("\nUnique domains:")
print(df["domain"].unique())