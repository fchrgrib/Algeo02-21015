import numpy as np
import src.backend.tools.covarianceRemake as CR
from matplotlib import pyplot as plt

def getVektor(matrix, idx):
    # Mendapatkan kolom matrix ke i
    # return bentuk array
    vec = [0 for j in range (len(matrix[idx]))]
    for i in range(len(matrix[idx])):
        vec[i] = matrix[i][idx]
    return vec


# def eigenValVec(matrix,iteration=10):
#     mat = np.copy(matrix)
#     row = len(matrix)
#     col = len(matrix[0])
#     n = matrix.shape[0]
#     QQ = np.eye(n)
#     for i in range(iteration):
#         s = mat.item(n-1,n-1)
#         smult = s*np.eye(n)
#         Q, R = np.linalg.qr(np.subtract(mat,smult))
#         mat = np.add(R @ Q,smult)
#         QQ = QQ @ Q
#     eigVal = [0 for i in range(len(mat))]
#     for i in range(len(mat)):
#         eigVal[i] = mat[i][i]
#     return eigVal,QQ


def magnitude(vec):
    # vec merupakan vektor
    # mengembalikan bentuk desimal panjang dari vec
    res = 0
    for i in range(len(vec)):
        res += vec[i]**2
    res**=0.5
    return res


def magnitudeSquare(vec):
    # vec merupakan vektor
    # mengembalikan bentuk desimal panjang dari vec lalu dikuadratkan
    res = 0
    for i in range(len(vec)):
        res += vec[i]**2
    return res


def scalarXvec(val, vector):
    # val merupakan skalar
    # vector merupakan vektor atau array
    res = [0 for i in range(len(vector))]
    for i in range(len(vector)):
        res[i] = val * vector[i]
    return res

    
def orthogonalProjection(A,B):
    # A dan B merupakan vektor
    # mereturn proyeksi ortogonal dalam bentuk vektor
    hasilDot = np.dot(A,B)
    magnitude_B = magnitudeSquare(B)
    getScalar = hasilDot / magnitude_B
    hasil = scalarXvec(getScalar, B)
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


def QR_decompositionV2(matrix):
    # Melakukan dekomposisi matrix dengan QR
    # Returnnya adalah matrix Q dan R
    m, n = matrix.shape
    Q = np.zeros((m, n))
    R = np.zeros((m, n))
    for j in range(n):
        v = matrix[:, j]
        norm = np.linalg.norm(v)
        for i in range(j):
            temp = matrix[:, j] 
            q = Q[:, i]
            qt = np.transpose(q)
            temp1 = np.dot(qt, temp)
            temp2 = np.multiply(temp1, q)
            R[i][j] = temp1
            v = np.subtract(v, temp2)
        if j == 0:
            R[j][j] = norm
            Q[:, j] = np.divide(v, norm)
        else :
            norm = np.linalg.norm(v)
            R[j][j] = round(norm, 6)
            v = np.divide(v, norm)
            Q[:, j] = v

    return Q, R

def eigenValVecV2(matrix,iteration):
    mat = np.copy(matrix)
    row = len(matrix)
    col = len(matrix[0])
    n = matrix.shape[0]
    QQ = np.eye(n)
    for i in range(iteration):
        s = mat.item(n-1,n-1)
        smult = s*np.eye(n)
        Q, R = QR_decompositionV2(matrix)
        mat = np.add(R @ Q,smult)
        QQ = QQ @ Q
    eigVal = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        eigVal[i] = mat[i][i]
    return eigVal,QQ


def getEigenValueQR (matrix, iteration):
    # Mendapatkan eigen value dari matrix
    # return bentuk array
    ret = [0 for m in range (len(matrix))]
    A = np.copy(matrix)
    for i in range (iteration):
        [Q,R] = QR_decompositionV2(A)
        A = np.matmul(R,Q)
    for j in range (len(A)):
        ret[j] = (A[j][j])
    ret.sort(reverse=True)
    return ret
    

