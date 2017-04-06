# Q2_PART TWO
# • Use 'employee_compensation' data set.
# • Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# • Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# • For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# • Display the top 5 Job Families according to this percentage value using df.head().
# • Write the output (jobs and percentage value) to a csv





import pandas as pd
from pandas import DataFrame

# read raw data
raw_data = pd.read_csv('Data/employee_compensation.csv')
raw_data.head(6)

# filter raw data by Calendar
raw_data = raw_data[raw_data['Year Type']=='Calendar']
raw_data.head(6)


# to keep the columns that we need
raw_data = raw_data[['Job Family', 'Employee Identifier' , 'Salaries', 'Overtime', 'Total Benefits', 'Total Compensation']]
raw_data.head(6)

# to calculate the average of ever person by grouping
raw_mean = raw_data.groupby(['Job Family', 'Employee Identifier'],as_index=False).mean()
raw_mean.head(6)

# to find the people whose overtime salary is greater than 5% of salaries 
raw_overtime = raw_mean[raw_mean['Overtime'] > raw_mean['Salaries'] *0.05]
raw_overtime.head(6)

# delete the unnecessary columns
raw_overtime2 = raw_overtime[['Job Family', 'Total Benefits', 'Total Compensation']]
raw_overtime2.head(6)

# to group by job family
raw_JF = raw_overtime2.groupby(['Job Family'],as_index= False).mean()
raw_JF.head(6)

# to calculate  the percentage of total benefits with respect to total compensation and sort
raw_JF['Percent_Total_Benefit'] = raw_JF['Total Benefits']/raw_JF['Total Compensation'] * 100
final_data = raw_JF.sort_values(by = 'Percent_Total_Benefit',ascending=False)

fianl_data.head(6)

# to output the result to a csv file
final_data.to_csv('Output/Q2_P2.csv',index = False,header=True)




