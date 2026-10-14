
import pandas as pd
import sqlite3
from pathlib import Path

# Locate project folder
project = Path(__file__).resolve().parent.parent

# Read cleaned dataset
csv_path = project / "02_Cleaned_Data" / "Online_Retail_Python_Cleaned.csv"
df = pd.read_csv(csv_path)

# Create SQLite database
db_path = project / "04_SQL" / "ecommerce.db"
conn = sqlite3.connect(db_path)

# Import data into SQL table
df.to_sql("retail_sales", conn, if_exists="replace", index=False)

print("Database created successfully!")
print("Total rows imported:", len(df))
print("Columns:", df.columns.tolist())

conn.close()
