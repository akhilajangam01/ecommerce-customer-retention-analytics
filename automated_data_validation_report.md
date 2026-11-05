
# Automated Data Validation Report

## Project
E-Commerce Customer Retention & Sales Performance Analytics

## Objective
Implement automated data validation checks to identify
revenue discrepancies and potential duplicate orders.

## Tools Used
- Python
- pandas
- VS Code
- GitHub

## Validation Checks
1. Missing value detection
2. Revenue calculation validation
3. Exact duplicate row detection
4. Potential duplicate order-line detection
5. Automated CSV report generation

## Validation Results
- Total Records: 392,692
- Revenue Discrepancies: 0
- Potential Duplicate Order Lines: 6
- Exact Duplicate Rows: 0

## Key Findings
- No revenue discrepancies were identified using
  the implemented validation rules.
- Six order lines were flagged as potential duplicates.
- The flagged records require further review before
  being classified as actual duplicates.
- Automated reports were generated successfully.

## Deliverables
- automated_data_validation.py
- validation_summary.csv
- revenue_discrepancies.csv (local)
- duplicate_orders.csv (local)
- automated_data_validation_report.md

## Conclusion
Automated validation checks were implemented to
monitor revenue consistency and identify potentially
duplicated order lines. The Python script can be
rerun whenever the cleaned dataset is updated.
