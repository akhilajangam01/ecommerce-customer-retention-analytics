# Discount Sensitivity Analysis Report

**Project:** E-Commerce Customer Retention & Sales Performance Analytics

**Tools:** Python (pandas, matplotlib), Excel, Power BI, SQL

## 1. Objective

Evaluate how different promotional discount percentages affect estimated revenue, profitability, and profit margins.

## 2. Dataset

The analysis uses the cleaned Online Retail dataset from the existing e-commerce analytics project.

Relevant fields include:
- Quantity
- UnitPrice
- Revenue
- InvoiceDate
- CustomerID

The dataset does not include actual promotional campaigns, discount percentages, or product costs.

## 3. Methodology

Seven hypothetical discount scenarios were evaluated: 0%, 5%, 10%, 15%, 20%, 25%, and 30%.

**Assumptions:**
- Product costs equal 60% of original revenue.
- Sales quantities remain constant across scenarios.
- Discounts are applied uniformly to eligible positive sales.
- Campaign names are illustrative rather than actual historical promotions.

Estimated Profit = Discounted Revenue − Estimated Cost

Profit Margin (%) = Estimated Profit / Discounted Revenue × 100

## 4. Key Findings

Under the stated assumptions:

- A 0% discount produces a 40.00% estimated profit margin.
- A 10% discount reduces the estimated profit margin to 33.33%.
- A 20% discount reduces the estimated profit margin to 25.00%.
- A 30% discount reduces the estimated profit margin to 14.29%.

Estimated revenue and profit decline as discounts increase when sales quantities remain unchanged.

## 5. Promotional Campaign Comparison

Seven illustrative campaign scenarios were created, including loyalty offers, seasonal sales, holiday promotions, flash sales, and clearance sales.

Smaller discounts preserve more profit per sale under the assumed cost structure.

## 6. Business Recommendations

1. Test moderate discounts before launching larger promotions.
2. Monitor gross profit and margin alongside sales revenue.
3. Evaluate whether increased sales volume offsets discount-related margin reductions.
4. Use customer segmentation to target promotions more effectively.
5. Obtain actual product costs and campaign performance data before making final pricing decisions.

## 7. Limitations

This is a scenario-based sensitivity analysis, not a measurement of actual promotional campaign profitability.

The analysis does not estimate customer demand response, campaign expenses, returns, or additional fulfillment costs.

## 8. Conclusion

Discount sensitivity analysis demonstrates the trade-off between promotional pricing and estimated profitability.

Under a fixed-volume assumption, increasing discounts reduces both revenue and profit margins. Actual campaign effectiveness requires sales-volume response and cost data.