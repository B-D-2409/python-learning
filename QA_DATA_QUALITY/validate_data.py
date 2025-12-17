import pandas as pd

df = pd.read_csv("master_data_soda.csv")

# 1. Check for Duplicates (Primary Key Constraint)
duplicates = df[df.duplicated(subset=["Material_ID"], keep=False)]
print(f"\nDuplicate IDs found: {len(duplicates)}")

# 2. Logic Check: Negative Prices
negative_prices = df[df["Unit_Price"] < 0]
print(f"Invalid Prices found: {len(negative_prices)}")


negative_stock = df[df["Stock_Quantity"] < 0]
print(f"Invalid Stock Levels found: {len(negative_stock)}")