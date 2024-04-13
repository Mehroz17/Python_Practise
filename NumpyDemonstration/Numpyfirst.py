import numpy as np


# numpy is a library for python which is used to handel data more efficently and effectivly

"""
l = range(1000000)
d = np.array(1000000)

for i in range(1,10):
    x = [x*2 for x in l]


for i in range(1,10):
    r = d*2
"""




l = [1,5,9,87,456,200,646]
m = np.array(l)

k = m.reshape((10,10))
print(m)
