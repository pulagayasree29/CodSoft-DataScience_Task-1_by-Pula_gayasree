# -*- coding: utf-8 -*-
"""Task-01_CodSoft_Titanic Survival_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RpABW2gi-HrLDMWz6kSnD2AkBLN9BKXF

**Task-1**: Titanic Survial Prediction

**Author**: pula gayasree

**Batch**: November-December

**Domain**: Data Science

**Aim**: To build a model that predicts whether a passenger on the Titanic survived or not

***Importing Important Libraries***
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""'''***Importing Data Set***'''"""

df = pd.read_csv("/content/pulagayasreetested.csv")
df.head(20)

df.shape

df.describe()

df['Survived'].value_counts()

sns.countplot(x=df['Survived'], hue=df['Pclass'])

df['Sex']

sns.countplot(x=df['Sex'], hue=df['Survived'])

df.groupby('Sex')[['Survived']].mean()

df['Sex'].unique()

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
df['Sex']= labelencoder.fit_transform(df['Sex'])
df.head()

df['Sex'], df['Survived']

sns.countplot(x=df['Sex'], hue=df['Survived'])

df.isna().sum()

df=df.drop(['Age'], axis=1)

df_final = df
df_final.head(20)

"""'''***Model Training***'''"""

X= df[['Pclass', 'Sex']]
Y= df['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression

log = LogisticRegression(random_state=0)
log.fit(X_train, Y_train)

"""'''***Model Prediction***'''"""

pred = print(log.predict(X_test))

print(Y_test)

import warnings
warnings.filterwarnings("ignore")

res = log.predict([[2,0]])

if(res==0):
  print("I'm So Sorry to say like this! Not Survived")
else:
    print("It's a good news!, Survived")

res = log.predict([[2,1]])

if(res==0):
  print("I'm So Sorry to say like this! Not Survived")
else:
    print("It's a good news!, Survived")