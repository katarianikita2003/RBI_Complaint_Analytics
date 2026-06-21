import pandas as pd

df = pd.read_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\final_dashboard_dataset.csv"
)

# -----------------------
# Monthly Trend
# -----------------------
monthly = (
    df.groupby("Complaint_Month")
      .size()
      .reset_index(name="Complaint_Count")
      .sort_values("Complaint_Month")
)

monthly.to_csv(
    r"D:\RBI_Complaint_Analytics\reports\monthly_trend.csv",
    index=False
)

# -----------------------
# Product Distribution
# -----------------------
products = (
    df.groupby("Complaint_Category")
      .size()
      .reset_index(name="Complaint_Count")
      .sort_values(
          "Complaint_Count",
          ascending=False
      )
)

products.to_csv(
    r"D:\RBI_Complaint_Analytics\reports\product_distribution.csv",
    index=False
)

# -----------------------
# State Distribution
# -----------------------
states = (
    df.groupby("State")
      .size()
      .reset_index(name="Complaint_Count")
      .sort_values(
          "Complaint_Count",
          ascending=False
      )
)

states.to_csv(
    r"D:\RBI_Complaint_Analytics\reports\state_distribution.csv",
    index=False
)

# -----------------------
# Company Distribution
# -----------------------
companies = (
    df.groupby("Company")
      .size()
      .reset_index(name="Complaint_Count")
      .sort_values(
          "Complaint_Count",
          ascending=False
      )
)

companies.to_csv(
    r"D:\RBI_Complaint_Analytics\reports\company_distribution.csv",
    index=False
)

# -----------------------
# Timely Response Rate
# -----------------------
response_rate = (
    df["Timely_Response_Flag"]
      .mean() * 100
)

print("\nTotal Complaints:", len(df))
print("\nTimely Response Rate:", round(response_rate, 2), "%")

print("\nTop 10 Products:")
print(products.head(10))

print("\nTop 10 States:")
print(states.head(10))

print("\nTop 10 Companies:")
print(companies.head(10))