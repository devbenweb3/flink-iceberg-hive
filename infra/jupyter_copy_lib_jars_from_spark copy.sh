docker cp spark-master:/opt/bitnami/spark/jars/ ./spark_jars_jupyter/ &&
mv ./spark_jars_jupyter/jars/* ./spark_jars_jupyter/ &&
rm -rf ./spark_jars_jupyter/jars
