# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 22:21:48 2021

@author: saras
"""
'''
import pandas as pd
import numpy as np

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42],'Dept': ['AI','CSE','AI','CSE']}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
agr = df['Age'].aggregate(np.mean)
print(agr)

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)


print(df)
#print (df.groupby('Team').groups)
#print(df.groupby(['Team','Year']).groups)

grouped = df.groupby('Year')

for name,group in grouped:
   print (name)
   print (group)



print(df['Points'].agg(np.mean))

import pandas as pd
import numpy as np
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42],'Dept': ['AI','CSE','AI','CSE']}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
agr = df['Age'].agg([np.sum,np.mean, np.std])
print(agr)

'''
import pandas as pd
one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
print (pd.concat([one,two],ignore_index = True))

