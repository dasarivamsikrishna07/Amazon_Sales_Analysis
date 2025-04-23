-- Average rating per category
SELECT category, ROUND(AVG(rating), 2) AS avg_rating
FROM products
GROUP BY category
ORDER BY avg_rating DESC;
