from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

# Cấu hình DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 21),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "spark_iceberg_job",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

# Cấu hình Spark Job
spark_job = SparkSubmitOperator(
    task_id="insert_orders_to_iceberg",
    application="/opt/spark/scripts/insert_orders.py",
    conn_id="spark_master",
    conf={
        "spark.sql.catalog.iceberg": "org.apache.iceberg.spark.SparkCatalog",
        "spark.sql.catalog.iceberg.type": "hive",
        "spark.sql.catalog.iceberg.uri": "thrift://hive-metastore:9083",
        "spark.sql.catalog.iceberg.warehouse": "s3://warehouse/",
        "spark.hadoop.fs.s3a.endpoint": "http://minio:9000",
        "spark.hadoop.fs.s3a.access.key": "admin",
        "spark.hadoop.fs.s3a.secret.key": "password",
        "spark.hadoop.fs.s3a.path.style.access": "true",
        "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
    },
    jars="/opt/spark/jars/iceberg-spark-runtime-3.5_2.12-1.8.1.jar,/opt/spark/jars/hadoop-aws-3.3.4.jar,/opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar",
    executor_cores=1,
    executor_memory="1g",
    driver_memory="1g",
    name="SparkIcebergJob",
    verbose=True,
    dag=dag,
)

spark_job
