import pandas as pd
from validator import validate

df = pd.read_csv("data/sample.csv")

report = validate(df)

print("=== DATA QUALITY REPORT ===\n")

for key, value in report.items():
    print(f"{key}: {value}")