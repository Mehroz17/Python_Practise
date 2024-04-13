import pandas as pd
import numpy as np
d1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','d'])
d2 = pd.DataFrame(np.arange(20).reshape((4,5)),columns=['a','b','c','d','e'])
print(d1,"\n",d2)

d4 =d1+d2
print("Adding with + sign") # traditionaly we will get NAN value as d2 has more data then d1 so at the time of adding we will get NAN value
print(d4)
print("\n")
d3  =d1.add(d2,fill_value = 0) # fill values means that NAN values will be replaced by 0
print("Adding with the Add Method ")
print(d3)

"""
so we have to use method to perform the arithmetic operation on the data frames instead of the signs
"""

series = pd.Series([1,2,3,4],index=['a','b','c','d']) # series will add this in row vise
print("Before aadding\n",d1)
print(series+d1)
