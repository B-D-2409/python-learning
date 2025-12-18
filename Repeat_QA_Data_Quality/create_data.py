import pandas as pd
import numpy as np
from datetime import timedelta,datetime

num_rows = 50000
ids = range(1000,1000 + num_rows)
categories = ["Beverages", "Snacks", "Alcohol", "Merchandise", "Raw Material"]
vendors  = ["V001","V002","V003","V004","V005"]

data = {
    "Material_ID": ids,
    "Material_Description": [f"Product_{i}" for i in ids],
    "Category": np.random.choice(categories,num_rows),
    "Unit_Price": np.round(np.random.uniform(10,500,num_rows), 2),
    "Stock_Quantity": np.random.randint(-10,1000,num_rows),
    "Vendor_Code": np.random.choice(vendors,num_rows),
    "Last_Updated": [datetime.today() - timedelta(days=x) for x in range(num_rows)],
    "Active_Status": np.random.choice(["Y","N", None], num_rows)
}

df = pd.DataFrame(data)

df.loc[100:105, "Material_ID"]  = 1000

df.loc[500:520, "Unit_Price"] = -50.00

df.loc[1000:1100, 'Vendor_Code'] = np.nan