# Creating Hierarichal indexing in Series
import pandas as pd
import numpy as np

data = pd.Series(np.random.rand(9),index=[['a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,3]])
print(data)
print(data[:,1]) # it will print the data of 1 index either it is in a , b, c ,d


"""
unstack function will make hieraricahl data in to dataframe from 
          1         2         3
a  0.540617  0.261154       NaN
b  0.649277  0.533253  0.636784
c  0.317025       NaN  0.400100
d       NaN  0.474163  0.078987

"""

data = data.unstack()



# now making an hierarichal data frame

f = pd.DataFrame(np.arange(12).reshape((4,3)),
                 index= [['a','a','b','b'],[1,2,1,2]],
                 columns=[['ohio','ohio','colorado'],
                          ['green','red','green']])
f.columns.names = ['state','green']
f.index.names =['key1','key2']
print(f)

f = f.swaplevel("key1","key2").sort_index(level=1) # level of the index are the name of the index we have given
print(f)


# seting sum

print(f.sum(level='key2'))