-- Top 10 most rated products (assumed as top sellers)
SELECT product_name, rating_count, rating
FROM products
ORDER BY rating_count DESC
LIMIT 10;
