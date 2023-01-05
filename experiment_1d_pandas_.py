# -*- coding: utf-8 -*-
"""EXPERIMENT 1D Pandas .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ixKHNTOkUv1bjfcXdTR8pHJd0ORDv6Pm

<h1 align="center">  Experiment 1.D</h1> 

Date_____________

AIM :Familarization of Pandas
"""

import numpy as np
import pandas as pd

"""#### Pandas Series
* Create series type of data using data structures like tuples, arrays, list dictionary etc.
"""

# This is 1D representation of Data
data = pd.Series([10, 20, 30, 40, 50, 60, 70])
data

data = pd.Series([10, 20, 30, 40, 50, 60, 128], index = ['a','b','c','d','e','f','g'], dtype = 'int8')  # int8 - 8bytes (-128 to +127)

data.values

data.index

### Collection of Series
# dtype = int16
data_series = {
                'Column1' :  pd.Series([100, 200, 300, 400, 500, 600, 700], dtype = 'int16'),
                'Column2' :  pd.Series([10, 20, 30, 40, 50, 60, 70], dtype = 'int16')
              }

data_series

pd.DataFrame(data_series)

"""#### DataFrame
* Represents multi-dimentional data into excel like spreadsheet or 2D representation of muti-dimentional
"""

movies_df = pd.read_csv('https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/boston_train.csv', sep = ',')
display(movies_df)

# head display first five rows , tail() displays last 5 rows of DF
movies_df.head()

# head display first five rows , tail() displays last 5 rows of DF
movies_df.tail()

# Read an excel file
stock_data = pd.read_excel("https://github.com/ammishra08/MachineLearning/blob/master/Datasets/data_akbilgic.xlsx?raw=true", header=1 )

stock_data

# Display Shape (rows, columns)
movies_df.shape

movies_df.columns

len(movies_df.columns)

# print rows & columns
# indexes
print(movies_df.shape[0], movies_df.shape[1])

"""#### Data Manipulation"""

data_series = {
                'Column1' :  pd.Series([100, 200, 300, 400, 500, 600], index = ['a','b','c','d','e','f'], dtype = 'int16'),
                'Column2' :  pd.Series([10, 20, 30, 40, 50, 70], index = ['a','b','c','d','e','g'], dtype = 'int16')
              }

df = pd.DataFrame(data_series)

df.isnull()

df.isnull().sum()

df.isna().sum()

df.notnull()

df[df['Column1'].isnull() == True]

df[df['Column2'].isnull() == True]

