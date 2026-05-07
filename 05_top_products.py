import duckdb

query = """
SELECT
    Description,
    SUM(Quantity) AS total_quantity,
    ROUND(SUM(Quantity * CAST(UnitPrice AS DOUBLE)), 2) AS revenue
FROM read_csv_auto('online_retail.csv')
WHERE Description IS NOT NULL
GROUP BY Description
ORDER BY revenue DESC
LIMIT 10;
"""

result = duckdb.sql(query).df()

print(result)