import duckdb

query = """
SELECT
    strftime(strptime(InvoiceDate, '%m/%d/%Y %H:%M'), '%Y-%m') AS month,
    ROUND(SUM(Quantity * CAST(UnitPrice AS DOUBLE)), 2) AS revenue
FROM read_csv_auto('online_retail.csv')
GROUP BY month
ORDER BY month;
"""

result = duckdb.sql(query).df()

print(result)