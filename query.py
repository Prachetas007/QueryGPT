# bq_query.py
from google.cloud import bigquery

def run_query(sql: str):
    """Run a SQL query on BigQuery and return results as a list of dicts."""
    client = bigquery.Client()
    query_job = client.query(sql)
    results = query_job.result()
    rows = [dict(row) for row in results]
    return rows
