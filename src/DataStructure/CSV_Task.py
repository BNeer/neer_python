import pandas as pd
df = pd.read_csv('C:/Users/nbhar/Downloads/employee_data.csv')
print(df.to_string()) 



##Calculate and display the total number of rows and columns in the CSV file. 
num_rows, num_columns = df.shape
print(f'Total number of rows: {num_rows}')
print(f'Total number of collumns: {num_columns}')


##Display the first 5 rows of data###
print('First Five rows of data:')
print(df.head(5))


#Filter the data to include only rows where the "Age" column is greater than 30. Display the filtered data.
filtered_data = df[df['Age'] > 30]
print('Filtered data where Age is greater than 30:')
print(filtered_data)


#Sort the data in ascending order by the "FirstName" column 
# and in descending order by the "Salary" column. Display the sorted data.
data_order = df.sort_values(by=['FirstName','Salary'], ascending=[True,False])
print(data_order)

#Calculate and display the average, minimum, and maximum values of the "Salary" column.
minimum_salary = df['Salary'].min()
print(minimum_salary)

maximum_salary = df['Salary'].max()
print(maximum_salary)

average_salary = df['Salary'].mean()
print(average_salary)


#####  Data Manipulation: ####
# 1. Add a new employee to the CSV file with a unique EmployeeID and other details. 
# Save the updated CSV file.

new_employee_data = {
    'EmployeeID' : 97,
    'FirstName' : 'Max',
    'LastName' : 'Well',
    'Age' : 36,
    'Department' : 'Finance',
    'Salary' : 72000,
    'Status' : 'Active'
}

df = pd.concat([df,pd.DataFrame(new_employee_data,index=[0])])
print(df)
df.to_csv('C:/Users/nbhar/Downloads/employee.data.csv', index=False, header=False)


df_1 = pd.DataFrame(new_employee_data,index=[0])
df_1.to_csv('C:/Users/nbhar/Downloads/employee.data.csv', mode='a', index=False, header=False)



#### 
#  2. Update the salary of a specific employee in the CSV file based on 
# their EmployeeID. Save the updated CSV file.

df.loc[df["EmployeeID"] == 97, "Salary"] = 12000
df.to_csv('C:/Users/nbhar/Downloads/employee_data.csv', index=False, header=False)


#Delete all rows with the "Status" column value "Inactive" from the CSV file. 
# Save the updated CSV file.
df = df.drop(df[df.FirstName == 'Max'].index)
df.to_csv('C:/Users/nbhar/Downloads/employee_data.csv', index=False, header=False)

#Export all rows where the "Department" column is "HR" to a new CSV file named "hr_data.csv."
hr_data = df[df['Department'] == 'HR']
print(hr_data)
hr_data.to_csv('C:/Users/nbhar/Downloads/hr_data.csv', index=False)


#Create a new column "Full Name" by combining the "FirstName" and "LastName" columns.
# Display the modified dataset.
df['FullName'] = df['FirstName'] + " " +df['LastName']


#Convert the "Salary" column from dollars to euros (assume an exchange rate) 
# and display the updated data.
exchange_rate = 0.65
df['Salary'] = df['Salary'] * exchange_rate
print(df)


### Data Exploration:##
# 1. Calculate and display the count of employees in each department.
department_counts = df['Department'].value_counts()
print(department_counts)


# Find the employees with the highest and lowest salaries and display their details.
# df = df['Salary'].max()
# df = df['Salary'].min()

# print(df)
# print("lowest salary record : ")
# print(df[df['Salary'] == df['Salary'].min()])
# print("highest salary record : ")
# print(df[df['Salary'] == df['Salary'].max()])

most_salaries = df.loc[df['Salary'].idxmax()]
least_salaries = df.loc[df['Salary'].idxmin()]
least_salaries
most_salaries


#Calculate and display the average age of employees in each department.
average_age_by_department = df.groupby('Department')['Age'].mean()
print(average_age_by_department)

#Calculate the total payroll for each department and display it in descending order.
total_payroll_fordepartment = df.groupby('Department')['Salary'].sum()
print(total_payroll_fordepartment)

#Identify and display the top 5 highest-paid employees.
top5_highest_employees = df.sort_values (by=['Salary'], ascending = [False]).head()
print(top5_highest_employees)

#Group the data by "Department" and calculate the total salary expenditure for each department.
salary_expenditure_for_department =  df.groupby('Department')['Salary'].sum()
print(salary_expenditure_for_department)

#Calculate the age distribution of employees and create a histogram.

import matplotlib.pyplot as plt

plt.hist(df['Age'], bins=10, color='red', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Employees')
plt.title('Age Distribution of Employees')
plt.show()



#######################
# To create connection to dbbase
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqlconnector://root:root123!@localhost:3306/testdb", echo=True)
my_conn = my_conn.connect()

#To create a table in Mysql having all CSV file content
df.to_sql(con=my_conn,name='Employee',if_exists='append')

# To read the table 
db_df = pd.read_sql_table('employee', my_conn)
print(db_df)



