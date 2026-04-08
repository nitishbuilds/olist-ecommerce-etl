-- Monthly revenue
SELECT year, month, SUM(revenue)
FROM fact_orders
GROUP BY year, month;

-- Top categories
SELECT product_category_name, SUM(revenue)
FROM fact_orders
GROUP BY product_category_name
ORDER BY SUM(revenue) DESC;

 --Top cities
SELECT customer_city, SUM(revenue)
FROM fact_orders
GROUP BY customer_city
ORDER BY SUM(revenue) DESC;