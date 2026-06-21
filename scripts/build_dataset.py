import pandas as pd

source_file = r"D:\RBI_Complaint_Analytics\data\raw\complaints.csv"

products_needed = [
    "Checking or savings account",
    "Credit card",
    "Mortgage",
    "Student loan",
    "Vehicle loan or lease",
    "Money transfer, virtual currency, or money service"
]

result = []

chunk_no = 0

for chunk in pd.read_csv(
        source_file,
        chunksize=5000,
        low_memory=False):

    chunk_no += 1

    filtered = chunk[
        chunk["Product"].isin(products_needed)
    ]

    result.append(filtered)

    current_rows = sum(len(x) for x in result)

    print(
        f"Chunk {chunk_no} | Rows collected: {current_rows}"
    )

    if current_rows >= 50000:
        break

df = pd.concat(result)

df = df.head(50000)

df.to_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\banking_complaints.csv",
    index=False
)

print("\nDone")
print("Final Shape:", df.shape)
print(df["Product"].value_counts())