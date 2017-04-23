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

### 3.1   Analysis One----This analysis is about the probability of death in Titanic relating age

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

### 3.2   Analysis Two----To find the highest rate of survived female by ageband
 3.2.1 Load data
 ```
 raw_data = pd.read_csv('..\data\Titanic.csv',na_values='N/A')
raw_data.head()
```
 3.2.2 Deal with null values
```
raw_data['Embarked'] = raw_data['Embarked'].fillna('S')
raw_data.drop('Cabin',axis=1,inplace=True)
raw_data.Age=raw_data['Age'].fillna(raw_data['Age'].mean())
```

 3.2.3 To draw many pictures in one plot
```
fig = plt.figure(figsize=(13,7))
fig.set(alpha = 0.2)
```
 First one is about the count of Pclass
 ```
 plt.subplot2grid((2,3),(0,0))
raw_data.Pclass.value_counts().plot(kind='bar')
plt.ylabel('Count')
plt.xlabel('Class')
plt.title('Pclass')
```
 Second one is about the count of Survived
```
plt.subplot2grid((2,3),(0,1))
raw_data.Survived.value_counts().plot(kind='bar')
plt.ylabel('Count')
plt.title('Survived')
```

 Third one is about the distribution of age in class
```
plt.subplot2grid((2,3),(1,0),colspan=2)
raw_data.Age[raw_data.Pclass==1].plot(kind='kde')
raw_data.Age[raw_data.Pclass==2].plot(kind='kde')
raw_data.Age[raw_data.Pclass==3].plot(kind='kde')
plt.xlabel('Age')
plt.ylabel('Density')
plt.title('Distribution of age by class')
plt.ylim(-0.01)
plt.xlim(0,100)
plt.legend(('1','2','3'),loc='best')
```

 Last one is about the count of each Embarked
```
plt.subplot2grid((2,3),(1,2))
raw_data.Embarked.value_counts().plot(kind='bar')
plt.title('Count of each Embarked')
plt.ylabel("Count")
plt.savefig('ana_2_multiple.png')
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/ana_2_multiple.png)

 3.2.4 Keep the columns we need
```
deal_data = raw_data[['Survived','Sex','Age']]
deal_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/deal_data.png)

 3.2.5 Delete data which sex is male 
```
female_data = deal_data[deal_data.Sex == 'female']
female_data.Age= female_data['Age'].fillna(female_data['Age'].mean())
female_data.isnull().sum()
female_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/female_data.png)

 3.2.6 Change the type of Age into str
 ```
 female_data['Age']=female_data['Age'].astype(int)
female_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/female_data_int.png)


 3.2.7 To divide age into 3 band(bins)
 ```
 female_data['AgeBand_3'] = pd.cut(female_data['Age'],3)
female_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/AgeBand_31.png)

 Sort the data according to AgeBand
```
final_data_3=female_data[['AgeBand_3','Survived']].groupby(['AgeBand_3'],as_index=False).mean().sort_values(by='AgeBand_3',ascending=True)
final_data_3
``` 
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/AgeBand_32.png) 
 
3.2.8 To divide age into 5 band(bins)
 ```
 female_data['AgeBand_5'] = pd.cut(female_data['Age'],5)
female_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/AgeBand_51.png)

 Sort the data according to AgeBand
```
final_data_5=female_data[['AgeBand_5','Survived']].groupby(['AgeBand_5'],as_index=False).mean().sort_values(by='AgeBand_5',ascending=True)
final_data_5
``` 
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/Ageband_52.png) 
 
 3.2.9 To divide age into 7 band(bins)
 ```
 female_data['AgeBand_7'] = pd.cut(female_data['Age'],7)
female_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/Ageband_71.png)

 Sort the data according to AgeBand
```
final_data_7=female_data[['AgeBand_7','Survived']].groupby(['AgeBand_7'],as_index=False).mean().sort_values(by='AgeBand_7',ascending=True)
final_data_7
``` 
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/Ageband_72.png) 
         
 3.2.10 Find age >50
 
 female_data[female_data['Age'] > 50]
 
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_2/Age_50above.png)
 
 3.2.11 Summary
 
 From this picture above, we can see the age between 50 and 63 is the highest survived. Because the number of female is small and most of them is survived. For other ageband, the probability is greater than 50%. So the rate of women\`s salvation is higher. 
 
 
 
 
 
 
### 3.3   Analysis Three---- Anlysis Cabin with survived 

 3.3.1 Load data
```
raw_data = pd.read_csv('..\data\Titanic.csv',na_values='N/A')
raw_data.head()
```
 3.3.2 Extract the needed attributes 
 ```
 deal_data = raw_data[['PassengerId','Survived','Pclass','Cabin']]
