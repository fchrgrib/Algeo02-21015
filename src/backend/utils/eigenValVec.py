# Import modules -------------------------------------------

import numpy as np

# Import custom modules ------------------------------------

    
# 1. Decomposite matrix to QR form
def QR_DecompositionV3(matrix):
    n, m = matrix.shape 
    matrixQ = np.empty((n, n)) 
    matrixU = np.empty((n, n)) 
    matrixU[:, 0] = matrix[:, 0]      
    matrixQ[:, 0] = matrixU[:, 0] / EuclideanDistance(matrixU[:, 0]) 
    for i in range(1, n):       
        matrixU[:, i] = matrix[:, i]  
        for j in range(i):    
            matrixU[:, i] -= (matrix[:, i] @ matrixQ[:, j]) * matrixQ[:, j]
        matrixQ[:, i] = matrixU[:, i] / EuclideanDistance(matrixU[:, i])
    matrixR = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):   
            matrixR[i, j] = matrix[:, j] @ matrixQ[:, i]    
    return matrixQ, matrixR 

# 2. Get euclidian distance of a matrix
def EuclideanDistance(matrix):
    return np.sqrt(np.sum(np.square(matrix)))