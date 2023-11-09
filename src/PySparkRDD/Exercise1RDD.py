#from importlib import reload
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import sys

#from imp import reload
#reload(sys)

#sys.setdefaultencoding('utf-8')
# Create a SparkSession
spark = SparkSession.builder \
    .appName("LocalSparkSession") \
    .master("local[*]") \
    .getOrCreate()
# Create a SparkConf and SparkContext
#conf = SparkConf().setAppName("RDDOperations")
#sc = SparkContext(conf=conf)

# Load the text file as an RDD and text lines to integer values
inputFile = "/tmp/bduk1710/Neeraj/Exercise1.txt"  # Replace with the actual file path
numbersRDD = spark.sparkContext.textFile(inputFile).map(lambda x: int(x))



# Convert text lines to integer values and create an RDD of integers
#numbersRDD = rdd.map(lambda line: int(line))

# Calculate the sum of all numbers
total_sum = numbersRDD.reduce(lambda x, y: x + y)

# Find the maximum and minimum values
max_value = numbersRDD.max()
min_value = numbersRDD.min()

# Filter out even numbers and create a new RDD
even_numbersRDD = numbersRDD.filter(lambda x: x % 2 == 0)

# Calculate the average of the filtered RDD
count = even_numbersRDD.count()
average = even_numbersRDD.sum() / count

# Count the number of elements in the filtered RDD
count_filtered = even_numbersRDD.count()

# Print the results
print("Sum of all numbers:", total_sum)
print("Maximum number:", max_value)
print("Minimum number:", min_value)
print("Even numbers:", even_numbersRDD.collect())
print("Average of even numbers:", average)
print("Count of even numbers:", count_filtered)

# Stop the SparkSession
spark.stop()