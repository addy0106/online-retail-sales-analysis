import duckdb

query = """
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT CustomerID) AS unique_customers,
    COUNT(DISTINCT InvoiceNo) AS total_orders
FROM read_csv_auto('online_retail.csv');
"""

result = duckdb.sql(query).df()

print(result)