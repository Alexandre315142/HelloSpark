from utils.helpers import getLocalSparkSession


spark = getLocalSparkSession(appName="Hello Spark", localThread= 'local[3]')

sampleDF = (
    spark
    .read
    .format('csv')
    .option("path","./inputData/sample.csv")
    .option("header", "true")
    .load()
)

modifiedSampleDF = (
    sampleDF
    .select("Age", "State", "Country")
)

modifiedSampleDF.show()

spark.stop()