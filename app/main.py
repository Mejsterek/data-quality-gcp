import pandas as pd

df = pd.read_csv("data/sample.csv")

print(df.head())
print(f"Liczba rekordów: {len(df)}")