SHOW CATALOGS;

SHOW SCHEMAS FROM iceberg;

CREATE SCHEMA iceberg.mydb WITH (location = 's3a://warehouse/mydb/' );

SHOW TABLES FROM iceberg.mydb;

CREATE TABLE iceberg.mydb.orders (
    id BIGINT,
    name VARCHAR,
    amount DOUBLE
)
WITH (
    format = 'parquet',
    location = 's3a://warehouse/mydb/orders/'
);

INSERT INTO iceberg.mydb.orders VALUES (1, 'Product A', 100.0);
INSERT INTO iceberg.mydb.orders VALUES (2, 'Product B', 200.0);

SELECT * FROM iceberg.mydb.orders;

-- INSERT INTO iceberg.mydb.orders VALUES (3, 'Product 3', 300.0) 
-- UPDATE iceberg.mydb.orders SET amount = 301.0 WHERE ID = 3
-- DELETE FROM  iceberg.mydb.orders WHERE ID IN (3,4,5);