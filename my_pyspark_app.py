    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("MyPySparkApp").getOrCreate()
    
    # Your PySpark code goes here
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    columns = ["name", "age"]
    df = spark.createDataFrame(data, columns)
    
    df.show()

    spark.stop()
