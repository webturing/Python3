import pandas as pd

fss = '../data/iris.csv'
df = pd.read_csv(fss, index_col=False)
print(df.tail())
print(df.describe())
