# Q4_PART ONE
# • Use ‘movies_awards’ data set.
# • You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
# • The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# • You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award.
# • If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated).
# • Create two separate columns for each award category (won and nominated).
# • Write your output to a csv file. (Sample output is given in next page)

import pandas as pd
from pandas import DataFrame

raw_data = pd.read_csv('Data/movies_awards.csv')
raw_data.head(6)

# to clean the data
raw_data= raw_data[['imdbID','Awards']]
raw_data2 =raw_data.dropna()
raw_data2.head(6)

import re
# to calculate the number of wins,categories can be Oscar,BAFTA etc
def calculate_wins(categories,row):
    pattern = r'Won (\d+) '+ categories
    numbers = re.findall(pattern,row)
    if len(numbers) > 0:return numbers[0]
    else:return '0'

# to calculate the number of nominations,categories can be Oscar,BAFTA etc
def calculate_nominations(categories,row):
    pattern = r'Nominated for (\d+) '+ categories
    numbers = re.findall(pattern,row)
    if len(numbers) > 0:return numbers[0]
    else:return '0'

# to calculate the total win
def calculate_total_wins(row):
    pattern = r'(\d+) wins'
    total_wins = int(row['Oscar_Won'])+int(row['Golden_Globe_Won'])+int(row['BAFTA_Won'])+int(row['Prime_Won'])
    numbers = re.findall(pattern,row['Awards'])
    if len(numbers) > 0:return int(numbers[0])+ total_wins
    else: return total_wins

# to calculate the total nomination
def calculate_total_nominations(row):
    pattern = r'(\d+) nominations'
    total_nominations = int(row['Oscar_Nominated'])+int(row['Golden_Globe_Nominated'])+int(row['BAFTA_Nominated'])+int(row['Prime_Nominated'])
    numbers = re.findall(pattern,row['Awards'])
    if len(numbers) > 0:return int(numbers[0])+ total_nominations
    else: return total_nominations

# to find Oscar_won
raw_data2['Oscar_Won'] = raw_data2.apply(lambda x:calculate_wins('Oscar',x['Awards']),axis = 1)
raw_data2.head(6)

# to find Golden_Globe_Won
raw_data2['Golden_Globe_Won'] = raw_data2.apply(lambda x:calculate_wins('Golden',x['Awards']),axis = 1)
raw_data2.head(6)

# to find BAFTA_Won
raw_data2['BAFTA_Won'] = raw_data2.apply(lambda x:calculate_wins('BAFTA',x['Awards']),axis = 1)
raw_data2.head(6)

# to find Prime_Won
raw_data2['Prime_Won'] = raw_data2.apply(lambda x:calculate_wins('Prime',x['Awards']),axis = 1)
raw_data2.head(6)

# to find Oscar_Nominated
raw_data2['Oscar_Nominated'] = raw_data2.apply(lambda x:calculate_nominations('Oscar',x['Awards']),axis = 1)
raw_data2.head(6)

# to find Golden_Globe_Nominated
raw_data2['Golden_Globe_Nominated'] = raw_data2.apply(lambda x:calculate_nominations('Golden',x['Awards']),axis = 1)
raw_data2.head(6)

# to find BAFTA_Nominated
raw_data2['BAFTA_Nominated'] = raw_data2.apply(lambda x:calculate_nominations('BAFTA',x['Awards']),axis = 1)
raw_data2.head(6)

# to find Prime_Nominated
raw_data2['Prime_Nominated'] = raw_data2.apply(lambda x:calculate_nominations('Prime',x['Awards']),axis = 1)
raw_data2.head(6)

# finally to calculate the total of won and Nominated seperately
raw_data2['Total_Wins'] = raw_data2.apply(calculate_total_wins,axis=1)

raw_data2['Total_Nominations'] = raw_data2.apply(calculate_total_nominations,axis=1)

raw_data2.head(7)

# output the result to a csv file
raw_data2.to_csv('Output/Q4_P1.csv',index=False,header=True)

