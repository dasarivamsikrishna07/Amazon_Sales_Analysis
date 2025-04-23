-- Group products by rating range
SELECT 
  CASE
    WHEN rating >= 4.5 THEN 'Excellent (4.5-5)'
    WHEN rating >= 4 THEN 'Good (4-4.4)'
    WHEN rating >= 3 THEN 'Average (3-3.9)'
    ELSE 'Low (<3)'
  END AS rating_group,
  COUNT(*) AS product_count
FROM products
GROUP BY rating_group
ORDER BY product_count DESC;
