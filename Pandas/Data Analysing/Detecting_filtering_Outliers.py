# Detecting and Filtering Outlieers

#Outliers means that for example you want the age less than 50 but in data ages are above 50 so it is an outlier

import pandas as pd
import numpy as np
"""

data = pd.DataFrame(np.random.rand(1000,4))
print(data)
print("Data Description\n\n")
print(data.describe()) # describe method will show all the major information about the data like mean median and standard deviation
col = data[2]
#print("Printing 2nd Columns\n\n",col)
#print("Printing value >3 from Column 2\n",col[np.abs(col)>3])

outliners = data[(np.abs(data)>3).any(1)] # it is giving the length of the data which is greater than 3
print(len(outliners),len(data))

"""


data = pd.DataFrame(np.arange(5*4).reshape((5,4)))
print(data)
sampler = np.random.permutation(4)
print(sampler)
data = data[sampler]
print("After Permutation\n\n",data)
