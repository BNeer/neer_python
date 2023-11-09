from pyspark.sql import SparkSession
from pyspark.sql.functions import avg,sum
from pyspark.sql.functions import format_number

# Create a Spark session
#spark = SparkSession.builder.appName("EmployeeDataFrame").getOrCreate()
spark = SparkSession.builder \
    .appName("LocalSparkSession") \
    .master("local[*]") \
    .getOrCreate()


# Load the CSV file into a DataFrame
#csv_path =  "file:///C:/Users/nbhar/Downloads/employee_data.csv"
inputFile = "/tmp/bduk1710/Neeraj/employee_data.csv"
employee_df = spark.read.csv(inputFile, header=True, inferSchema=True)

# 2.1 Calculate the average age of employees in each department
avg_age_by_department = employee_df.groupBy("department").agg(avg("age").alias("avg_age"))

# Format the 'avg_age' column to display only 2 decimal places
result_df = avg_age_by_department.withColumn("avg_age", format_number(avg_age_by_department["avg_age"], 2))

# Show the result
result_df.show()


# 2.2 Find the total salary expense for each department

# Calculate the total salary expense for each department
total_salary_expense = employee_df.groupBy("department").agg(sum("salary").alias("total_salary_expense"))

# Show the result
total_salary_expense.show()

#2.3 Filter out employees with a salary above a certain threshold (e.g., $50,000) and create a new DataFrame
salary_threshold = 50000  # Set the salary threshold

# Filter out employees with a salary above the threshold
filtered_employee_df = employee_df.filter(employee_df["salary"] >= salary_threshold)

# Show the filtered DataFrame
filtered_employee_df.show()


# 2.4 Calculate the average salary of the filtered employees
avg_salary_filtered = filtered_employee_df.agg(avg("salary").alias("avg_salary_filtered"))

# Format the 'avg_salary_filtered' column to display only 2 decimal places
result_df = avg_salary_filtered.withColumn("avg_salary_filtered", format_number(avg_salary_filtered["avg_salary_filtered"], 2))

# Show the result
result_df.show()

# 2.5 Count the number of employees in each department in the filtered DataFrame.
employee_count_by_department = filtered_employee_df.groupBy("department").count()

# Show the result
employee_count_by_department.show()

# Stop the SparkSession
spark.stop()


