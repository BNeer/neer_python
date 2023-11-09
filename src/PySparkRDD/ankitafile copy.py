from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract
from pyspark.sql.functions import sum as spark_sum
from pyspark.sql.functions import col, max, min, avg

spark = SparkSession.builder.appName("ReadTextFileFromDesktop").getOrCreate()

filepath = r"file:///C:\Users\nbhar\Downloads\Exercise1.txt"
rdd = spark.read.text(filepath)

rdd.show()

sc=spark.sparkContext
print('sc: ',sc)

def print_line(line): 
    print(line)


rdd2 = sc.textFile(filepath)
rdd2.foreach(print_line)

integers = rdd2.flatMap(lambda l: l.split("\n"))

# Split each line to get individual numbers, then convert them to integers
numbersRDD = rdd2.flatMap(lambda line: line.split("\n")).map(lambda number: number)

print(f'nmbersRdd : {numbersRDD.count()}')

# Calculate the sum of all the numbers in the RDD.
# Extract numbers from each line using regular expressions
extracted_df = rdd.select(regexp_extract('value', r'\d+', 0).alias('number'))

# Convert the 'number' column to integers
converted_df = extracted_df.withColumn('number', extracted_df['number'].cast('int'))

# Calculate the sum of all numbers
sum_df = converted_df.agg(spark_sum('number').alias('total_sum'))

# Find the maximum and minimum values in the RDD.
max_df = converted_df.agg(max(col('number'))).collect()[0][0]
min_df = converted_df.agg(min(col('number'))).collect()[0][0]

# Filter out even numbers and create a new RDD
even_numbers_df = converted_df.filter(converted_df['number'] % 2 == 0)

# Calculate the average of even numbers
average_df = even_numbers_df.agg(avg(col('number')).alias('average'))

# Count the number of elements in the filtered RDD
count_df = even_numbers_df.count()

print('Maximum number:', max_df)
print('Minimum number:', min_df)
print('Even numbers:')
even_numbers_df.show()
print('Average of even numbers:')
average_df.show()
print('Count of even numbers:', count_df)
