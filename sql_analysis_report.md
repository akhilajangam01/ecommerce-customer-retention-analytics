# SQL Customer Retention & Sales Performance Analysis

## Project Overview

**Project:** E-Commerce Customer Retention & Sales Performance Analytics

**Tools:** SQLite, SQL, Python, pandas, VS Code, GitHub

**Dataset:** Online Retail Transaction Dataset

**Records Analyzed:** 392,692

**Analysis Period:** December 1, 2010 – December 9, 2011

## Objective

Develop advanced SQL queries to analyze customer repurchase behavior, identify customers with prolonged purchasing inactivity, and evaluate average basket sizes and order values.

## SQL Techniques Used

- Common Table Expressions (CTEs)
- Aggregate functions: COUNT, SUM, AVG
- DISTINCT and GROUP BY
- CASE WHEN conditional logic
- Date functions and date arithmetic
- NULL handling and data filtering

## Key Findings

| Metric | Result |
|---|---:|
| Total Customers | 4,338 |
| Repeat Customers | 2,845 |
| Repurchase Rate | 65.58% |
| Inactive Customers (90+ Days) | 1,449 |
| Inactivity-Based Churn Rate | 33.40% |
| Total Orders | 18,532 |
| Total Units Sold | 5,152,002 |
| Average Basket Size | 278.01 units |
| Average Order Value | $479.56 |

## Business Insights

### Customer Repurchase Analysis

The customer repurchase rate was 65.58%, indicating that approximately two-thirds of identified customers completed more than one purchase during the analysis period.

### Customer Churn Analysis

Approximately 33.40% of customers had not purchased within the final 90 days of the dataset. This inactivity-based measure can help identify customers for potential re-engagement campaigns. It does not establish permanent customer churn.

### Average Basket Analysis

The average order contained 278.01 units, with an average order value of 479.56 in the dataset's currency. The high average unit count suggests that some transactions may involve bulk purchases.

## Data Quality Validation

- Verified that all 392,692 imported records had SQLite-compatible transaction dates.
- Confirmed the analysis period from December 1, 2010, through December 9, 2011.
- Applied transaction filters to exclude cancellations and invalid quantities where relevant.
- Used distinct invoice numbers to avoid counting individual product lines as separate orders.

## Recommendations

1. Develop targeted re-engagement campaigns for customers inactive for more than 90 days.
2. Segment repeat customers based on purchase frequency and spending.
3. Analyze high-volume baskets to identify potential wholesale purchasing patterns.
4. Track retention and basket metrics over time using Power BI dashboards.

## Deliverables

- `customer_retention_analysis.sql`
- `customer_churn_analysis.sql`
- `average_basket_analysis.sql`
- `validate_dates.sql`
- `run_all_queries.py`
- SQL execution screenshots
- `sql_analysis_report.md`

## Conclusion

Advanced SQL queries were developed and executed to evaluate customer repurchase behavior, purchasing inactivity, and basket performance. The findings provide a foundation for customer segmentation, retention analysis, and future Power BI reporting.