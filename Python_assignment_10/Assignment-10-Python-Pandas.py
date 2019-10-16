import pandas as pd

data = pd.read_csv('EmployeeAttrition.csv')

print(data.head())

#Check the head of the DataFrame.
print(data.head())

#Q1: Find the number of entries/rows and columns in the data.

#Q2: What is the average Monthly Income?

#Q3: What is the highest amount of HourlyRate ?

#Q4: What is the Department, JobRole, MaritalStatus and OverTime of EmployeeNumber 10?


#Q5: What is the Employee ID of highest MonthlyIncome paid employee?


#Q6: What is the average(mean) DailyRate group by Age for all Employees whose age is greater than 58. (hint: use groupby function)


#Q7: How many unique EducationField are there?


#Q8: What are the top 5 most common JobRole?


#Q9: How many JobRoles represented by less than 100 employees?


#Q10: What is the correlation between Education and JobSatisfaction?
