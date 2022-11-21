import numpy as np


def getVektor(matrix, idx):
    # Mendapatkan kolom matrix ke i
    # return bentuk array
    vec = [0 for j in range (len(matrix[idx]))]
    for i in range(len(matrix[idx])):
        vec[i] = matrix[i][idx]
    return vec


def eigenValVec(matrix,iteration=10):
    mat = np.copy(matrix)
    row = len(matrix)
    col = len(matrix[0])
    n = matrix.shape[0]
    QQ = np.eye(n)
    for i in range(iteration):
        s = mat.item(n-1,n-1)
        smult = s*np.eye(n)
        Q, R = np.linalg.qr(np.subtract(mat,smult))
        mat = np.add(R @ Q,smult)
        QQ = QQ @ Q
    eigVal = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        eigVal[i] = mat[i][i]
    return eigVal,QQ


def magnitude(vec):
    # vec merupakan vektor
    # mengembalikan bentuk desimal panjang dari vec
    res = 0
    for i in range(len(vec)):
        res += vec[i]**2
    res**0.5
    return res


def magnitudeSquare(vec):
    # vec merupakan vektor
    # mengembalikan bentuk desimal panjang dari vec lalu dikuadratkan
    res = 0
    for i in range(len(vec)):
        res += vec[i]**2
    return res


def orthogonalProjection(A,B):
    # A dan B merupakan vektor
    # mereturn proyeksi ortogonal dalam bentuk vektor
    hasilDot = np.dot(A,B)
    magnitude_B = magnitudeSquare(B)
    getScalar = hasilDot / magnitude_B
    hasil = np.matmul(getScalar, B)
    return hasil


def QR_decomposition (matrix):
    # Melakukan dekomposisi matrix dengan QR
    # Returnnya adalah matrix Q dan R
    Q = np.copy(matrix)
    row = len(matrix)
    col = len(matrix[0])
    for j in range (col):
        u = getVektor(Q,j)
        v = getVektor(Q,j)
        # GramSmith method
        for k in range (j-1,-1,-1):
            uk = getVektor(Q,k)
            u = np.subtract(u, orthogonalProjection(uk,v))
        for i in range (col):
            Q[i][j] = u[i] / magnitudeSquare(u)
    temp = np.matmul(np.transpose(Q), matrix)
    R = [[0 for i in range (row) ] for j in range (col)]
    for m in range (row):
        for n in range (col):
            if (j >= i):
                R[m][n] = temp[m][n]
    return Q, R


def getEigenValueQR (matrix, iteration):
    # Mendapatkan eigen value dari matrix
    # return bentuk array
    ret = [0 for m in range (len(matrix))]
    A = np.copy(matrix)
    for i in range (iteration):
        [Q,R] = QR_decomposition(A)
        A = np.matmul(R,Q)
    for j in range (len(A)):
        ret[i] = (A[i][i])
    return ret
    


def getEigenVectorQR (matrix, eigenValue):
    # eigenValue merupakan nilai eigen value dari matrix
    # Mendapatkan eigen vector dari matrix
    # return dalam bentuk matrix
    res = []
    for i in range(len(eigenValue)):
        Matrix_temp = np.copy(matrix)
        eigenValue_temp = np.copy(eigenValue)
        for j in range(len(eigenValue)):
            Matrix_temp[j][j] = eigenValue_temp[i]
        Eigen_Vector = np.linalg.solve(Matrix_temp, eigenValue_temp)
        normalize_Vector = magnitudeSquare(Eigen_Vector)
        for k in range (len(eigenValue)):
            Eigen_Vector[k] /= normalize_Vector
        res.append(Eigen_Vector)
        return res

        
        