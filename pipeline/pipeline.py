import sys

import pandas as pd

print('arguments', sys.argv)

month = int(sys.argv[1])
# date = int(sys.argv[2])
# filename = sys.argv[0]

df = pd.DataFrame({"day":[1,2], "num_passengers":[3,4]})
df['month'] = month

print(df.head())

df.to_parquet(f"pipeline_output_month={month}.parquet")

print(f"hello pipeline, month={month}")