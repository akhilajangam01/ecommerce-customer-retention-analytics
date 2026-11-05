
import pandas as pd
from pathlib import Path

# Locate the cleaned dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "02_Cleaned_Data" / "Online_Retail_Python_Cleaned.csv"

# Load the dataset
df = pd.read_csv(file_path, low_memory=False)

print("===== AUTOMATED DATA VALIDATION =====")
print("Total rows:", len(df))
print("\nDataset columns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nExact duplicate rows:", df.duplicated().sum())

# Revenue discrepancy validation
print("\n===== REVENUE VALIDATION =====")

# Convert columns to numeric
for col in ["Quantity", "UnitPrice", "Revenue"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Calculate expected revenue
df["ExpectedRevenue"] = df["Quantity"] * df["UnitPrice"]

# Identify revenue discrepancies
df["RevenueDifference"] = (
    df["Revenue"] - df["ExpectedRevenue"]
).round(2)

revenue_errors = df[
    df[["Quantity", "UnitPrice", "Revenue"]].isna().any(axis=1)
    | (df["RevenueDifference"].abs() > 0.01)
]

print("Total revenue discrepancies:", len(revenue_errors))

print("\nSample revenue discrepancies:")
print(revenue_errors.head(10))

# Duplicate order validation
print("\n===== DUPLICATE ORDER VALIDATION =====")

# Identify potentially duplicated order lines
duplicate_columns = [
    "InvoiceNo",
    "StockCode",
    "Quantity",
    "UnitPrice"
]

duplicate_orders = df[
    df.duplicated(subset=duplicate_columns, keep=False)
].copy()

print("Potential duplicate order lines:", len(duplicate_orders))

print("\nSample duplicate order lines:")
print(duplicate_orders.head(10))

# Generate automated validation reports
print("\n===== GENERATING VALIDATION REPORTS =====")

# Create output folder
output_folder = project_folder / "04_Validation_Reports"
output_folder.mkdir(parents=True, exist_ok=True)

# Save revenue discrepancies
revenue_errors.to_csv(
    output_folder / "revenue_discrepancies.csv",
    index=False
)

# Save potential duplicate orders
duplicate_orders.to_csv(
    output_folder / "duplicate_orders.csv",
    index=False
)

# Create validation summary
validation_summary = pd.DataFrame({
    "Validation_Check": [
        "Total Records",
        "Revenue Discrepancies",
        "Potential Duplicate Order Lines",
        "Exact Duplicate Rows"
    ],
    "Count": [
        len(df),
        len(revenue_errors),
        len(duplicate_orders),
        df.duplicated(
            subset=df.columns.drop(
                ["ExpectedRevenue", "RevenueDifference"]
            ).tolist()
        ).sum()
    ]
})

validation_summary.to_csv(
    output_folder / "validation_summary.csv",
    index=False
)

print(validation_summary)
print("\nValidation reports saved successfully!")
