# Import modules -------------------------------------------

import glob
import cv2
import numpy as np

# Functions ------------------------------------------------

# 1. Get matrix from image path
def readImgV2 (img_path):
    # membaca image dari file
    # return bentuk matriksnya
    img = cv2.imread(img_path,0)
    return img

# 2. Get array of images path
def getHimpunanImgV3(path):
    # Mendapatkan himpunan gambar hanya dengan memasukkan folder
    # File yang dibaca hanyalah bentuk jpg dengan nama sembarang
    file = glob.glob(str(path)+"/*")
    new_file = []
    for i in range (len(file)):
        new_file.append(file[i].replace("\\","/"))
    # new_file merupakan seluruh path yang ada di folder image
    S = []
    for j in range (len(new_file)):
        S.append(readImgV2(new_file[j]))
    N = len(S)
    SET = 256
    for i in range (N):
        S[i] = cv2.resize(S[i], (SET,SET), fx = 1, fy = 1)
    return S

# 3. Get all image average
def averageImgV7(path):
    # merata-ratakan seluruh image dari folder path
    # isi folder sembarang dan ukuran bisa bervariasi
    S = getHimpunanImgV3(path)
    N = len(S)
    SET = 256
    rata = [[0 for i in range (SET)] for j in range (SET)]
    for j in range (N):
        for k in range (SET):
            for l in range (SET):
                rata[k][l] += S[j][k][l]
    for m in range (SET):
        for n in range (SET):
            rata[m][n] /= N
    return rata

# 5. Get average of all images from an array of path
def averageImgV8(S):
    # merata-ratakan seluruh image dari himpunan S
    N = len(S)
    SET = 256
    rata = [[0 for i in range (SET)] for j in range (SET)]
    for j in range (N):
        for k in range (SET):
            for l in range (SET):
                rata[k][l] += S[j][k][l]
    for m in range (SET):
        for n in range (SET):
            rata[m][n] /= N
    return rata

# 7. Substract all images with average of set
def substractAllHimpunan(S):
    # Mendapatkan nilai gambar dikurangi average
    # Keluaran outputnya adalah matrix 2 dimensi
    avg = averageImgV8(S) # Dapet nilai rata-ratanya
    npAvg = np.array(avg)
    avgFlat = npAvg.flatten()
    N = len(S) # Dapet banyaknya gambar dalam dataset
    matrixGreek = []
    for i in range (N):
        temp = np.array(S[i])
        tempFlat = temp.flatten()
        tempAppender = np.subtract(tempFlat,avgFlat)
        matrixGreek.append(tempAppender)
    return matrixGreek

# 7. Substact all images with average of set
def substractAllNew(path, pathOld):
    S = getHimpunanImgV3(path)  # Dapet himpunan gambar
    avg = averageImgV7(pathOld)  # Dapet nilai rata-ratanya
    npAvg = np.array(avg)
    avgFlat = npAvg.flatten()
    N = len(S)  # Dapet banyaknya gambar dalam dataset
    matrixGreek = []
    for i in range(N):
        temp = np.array(S[i])
        tempFlat = temp.flatten()
        matrixGreek.append(np.subtract(tempFlat, avgFlat))
    return matrixGreek

# 8. Get covariance 
def covarianceGreekNew(path,pathOld):
    # Mendapatkan nilai covariance aksen dari referensi greek
    matrixGreek = substractAllNew(path,pathOld)
    greekTranspose = np.transpose(matrixGreek)
    greekCovariance = np.matmul(matrixGreek,greekTranspose)
    return greekCovariance

# 2. Get weight of eigen face
def getWeight(matrix, eigenface):
    # matrix merupakan norm
    # eigenFace dihitung
    # ukuran sama sama 5 x 256^2
    # W matrix jumlah gambar^2
    W = [] # matrix
    for i in range (len(matrix)): # jumlah image
        W_temp = []
        for j in range (len(matrix)):
            W_temp.append(np.dot(matrix[i], eigenface[j]))
        W.append(W_temp)
    return W

# 3. Get weight of training image
def getWeightOne(T, eigenFace):
    # mencari W dari training image
    W = []
    for i in range (len(eigenFace)):
        W.append(np.dot(T, eigenFace[i]))
    return W

# 1. Get length of 2 arrays
def getLength(array1, array2):
    # mendapatkan jarak dua array
    temp = 0
    for i in range (len(array1)):
        temp += (array1[i] - array2[i])**2
    return temp**0.5

# 1. Get euclidian distance 
def getDistanceW(W_set, W):
    # mencari distance terendah 
    min = getLength(W_set[0], W)
    max = min
    numberFile = 1
    # print(min)
    for i in range (len(W_set) - 1):
        temp = getLength(W_set[i+1], W)
        # print(temp)
        if (temp < min):
            min = temp
            numberFile = i+1
        if (temp > max):
            max = temp
    return numberFile, max, min