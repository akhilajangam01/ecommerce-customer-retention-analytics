
-- Average Basket Size Analysis

WITH order_baskets AS (
    SELECT
        InvoiceNo,
        CustomerID,
        SUM(Quantity) AS total_items,
        SUM(Quantity * UnitPrice) AS basket_value
    FROM retail_sales
    WHERE InvoiceNo IS NOT NULL
      AND InvoiceNo NOT LIKE 'C%'
      AND Quantity > 0
      AND UnitPrice > 0
    GROUP BY InvoiceNo
)
SELECT
    COUNT(*) AS total_orders,
    SUM(total_items) AS total_items_sold,
    ROUND(AVG(total_items), 2) AS average_basket_size,
    ROUND(AVG(basket_value), 2) AS average_order_value
FROM order_baskets;
