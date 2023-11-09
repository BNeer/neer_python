from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract
from pyspark.sql.functions import sum as spark_sum
from pyspark.sql.functions import col, max, min, avg

spark = SparkSession.builder.appName("ReadTextFileFromDesktop").getOrCreate()


filepath = r"file:///C:\Users\nbhar\Downloads\Exercise1.txt"
#inputFile = "/tmp/bduk1710/Neeraj/employee_data.csv"
rdd = spark.read.text(filepath)

rdd.show()

# 1.1Calculate the sum of all the numbers in the RDD.
# Extract numbers from each line using regular expressions
extracted_df = rdd.select(regexp_extract('value', r'\d+', 0).alias('number'))

# Convert the 'number' column to integers
converted_df = extracted_df.withColumn('number', extracted_df['number'].cast('int'))

# Calculate the sum of all numbers
sum_df = converted_df.agg(spark_sum('number').alias('total_sum'))

# 1.2 Find the maximum and minimum values in the RDD.
max_df = converted_df.agg(max(col('number'))).collect()[0][0]
min_df = converted_df.agg(min(col('number'))).collect()[0][0]

# 1.3 Filter out even numbers and create a new RDD
even_numbers_df = converted_df.filter(converted_df['number'] % 2 == 0)

# 1.4 Calculate the average of even numbers
average_df = even_numbers_df.agg(avg(col('number')).alias('average'))

# 1.5 Count the number of elements in the filtered RDD
count_df = even_numbers_df.count()

print('Maximum number:', max_df)
print('Minimum number:', min_df)
print('Even numbers:')
even_numbers_df.show()
print('Average of even numbers:')
average_df.show()
print('Count of even numbers:', count_df)
