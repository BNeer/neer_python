from pyspark import SparkContext, SparkConf

# Create a SparkConf and SparkContext
#conf = SparkConf().setAppName("RDDOperations")
conf = SparkConf().setAppName("RDDOperations").set("spark.driver.memory", "2g")

sc = SparkContext(master="local[1]",appName="test")

# Load the text file as an RDD
#filepath = "file:///C:/Users/nbhar/Downloads/Exercise1.txt"

my_list = [1,2,3,4,5]
#rdd = sc.textFile(filepath)
rdd = sc.parallelize(my_list)
doubled = rdd.map(lambda x: x*2)
result = doubled.collect()

print("count: %s" % result)

# Stop the SparkContext
sc.stop()
