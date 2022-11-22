import eigenValVec as EV
import averageImage as AV 
import numpy as np  
import cv2


def getOneImage (path):
    # Mengambil 1 image dari path
    img = AV.readImg(path)
    img = cv2.resize(img, (256,256), fx = 1, fy = 1)
    return img

def subtractOneImage (matrix, avg):
    # matrix merupakan image yang ingin dikurang
    # avg merupakan average dataset
    A = np.subtract(matrix,avg)
    return A

def getEigenOneImg(m_subtracted):
    # mendapatkan eigenFace dari one image
    # m_subtracted merupakan image yang sudah dikurang
    # eigVal = EV.getEigenValueQR(m_subtracted, 100)
    # eigVec = EV.getEigenVectorQR(m_subtracted, eigVal)
    eigVal, eigVec = EV.eigenValVecV4(m_subtracted)
    eigFace = np.matmul(eigVec, m_subtracted)
    return eigFace

def magnitudeMatrix(matrix):
    # mendapatkan magnitude dari sembarang matrix
    res = 0
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            res += matrix[i][j]**2
    res **= 0.5
    return res

def euclideanDistance(eigFaceOld, eigFaceNew):
    # eigen face img lama dikurang eigen face image baru
    # lalu dicari panjangnya
    res = np.subtract(eigFaceOld,eigFaceNew)
    result = magnitudeMatrix(res)
    return result

def getClosestImg(EigFaces, eigFaceNew):
    # EigFaces   : eigFace dari img dataset yg sudah dikurang
    # EigFaces berbentuk 3D
    # eigFaceNew : eigFace dari image new
    # return minFace merupakan index ke minFace gambar
    minFace = 0
    min = euclideanDistance(EigFaces[0], eigFaceNew)
    for i in range (len(EigFaces) - 1):
        temp = euclideanDistance(EigFaces[i+1], eigFaceNew)
        print(temp)
        if (temp < min):
            min = temp
            minFace = i+1
        if (temp > max):
            max = temp
    return minFace+1, min, max