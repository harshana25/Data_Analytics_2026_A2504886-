import numpy as np

# create a matrix
matrix = np.random.randint(1,100,(15,15))
print(matrix)

# save the matrix to a file
np.savetxt('matrix.txt', matrix,fmt='%d')
