-- Compare actual vs discounted price averages by category
SELECT category,
       ROUND(AVG(actual_price), 2) AS avg_actual_price,
       ROUND(AVG(discounted_price), 2) AS avg_discounted_price
FROM products
GROUP BY category
ORDER BY avg_actual_price DESC;
