from pyspark import SparkConf, SparkContext

# Create a SparkConf and SparkContext
conf = SparkConf().setAppName("RDDOperations")
sc = SparkContext(conf=conf)

# Load a text file into an RDD
numbersRDD = sc.textFile("C:/Users/nbhar/Downloads/Exercise1.txt")

# Calculate the sum of all numbers in the RDD
sum = numbersRDD.map(float).reduce(lambda x, y: x + y)
print("Sum of all numbers:", sum)

# Find the maximum and minimum values in the RDD
numbers = numbersRDD.map(float)
max_val = numbers.max()
min_val = numbers.min()
print("Maximum value:", max_val)
print("Minimum value:", min_val)

# Filter out all even numbers and create a new RDD
evenNumbersRDD = numbersRDD.filter(lambda x: int(x) % 2 == 0)

# Calculate the average of the numbers in the filtered RDD
evenNumbers = evenNumbersRDD.map(float)
average = evenNumbers.sum() / evenNumbers.count()
print("Average of even numbers:", average)

# Count the number of elements in the filtered RDD
count = evenNumbersRDD.count()
print("Number of even numbers:", count)

# Stop the SparkContext
sc.stop()