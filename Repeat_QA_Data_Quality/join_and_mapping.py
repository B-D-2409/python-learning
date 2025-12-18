import pandas as pd


df = pd.read_csv("master_data_soda.csv")

vendor_data = pd.DataFrame({
    "Vendor_Code": ["V001","V002","V003"],
    "Vendor_Name": ["Coca_Cola Hellenic", "Glass Bottle Co.", "Sugar Refinery "]
})

df_enriched = pd.merge(df,vendor_data, on="Vendor_Code", how= "left")

failed_joins = df_enriched[df_enriched["Vendor_Name"].isnull()]
print(f"\nRows with unknown vendors (integration Error: {len(failed_joins)})")


category_map = {
    "Beverage": "BEV_01",
    "Snacks": "SNK_01",
    "Alcohol": "ALC_01",
}

df["SAP_Category_Code"] = df["Category"].map(category_map)

print("Unknown Vendor Codes:")
print(failed_joins["Vendor_Code"].value_counts())