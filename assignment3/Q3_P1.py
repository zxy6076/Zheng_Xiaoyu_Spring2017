
# Q3_PART ONE
# • Use ‘cricket_matches’ data set.
# • Calculate the average score for each team which host the game and win the game.
# • Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# • Display a few rows of the output use df.head()
# • Generate a csv output




import pandas as pd
from pandas import DataFrame

raw_data = pd.read_csv('Data/cricket_matches.csv')
raw_data.head(6)

#  to check if the host team won the game
raw_data = raw_data[raw_data['home'] == raw_data['winner']]
raw_data.head(6)

# to clean the data 
raw_data2 = raw_data[['home', 'innings1' , 'innings2', 'innings1_runs', 'innings2_runs']]
raw_data2.head(6)

# according to the  innings_1 runs and innings_2 runs, to check if the host team won the game, check which innings they played in 
def choose_innings(row):
    if row['home'] == row['innings1']:return row['innings1_runs']
    else: return row['innings2_runs']



# to take the runs scored in that innings
raw_data2['Score'] = raw_data2.apply(choose_innings,axis = 1)
raw_data2.head(6)

# delete the unnecessary columns
raw_innings = raw_data2[['home','Score']]
raw_innings.head(6)


# finally, to calculate the average score of each team
final_data = raw_innings.groupby(['home'],as_index=False).mean()
final_data.head(6)


# to output the result to a csv file
final_data.to_csv('Output/Q3_P1.csv',index=False,header=True)











