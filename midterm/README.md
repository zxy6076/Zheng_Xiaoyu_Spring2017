# Final Midterm Report

# Question1

# Analysis_1
1. To find top 10 used word in 1. of sent email 
2. outputing the result to a csv file

# Analysis_2
1. dealing with the raw data
2. finding the number of user

# Analysis_3


# Question2

# Data_download

1. article search---q= japan, begin_data = 19900601, end_data=19900630
2. article search---q= japan, begin_data = 20100601, end_data=20100630
3. archive search----year= 1990, month=6
4. archive search----year = 2010, month=6

# Analysis_1
1. using NYT archive API in 1990_06
2. finding section_name of articel in 1990_06
3. calculating frequency of each section_name and getting top 20
4. generating a .csv to show the result

First, I get all the section_name from the NYT data, and then put them into a list.
Secondly, I calculate the frequency of each section_name and get top 20
Finally , I output the top20 to a csv file which is stord as que2\ana_1\archive_section_name_1990_06.csv

From the result , we can conclude that the Business Section is the most posted one


# Analysis_2

1. using NYT archive API in 2010_06
2. finding value of name(=subject) of keywords in 2010_06
3. calculating frequency of each section_name and getting top 20
4. generating a csv file to store result

First, I get all the value of name from the NYT data, and then put them into a list.
Secondly, I calculate the frequency of each value_subject and get top 20
Finally , I output the top20 to a csv file which is stord as que2\ana_2\archive_value_subject_2010_06.csv

From the result , we can conclude that the name = subject and value = Accidents and Safety is the most posted one

# Analysis_3

1. using NYT API for article_search with query = japan  to get year =1990 and year = 2010
2. comparing year=1990 and year =2010 in section_name
3. finding the intresting of the two year and also seeing whether changeing
4. combing the two results to one csv file and storeing the result

First, dealing with the two raw data input of japan
Second, getting the name and frequency in year=1990 and year = 2010
Finally,combing the two outputs of 1990 and 2010 into one csv file

From the result , we can see that the Business Section is the most posted one in 1990 and 2010 of Japan respectively 102,67.
In 1990,World is in the second position with 21 posted while in the fourth position with 22 posted in 2010.
While the Sports is in different position respectively 4th in 1990 with 15 posted,2th in 2010 with 63 posted.
So i conclude that the Japanses are more concerning about the leisure time than before.
