
-- Customer Churn Rate (90-Day Inactivity)

WITH valid_orders AS (
    SELECT
        CustomerID,
        InvoiceNo,
        DATE(InvoiceDate) AS order_date
    FROM retail_sales
    WHERE CustomerID IS NOT NULL
      AND TRIM(CAST(CustomerID AS TEXT)) <> ''
      AND InvoiceNo NOT LIKE 'C%'
      AND Quantity > 0
),
customer_last_purchase AS (
    SELECT
        CustomerID,
        MAX(order_date) AS last_purchase
    FROM valid_orders
    GROUP BY CustomerID
),
reference_date AS (
    SELECT MAX(order_date) AS max_date
    FROM valid_orders
)
SELECT
    COUNT(*) AS total_customers,
    SUM(
        CASE
            WHEN julianday(r.max_date) -
                 julianday(c.last_purchase) > 90
            THEN 1 ELSE 0
        END
    ) AS churned_customers,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN julianday(r.max_date) -
                     julianday(c.last_purchase) > 90
                THEN 1 ELSE 0
            END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS churn_rate_percentage
FROM customer_last_purchase c
CROSS JOIN reference_date r;
