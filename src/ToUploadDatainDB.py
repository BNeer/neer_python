import pandas as pd
from sqlalchemy import create_engine

# Replace with your MySQL database connection information
db_username = "root"
db_password = "root123!"
db_host = "localhost"
db_port = 3306
db_name = "testdb"

# CSV file path
csv_file_path = "C:/Users/nbhar/Downloads/employee_data.csv"

# Create a DataFrame from the CSV file
df = pd.read_csv(csv_file_path)

# Create a database connection
engine = create_engine(f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

# Write the DataFrame to the MySQL database
df.to_sql(name="employee2", con=engine, if_exists="replace", index=False)

# Close the database connection
engine.dispose()

print(f"Table 'your_table_name' created in the database '{db_name}' with data from CSV.")
