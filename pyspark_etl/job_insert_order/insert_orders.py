from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("insert_orders") \
    .config("spark.sql.catalog.iceberg", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.iceberg.type", "hive") \
    .config("spark.sql.catalog.iceberg.uri", "thrift://hive-metastore:9083") \
    .config("spark.sql.catalog.iceberg.warehouse", "s3://warehouse/") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "miniopassword") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.sql("SELECT * FROM iceberg.mydb.orders")
df.show()

df1 = spark.sql("SELECT COUNT(1) FROM iceberg.mydb.orders")
df1.show()

spark.sql(" INSERT INTO iceberg.mydb.orders VALUES (3, 'Product 3', 300.0) ")

df2 = spark.sql("SELECT * FROM iceberg.mydb.orders")
df2.show()

spark.sql(" UPDATE iceberg.mydb.orders SET amount = 301.0 WHERE ID = 3")

df3 = spark.sql("SELECT * FROM iceberg.mydb.orders")
df3.show()

spark.sql(" DELETE FROM iceberg.mydb.orders WHERE ID = 3")

df4 = spark.sql("SELECT * FROM iceberg.mydb.orders")
df4.show()

# Dừng SparkSession
spark.stop()
