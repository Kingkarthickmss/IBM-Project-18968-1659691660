# -*- coding: utf-8 -*-
"""Assignment_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lM0UrJ3l-mHGtM1FHUCn85v36cyaFqRb

Data Visualization and Pre-processing

Perform Below Tasks to complete the assignment:-

Tasks:-
1. Download the dataset: Dataset
2. Load the dataset.
3. Perform Below Visualizations.
● Univariate Analysis
● Bi - Variate Analysis
● Multi - Variate Analysis
4. Perform descriptive statistics on the dataset.
5. Handle the Missing values.
6. Find the outliers and replace the outliers
7. Check for Categorical columns and perform encoding.
8. Split the data into dependent and independent variables.
9. Scale the independent variables
10. Split the data into training and testing

"""


import numpy as np
import pandas as pd



df = pd.read_csv("Churn_Modelling.csv")

df

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

plt.figure(figsize=(8,8))
sns.countplot(x="Exited", data=df)
plt.xlabel("0 - Still with bank :: 1 - Exited from bank")
plt.ylabel("Count")
plt.title("Visual")
plt.show()

sns.countplot(df['Geography'])

df.shape

df.columns

df['NumOfProducts'].unique()

df['NumOfProducts'].value_counts()

df.describe()

df.isna().any()

df.isnull().sum()

df1=df.copy()

df.drop(['RowNumber', 'CustomerId', 'Surname'],axis=1,inplace=True)

df.head()

df['Geography'].value_counts()

geo = pd.get_dummies(df['Geography'])
geo

gen = pd.get_dummies(df['Gender'])
gen

df.drop(['Geography', 'Gender'],axis=1,inplace=True)

df

df = pd.concat([df,geo,gen],axis=1)

df

x = df.drop('Exited',axis=1)

y = df['Exited']

x.head()

y.head()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

print("x train shape : {} , y train shape : {}".format(x_train.shape,y_train.shape))

print("x test shape : {} , y test shape : {}".format(x_test.shape,y_test.shape))

x_train

y_train

x_test

y_test