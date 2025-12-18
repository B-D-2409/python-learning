import pandas as pd

df = pd.read_csv("master_data_soda.csv")

duplicates = df[df.duplicated(subset=["Material_ID"], keep=False)]
print(f"\nDuplicate IDs found: {len(duplicates)}")


negative_price = df[df["Unit_Price"] < 0 ]
print(f"Invalid Prices found: {len(negative_price)}")


negative_stock = df[df["Stock_Quantity"] < 0]
print(f"Invalid Stock Levels found: {len(negative_stock)}")