import pandas as pd

df = pd.read_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\complaints_sample.csv"
)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nProducts:")
print(df["Product"].value_counts().head(20))

print("\nStates:")
print(df["State"].value_counts().head(20))

print("\nResponse Types:")
print(df["Company response to consumer"].value_counts().head(10))
