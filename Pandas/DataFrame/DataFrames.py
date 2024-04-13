### Data frames
import numpy as np
import pandas as pd

"""
data frame represents a rectangular tabel of data and contains an ordered collection of columns each of which can be a different value type (numeric , string , boolean).
The data frame has both rows and columns index
"""


## Difference between series and dataframe
"""
Data frame are multidimensional(have rows and columns) but series is only 1 dimensional
"""
## We can also create data frame from the mergeing of series
# conditions for mergeing of 2 or more series in one dataframe
"""
1. both have same indexies 
2. then we make a dictionary the key values of the dictionaries are the name of the columns

"""
"""

series1 = pd.Series([1,2,3,4])
series2 = pd.Series([4,5,6,7])

# making a dic
data_dic = {'Oranges': series1,'Apples':series2}
dataframe1  =pd.DataFrame(data_dic)
print(dataframe1)

d2 = {'States':['Punjab','KPK','Sindh','Balochistan'],'Year':[2000,2002,2001,2003],"POp":['10M','9M','8M','4M']}

data = pd.DataFrame(d2,index=[1,2,3,4])
print(data)


## Head Function
print(data.head()) # head function will print the first 5 values of the data frame

"""

dict = {"States":['Punjab','KPK','Sindh','Bal'],"POP":[122,200,56,122],"year":[2000,2001,2002,2003]}

data = pd.DataFrame(dict,columns= ['st','year','pop','debt'])

data['st'] = ['punjab','kp','s','ba']
print(data.columns)

print(data)

print("\nThe lenght of the data",len(data)) # the length it will return is the number of rows the data frame has

# here we are adding values to the new column in the data frame from an np array
# remeber the length of the np array has to be same as of the number of the columns
rpg = np.arange(4)
data['debt'] = rpg
pop = [200,300,400,500]
data['pop'] = pop
print("\nAfter the insertion of new \n",data)


se = pd.Series([45,10,65,98],index=[1,2,3,4])
data['debt'] = se

print("\n\n\n",data)

data ["debt"] = ['p','f','p','r']

data['st'] = ["Punjab","KPK","Sindh","Balochistan"]

print('\n\n',data)
