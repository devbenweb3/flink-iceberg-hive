docker cp ./spark_jars/iceberg-spark-runtime-3.5_2.12-1.8.1.jar jupyter_pyspark_notebook:/usr/local/spark/jars &&
docker cp ./spark_jars/aws-java-sdk-bundle-1.12.262.jar jupyter_pyspark_notebook:/usr/local/spark/jars &&
docker cp ./spark_jars/hadoop-aws-3.3.4.jar jupyter_pyspark_notebook:/usr/local/spark/jars 

