# coding=utf-8

import pandas as pd

# 1
fss = '../data/iris.csv'
df = pd.read_csv(fss, index_col=False)

# 2
df.loc[df['xname'] == 'virginica', 'xid'] = 1
df.loc[df['xname'] == 'setosa', 'xid'] = 2
df.loc[df['xname'] == 'versicolor', 'xid'] = 3
df['xid'] = df['xid'].astype(int)
df.to_csv('../data/iris2.csv', index=False)
