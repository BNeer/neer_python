from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName("JoinRDDDataFrame").getOrCreate()

# Step 1: Create an RDD of (employee_id, department_id) pairs
rdd = spark.sparkContext.parallelize([(1, "HR"), (2, "IT"), (3, "Finance"), (4, "IT"), (5, "Finance")])
print(rdd)

# Step 2: Read the CSV file into a DataFrame
csv_file = "/tmp/bduk1710/Neeraj/employee_data.csv"
df = spark.read.csv(csv_file, header=True)  # Assuming the first row contains headers

# Rename the column if necessary
df = df.withColumnRenamed("EmployeeID", "employee_id")

# Cast the "salary" column to a DoubleType
df = df.withColumn("salary", col("salary").cast("double"))

# Step 3: Join the RDD and DataFrame on the employee_id
rdd_df = rdd.map(lambda x: (x[0], x[1])).toDF(["employee_id", "department_id"])  # Transform the RDD to match the DataFrame schema
print(" Step 3 : ", rdd_df)
joined_df = df.join(rdd_df, "employee_id")
print("Step 3.1 :", joined_df)

# Step 4: Calculate the total salary expense for each department
total_salary_expense = joined_df.groupBy("department_id").sum("salary").withColumnRenamed("sum(salary)", "total_salary")

# Step 5: Find the department with the highest total salary expense
max_salary_dept = total_salary_expense.orderBy("total_salary", ascending=False).first()

# Display the result
print("Total Salary Expense for Each Department:")
total_salary_expense.show()

print("Department with the Highest Total Salary Expense:")
print(max_salary_dept)

# Stop the SparkSession
spark.stop()