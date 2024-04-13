### Saving numpy array in a file

import numpy as np

"""
There are 3 function
np.save(filename.npy , array)
np.load(filename.npy,)
np.savez(filename,array1,array2)


"""

array1 = np.array([1,2,3,4])
np.save('numpysave',array1)

print(np.load('numpysave.npy'))

x = np.random.randint(20,30,(2,3))
print(x)
y =x.transpose()
print(y)

x = np.random.seed(100)
print(x)