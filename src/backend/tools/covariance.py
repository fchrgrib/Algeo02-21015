import src.backend.tools.subtractAvAndTrain as subs


def transpose(matrix):
    trans = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(matrix[0]):
        for j in range(matrix):
            trans[i][j] = matrix[j][i]
    return trans


def multiplyMtrx(mtrx1,mtrx2):
    result = [[0 for i in range(len(mtrx1))] for j in range(mtrx2[0])]
    rang = len(mtrx1[0])
    for i in range(len(mtrx1)):
        for j in range(len(mtrx2[0])):
            for k in range(rang):
                result[i][j] += mtrx1[i][k]*mtrx2[k][j]
    return result


def covariance(path):
    A = [[0 for i in range(256)] for j in range(256)]
    x = subs.subtractAvAndTrain(path)
    all = len(x)
    for i in range(all):
        for j in range(256):
            for k in range(256):
                A[j][k] += x[i][j][k]
    return multiplyMtrx(A, transpose(A))


def L(path):
    A = [[0 for i in range(256)] for j in range(256)]
    x = subs.subtractAvAndTrain(path)
    all = len(x)
    for i in range(all):
        for j in range(256):
            for k in range(256):
                A[j][k] += x[i][j][k]
    return multiplyMtrx(transpose(A), A)


