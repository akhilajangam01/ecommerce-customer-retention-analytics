
import pandas as pd
from pathlib import Path

# Project folder
project = Path(__file__).resolve().parent.parent

# Load RFM segmentation results
rfm = pd.read_csv(
    project / "03_Python" / "rfm_customer_segments.csv"
)

# Calculate overall customer revenue
total_revenue = rfm["Monetary"].sum()
total_customers = len(rfm)

# Select VIP customers
vip = rfm[
    rfm["CustomerSegment"] == "VIP Customers"
].copy()

# Calculate VIP performance
vip_revenue = vip["Monetary"].sum()
vip_count = len(vip)

vip_revenue_percentage = (
    vip_revenue / total_revenue * 100
    if total_revenue > 0 else 0
)

vip_customer_percentage = (
    vip_count / total_customers * 100
    if total_customers > 0 else 0
)

# Display results
print("\nVIP CUSTOMER REVENUE ANALYSIS")
print("--------------------------------")
print("Total Customers:", total_customers)
print("VIP Customers:", vip_count)
print("VIP Customer Percentage:",
      round(vip_customer_percentage, 2), "%")
print("Total Revenue:", round(total_revenue, 2))
print("VIP Revenue:", round(vip_revenue, 2))
print("VIP Revenue Contribution:",
      round(vip_revenue_percentage, 2), "%")

# Top 10 VIP accounts
top_vip = vip.sort_values(
    "Monetary", ascending=False
).head(10)

print("\nTOP 10 VIP CUSTOMERS")
print("--------------------------------")

print(
    top_vip[
        ["CustomerID", "Recency", "Frequency",
         "Monetary", "RFM_Score"]
    ].to_string(index=False)
)

# Save results
output_folder = project / "03_Python"

top_vip.to_csv(
    output_folder / "rfm_top_10_vip.csv",
    index=False
)

# Save revenue summary
summary = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "VIP Customers",
        "VIP Customer Percentage",
        "Total Revenue",
        "VIP Revenue",
        "VIP Revenue Contribution Percentage"
    ],
    "Value": [
        total_customers,
        vip_count,
        round(vip_customer_percentage, 2),
        round(total_revenue, 2),
        round(vip_revenue, 2),
        round(vip_revenue_percentage, 2)
    ]
})

summary.to_csv(
    output_folder / "rfm_vip_revenue_summary.csv",
    index=False
)

print("\nVIP analysis files saved successfully!")
