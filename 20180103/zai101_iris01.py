# coding=utf-8
import pandas as pd

# 1
fss = '../data/iris.csv'
df = pd.read_csv(fss, index_col=False)
print('\n#1 df')
print(df.tail())
print(df.describe())

# 2
d10 = df['xname'].value_counts()
print('\n#2 xname')
print(d10)
