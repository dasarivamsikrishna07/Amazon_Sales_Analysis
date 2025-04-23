USE amazon_sales;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    discounted_price DECIMAL(10,2),
    actual_price DECIMAL(10,2),
    discount_percentage VARCHAR(10),
    rating FLOAT,
    rating_count INT
);
