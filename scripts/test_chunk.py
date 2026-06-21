import pandas as pd

print("Script started")

file = r"D:\RBI_Complaint_Analytics\data\raw\complaints.csv"

try:
    for chunk in pd.read_csv(
        file,
        chunksize=10000,
        low_memory=False
    ):
        print("Chunk loaded")
        print(chunk.shape)

        print(chunk["Product"].value_counts().head())

        break

except Exception as e:
    print("ERROR:")
    print(e)

print("Script finished")