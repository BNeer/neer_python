from pyspark.sql import SparkSession
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# Initialize a Spark session
spark = SparkSession.builder.appName("PostgresExample").master("local[*]").getOrCreate()

df = spark.read \
   .format("jdbc") \
   .option("url", "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb") \
   .option("dbtable", "b1") \
   .option("user", "consultants") \
   .option("password", "WelcomeItc@2022") \
   .option("driver", "org.postgresql.Driver") \
   .load()

df.show()

# Stop the Spark session
spark.stop()
