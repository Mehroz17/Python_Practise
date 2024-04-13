#Concatination Function
'''
Takes a sequence (tuple,list,etc). of arrays and joins them together in order along the input axis

if we give axis as 0 then it will concatinate row wise and if we give 1 then at column wise

'''

import  numpy as np
ar1 = np.array([[1,2,3],[5,6,8]])
ar2 = np.array([["a","b",'c'],['h','h','l']])

y = np.concatenate((ar1,ar2),axis=0)
print(y)
"""
h = np.concatenate((ar1,ar2),axis=1)
print("Column wise",h)

print(np.vstack(ar1,ar2))

"""

m= np.split(y,[2,2])
print(m)