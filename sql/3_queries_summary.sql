-- Total number of products
SELECT COUNT(*) AS total_products FROM products;

-- Number of categories
SELECT COUNT(DISTINCT category) AS total_categories FROM products;

-- Average rating overall
SELECT ROUND(AVG(rating), 2) AS avg_rating FROM products;
