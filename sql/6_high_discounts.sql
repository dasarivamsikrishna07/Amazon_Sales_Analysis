-- Products with more than 50% discount
SELECT product_name, discount_percentage, actual_price, discounted_price
FROM products
WHERE discount_percentage LIKE '%50%' OR
      CAST(REPLACE(discount_percentage, '%', '') AS UNSIGNED) > 50
ORDER BY actual_price DESC;
