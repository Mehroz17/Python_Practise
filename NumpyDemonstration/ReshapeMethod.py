## Reshape MEthtod
'''
it is used to reshape the array if elements are fusible
 then we have to assign order of the matrix like roq major or column major

 syntax
 array.reshape((4,3),order = ?)
 c = row major
 f = coloumn major
'''


import numpy as np

ar = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x = ar.reshape((4,3),order='F')
y = ar.reshape((4,3),order='C')
print("Column Major Order" , x)
print("\nRow Major Order" , y)
print("\nConverting back to 1 d\n",y.ravel())

