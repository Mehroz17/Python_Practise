# in this we will learn about function application and mapping on data frame
import numpy as np
import pandas as pd


# making a data frame
frame = pd.DataFrame([[1,2,3],[7,8,9],[11,21,36],[-9,0,-9]],columns = ['b','d','s'],index=['pakistan','india','afganistan','iran'])

print(frame)
# getting max value from any column
print('minumum value of column s: ',frame['s'].min())
print('Mam - min from columns s',frame['s'].max() - frame['s'].min())

# we can perform max - min for all the columns by using a function
f = lambda x : x.max() - x.min() # lambda means that it is an un named function x is an variable in which we are storing the max - min values
df = frame.apply(f)
d = frame.apply(f,axis=1) # axis = 1 means row vise operation
print('df\n',df)
print('\nd\n',d)
""" 
the purpose of the above task is that you can perform the complex operation on the columns of the dataframe easily

"""
"""
def checking_data(data,a):
    if a in set(frame['s']):
        print(a," found in the data frame")
    else:
        print('Not found')

checking_data(frame,10)

"""



# checking min max by using a function
def min_max(x):
    print("Min Max using function")
    m = x.max()
    n = x.min()
    return pd.Series([m , n],index=['max','min']) # we will return the series of the results

d3 = frame.apply(min_max,axis=1)
print('d3\n',d3)


# using kaggle info
print("\nDescribes Function") #descibes function will define some important data regarding that columns are row
print("Data Regarding 'b' column\n",frame.b.describe())

"""
This method generates a high-level summary of the attributes of the given column. It is type-aware, meaning that its output
changes based on the data type of the input. The output above only makes sense for numerical data; for string data 
"""

# making an other dataframe with string data

s = pd.DataFrame({"students":['Muhammad Mehroz', 'Abdullah', 'Saim', 'Arslan'], 'Teachers':['DR.Abid', 'Miss Umara Shaeen', 'Miss Fabeha Shahzed', 'Ali Khan']})
print("\nStudents Data Frame")
print(s)
print("\nDescribing Student Data Frame")
print(s.describe())

"""
we can also call some specific function on the rows or columns like
1. min()
2. max()
3. mena()
4. Unique
"""
print("Unique Data from Students",s.students.unique())
print("Unique Data from Students and count\n",s.students.value_counts()) #To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method
print("Mean from Frame Data Frame",frame.mean())

"""
A map is a term, borrowed from mathematics,
for a function that takes one set of values and "maps" them to another set of values.
In data science we often have a need for creating new representations from existing data, or for transforming data
from the format it is in now to the format that we want it to be in later. Maps are what handle this work, making them
extremely important for getting your work done!

There are two mapping methods that you will use often.

map() is the first, and slightly simpler one. For example, suppose that we wanted to remean the scores the wines received to 0. We can do this as follows:


"""
c = frame.b - frame.b.mean()
print("Value of \n",c)