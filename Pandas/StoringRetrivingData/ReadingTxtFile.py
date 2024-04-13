import csv

import numpy as np
import pandas as pd

p = list(open("xtsample.txt"))
print("this is regular file read ")
print(p)

p2 = pd.read_table("xtsample.txt", sep= '\s+')
#use space (one or more )as a delimeter s+ is  regex
print("\nthis is txt file read in a dtaframe")
print(p2)


# skiping rows
print("skiping rows 0 1 3 ")
skipr = pd.read_table("xtsample.txt", skiprows=[0,1,3])
print(skipr)


# reading null values
s = {'math':[50]}
cs = pd.read_csv('sample.csv',na_values= s)

#print(pd.isnull(cs))
print(cs)



# writing data to txt file
date = pd.date_range('2/2/2002',periods=8)
ts = pd.Series(np.arange(8),index=date)
ts.to_csv('xtsample.txt')
print(ts)

o = list(open('xtsample.txt'))
print(o)


a = np.array(['Mehroz','Moeez','Maheen'])
w = pd.DataFrame(a)
w.to_csv('write.csv')
print(pd.read_csv('write.csv'))




