# Question1_Part1
# Use ‘vehicle_collisions’ data set.
# • For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# • Display a few rows of the output use df.head().
# • Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’,‘Percentage’)


import pandas as pd
from pandas import DataFrame

row_data = pd.read_csv('Data/vehicle_collisions.csv')
row_data.tail()

#to get the data of 2016
data2016 = row_data[row_data.apply(lambda x : x['DATE'].split('/')[2] == '16',axis = 1)]
data2016.head()

# get total number of month in NYC
NYU_total_count = data2016['DATE'].apply(lambda x : x.split('/')[0]).value_counts()
NYU_total_count

# get total number of each month in Manhattan
Man = data2016[data2016.apply(lambda x : x['BOROUGH'] == 'MANHATTAN',axis = 1)]
Manhattan_Month_total = Man['DATE'].apply(lambda x : x.split('/')[0]).value_counts()

Manhattan_Month_total

# to put the Manhattan_Month_total and NYU_total_count into a DataFrame
output_df = pd.concat([Manhattan_Month_total,NYU_total_count],axis =1)
output_df.columns=['MANHATTAN', 'NYC']
#output_df
output_df.index = output_df.index.map(int)
#sort the data according the index
output_df.sort_index(inplace = True)
# output_df.index.dtype   # from dtype('0')  to dtype('int64)
output_df.columns.name = 'MONTH'
output_df

# sum up and get total in the last row
output_df2 = output_df.append(output_df.sum(numeric_only=True), ignore_index=True)
output_df2.head()

# to calculate the percentage
output_df2['PERCENTAGE'] = output_df2['MANHATTAN']/output_df2['NYC']
output_final=output_df2.rename(index={0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May', 5: 'Jun', 6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov', 11: 'Dec', 12: 'Total'})
output_final.head()

# to outpuyt the result to a csv file
output_final.to_csv('Output/Q1_P1.csv',index=True,header=True,index_label='MONTH')









