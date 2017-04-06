# Q1_P2
# • Use ‘vehicle_collisions’ data set.
# • For each borough, find out distribution of each collision scale. (One carinvolved? Two? Three? or more?) (From 2015 to present)
#• Display a few rows of the output use df.head().
#• Generate a csv output with five columns ('borough', 'one-vehicle', 'twovehicles', 'three-vehicles', 'more-vehicles')


import pandas as pd
from pandas import DataFrame

raw_data = pd.read_csv('Data/vehicle_collisions.csv')
# raw_data.head(4)
# to get the data columns that we need
raw_data = raw_data[['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE']]
raw_data.head(6)


# to calculate how many involved vehicle
raw_data['VEHICLE COUNT'] = raw_data.count(axis =1)-1
raw_data.head()

# keep the columns we need
raw_data = raw_data[['BOROUGH', 'VEHICLE COUNT']]
raw_data.head(3)


# to clean the raw_data deleting 0 in VEHICLE COUNT
raw_data = raw_data[raw_data['VEHICLE COUNT'] != 0]
raw_data.head(6)


# to clean the raw_data deleting NAN in BOROUGH
raw_data = raw_data[pd.notnull(raw_data['BOROUGH'])]
raw_data.head(6)


# raw_data.columns.dtype   dtype('O')
# change datatype and make VEHICLE COUNT >3 become 3+
raw_data['VEHICLE COUNT'] =raw_data['VEHICLE COUNT'].apply(lambda x : str(x) if x < 4 else '3+')
raw_data.head(6)


# to groupt borough and vehicle count, then calculate the occurance of each count in each borough
raw_data2 = raw_data.groupby(['BOROUGH','VEHICLE COUNT'],as_index=False).size().reset_index()


raw_data2 .head(6)

# to use Borough as index,vehicle count as columns
raw_data3 = raw_data2.pivot(index='BOROUGH',columns='VEHICLE COUNT',values=0)

raw_data3

# change thre columns name
raw_data3.columns = ['ONE_VEHICLE_INVOLVED', 'TWO_VEHICLE_INVOLVED', 'THREE_VEHICLE_INVOLVED', 'MORE_VEHICLE_INVOLVED']
raw_data3

final_data = raw_data3.reset_index()
final_data

# to output the result
final_data.to_csv('Output/Q1_P2.csv',index = False,header=True)










