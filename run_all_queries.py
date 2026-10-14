
import sqlite3
from pathlib import Path

folder = Path(__file__).resolve().parent

queries = {
    "CUSTOMER REPURCHASE RATE": "customer_retention_analysis.sql",
    "CUSTOMER CHURN RATE": "customer_churn_analysis.sql",
    "AVERAGE BASKET SIZE": "average_basket_analysis.sql"
}

conn = sqlite3.connect(folder / "ecommerce.db")

try:
    for title, filename in queries.items():
        print("\n" + "=" * 50)
        print(title)
        print("=" * 50)

        sql = (folder / filename).read_text(
            encoding="utf-8"
        ).strip()

        if not sql:
            print("ERROR: SQL file is empty.")
            continue

        try:
            cursor = conn.execute(sql)

            if cursor.description is None:
                print("ERROR: Query did not return results.")
                continue

            columns = [col[0] for col in cursor.description]
            print("Columns:", columns)

            for row in cursor.fetchall():
                print("Results:", row)

        except sqlite3.Error as error:
            print("SQL Error:", error)

finally:
    conn.close()
