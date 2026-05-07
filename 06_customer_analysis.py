import duckdb

query = """
SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    ROUND(SUM(Quantity * CAST(UnitPrice AS DOUBLE)), 2) AS customer_value
FROM read_csv_auto('online_retail.csv')
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY customer_value DESC
LIMIT 10;
"""

result = duckdb.sql(query).df()

print(result)