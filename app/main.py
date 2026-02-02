# main.py
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
def main():
    spark = SparkSession.builder.appName("KMeansSegmentation").getOrCreate()
    # En production, on lit depuis HDFS
    # hdfs_path = "hdfs://namenode:9000/data/clients.csv"
    # Pour le test local, on lit le fichier local
    df = spark.read.csv("/opt/spark/work-dir/data/clients.csv", header=True, inferSchema=True)
    # Pipeline ML
    assembler = VectorAssembler(inputCols=["Age", "RevenuAnnuel", 
"ScoreDepense"], outputCol="features_unscaled")
    scaler = StandardScaler(inputCol="features_unscaled", 
outputCol="features")
    kmeans = KMeans(k=5, seed=1)
    pipeline = Pipeline(stages=[assembler, scaler, kmeans])
    # Entraînement
    model = pipeline.fit(df)
    # Prédiction
    predictions = model.transform(df)
    # Sauvegarde des résultats (ex: sur HDFS)
    # output_path = "hdfs://namenode:9000/output/segments"
    # predictions.select("CustomerID", 
    # "prediction").write.mode("overwrite").parquet(output_path)
    # Pour le test local, on affiche
    print("Segmentation terminée. Aperçu des résultats :")
    predictions.select("CustomerID", "prediction").show(10)
    spark.stop()
    
if __name__ == "__main__":
    main()