import src.backend.tools.subtractAvAndTrain as subs
import numpy as np

def transpose(matrix):
    trans = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(matrix[0]):
        for j in range(matrix):
            trans[i][j] = matrix[j][i]
    return trans


def covariance(path):
    A = [[0 for i in range(256)] for j in range(256)]
    x = subs.subtractAvAndTrain(path)
    all = len(x)
    print(all)
    for i in range(all):
        for j in range(256):
            for k in range(256):
                A[j][k] += x[i][j][k]
    return np.matmul(A, transpose(A))


def L(path):
    A = [[0 for i in range(256)] for j in range(256)]
    x = subs.subtractAvAndTrain(path)
    all = len(x)
    for i in range(all):
        for j in range(256):
            for k in range(256):
                A[j][k] += x[i][j][k]
    return np.matmul(transpose(A), A)


