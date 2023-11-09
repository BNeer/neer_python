from pyspark import SparkContext

with SparkContext(appName="MyApp") as sc:
    # Your PySpark code here


    # Create an RDD from a text file
    filepath = "src/source.txt"
    rdd = sc.textFile(filepath)

    # Display the content of the RDD
    rdd.collect()

# Stop the SparkContext
    sc.stop()
