from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("insert_orders") \
    .config("spark.sql.catalog.iceberg", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.iceberg.type", "hive") \
    .config("spark.sql.catalog.iceberg.uri", "thrift://hive-metastore:9083") \
    .config("spark.sql.catalog.iceberg.warehouse", "s3://warehouse/") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.sql("SELECT * FROM iceberg.mydb.orders")
df.show()

df1 = spark.sql("SELECT COUNT(1) FROM iceberg.mydb.orders")
df1.show()

# Dừng SparkSession
spark.stop()
