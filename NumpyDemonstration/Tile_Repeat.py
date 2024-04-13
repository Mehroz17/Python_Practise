# # #tile and repeat function
import numpy as np

a = np.array([1,2,3])
v = np.repeat(a,3)
print("Repeat function :",v)

b = np.tile(a,3)
print("Tile Function: ",b)