deal_data.head()
 ```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/need_attribute.png) 

 3.3.3 Check whether the null value of Cabin influence the Survival
 ```
 Survived_cabin = deal_data.Survived[pd.notnull(deal_data.Cabin)].value_counts()
Survived_nullcabin = deal_data.Survived[pd.isnull(deal_data.Cabin)].value_counts()
draw = DataFrame({'Have_cabin': Survived_cabin, 'Null_cabin' : Survived_nullcabin}).T
draw.head()
``` 
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/check_null.png) 

 3.3.4 Plot
 ```
 fig = plt.figure(figsize=(12,10))
fig.set(alpha= 0.2)

draw.plot(kind='bar',stacked = True)
plt.title('Survival of Cabin')
plt.xlabel('Cabin record?')
plt.ylabel('Count')
plt.savefig("Survival of Cabin.png")
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/Survival%20of%20Cabin.png)

3.3.5 Chek null values 

 deal_data['Cabin'].isnull().sum() -----687

3.3.6 Replace Null value

 From above picture, the null value of cabin influence the Survival of people. So need to replace the missing values of Cabin with U( U for unknown)
```
deal_data['Cabin'] = deal_data['Cabin'].fillna('U')
deal_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/deal_null.png)

3.3.7 Deal with Cabin

 To map each Cabin value with the first letter of cabin
```
deal_data['Cabin'].isnull().sum() --------- 0
deal_data['Cabin'] = deal_data['Cabin'].map(lambda x :  'Cabin_'+ x[0])
deal_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/cabin_letter.png)

3.3.8 Show cabin with related survival

 pd.crosstab(deal_data.Cabin,deal_data.Survived,margins =True)
 
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/crosstabe_1.png)
 
3.3.9 Show cabin with related survival probability
```
final_draw = pd.crosstab(deal_data.Cabin,deal_data.Survived,margins =True).apply(lambda x : x/float(x[-1]),axis = 1)
final_draw
```
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/crosstabe_2.png) 

3.3.10  Plot
```
fig = plt.figure(figsize=(12,12))
fig.set(alpha= 0.2)

final_draw.plot(kind='bar')

plt.ylabel('Probability')
plt.legend(loc = 'upper left',fontsize='small')
plt.savefig("final_Cabin_comparison.png")
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_3/final_Cabin_comparison.png) 

3.3.11 Summary

 From the picture above, we can conclude that the higher the grade, the probability of survival is higher.
 
 
### 3.4   Analysis Four---- Analysis the fare with survival

 3.4.1 Load data
  ```
  raw_data = pd.read_csv('..\data\Titanic.csv',na_values='N/A')  #,index_col=0
raw_data.head()
```
 3.4.2 Keep the needed attributes
 
```
deal_data = raw_data[['PassengerId','Survived','Pclass','Fare']]
deal_data.head()
 ```
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/needed_attributes.png)
 
 3.4.3 Check null values
 
  deal_data.isnull().sum()
  
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/NO_null.png)
 
 3.4.4 Cut the fare into 5 bins
 ```
 deal_data['FareBand'] = pd.qcut(deal_data['Fare'],5)
deal_data.head()
 ```
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/fareband.png)
 
 3.4.5 Fareband and Survived
 
 deal_data[['FareBand','Survived']].groupby(['FareBand'],as_index=False).mean().sort_values(by='FareBand',ascending = True)
 
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/fareband_survived.png)
 
 3.4.6 Draw the relation between fare and survival
 ```
