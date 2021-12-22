# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:06:35 2021

@author: saras
"""
'''
import pandas as pd
import numpy as np
data = np.array([1,2,3,4,5,6,7,8,87,90,23,45])
s = pd.Series(data)
print (s)

print (s[:3])
print (s[-3:])
print (s[[0,1]])
print (s.values)
print (s.index)

'''

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42],'Dept': ['AI','CSE','AI','CSE']}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])

data1 = pd.DataFrame({'Name':['Mercy','Jackey'],'Age':[34,56],'Dept':['AI','CSE']}, index=['rank5','rank6'])

#print (df)
#print (df['Age'])
#df['dept']= pd.Series(['AI','CSE','AI','CSE'],index=['rank1','rank2','rank3','rank4'])
#print (df)
'''
print ("Deleting the first column using DEL function:")
del df['Name']
print(df)
'''
#print(df.iloc[0])
#print (df[2:4])

print(data1)
df = df.append(data1)
df = df.drop('rank1')
print(df)

