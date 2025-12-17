import pandas as pd

df = pd.read_csv('master_data_soda.csv')

chunk_size = 10000

for chunk in pd.read_csv('master_data_soda.csv', chunksize=chunk_size):
    print(f"Processing chunk of size {len(chunk)}")
    break # Just showing the firs chunk for now

# Quick Overview
print(df.info())

# 2. Check for Nulls (Missing Data)
# This mimics "Ensuring compliance with KBIs" (Key Business Indicators)
missing_data = df.isnull().sum()
print("\n --- Missing Data Report --- ")
print(missing_data[missing_data > 0])