import pandas as pd

df = pd.read_csv("master_data_soda.csv")

bad_data_mask = (
    (df["Unit_Price"] < 0) |
    (df["Stock_Qantity"] < 0) |
    (df.duplicated(subset=["Material_ID"], keep=False))
)



bug_report = df[bad_data_mask]

bug_report.to_excel("QA_Bug_Report.xlsx", index=False)

print(f"\nBug report generated with {len(bug_report)} issues.")