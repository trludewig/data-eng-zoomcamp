import sys
import pandas as pd

print("Arguments: ", sys.argv)
month = int(sys.argv[1])
print(f"Month: {month}")

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df.head())

df.to_parquet(f"output_month_{month}.parquet")