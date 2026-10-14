
-- Customer Repurchase Rate
-- Assumes columns: CustomerID, InvoiceNo

WITH customer_orders AS (
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS total_orders
    FROM retail_sales
    WHERE CustomerID IS NOT NULL
      AND TRIM(CAST(CustomerID AS TEXT)) <> ''
      AND InvoiceNo NOT LIKE 'C%'
    GROUP BY CustomerID
)
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN total_orders > 1 THEN 1 ELSE 0 END)
        AS repeat_customers,
    ROUND(
        100.0 * SUM(
            CASE WHEN total_orders > 1 THEN 1 ELSE 0 END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS repurchase_rate_percentage
FROM customer_orders;
