import pandas as pd
import numpy as np
df1 = {
    'ID':['A','B','C','D'],
    'LAT':[1,2,3,4],
    'LONG':[5,6,7,8],
}

df2 = {
    'ID':['E','F','G'],
    'LAT':[9,10,11],
    'LONG':[12,13,14],
}

df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)

for index, coor in df1.iterrows():
    print(coor['LAT'] - df2['LAT'].max(), coor['LONG'] - df2['LONG'].max())