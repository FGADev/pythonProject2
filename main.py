import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')
df_sort = df.sort_values(by='bottles_sold', ascending=False)

df2 = df.groupby(['zip_code', 'item_description', 'bottles_sold']).agg({'bottles_sold': 'sum'})
g = df2['bottles_sold'].groupby('zip_code', group_keys=False)
res = g.apply(lambda x: x.sort_values(ascending=False))
print(res)
res.to_csv('data_final.csv')
fdf = pd.read_csv('data_final.csv')

x = np.array(fdf['zip_code'].to_numpy())
y = np.array(fdf['bottles_sold'].to_numpy())
plt.scatter(x, y)
# plt.scatter(fdf.zip_code, fdf.bottles_sold)
plt.show()
