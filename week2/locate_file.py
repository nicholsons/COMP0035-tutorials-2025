from pathlib import Path
import csv
import pandas as pd

df = pd.read_csv("../src/activities/data/paralympics_raw.csv")
# print(df.head())
# print(df.describe)
# print(df.shape)
df_new = df.loc[df['year'] == 2000]
print(df_new)