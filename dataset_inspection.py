import pandas as pd
import matplotlib.pyplot as plt

file_path = "../01_Raw_Data/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist()) 
# Dataset information
print("\n--- DATASET INFORMATION ---")
print(df.info())

# Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", df.duplicated().sum())

# Unique values
print("\n--- UNIQUE COUNTS ---")
print("Unique invoices:", df["InvoiceNo"].nunique())
print("Unique products:", df["StockCode"].nunique())
print("Unique customers:", df["CustomerID"].nunique())
print("Unique countries:", df["Country"].nunique())

# Date range
print("\n--- DATE RANGE ---")
print("Start Date:", df["InvoiceDate"].min())
print("End Date:", df["InvoiceDate"].max())

# Negative quantities
negative_quantity = (df["Quantity"] < 0).sum()
print("\nNegative Quantity Records:", negative_quantity)

# Zero or negative prices
invalid_price = (df["UnitPrice"] <= 0).sum()
print("Zero/Negative UnitPrice Records:", invalid_price)

# Cancelled invoices
cancelled = df["InvoiceNo"].astype(str).str.startswith("C").sum()
print("Cancelled Transaction Rows:", cancelled)