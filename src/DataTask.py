import pandas as pd
#Read the "employee_data.csv" file and display its contents.
df = pd.read_csv('C:/Users/nbhar/Downloads/employee_data.csv')
print(df.to_string())

#Calculate and display the total number of rows and columns in the CSV file. Display the first 5 rows of data.
num_rows, num_columns = df.shape
print(f'Total number of rows: {num_rows}')
print(f'Total number of collumns: {num_columns}')
print('First 5 rows of data:')
print(df.head(5))

#Filter the data to include only rows where the "Age" column is greater than 30. Display the filtered data.
filtered_data = df[df['Age'] > 30]
print('Filtered data where Age is greater than 30:')
print(filtered_data)

#Sort the data in ascending order by the "FirstName" column and in descending order by the "Salary" column. 
#Display the sorted data.
data_order = df.sort_values(by=['FirstName','Salary'], ascending=[True, False])
print(data_order)

#Calculate and display the average, minimum, and maximum values of the "Salary" column.
data_average = df['Salary'].mean ()
data_average
data_maximum = df['Salary'].max ()
data_maximum
date_minimum = df['Salary'].min ()
date_minimum

#Add a new employee to the CSV file with a unique EmployeeID and other details. Save the updated CSV file.
new_employee_data = {
    'EmployeeID': 97,
    'FirstName': 'New_first_name',
    'LastName': 'new_surname',
    'Age': 35,
    'Department': 'IT',
    'Salary': 50000,
    'Status': 'Active'
}
df = pd.concat([df,pd.DataFrame(new_employee_data,index=[0])])
df.to_csv('C:/Users/islam/Downloads/employee.data.csv', index=False, header=False)


#Update the salary of a specific employee in the CSV file based on their EmployeeID. Save the updated CSV file.
specific_employee_id = 95
new_salary = 55000

df.loc[df['EmployeeID'] == specific_employee_id, 'Salary'] = new_salary
df.to_csv('C:/Users/islam/Downloads/employee.data.csv', index=False, header= False)
df

#Delete all rows with the "Status" column value "Inactive" from the CSV file. Save the updated CSV file.
df = df[df['Status'] != 'Inactive']
df.to_csv('C:/Users/islam/Downloads/employee.data.csv', index=False)

#Export all rows where the "Department" column is "HR" to a new CSV file named "hr_data.csv."
hr_data = df[df['Department'] == 'HR']
hr_data.to_csv('C:/Users/islam/Downloads/hr_data.csv', index=False)

#Create a new column "Full Name" by combining the "FirstName" and "LastName" columns. Display the modified dataset.
df['Full Name'] = df['FirstName'] + ' ' + df['LastName']

#Convert the "Salary" column from dollars to euros (assume an exchange rate) and display the updated data.
exchange_rate = 0.85
df['Salary'] = df['Salary']*exchange_rate

#Calculate and display the count of employees in each department.
department_counts = df['Department'].value_counts()
department_counts

#Find the employees with the highest and lowest salaries and display their details.
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

plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Employees')
plt.title('Age Distribution of Employees')
plt.show()