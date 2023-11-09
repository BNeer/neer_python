import pandas as pd
from sqlalchemy import create_engine


# Replace with your MySQL database connection information
db_username = "consultants"
db_password = "WelcomeItc@2022"
#print(db_password)
db_host = "ec2-3-9-191-104.eu-west-2.compute.amazonaws.com"
db_port = "5432"
db_name = "testdb"


# CSV file path
csv_file_path = "C:/Users/nbhar/Downloads/employee_data.csv"

# Create a DataFrame from the CSV file
df = pd.read_csv(csv_file_path)

# Create a database connection
engine = create_engine(f"postgresql+psycopg2://consultants:WelcomeItc%402022@ec2-3-9-191-104.eu-west-2.compute.amazonaws.com/testdb")

# Write the DataFrame to the MySQL database
df.to_sql(name="EMPLOYEETEST", con=engine, if_exists="replace", index=False)

# Close the database connection
engine.dispose()

print(f"Table 'your_table_name' created in the database '{db_name}' with data from CSV.")
