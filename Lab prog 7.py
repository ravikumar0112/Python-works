# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:39:56 2021

@author: saras
"""
import pandas as pd
import numpy as np

Ds = pd.read_csv("E:/New folder/2021 - 2022/AD8302 - FDS/Data Sets for Assignment/police.csv")

my_tab = pd.crosstab(index=Ds["driver_race"],columns="count") 
#print(type(my_tab))
result = my_tab.sort_values("count")
print(result)
result.columns =['Frequency']
print(result)
sum = result['Frequency'].sum()
#print(sum)

c = result.loc[: , "Frequency"].tolist()
#print(type(c))
Col3 = []
for i in c:
    Col3.append((i/sum)*100)

#print(Col3)
result['rel.freq'] = Col3
#print(result)

