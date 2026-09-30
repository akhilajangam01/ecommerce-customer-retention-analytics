# Exploratory Data Analysis Report

## Project
E-Commerce Customer Retention & Sales Performance Analytics

## Objective

The objective of this analysis was to perform exploratory data analysis (EDA) on the cleaned e-commerce transactional dataset, focusing on sales volume by product, product category, and geography.

The assignment also requested discount-rate analysis. The availability of discount information was validated before attempting this analysis.

## Tools Used

- Python
- pandas
- matplotlib
- Excel / Power Query
- VS Code
- GitHub

## Dataset

The cleaned Online Retail transactional dataset was used for this analysis.

The main fields used included:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

The dataset had previously been cleaned and validated using Power Query and Python.

---

## 1. Sales Volume by Product

Sales volume was calculated by grouping transactions by product description and summing the Quantity sold.

The analysis identified the Top 10 products based on total quantity sold.

Among the highest-volume products were:

- PAPER CRAFT, LITTLE BIRDIE
- MEDIUM CERAMIC TOP STORAGE JAR
- WORLD WAR 2 GLIDERS ASSTD DESIGNS
- JUMBO BAG RED RETROSPOT
- WHITE HANGING HEART T-LIGHT HOLDER

A horizontal bar chart was created to visualize the Top 10 products.

Chart:

`07_Screenshots/top_10_products_sales_volume.png`

### Observation

A relatively small group of products generated high unit-sales volumes, indicating that these products may be important for inventory planning and product-demand analysis.

---

## 2. Sales Volume by Geography

Geographic sales performance was analyzed by grouping transactions by Country and calculating total Quantity sold.

The Top 10 countries by sales volume were identified and visualized using a horizontal bar chart.

Chart:

`07_Screenshots/top_10_countries_sales_volume.png`

### Observation

Sales volume varies significantly across geographic markets. This analysis can help identify high-volume markets and support future geographic sales and customer-retention analysis.

---

## 3. Sales Volume by Product Category

The source Online Retail dataset does not provide an explicit Product Category field.

For exploratory purposes, transparent keyword-based categories were therefore derived from the product Description field.

The derived categories included:

- Bags
- Kitchen & Dining
- Lighting & Candles
- Stationery & Crafts
- Seasonal & Decorations
- Toys & Games
- Other

The analysis produced the following sales volumes:

- Other: 2,872,097 units
- Bags: 571,732 units
- Stationery & Crafts: 487,610 units
- Lighting & Candles: 433,243 units
- Kitchen & Dining: 374,617 units
- Seasonal & Decorations: 354,459 units
- Toys & Games: 58,244 units

Chart:

`07_Screenshots/sales_volume_by_product_category.png`

### Observation

The "Other" category represents a large portion of total sales volume because the source dataset does not contain standardized product categories and the keyword-based classification only covers selected product groups.

Therefore, these derived categories should be treated as exploratory rather than official merchandising classifications.

---

## 4. Discount Rate Analysis

The source dataset was reviewed for fields related to discounts.

No Discount, DiscountRate, OriginalPrice, or equivalent field was available.

Therefore, a reliable discount rate cannot be calculated from the available source data.

Rather than generating artificial discount values, the limitation was documented.

### Recommendation

For future discount analysis, the dataset should include fields such as:

- Original/List Price
- Selling Price
- Discount Amount
- Discount Percentage
- Promotion Code

With this information, discount effectiveness could be analyzed against sales volume, revenue, and customer purchasing behavior.

---

## Key Findings

The EDA identified several high-volume products and substantial differences in sales volume across geographic markets.

Keyword-based product categorization provided an exploratory view of category-level demand, while also highlighting the need for a standardized product-category field.

Discount-rate analysis could not be reliably performed because discount information was not included in the source dataset.

---

## Deliverables

Python EDA Script:

`03_Python/exploratory_data_analysis.py`

Visualizations:

`07_Screenshots/top_10_products_sales_volume.png`

`07_Screenshots/top_10_countries_sales_volume.png`

`07_Screenshots/sales_volume_by_product_category.png`

Documentation:

`06_Documentation/eda_report.md`

## Status

Completed:

- Sales volume analysis by product
- Geographic sales-volume analysis
- Derived product-category analysis
- Matplotlib visualizations
- Discount-field validation
- Dataset limitation documentation
- EDA documentation