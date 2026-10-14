
import pandas as pd
from pathlib import Path

# Locate project folder
project = Path(__file__).resolve().parent.parent

# Load cleaned retail dataset
file_path = (
    project / "02_Cleaned_Data"
    / "Online_Retail_Python_Cleaned.csv"
)

df = pd.read_csv(file_path)

# Convert transaction dates
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)

# Remove invalid transactions
df = df.dropna(subset=["CustomerID", "InvoiceDate"])

df = df[
    (df["Quantity"] > 0)
    & (df["UnitPrice"] > 0)
    & (~df["InvoiceNo"].astype(str).str.startswith("C"))
].copy()

# Calculate sales revenue
df["TotalAmount"] = (
    df["Quantity"] * df["UnitPrice"]
)

# Reference date: one day after last transaction
reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Calculate RFM metrics
rfm = df.groupby("CustomerID").agg(
    Recency=(
        "InvoiceDate",
        lambda x: (reference_date - x.max()).days
    ),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("TotalAmount", "sum")
).reset_index()

print("\nRFM ANALYSIS COMPLETED")
print("----------------------")
print("Total Customers:", len(rfm))
print(rfm.head())

# Save initial RFM results
output_folder = project / "03_Python"
rfm.to_csv(
    output_folder / "rfm_customer_metrics.csv",
    index=False
)

print("\nRFM metrics saved successfully!")

# STEP 4: RFM Scoring

# Assign scores from 1 to 5 using percentile ranks.
# Recency: lower number of days = higher score.
# Frequency and Monetary: higher values = higher scores.

rfm["R_Score"] = (
    6 - pd.cut(
        rfm["Recency"].rank(method="first"),
        bins=5,
        labels=[1, 2, 3, 4, 5]
    ).astype(int)
)

rfm["F_Score"] = pd.cut(
    rfm["Frequency"].rank(method="first"),
    bins=5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.cut(
    rfm["Monetary"].rank(method="first"),
    bins=5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

# Calculate total RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"]
    + rfm["F_Score"]
    + rfm["M_Score"]
)

# Assign customer segments
def assign_segment(row):
    if (
        row["R_Score"] >= 4
        and row["F_Score"] >= 4
        and row["M_Score"] >= 4
    ):
        return "VIP Customers"
    elif row["RFM_Score"] >= 10:
        return "Loyal Customers"
    elif row["R_Score"] <= 2:
        return "At Risk"
    else:
        return "Regular Customers"

rfm["CustomerSegment"] = rfm.apply(
    assign_segment, axis=1
)

# Save segmentation results
rfm.to_csv(
    output_folder / "rfm_customer_segments.csv",
    index=False
)

# Save VIP customers, highest monetary value first
vip = rfm[
    rfm["CustomerSegment"] == "VIP Customers"
].sort_values("Monetary", ascending=False)

vip.to_csv(
    output_folder / "rfm_vip_customers.csv",
    index=False
)

print("\nRFM SEGMENTATION RESULTS")
print("------------------------")
print(rfm["CustomerSegment"].value_counts())

print("\nTOP 10 VIP CUSTOMERS")
print(vip.head(10).to_string(index=False))

print("\nFiles saved successfully!")
