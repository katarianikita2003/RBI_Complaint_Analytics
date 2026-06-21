import pandas as pd

df = pd.read_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\banking_complaints.csv"
)

# Date conversion
df["Date received"] = pd.to_datetime(
    df["Date received"],
    errors="coerce",
    utc=True
)

print("Missing dates:",
      df["Date received"].isna().sum())

# Year
df["Complaint_Year"] = (
    df["Date received"].dt.year
)

# Month
df["Complaint_Month"] = (
    df["Date received"]
    .dt.strftime("%Y-%m")
)

# Timely Response Flag
df["Timely_Response_Flag"] = (
    df["Timely response?"]
    .map({"Yes": 1, "No": 0})
)

# Select relevant columns
dashboard_df = df[
    [
        "Complaint ID",
        "Date received",
        "Complaint_Year",
        "Complaint_Month",
        "Product",
        "Issue",
        "Company",
        "State",
        "Submitted via",
        "Company response to consumer",
        "Timely_Response_Flag"
    ]
]

# Rename columns
dashboard_df.columns = [
    "Complaint_ID",
    "Complaint_Date",
    "Complaint_Year",
    "Complaint_Month",
    "Complaint_Category",
    "Issue",
    "Company",
    "State",
    "Submission_Channel",
    "Resolution_Status",
    "Timely_Response_Flag"
]

dashboard_df.to_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\final_dashboard_dataset.csv",
    index=False
)

print("Shape:", dashboard_df.shape)
print("\nColumns:")
print(dashboard_df.columns.tolist())

print("\nYears:")
print(dashboard_df["Complaint_Year"].value_counts().sort_index())