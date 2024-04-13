# Slicing and indexing of array


import numpy as np
m = np.array([[1,5,6,0],[100,7,8,9]])
print(m)

print("Print the 3rd element of 2nd row ",m[1,2])
print("First row and 2nd column of array",m[0][1])
print("This will print the elements of 1st row from 0 index to 2",m[0,0:2])
print(m[::,0:3])


# making an square from numpy array

sqaure = np.ones((5,5))
sqaure[1:4,1:4] = 0


# making a chess board
chessboard = np.ones((8,8))
for i in range(0,8,2):
    for m in range(1,8,2):
        chessboard[i][m] = 0


for i in range(1,8,2):
    for x in range(0,8,2):
        chessboard[i][x] = 0
print("\nChess Board\n")
print(chessboard)