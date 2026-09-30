# Week 2 - Data Cleaning and Transformation Report

## Project
E-Commerce Customer Retention & Sales Performance Analytics

## Objective

The objective of this week's work was to clean and transform the raw transactional retail dataset using Excel Power Query and Python (pandas), with particular attention to missing records, invalid transactions, duplicates, and data consistency.

## Tools Used

- Excel
- Power Query
- Python
- pandas
- VS Code
- GitHub

## Power Query Data Cleaning

The raw Online Retail dataset was imported into Power Query while preserving the original source data.

The following transformations were performed:

### 1. Data Type Validation

The columns were assigned appropriate data types:

- InvoiceNo - Text
- StockCode - Text
- Description - Text
- Quantity - Whole Number
- InvoiceDate - Date/Time
- UnitPrice - Decimal Number
- CustomerID - Text
- Country - Text

### 2. Missing Customer Records

Rows with missing CustomerID values were excluded from the customer-analysis dataset.

CustomerID is required for customer retention, repeat-purchase analysis, and customer segmentation.

### 3. Missing Product Descriptions

Records with null or empty Description values were removed to improve product-level analysis.

### 4. Cancelled Transactions

Invoices beginning with "C" were excluded from the completed-sales dataset.

These records represent cancelled/returned transactions and should not be combined with normal completed sales when calculating positive sales revenue.

### 5. Quantity Validation

Only records where:

Quantity > 0

were retained in the completed-sales dataset.

This prevents returned or invalid quantities from affecting normal sales KPIs.

### 6. Unit Price Validation

Only records where:

UnitPrice > 0

were retained.

Zero and negative prices were excluded from normal revenue calculations.

### 7. Duplicate Removal

Exact duplicate transaction rows were removed to prevent duplicate sales from inflating revenue and transaction metrics.

### 8. Text Standardization

Description and Country fields were cleaned using Power Query Trim and Clean transformations.

This helps prevent inconsistent categories caused by unnecessary spaces or hidden characters.

### 9. Revenue Calculation

A new Revenue field was created using:

Revenue = Quantity × UnitPrice

This field will be used for future sales and revenue analysis.

## Python Cleaning and Validation

A Python pandas cleaning workflow was created in:

`data_cleaning.py`

Python was used to:

- Load the transformed retail dataset
- Check missing values
- Remove records with missing CustomerID
- Remove records with missing Description
- Validate Quantity
- Validate UnitPrice
- Exclude cancelled invoices
- Remove duplicate rows
- Perform final data-quality validation
- Export the cleaned dataset to CSV

## Output Files

Full cleaned dataset:

`Online_Retail_Python_Cleaned.csv`

GitHub sample dataset:

`Online_Retail_Cleaned_Sample.csv`

The GitHub sample contains 1,000 rows because the complete cleaned dataset is too large for a normal browser upload.

The complete cleaned dataset is generated reproducibly by running the Python cleaning script.

## Data Quality Validation

The final cleaned dataset was checked for:

- Missing CustomerID values
- Missing product descriptions
- Duplicate records
- Zero/negative quantities
- Zero/negative unit prices
- Cancelled invoices

The cleaned completed-sales dataset is now suitable for downstream customer and sales analytics.

## Next Steps

The cleaned dataset can be used for:

- Customer segmentation
- Repeat-purchase analysis
- Customer retention analysis
- Monthly revenue trends
- Revenue velocity analysis
- Product performance analysis
- Country-level sales analysis
- SQL-based KPI calculations
- Power BI data modeling and dashboard development

## Week 2 Status

Completed:

- Power Query cleaning
- Missing-record handling
- Transaction validation
- Duplicate removal
- Text standardization
- Revenue calculation
- Python/pandas cleaning
- Final data validation
- Cleaned CSV export
- GitHub sample dataset creation