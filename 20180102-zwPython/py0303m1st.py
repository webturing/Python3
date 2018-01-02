import pandas as pd
import pip

x10 = pip.get_installed_distributions()
df = pd.DataFrame()
df['name'] = x10
print(df.head())
df.to_csv('../tmp/m10.csv', index=False)
