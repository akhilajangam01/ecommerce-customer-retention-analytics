## Power BI Dashboard – Sales Performance & Customer Segmentation

### Project Overview
Developed an interactive Power BI dashboard to analyze e-commerce sales performance, customer retention, and customer segmentation using RFM (Recency, Frequency, Monetary) analysis.

### Tools Used
- Power BI Desktop
- DAX
- SQL
- Python (Pandas)
- Excel Power Query
- GitHub

### Dashboard 1: Sales Overview
- Total Revenue: 10.67M
- Total Orders: Approximately 20K
- Total Customers: Approximately 4K
- Average Order Value: 534.40
- Monthly revenue trends
- Revenue forecasting
- Country-based filtering

### Dashboard 2: Customer Segmentation & RFM Analysis
- Calculated Recency, Frequency, and Monetary metrics.
- Created RFM scores to categorize customers.
- Identified five customer segments: VIP, Loyal, Regular, New, and At Risk.
- Visualized customer counts and revenue by segment.
- Analyzed high-value customer groups.

### Key Insights
- VIP customers generated the highest revenue.
- Regular customers represented the largest customer segment.
- Monthly revenue showed fluctuations and periods of strong growth.
- RFM analysis helped identify opportunities for customer retention and targeted marketing.

### Deliverables
- `Ecommerce_Sales_Analytics.pbix` – Interactive Power BI report
- `Ecommerce_Sales_Dashboard.pdf` – Dashboard export
# E-Commerce Customer Retention & Sales Performance Analytics

## Project Overview

This project analyzes e-commerce retail transaction data to evaluate customer retention, purchasing behavior, sales performance, and revenue trends.

The project uses Excel Power Query, Python, SQL, Power BI, and GitHub to build an end-to-end analytics workflow.

## Tech Stack

- Excel / Power Query
- Python (pandas, matplotlib)
- SQL
- Power BI Desktop
- GitHub

## Dataset

The project uses the Online Retail dataset containing 541,909 transaction records.

### Key Fields

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

## Week 1 - Dataset Acquisition & Inspection

### Completed Tasks

- Acquired the e-commerce retail dataset
- Reviewed 541,909 transaction records
- Inspected dataset columns and data types
- Used Excel Power Query for initial data inspection
- Used Python/pandas for dataset profiling
- Identified missing CustomerID values
- Identified negative quantities
- Identified zero/non-positive prices
- Identified cancelled transactions
- Defined proposed table relationships
- Defined analysis scope and future KPIs

## Initial Data Quality Findings

- Negative Quantity Records: 10,624
- Zero/Negative UnitPrice Records: 2,517
- Cancelled Transaction Rows: 9,288
- Dataset Start Date: December 1, 2010
- Dataset End Date: December 9, 2011

## Proposed Data Model

The raw dataset is transaction-level data.

The proposed analytical model will use:

- FactSales
- DimCustomer
- DimProduct
- DimDate

### Relationships

- DimCustomer (1) -> (*) FactSales
- DimProduct (1) -> (*) FactSales
- DimDate (1) -> (*) FactSales

## Planned Analysis

Future analysis will include:

- Customer retention
- Repeat purchase behavior
- Customer segmentation
- Monthly revenue trends
- Revenue velocity
- Product performance
- Country performance
- Average order value
- Purchase frequency
- Returns and cancellations

## Project Structure

01_Raw_Data - Original source dataset

02_Cleaned_Data - Cleaned datasets

03_Python - Python analysis scripts

04_SQL - SQL scripts

05_PowerBI - Power BI dashboard files

06_Documentation - Analysis scope and project documentation

07_Screenshots - Project evidence and output screenshots

## Current Status

Week 1 dataset acquisition, initial data inspection, relationship design, and analysis scope definition completed.
