

#Create a Dictionary of series

import pandas as pd
import numpy as np
from scipy.stats import *


arr = np.array([56,56,56,78,98,76,54,56,43,32,34,34,34,34,51])
arr_mode = mode(arr)
print(arr_mode)


arr_median = np.mode(arr)
print ("Median Values in the Distribution",end =' ')
print(arr_median)


d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}



#Create a DataFrame
df = pd.DataFrame(d)
print ("Mode Values in the Distribution")
print(df['Age'].mode())

import matplotlib.pyplot as plt

plt.plot(df['Age'])
print( '\nSkewness for data : ', skew(df['Age']))

