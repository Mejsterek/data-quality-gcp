import pandas as pd
from app.validator import validate


def test_validate():
    df = pd.DataFrame({
        "id": [1, 2, 2],
        "name": ["Jan", None, "Anna"],
        "email": ["jan@test.pl", "bad-email", "anna@test.pl"],
        "age": [25, 150, 30]
    })

    report = validate(df)

    assert report["duplicate_ids"] == 1
    assert report["missing"]["name"] == 1
    assert report["invalid_emails"] == 1
    assert report["invalid_ages"] == 1