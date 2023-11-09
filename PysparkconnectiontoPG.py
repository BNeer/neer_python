from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("PostgresToHive") \
    .enableHiveSupport() \
    .getOrCreate()

dburl="jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"

# The value of postgres_query will be passed to argument (.option) of line 15 below
postgres_query = "(select * from b1) AS B1"

df = spark.read.format("jdbc").option("url",dburl) \
    .option("driver", "org.postgresql.Driver").option("dbtable", postgres_query) \
    .option("user", "consultants").option("password", "WelcomeItc@2022").load()


df.show()

# Stop the Spark session
spark.stop()
