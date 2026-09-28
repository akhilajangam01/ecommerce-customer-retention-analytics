# E-Commerce Customer Retention & Sales Performance Analytics

## 1. Project Objective

The objective of this project is to analyze e-commerce transaction data to understand customer purchasing behavior, customer retention, sales performance, and revenue trends.

The project will use Excel Power Query, SQL, Power BI, Python, and GitHub to clean, validate, analyze, visualize, and document the retail data.

## 2. Dataset

Dataset: UCI Online Retail Dataset

The dataset contains transactional e-commerce retail data with 541,909 records and 8 attributes.

### Dataset Fields

- InvoiceNo - Unique invoice/order identifier
- StockCode - Product identifier
- Description - Product description
- Quantity - Number of units purchased or returned
- InvoiceDate - Transaction date and time
- UnitPrice - Price per unit
- CustomerID - Customer identifier
- Country - Customer/transaction country

## 3. Data Quality Observations

Initial inspection identified several data-quality considerations:

- Missing CustomerID values are present.
- Negative Quantity values are present and may represent returns or cancellations.
- Zero or negative UnitPrice records require validation.
- Cancelled invoices are present and can be identified by InvoiceNo values beginning with "C".
- Duplicate transaction rows require further validation.

Python inspection identified:

- Negative Quantity Records: 10,624
- Zero/Negative UnitPrice Records: 2,517
- Cancelled Transaction Rows: 9,288
- Data Period: December 1, 2010 through December 9, 2011

## 4. Proposed Data Model

The raw source contains one transaction-level table.

For analysis and Power BI reporting, the dataset can later be organized into a star-schema-style model.

### Fact Table

FactSales

Fields may include:
- InvoiceNo
- CustomerID
- StockCode
- InvoiceDate
- Quantity
- UnitPrice
- Revenue

### Dimension Tables

DimCustomer
- CustomerID
- Country

DimProduct
- StockCode
- Description

DimDate
- Date
- Month
- Quarter
- Year

### Relationships

DimCustomer (1) -> (*) FactSales

DimProduct (1) -> (*) FactSales

DimDate (1) -> (*) FactSales

One customer can have many transactions.

One product can appear in many transaction records.

One date can contain many transactions.

## 5. Analysis Scope

The planned analysis will focus on:

1. Customer retention and repeat-purchase behavior
2. Customer segmentation
3. Monthly revenue trends and revenue velocity
4. Product sales performance
5. Geographic/country sales performance
6. Order and transaction trends
7. Returns and cancellations
8. Average order value
9. Customer purchase frequency
10. Customer lifetime/revenue contribution

## 6. Planned KPIs

Potential KPIs include:

- Total Revenue
- Monthly Revenue
- Revenue Growth
- Total Orders
- Unique Customers
- Average Order Value
- Repeat Customer Rate
- Customer Retention Rate
- Purchase Frequency
- Revenue per Customer
- Return/Cancellation Rate
- Top Products by Revenue

## 7. Tools

- Excel Power Query - initial data inspection and transformation
- Python/pandas - data profiling, validation, and analysis
- matplotlib - exploratory visualizations
- SQL - querying and KPI calculations
- Power BI Desktop - data modeling and interactive dashboards
- GitHub - version control and project documentation

## 8. Current Week Deliverables

Completed:
- Acquired e-commerce retail dataset
- Reviewed dataset structure
- Validated data types using Power Query
- Inspected missing CustomerID values
- Identified negative quantities
- Identified zero/non-positive prices
- Identified cancelled transactions
- Performed initial Python data profiling
- Defined proposed table relationships
- Defined analysis scope and planned KPIs