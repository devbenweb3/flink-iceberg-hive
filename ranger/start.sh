# Enable only necessary services to be run along with CORE ranger services
export ENABLED_RANGER_SERVICES="tagsync,hadoop,hbase,kafka,hive,knox,kms"
# Execute this command to bring the services up (after successful build if it is not already build)
./ranger-master/ranger_in_docker up