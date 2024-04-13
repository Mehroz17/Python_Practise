import  pandas as pd
import numpy as np

"""
pandas.merge: it connects rows in dataframe based on one or more keys
pandas.concat: concatenates or stacks together objects along an axis
the combine_first instance method enables splicing together overlapping date values from another
"""

df1 = pd.DataFrame({"key":['b','b','a','c','a','a','b'],
                    "date1":range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],'date2':range(3)})
e = pd.merge(df1,df2,on='key')
print("DF1\n",df1)
print("\nDF2\n",df2)
print("\nMerge\n",e) # merging is like joins in RDBMS so 2 dataframes will be merged when both have same indexes


d = pd.merge(df1,df2,right_on= 'key',left_on='key')
print("\n\nMegring using left right key ")