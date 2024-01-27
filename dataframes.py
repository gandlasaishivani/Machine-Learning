import numpy as np
import pandas as pd
from numpy.random import randn as rn

# Set a seed for reproducibility
np.random.seed(101)

# Generate random matrix data of shape (5, 4) using randn
matrix_data = rn(5, 4)

# Define row labels and column headings
row_labels = ['A', 'B', 'C', 'D', 'E']
column_headings = [1, 2, 3, 4]

# Create a DataFrame using Pandas
df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)

# Print the DataFrame
print(df)
#           1         2         3         4
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509
print(df.loc[['C','B']])
#           1         2         3         4
# C -2.018168  0.740122  0.528813 -0.589001
# B  0.651118 -0.319318 -0.848077  0.605965
# )

print(df.loc['C'])
# 1   -2.018168
# 2    0.740122
# 3    0.528813
# 4   -0.589001
# Name: C, dtype: float64
print(df.loc[['B','D'],[1,2]])
print(df>0)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df = pd.DataFrame(data)
print(df)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df1 = pd.DataFrame(data)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df2 = pd.DataFrame(data)
df3 = pd.concat([df,df1,df2],axis=0)
print(df3)
          1         2
B  0.651118 -0.319318
D  0.188695 -0.758872
print(df>0)
print(df>0)
       1      2      3      4
A   True   True   True   True
B   True  False  False   True
C  False   True   True  False
D   True  False  False   True
E   True   True   True   True
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df = pd.DataFrame(data)
print(df)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df1 = pd.DataFrame(data)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df2 = pd.DataFrame(data)
df3 = pd.concat([df,df1,df2],axis=0)
print(df3)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df = pd.DataFrame(data)
print(df)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df1 = pd.DataFrame(data)
data = {'Company':[1,2,3],'Ball':[9,8,7],'Cooo':[1,5,6]}
df2 = pd.DataFrame(data)
df3 = pd.concat([df,df1,df2],axis=0)
print(df3)
#    Company  Ball  Cooo
# 0        1     9     1
# 1        2     8     5
# 2        3     7     6
#    Company  Ball  Cooo
# 0        1     9     1
# 1        2     8     5
# 2        3     7     6
# 0        1     9     1
# 1        2     8     5
# 2        3     7     6
# 0        1     9     1
# 1        2     8     5
# 2        3     7     6
df4 = pd.concat([df,df1,df2],axis=1)
print(df4)
#   Company  Ball  Cooo  Company  Ball  Cooo  Company  Ball  Cooo
# 0        1     9     1        1     9     1        1     9     1
# 1        2     8     5        2     8     5        2     8     5
# 2        3     7     6        3     7     6        3     7     6
​