def getEigenVectorQR (matrix, eigenValue):
    # eigenValue merupakan nilai eigen value dari matrix
    # Mendapatkan eigen vector dari matrix
    # return dalam bentuk matrix
    res = [[0 for m in range (len(matrix))] for n in range (len(matrix))]
    for i in range(len(eigenValue)):
        Matrix_temp = np.copy(matrix)
        eigenValue_temp = np.copy(eigenValue)
        
        # untuk mendapatkan matrix yang dikurang eigen value ke i
        for j in range(len(eigenValue)): 
            Matrix_temp[j][j] -= eigenValue_temp[i]
            
        # solve matrix A - lambda I dapat eigen vektor
        Eigen_Vector = np.linalg.solve(Matrix_temp, eigenValue_temp)
        
        # cari panjang dari eigen vektor yang telah didapat
        normalize_Vector = magnitude(Eigen_Vector)
        
        # normalisasikan (tiap elemen eigen vektor dibagi panjangnya)
        for k in range (len(eigenValue)):
            Eigen_Vector[k] /= normalize_Vector
            
        # saat ini HARUSNYA sudah dapat eigen vektor sebenarnya
        # jadi di append ke res lalu proses diulangi untuk eigen berikutnya
        for z in range (len(matrix)):
            res[z][i] = Eigen_Vector[z]

    return res


def getEigenVectorQRV2 (matrix):
    pass
    

def getRealEigenVector (S, eigenVectorQR):
    # eigenVectorQR merupakan eigen vektor yang didapat dari kovarian kecil
    # S merupakan hipunan gambar yang sudah di subtract
    # ukuran S = 256^2 X N dengan N banyak file
    realVector = [[0 for m in range(len(S[0]))] for n in range (len(S))] # 2 dimensi
    for i in range(len(S[0])): 
        # Mendapatkan eigen vektor dari S ke i
        tempVec = getVektor(eigenVectorQR,i)
        A = np.matmul(S, tempVec)
        for j in range(len(S)):
            realVector[j][i] = A[j]
    return realVector
        

def getEigenFace (S, realEigenVector):
    # S merupakan himpunan gambar yang sudah di subtract
    # ukuran S = 256^2 X N dengan N banyak file
    eigenFace = [[0 for m in range(len(S[0]))] for n in range (len(S))] # 2 dimensi 
    for i in range (len(S[0])): # loop N kali dengan N banyak file
        tempVec = getVektor(realEigenVector,i)
        A = np.matmul(S, tempVec)
        for j in range(len(S)):
            eigenFace[j][i] = A[j]
    return eigenFace


def getVektorAsMatrix(matrix, idx):
    # Mendapatkan kolom matrix ke i
    # return bentuk matrix N x 1
    vec = [0 for j in range (len(matrix[idx]))]
    for i in range(len(matrix[idx])):
        vec[i] = matrix[i][idx]
    return vec


def getEigenFaceV2 (S, realEigenVector):
    # S merupakan himpunan gambar yang sudah di subtract
    # covariance yang dugybajab adalah yang asli
    # ukuran S = 3 dimensi
    eigenFace = [] # akan dibuat 3 dimensi
    for i in range (len(S)): # loop N kali dengan N banyak file
        A = np.matmul(realEigenVector, S[i])
        eigenFace.append(A)
#        img_plot = plt.imshow(A,cmap='gray', vmin=0, vmax=255)
#        plt.show()
    return eigenFace


def eigen_qr_simple(matrix, iterations=10000):
    Ak = np.copy(matrix)
    n = matrix.shape[0]
    QQ = np.eye(n)
    for k in range(iterations):
        [Q, R] = QR_decompositionV2(matrix)
        Ak = R @ Q
        QQ = QQ @ Q
        #if (k % 10000 == 0):
           # print("A",k,"=")
           # print(tabulate(Ak))
           # print("\n")
    return Ak, QQ


def getEigenFaceQR (eigenVector, path):
    # path merupakan path dari dataset
    # Mendapatkan nilai eigenFace
    matGreek = CR.substractAll(path)
    
    
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

def eigenValVecV3(matrix):
    eigVector = np.eye(matrix.shape[0])
    X = np.copy(matrix)
    for i in range(1):
            Q,R = QR_DecompositionV3(X)
            eigVector = np.matmul(eigVector, Q)
            X = np.matmul(R, Q)
    return np.diag(X), eigVector

def EuclideanDistance(matrix):
    return np.sqrt(np.sum(np.square(matrix)))

def eigenValVecV4(matrix, iterations=50):
    Ak = np.copy(matrix)
    n = matrix.shape[0]
    QQ = np.eye(n)
    for k in range(iterations):
        Q, R = QR_decompositionV2(Ak)
        Ak = R @ Q
        QQ = QQ @ Q
        # we "peek" into the structure of matrix A from time to time
        # to see how it looks
    return Ak, QQ
