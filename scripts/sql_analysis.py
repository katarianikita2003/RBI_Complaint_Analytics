import pandas as pd
import sqlite3

df = pd.read_csv(
    r"D:\RBI_Complaint_Analytics\data\clean\final_dashboard_dataset.csv"
)

conn = sqlite3.connect("complaints.db")

df.to_sql(
    "complaints",
    conn,
    if_exists="replace",
    index=False
)

query = """
SELECT Company,
       COUNT(*) AS complaints
FROM complaints
GROUP BY Company
ORDER BY complaints DESC
LIMIT 10
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()