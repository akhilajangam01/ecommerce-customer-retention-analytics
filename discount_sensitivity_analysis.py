
import pandas as pd

# Load cleaned retail dataset
df = pd.read_csv(
    "02_Cleaned_Data/Online_Retail_Python_Cleaned.csv"
)

# Display column names
print("Dataset Columns:")
print(df.columns.tolist())

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Discount sensitivity analysis
# Assumption: product cost is 60% of original revenue
cost_ratio = 0.60

# Simulated promotional discount percentages
discount_rates = [0, 5, 10, 15, 20, 25, 30]

# Keep valid sales transactions
sales = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

original_revenue = sales["Revenue"].sum()
estimated_cost = original_revenue * cost_ratio

results = []

for discount in discount_rates:
    discounted_revenue = original_revenue * (1 - discount / 100)
    estimated_profit = discounted_revenue - estimated_cost

    profit_margin = (
        estimated_profit / discounted_revenue * 100
    )

    results.append({
        "Discount_Percentage": discount,
        "Estimated_Revenue": round(discounted_revenue, 2),
        "Estimated_Profit": round(estimated_profit, 2),
        "Profit_Margin_Percentage": round(profit_margin, 2)
    })

results_df = pd.DataFrame(results)

print("\nDiscount Sensitivity Analysis:")
print(results_df.to_string(index=False))

# Save discount sensitivity results to CSV
output_file = "08_Discount_Analysis/discount_sensitivity_results.csv"

results_df.to_csv(output_file, index=False)

print("\nDiscount sensitivity results saved successfully!")
print("File:", output_file)

import matplotlib.pyplot as plt

# Create discount sensitivity chart
plt.figure(figsize=(10, 6))

plt.plot(
    results_df["Discount_Percentage"],
    results_df["Profit_Margin_Percentage"],
    marker="o",
    linewidth=2,
    color="blue"
)

plt.title("Discount Sensitivity vs Profit Margin")
plt.xlabel("Discount Percentage (%)")
plt.ylabel("Estimated Profit Margin (%)")

plt.grid(True)

# Save chart
plt.savefig(
    "08_Discount_Analysis/discount_profit_margin_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Profit margin chart saved successfully!")

# Revenue vs Discount Percentage Chart

plt.figure(figsize=(10, 6))

plt.bar(
    results_df["Discount_Percentage"].astype(str) + "%",
    results_df["Estimated_Revenue"],
    color="skyblue"
)

plt.title("Discount Percentage vs Estimated Revenue")
plt.xlabel("Discount Percentage (%)")
plt.ylabel("Estimated Revenue")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save the chart
plt.savefig(
    "08_Discount_Analysis/discount_revenue_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Revenue chart saved successfully!")

# Simulated promotional campaign comparison

campaign_names = {
    0: "No Promotion",
    5: "Loyalty Offer",
    10: "Seasonal Sale",
    15: "Holiday Promotion",
    20: "Flash Sale",
    25: "Clearance Sale",
    30: "Mega Sale"
}

campaign_df = results_df.copy()

campaign_df["Campaign"] = campaign_df[
    "Discount_Percentage"
].map(campaign_names)

campaign_df = campaign_df[
    [
        "Campaign",
        "Discount_Percentage",
        "Estimated_Revenue",
        "Estimated_Profit",
        "Profit_Margin_Percentage"
    ]
]

print("\nPromotional Campaign Comparison:")
print(campaign_df.to_string(index=False))

# Save campaign comparison
campaign_df.to_csv(
    "08_Discount_Analysis/campaign_comparison.csv",
    index=False
)

print("\nCampaign comparison saved successfully!")
