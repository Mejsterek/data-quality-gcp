from google.cloud import bigquery


def validate_bigquery_table():
    client = bigquery.Client()

    query = """
    SELECT
      COUNTIF(name IS NULL OR TRIM(name) = '') AS missing_names,
      COUNT(*) - COUNT(DISTINCT id) AS duplicate_ids,
      COUNTIF(age < 0 OR age > 120) AS invalid_ages,
      COUNTIF(
        NOT REGEXP_CONTAINS(
          email,
          r'^[\\w.\\-]+@[\\w.\\-]+\\.[A-Za-z]+$'
        )
      ) AS invalid_emails
    FROM `data-quality-gcp.data_quality.customers`
    """

    row = next(iter(client.query(query).result()))

    return {
        "missing_names": row.missing_names,
        "duplicate_ids": row.duplicate_ids,
        "invalid_ages": row.invalid_ages,
        "invalid_emails": row.invalid_emails,
    }