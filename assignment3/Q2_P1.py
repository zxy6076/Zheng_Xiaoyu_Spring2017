# Q2_PART ONE
# • Use 'employee_compensation' data set.
# • Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# • Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# • Display a few rows of the output use df.head().
# • Generate a csv output.

import pandas as pd
from pandas import DataFrame

raw_data = pd.read_csv('Data/employee_compensation.csv')
raw_data.head(6)

# to clean the data
raw_data = raw_data[['Organization Group','Department','Total Compensation']]
raw_data.head(6)

# to group by organization and department to get the mean 
raw_data2 = raw_data.groupby(['Organization Group','Department'],as_index=False).mean()
raw_data2.head(6)

final_data = raw_data2.sort_values(['Organization Group','Total Compensation'], ascending = False)
final_data.head(6)

# to output the result to a csv file
final_data.to_csv('Output/Q2_P1.csv',header = True,index=False)











