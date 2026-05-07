import duckdb
import matplotlib.pyplot as plt
import seaborn as sns

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

plt.figure(figsize=(12,6))

sns.barplot(
    data=result,
    x='Country',
    y='total_sales'
)

plt.title('Top 10 Countries by Revenue')
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('country_sales.png', dpi=300, bbox_inches='tight')