from pyspark.sql import SparkSession
#import urllib
#import urllib.parse
#import re


#jar_path = 'C:\\postgresql-42.6.0.jar'



spark = SparkSession.builder \
    .appName("PostgresToHive") \
    .enableHiveSupport() \
    .getOrCreate()

#pssword=urllib.parse.quote("WelcomeItc@2022")



#my_password = "WelcomeItc@2022"
#escaped_password = re.escape(my_password)

#pg_url = "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"
#pg_properties = {
#    "user": "consultants",
#    "password": escaped_password,
#    "driver": "org.postgresql.Driver"
#}

#pg_df = spark.read \
#    .jdbc(url=pg_url, table="EMPLOYEETEST", properties=pg_properties)

# Uncomment and customize these lines if you want to write to Hive
# pg_df.write \
#     .mode("overwrite") \
#     .saveAsTable("bduk.EMPLOYEETEST212")

# spark.stop()

dburl="jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"


# The value of postgres_query will be passed to argument .option of line 46 below
postgres_query = "(select * from b1) AS B1"

df = spark.read.format("jdbc").option("url",dburl) \
    .option("driver", "org.postgresql.Driver").option("dbtable", postgres_query) \
    .option("user", "consultants").option("password", "WelcomeItc@2022").load()


#df = spark.read \
#    .format("jdbc") \
#    .option("url", "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb") \
#    .option("dbtable", "testdb") \
#    .option("user", "consultants") \
#    .option("password", "WelcomeItc@2022") \
#    .option("driver", "org.postgresql.Driver") \
#    .load()


df.show()
