import re
import pandas as pd

EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validate(df):
    return {
        "missing": df.isnull().sum().to_dict(),
        "duplicate_ids": int(df["id"].duplicated().sum()),
        "invalid_emails": int(
            (~df["email"].fillna("").str.match(EMAIL_PATTERN)).sum()
        ),
        "invalid_ages": int(
            ((df["age"] < 0) | (df["age"] > 120)).sum()
        ),
    }