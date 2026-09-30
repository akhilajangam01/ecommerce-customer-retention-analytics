import pandas as pd

# Load the cleaned Excel data
file_path = "../02_Cleaned_Data/Online Retail.xlsx"
df = pd.read_excel(file_path)

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove rows with missing Description
df = df.dropna(subset=["Description"])

print("\nShape After Handling Missing Values:", df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum())
# Remove invalid transaction records
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove duplicate rows
df = df.drop_duplicates()

print("\n--- Final Validation ---")
print("Final Shape:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())
print("Missing CustomerID:", df["CustomerID"].isnull().sum())
print("Negative/Zero Quantity:", (df["Quantity"] <= 0).sum())
print("Negative/Zero UnitPrice:", (df["UnitPrice"] <= 0).sum())
# Export final cleaned dataset
output_path = "../02_Cleaned_Data/Online_Retail_Python_Cleaned.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset successfully saved to:")
print(output_path)