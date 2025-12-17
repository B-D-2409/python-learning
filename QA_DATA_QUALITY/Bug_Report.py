import pandas as pd

df = pd.read_csv("master_data_soda.csv")

# Create a mask for all bad data
bad_data_mask = (
    (df["Unit_Price"] < 0) |
    (df["Stock_Quantity"] < 0) |
    (df.duplicated(subset=["Material_ID"], keep=False))
)

# Create bug report
bug_report = df[bad_data_mask]

# Export to Excel for the Business Team
bug_report.to_excel("QA_Bug_Report.xlsx", index=False)

print(f"\nBug report generated with {len(bug_report)} issues.")
