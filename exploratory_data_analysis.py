import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = "../02_Cleaned_Data/Online_Retail_Python_Cleaned.csv"

df = pd.read_csv(file_path)

# Display basic dataset information
print("--- DATASET OVERVIEW ---")
print("Rows and Columns:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)
# -----------------------------------
# EDA 1: Sales Volume by Product
# -----------------------------------

product_sales = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 PRODUCTS BY SALES VOLUME ---")
print(product_sales)

# Create bar chart
plt.figure(figsize=(10, 6))
product_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales Volume")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()

# Save chart for project documentation
plt.savefig("../07_Screenshots/top_10_products_sales_volume.png",
            bbox_inches="tight")

plt.show()
# -----------------------------------
# EDA 2: Sales Volume by Geography
# -----------------------------------

country_sales = (
    df.groupby("Country")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 COUNTRIES BY SALES VOLUME ---")
print(country_sales)

# Create geography chart
plt.figure(figsize=(10, 6))
country_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Sales Volume")
plt.xlabel("Quantity Sold")
plt.ylabel("Country")
plt.tight_layout()

# Save chart
plt.savefig(
    "../07_Screenshots/top_10_countries_sales_volume.png",
    bbox_inches="tight"
)

plt.show()
# -----------------------------------
# EDA 3: Sales Volume by Product Category
# -----------------------------------

def assign_category(description):
    description = str(description).upper()

    if any(word in description for word in ["BAG", "PURSE", "HANDBAG"]):
        return "Bags"

    elif any(word in description for word in ["MUG", "CUP", "TEA", "PLATE", "BOWL"]):
        return "Kitchen & Dining"

    elif any(word in description for word in ["LIGHT", "LAMP", "CANDLE", "LANTERN"]):
        return "Lighting & Candles"

    elif any(word in description for word in ["CARD", "PAPER", "CRAFT", "NOTEBOOK"]):
        return "Stationery & Crafts"

    elif any(word in description for word in ["CHRISTMAS", "XMAS", "DECORATION", "ORNAMENT"]):
        return "Seasonal & Decorations"

    elif any(word in description for word in ["TOY", "DOLL", "GAME", "PUZZLE"]):
        return "Toys & Games"

    else:
        return "Other"


df["ProductCategory"] = df["Description"].apply(assign_category)

category_sales = (
    df.groupby("ProductCategory")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- SALES VOLUME BY DERIVED PRODUCT CATEGORY ---")
print(category_sales)

plt.figure(figsize=(10, 6))
category_sales.sort_values().plot(kind="barh")

plt.title("Sales Volume by Derived Product Category")
plt.xlabel("Quantity Sold")
plt.ylabel("Product Category")
plt.tight_layout()

plt.savefig(
    "../07_Screenshots/sales_volume_by_product_category.png",
    bbox_inches="tight"
)

plt.show()
# -----------------------------------
# EDA 4: Discount Rate Analysis
# -----------------------------------

print("\n--- DISCOUNT RATE ANALYSIS ---")

discount_columns = [
    col for col in df.columns
    if "discount" in col.lower()
]

if discount_columns:
    print("Discount-related columns found:", discount_columns)
else:
    print(
        "Discount rate analysis could not be performed because "
        "the source Online Retail dataset does not contain a "
        "discount or original-price field."
    )