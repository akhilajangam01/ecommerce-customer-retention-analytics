
import sqlite3
from pathlib import Path

folder = Path(__file__).resolve().parent

sql_file = folder / "validate_dates.sql"
query = sql_file.read_text(encoding="utf-8").strip()

if not query:
    raise ValueError("SQL file is empty. Paste and save the query.")

conn = sqlite3.connect(folder / "ecommerce.db")

try:
    cursor = conn.execute(query)

    if cursor.description is None:
        print("SQL executed but returned no result table.")
    else:
        print("\nAVERAGE BASKET SIZE")
        print("------------------------")

        columns = [col[0] for col in cursor.description]
        print(columns)

        for row in cursor.fetchall():
            print(row)

except sqlite3.Error as error:
    print("SQL Error:", error)

finally:
    conn.close()

