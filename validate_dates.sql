
SELECT
    MIN(InvoiceDate) AS earliest_raw_date,
    MAX(InvoiceDate) AS latest_raw_date,
    MIN(DATE(InvoiceDate)) AS earliest_parsed_date,
    MAX(DATE(InvoiceDate)) AS latest_parsed_date,
    SUM(
        CASE
            WHEN DATE(InvoiceDate) IS NULL THEN 1
            ELSE 0
        END
    ) AS invalid_date_rows
FROM retail_sales;
