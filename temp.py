import pandas as pd
import numpy as np

r=np.random.random(328)*100
r=[int(each) for each in r]
print()

df=pd.read_csv('datas/entity_pair_relations.csv')
print(df.head())
print(df.shape)#(328, 3)

df['unknow']=r
df.to_csv('datas/entity_pair_relations_new.csv',columns=[':START_ID','unknow',':END_ID',':TYPE'],index=False)
print(df.head())