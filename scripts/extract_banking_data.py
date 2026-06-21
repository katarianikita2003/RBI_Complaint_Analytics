import pandas as pd

file = r"D:\RBI_Complaint_Analytics\data\raw\complaints.csv"

products_needed = [
    "Checking or savings account",
    "Credit card",
    "Mortgage",
    "Money transfer, virtual currency, or money service",
    "Student loan",
    "Vehicle loan or lease"
]

chunks = []

for chunk in pd.read_csv(
        file,
        chunksize=50000,
        low_memory=False):

    filtered = chunk[
        chunk["Product"].isin(products_needed)
    ]

    chunks.append(filtered)

    if sum(len(x) for x in chunks) > 100000:
        break

df = pd.concat(chunks)

df = df.sample(
    min(50000, len(df)),
    random_state=42
)

df.to_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\banking_complaints.csv",
    index=False
)

print("Rows:", len(df))
print(df["Product"].value_counts())