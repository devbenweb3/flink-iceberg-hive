docker cp spark-master:/opt/bitnami/spark/jars/ ./spark_jars_airflow/ &&
mv ./spark_jars_airflow/jars/* ./spark_jars_airflow/ &&
rm -rf ./spark_jars_airflow/jars
