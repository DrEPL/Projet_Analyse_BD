# Script de déploiement : deploy.sh
SPARK_MASTER_URL="spark://localhost:7078"
APP_PATH="./app/main.py"
echo "Soumission de l'application au cluster Spark..."

docker exec -it spark-master-pj /bin/bash -c "
/opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --name KMeansSegmentationCluster \
  --executor-memory 1G \
  --total-executor-cores 2 \
  /opt/spark/work-dir/app/main.py
"

echo "Application terminée."