fare_1 = deal_data[deal_data['Survived'] == 1]
fare_0 = deal_data[deal_data['Survived'] == 0]
plt.boxplot((fare_1,fare_0),labels=('Survived','Dead'))
plt.ylim([-10,150])
plt.title("Boxplot of Fare")
plt.savefig('Fare_survival.png')
 ```
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/Fare_survival.png)
  
  So the higher the price, the more rescured
 
 3.4.7 Draw fare with class
```fare1 = deal_data.Fare[deal_data.Pclass == 1]
fare2 = deal_data.Fare[deal_data.Pclass == 2]
fare3 = deal_data.Fare[deal_data.Pclass == 3]
plt.boxplot((fare1,fare2,fare3),labels=("Pclass1","Pclass2","Pclass3"))
plt.ylim([-10,180])
plt.title("Boxplot of Fare and Pclass")
plt.savefig('Fare_Pclass.png')
 ```
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/Fare_Pclass.png)
 
 So the higher the class, the expensive fare.
 
 3.4.8 Class with Survived
 ```
 final_draw1 = pd.crosstab(deal_data.Survived,deal_data.Pclass,margins=True)
final_draw1
 ```
 ![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/final_draw1.png)
 
 ```
 final_draw2 = pd.crosstab(deal_data.Survived,deal_data.Pclass,margins=True).apply(lambda x: x/float(x[-1]))
final_draw2
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/final_draw2.png)

```
fig = plt.figure(figsize=(12,12))
fig.set(alpha= 0.2)
final_draw2.plot(kind = 'bar')
plt.ylabel('Probability')
plt.legend(loc = 'upper left',fontsize='small')
plt.savefig("Class_Survival_comparison.png")
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_4/Class_Survival_comparison.png)

 3.4.9 Summary
 
 We can conclude that the higher the fare,  the more rescured.




### 3.5   Analysis Five---- 

 3.5.1 Load data
 ```
 raw_data = pd.read_csv('..\data\Titanic.csv',na_values='N/A')  #,index_col=0
raw_data.tail()
#sibsp----  of siblings / spouses aboard the Titanic	
#parch---- of parents / children aboard the Titanic
```
3.5.2 Keep the needed attributes

```deal_data = raw_data[['PassengerId','Survived','Pclass','SibSp','Parch']]
deal_data.head()
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/needed%E2%80%94%E2%80%94attributes.png)

3.5.3 Check null values

```
deal_data['SibSp'].isnull().sum()
deal_data['Parch'].isnull().sum()
```

3.5.4 Draw the account of SibSp
 deal_data['SibSp'].value_counts().plot(kind='bar')
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/count_sib.png)

3.5.5 Count value of Sibsp and survival
```
SibSp_data = pd.crosstab(deal_data.SibSp,deal_data.Survived,margins=True)
SibSp_data
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/slib_data.png)

3.5.6 Count probability of  Sibsp and survival

```SibSp_data2 = pd.crosstab(deal_data.SibSp,deal_data.Survived,margins=True).apply(lambda x : x/float(x[-1]),axis=1)
SibSp_data2
```

![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/sib_data2.png)

 we can coclude that with 1 to 2 Sibsp,the survival probability is higher。And without sibsp，the probability of dead is higher

3.5.7 Draw the account of Parch

 deal_data['Parch'].value_counts().plot(kind='bar')
 
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/count_parch.png)

3.5.8 Count value of Parch and survival
```
Parch_data = pd.crosstab(deal_data.Parch,deal_data.Survived,margins=True)
Parch_data
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/parch_data.png)

3.5.9 Count probability of Parch and survival

```
Parch_data2 = pd.crosstab(deal_data.Parch,deal_data.Survived,margins=True).apply(lambda x : x/float(x[-1]),axis=1)
Parch_data2
```
![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/parch_data2.png)

 we can coclude that with 1 to 2 Parch,the survival probability is higher。And without sibsp，the probability of dead is higher

3.5.10 Concat Sibsp and Parch
```
full_data = pd.concat([Parch_data2,SibSp_data2],axis = 1)
full_data
```

![wrong](https://github.com/zxy6076/Zheng_Xiaoyu_Spring2017/blob/master/final/analysis/ana_5/concat.png)






