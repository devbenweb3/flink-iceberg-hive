spark.sql("SHOW CATALOGS").show()

spark.sql("SHOW DATABASES IN iceberg").show()

spark.sql("SELECT * FROM iceberg.mydb.orders").show()

spark.sql("""
    INSERT INTO iceberg.mydb.orders VALUES (3, 'Product Spark 3', 300.0);
""")