import os
from pyspark.sql import SparkSession

# Set the environment variable
os.environ['SPARK_DRIVER_EXTRA_CLASSPATH'] = 'C:\\postgresql-42.6.0.jar'

# Create SparkSession
spark = SparkSession.builder \
    .appName("PostgresToHive") \
    .enableHiveSupport() \
    .getOrCreate()

# Use the read attribute of SparkSession to create DataFrameReader
df_reader = spark.read

# Read from JDBC
url = "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"
properties = {"user": "consultants", "password": "WelcomeItc@2022", "driver": "org.postgresql.Driver"}
df = df_reader.jdbc(url=url, table="testdb", properties=properties)

# Show the DataFrame
df.show()