import pandas as pd
import numpy as np

### Starting Pandas
'''
it is a one dimensional array having index too
'''

##### Series
"""
ob = pd.Series(['Muhammad Mehroz','Moeez',15])
print(ob)
print("\nPrint only values\n",ob.values)
# we can also give custom indexes
ob2 = pd.Series(['Muhammad Mehroz','Moeez','Arif'],index = ['a','b','c'],name="Students")
print("\nOb2\n",ob2)
print(ob2.index)
print(ob2.name)


### Canteen Data
canteen = pd.Series([45,20,69,35,50,55,20],index=['Mon','Tue','Wed','Thu','Fir','Sat','Sun'],name="Canteen Record")
print(canteen[2:6])
print(canteen[canteen>50])
# we can also perform matematical operation on series
print(canteen*3)
# we can also check if an index exist in the series
print("Mon is present : ",'Mon' in canteen)
"""

## storing existing data from numpy array

ar = np.array(['Muhammad Mehroz','Abdullah','Saim']) # this is value array
reg = np.array(['FA20-BSE-071','FA20-BSE-075','FA20-BSE-011']) # this is index array

studentrecord = pd.Series(ar,index=reg)
print(studentrecord)

## Storing data from a dictionary
state = {"Punjab":200,"Sindh": 150,"KPK":100,"Balochistan":20}
p = pd.Series(state) # here indexes will be the key value of the dic , if we pass indexes again our selves then it just rearrange the data
p.index.name  = "States "
print(p)

"""
sources of series data
1. direct data in the series 
2. from numpy array or list
3. from dictionaries
"""

# checking the null values in the series
"""print(pd.isnull(p))
print(p.isnull())"""

## Changes in series
p["Punjab","Sindh"] = [12,45]
print(p)
