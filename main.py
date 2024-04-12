# Pandas: Find common Rows (intersection) between 2 DataFrames

import pandas as pd


df1 = pd.DataFrame({
    'ID': ['a', 'b', 'c'],
    'A': ['x', 'y', 'z'],
    'B': [1, 2, 3]
})

df2 = pd.DataFrame({
    'ID': ['a', 'b', 'Z'],
    'A': ['a', 's', 'd'],
    'B': [5, 6, 7]
})


common_rows = pd.merge(df1, df2, how='inner', on=['ID'])

#   ID A_x  B_x A_y  B_y
# 0  a   x    1   a    5
# 1  b   y    2   s    6
print(common_rows)