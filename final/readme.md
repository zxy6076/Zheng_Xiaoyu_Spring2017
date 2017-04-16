# Fianl Report ----Disaster of Titanic


## Part one ---load and preview the data
 using Titanic.csv
```import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
%matplotlib inline
```

### 1.1 See the variables, then to read the variable description below to understand them. 
 ```raw_data = pd.read_csv('..\data\Titanic.csv',na_values='N/A')
 raw_data.head()
 ```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_head.png) 

 From this picture we've got a sense of our variables, their class type, and the first few observations of each. And we can know there is two types of variables--Numerical feature and Categorical feature.

### 1.2 To get some numerical variables
 raw_data.describe()
 
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_num_des.png)
 
### 1.3 To get some categorical variables 
 raw_data.describe(include=['O'])
 
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_cate_des.png)

### 1.4 To test whether have null values
 raw_data.isnull().sum()
 ```PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64
```
 From the data above, there is 3 types of null values.

## Part two ---Deal with different type null value
1. Embarked 
2. Cabin 
3. Age

### 2.1 Embarked is categorical,so to choose the most frequent occurance which is s
 raw_data['Embarked'] = raw_data['Embarked'].fillna('S')

### 2.2 Cabin is also categorical but has lots of nulls, so drop them
 raw_data.drop('Cabin',axis=1,inplace=True)

### 2.3 Age is numerical,so to fill the null values using median value
 raw_data.Age=raw_data['Age'].fillna(raw_data['Age'].mean())

### 2.4 Check null values again
 raw_data.isnull().sum()
``` PassengerId    0
    Survived       0
    Pclass         0
    Name           0
    Sex            0
    Age            0
    SibSp          0
    Parch          0
    Ticket         0
    Fare           0
    Embarked       0
    dtype: int64
```

## Part there ---Analysis data(Five analysis)

### 3.1   Analysis one----This analysis is about the probability of death in Titanic relating age

 This scatter can detect whether having wrong data, because the value of Survived is either 0 (dead) or 1 (survived) 
```plt.scatter(raw_data.Age,raw_data.Survived,alpha=0.02)
plt.xlabel('Age')
plt.ylabel('Survied')
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_scatter.png)

- Because Age data is discrete, so need to calculate the probability of death at the same age bin (divide Age into 20 bins).
 
 bins = np.linspace(raw_data.Age.min(),raw_data.Age.max(),20)
 
- to group according to whether in the same bin
 
groups = raw_data.groupby(np.digitize(raw_data.Age,bins))
 
- calculate the probability 
 
 final_data = groups[['Age','Survived']].mean()

- Finally,plot the data and output the plot
```plt.plot(final_data.Age,final_data.Survived,'bo-')
plt.ylim(-0.2,2)
plt.xlim(0,90)
plt.xlabel('Age')
plt.ylabel('Probability')
plt.savefig('ana_fianl_20s.png')
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/ana_fianl_20s.png)
 

 

 ![wrong]()
 
 

