import pandas as pd
import numpy as np
    
    
Ds = pd.read_csv("E:/New folder/2021 - 2022/AD8302 - FDS/Data Sets for Assignment/police.csv")
min = int(Ds["driver_age"].min())
max = int(Ds["driver_age"].max())
bin2 = [x for x in range(min,max,5)]
 
Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []
    
for i in bin2:
    a = Ds["driver_age"].value_counts().sort_index()[i:i+4].sum()
    d = Ds["driver_age"].value_counts().sort_index()[:i+4].sum()
    st = str(i)+" - "+str(i+4)
    Col1.append(st)
    Col2.append(a)
    Col4.append(d)
    
df = pd.DataFrame(list(zip(Col1,Col2)),columns = ['Range','freq'] )
#print(df)
sum = np.sum(Col2)
c = df.loc[: , "freq"].tolist()
for i in c:
    Col3.append((i/sum)*100)

df['rel.freq'] = Col3
#print(df) 

df['cum.freq'] = Col4
#print(df) 
for i in e:
    Col5.append((i/sum)*100)
df['cum.freq %'] = Col5
print(df) 
   