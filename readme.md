copier ces fichier dans docker:
docker cp clients.csv spark-master-pj:/opt/spark/work-dir/data/
docker cp main.py spark-master-pj:/opt/spark/work-dir/app/

ensuite exécuté le scipt: deploy.sh

<!-- docker exec -it spark-master /bin/bash -c "
/opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --name KMeansSegmentationCluster \
  --executor-memory 1G \
  --total-executor-cores 2 \
  /opt/bitnami/spark/app/main.py
" -->
