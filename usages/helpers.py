# import library

import pyspark
from pyspark.sql import SparkSession, DataFrame


# function to get local Spark Session
def getLocalSparkSession(appName: str, localThread: str) -> SparkSession:
    """ function to return local Spark Session

    Args:
        appName (str): Spark master name
        localThread (str): Number of thread

    Returns:
        SparkSession: _description_
    """
    spark = (
        SparkSession
        .Builder()
        .appName(appName)
        .master(localThread)
        .getOrCreate()
    )
    return spark