docker run --rm --name spark_job_insert_orders \
  --network data_lakehouse_net \
  -v $(pwd)/insert_orders.py:/opt/spark/scripts/insert_orders.py \
  -v $(pwd)/spark_jars:/opt/spark/jars \
  bitnami/spark:latest \
  /bin/sh -c "/opt/bitnami/spark/bin/spark-submit \
    --master spark://spark-master:7077 \
    --deploy-mode client \
    --conf spark.sql.catalog.iceberg=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.iceberg.type=hive \
    --conf spark.sql.catalog.iceberg.uri=thrift://hive-metastore:9083 \
    --conf spark.sql.catalog.iceberg.warehouse=s3://warehouse/ \
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
    --conf spark.hadoop.fs.s3a.endpoint=http://minio:9000 \
    --conf spark.hadoop.fs.s3a.access.key=admin \
    --conf spark.hadoop.fs.s3a.secret.key=miniopassword \
    --conf spark.hadoop.fs.s3a.path.style.access=true \
    --jars /opt/spark/jars/iceberg-spark-runtime-3.5_2.12-1.8.1.jar \
    /opt/spark/scripts/insert_orders.py"