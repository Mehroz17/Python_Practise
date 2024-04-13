import pandas as pd
import numpy as np

# here we will learn to sort and rank the data in a DataFrame
# index sortin
f = pd.DataFrame([[0,100,15,13],[5,1,9,4]],columns=['d','a','c','b'],index=[1,2])
print("Original DataFrame\n",f)
print("Sorting the Rows\n",f.sort_index(axis=1,ascending=True)) # here we are sorting according to the columns as axies = 1
print('Sorting the columns\n',f.sort_index(ascending=False)) # default axies = 0 and asending in True

# value sorting

print(f.sort_values(by='b'))

#Rank means pirority to the values
print("\n\nRanking")
print(f.rank(method='first'))

"""
Method Description
'average' Default: assign the average rank to each entry in the equal group.
'min' Use the minimum rank for the whole group.
'max' Use the maximum rank for the whole group.
'first' Assign ranks in the order the values appear in the data.
"""


revi = pd.DataFrame({"Countries":['Afganistan','Pakistan','India','America','UAE','UK'],'POP':[0,1,2,3,4,5]})

print(revi)
print(revi.groupby('POP'))
print('Minimum population\n',revi.min())

print(revi.groupby("Countries").size())
print(revi.groupby("Countries").count())