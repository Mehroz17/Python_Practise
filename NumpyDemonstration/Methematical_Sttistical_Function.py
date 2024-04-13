### Mathematical and Satictical Function

# Mean() foind mean
# cumsum() return the cumulative sum of array
# cumprob() return the cumulative product of arra

import numpy as np
arra = np.array([[45,49,89,45],[1,2,3,4]])
print("The mean of Array is : ",np.mean(arra))
print("The cumulative sum of Array is : ",np.cumsum(arra))
print("The cumulative product of Array is : ",np.cumprod(arra))


### Methods for Boolean Array

#sum() : count True values in array
#any(): check wheather one or more values in an array are True
# all(): checks if every value is true

print("\n\nBoolean Function")
bolarr = np.array([[True,False],[True,False]])
print(np.sum(bolarr))
print(np.any(bolarr))
print(np.all(bolarr))