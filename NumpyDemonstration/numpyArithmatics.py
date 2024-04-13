# Arithmatic operations on Numpy
'''
in Arithmetic operation we perform arithmetic operation on np array with out using loops
'''

import numpy as np


# for example we have an array
array1 = np.ones((2,2)) # array of ones
array2 = np.array([[4,5],[8,10]])
print(array1 , array2)
print(array1*array2)


array3 = np.random.randint(20,30,(2,3))
print("\nRandome:\n", array3)


ar = np.array([[1,0.2]])
r = np.array([[0,3]])
c = ar>r
print(c)