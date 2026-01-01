import sys
import pandas as pd


month = int(sys.argv[1])

df = pd.DataFrame({"days": [1, 2], "num_of_passengers": [3, 4]})
df["month"] = month

print(df.head())
df.to_parquet(f"output_month{month}.parquet")

print(f'Hello World, month={month}', type(month))