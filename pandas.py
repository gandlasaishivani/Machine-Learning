import numpy as np
import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
print("Labels",labels)
print("My data ",my_data)
print("Dictionary : ",d)
print(arr)
pd.Series(data=my_data)
#output:
# Labels ['a', 'b', 'c']
# My data  [10, 20, 30]
# Dictionary :  {'a': 10, 'b': 20, 'c': 30}
# [10 20 30]
pd.Series(data=my_data,index=labels)
#output:
# a    10
# b    20
# c    30
# dtype: int64
pd.Series(arr,labels)
#output:
# a    10
# b    20
# c    30
# dtype: int32
