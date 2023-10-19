from usages.helpers import getLocalSparkSession


spark = getLocalSparkSession(appName="Hello Spark", localThread= 'local[3]')

sampleDF = (
    spark
    .read
    .format('csv')
    .option("path","./inputData/sample.csv")
    .option("header", "true")
    .load()
)


spark.stop()