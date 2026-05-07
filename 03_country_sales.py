import duckdb

query = """
SELECT
    Country,
    ROUND(SUM(Quantity * CAST(UnitPrice AS DOUBLE)), 2) AS total_sales
FROM read_csv_auto('online_retail.csv')
GROUP BY Country
ORDER BY total_sales DESC
LIMIT 10;
"""

result = duckdb.sql(query).df()



print(result)



