-- E-commerce Data Analysis
-- Table: ecommerce_sales

SELECT * FROM ecommerce_sales;

SELECT SUM(Quantity * Unit_Price) AS total_revenue
FROM ecommerce_sales;

SELECT COUNT(DISTINCT Order_ID) AS total_orders
FROM ecommerce_sales;

SELECT SUM(Quantity) AS total_quantity_sold
FROM ecommerce_sales;

SELECT Category, SUM(Quantity * Unit_Price) AS revenue
FROM ecommerce_sales
GROUP BY Category
ORDER BY revenue DESC;

SELECT City, SUM(Quantity * Unit_Price) AS revenue
FROM ecommerce_sales
GROUP BY City
ORDER BY revenue DESC;

SELECT Product, SUM(Quantity * Unit_Price) AS revenue
FROM ecommerce_sales
GROUP BY Product
ORDER BY revenue DESC;

SELECT Payment_Method, COUNT(DISTINCT Order_ID) AS orders
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY orders DESC;

SELECT Product, SUM(Quantity * Unit_Price) AS revenue
FROM ecommerce_sales
GROUP BY Product
ORDER BY revenue DESC
LIMIT 5;

-- Average order value
SELECT AVG(order_total) AS average_order_value
FROM (
    SELECT Order_ID, SUM(Quantity * Unit_Price) AS order_total
    FROM ecommerce_sales
    GROUP BY Order_ID
) AS orders;

-- City and category performance
SELECT City, Category, SUM(Quantity * Unit_Price) AS revenue
FROM ecommerce_sales
GROUP BY City, Category
ORDER BY revenue DESC;
