import numpy as np

# Now we are going to read the matrix from the file we just saved
data = np.loadtxt('matrix.txt', dtype=int)
print(data)