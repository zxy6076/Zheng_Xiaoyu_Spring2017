# Fianl Report ----Disaster of Titanic


## Part one ---load and preview the data
```import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
%matplotlib inline
```

### see the variables, then to read the variable description below to understand them. 
 raw_data = pd.read_csv('..\data\Titanic.csv',na_values='N/A')  #,index_col=0
 raw_data.head()
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_head.png) 

 From this picture we've got a sense of our variables, their class type, and the first few observations of each.And we can know there is two types of variables--Numerical feature and Categorical feature.

### to get some numerical variables
 raw_data.describe()
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_num_des.png)
 
### to get some categorical variables 
 raw_data.describe(include=['O'])
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_cate_des.png)

### to test whether have null values
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

 Embarked is categorical,so to choose the most frequent occurance which is s
 raw_data['Embarked'] = raw_data['Embarked'].fillna('S')


 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/ana_fianl_20s.png)
 

 
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_1/raw_data_scatter.png)
 ![wrong]()
 
 

