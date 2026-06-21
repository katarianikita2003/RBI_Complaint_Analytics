import pandas as pd

df = pd.read_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\banking_complaints.csv"
)

# Convert date
df["Date received"] = pd.to_datetime(
    df["Date received"]
)

# Month
df["Complaint_Month"] = (
    df["Date received"]
    .dt.to_period("M")
    .astype(str)
)

# Year
df["Complaint_Year"] = (
    df["Date received"]
    .dt.year
)

# Timely Response Flag
df["Timely_Response_Flag"] = (
    df["Timely response?"]
    .map({
        "Yes":1,
        "No":0
    })
)

# Simplified Resolution Status
df["Resolution_Status"] = (
    df["Company response to consumer"]
)

# Rename columns
df = df.rename(columns={
    "Product":"Complaint_Category",
    "Company":"Bank_Company",
    "State":"State"
})

# Keep useful columns
final_df = df[
    [
        "Complaint ID",
        "Date received",
        "Complaint_Month",
        "Complaint_Year",
        "Complaint_Category",
        "Issue",
        "Bank_Company",
        "State",
        "Submitted via",
        "Resolution_Status",
        "Timely_Response_Flag"
    ]
]

final_df.to_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\final_dashboard_dataset.csv",
    index=False
)

print(final_df.shape)

print("\nColumns:")
print(final_df.columns.tolist())

print("\nSample:")
print(final_df.head())