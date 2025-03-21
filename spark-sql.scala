spark.sql("SHOW CATALOGS").show()

spark.sql("SHOW DATABASES IN iceberg").show()

spark.sql("SELECT * FROM iceberg.mydb.orders").show()