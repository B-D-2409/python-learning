import pandas as pd

df = pd.read_csv("master_data_soda.csv")
chunk_size = 10000
for chunk in pd.read_csv("master_data_soda.csv", chunksize=chunk_size):
    print(f"Processing chunk of size {len(chunk)}")



print(df.info)


missing_data = df.isnull().sum()
print("\n --- Missing Data Report ---")
print(missing_data[missing_data > 0])