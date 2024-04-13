## Now we will learn how to clean and analyze the data using pandas

import pandas as pd
from numpy import nan as NA


data = pd.DataFrame([[1,6,3],[1,NA,"Mehroz"],
                     [NA,NA,NA],["Mehroz",6,3]],
                    columns = list("abc"))
"""
print(data)
clean = data.dropna(how="all") # how all means that it will remove the rows in which all values are NA
clean2 = data.dropna(how="any") # how any means that it will remove the rows in which all or any value is NA

print("Clean with All\n",clean)
print("Clean with Any\n",clean)


"""


#filling missing value
print(data)
s = data.fillna({'a':2,'b':4,'c':.2})
print(s)


# dropping duplicate values
print("\n\n")
d = data.drop_duplicates('a') # drop duplicate means it will delte the whole row of hte duplicate value

print(d)


# Replacing values
s2 = data.replace(NA,25) # replacing values of NA to 25
print("REplacing \n",s2)
s3 = data.replace([NA,25],["Mehroz","Muhammad Mehroz"])
print(s3)
