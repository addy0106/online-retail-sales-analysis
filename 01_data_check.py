import duckdb

query = """
SELECT *
FROM read_csv_auto('online_retail.csv')
LIMIT 10;
"""

result = duckdb.sql(query).df()

print(result)