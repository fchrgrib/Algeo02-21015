import glob
import cv2
import matplotlib as plt
import numpy as np
import src.backend.tools.subtractAvAndTrain as sub
# import averageImage as ag
# import eigenValVec as ev


def readImgV2 (img_path):
    # membaca image dari file
    # return bentuk matriksnya
    img = cv2.imread(img_path,0)
    return img


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


def substractAll(path):
    # Mendapatkan nilai gambar dikurangi average
    # Keluaran outputnya adalah matrix 2 dimensi
    S = getHimpunanImgV3(path) # Dapet himpunan gambar
    avg = averageImgV7(path) # Dapet nilai rata-ratanya
    npAvg = np.array(avg)
    avgFlat = npAvg.flatten()
    N = len(S) # Dapet banyaknya gambar dalam dataset
    matrixGreek = []
    for i in range (N):
        temp = np.array(S[i])
        tempFlat = temp.flatten()
        matrixGreek.append(np.subtract(tempFlat,avgFlat))
    return matrixGreek


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


def subtractArray(Arr1, Arr2):
    # mengembalikan nilai Arr1 - Arr2
    res = [0 for z in range (len(Arr1))]
    for i in range (len(Arr1)):
        res[i] += Arr1[i]
        res[i] -= Arr2[i]
    return res


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
def substractAllHimpunanNew(S,S1):
    # Mendapatkan nilai gambar dikurangi average
    # Keluaran outputnya adalah matrix 2 dimensi
    avg = averageImgV8(S1) # Dapet nilai rata-ratanya
    npAvg = np.array(avg)
    avgFlat = npAvg.flatten()
    N = len(S) # Dapet banyaknya gambar dalam dataset
    matrixGreek = []
    for i in range (N):
        temp = np.array(S[i])
        tempFlat = temp.flatten()
        tempAppender = np.subtract(tempFlat,avgFlat)
        matrixGreek.append(tempAppender)
    print(len(matrixGreek))
    print(len(matrixGreek[0]))
    return matrixGreek


def covarianceGreek(path):
    # Mendapatkan nilai covariance aksen dari referensi greek
    matrixGreek = sub.subtractAvAndTrain(path)
    greekCovariance = [0 for i in range(5)]
    for i in range(len(matrixGreek)):
        greekCovariance[i] = np.matmul(matrixGreek[i], np.transpose(matrixGreek[i]))
    return greekCovariance


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


def covarianceGreekNew(path,pathOld):
    # Mendapatkan nilai covariance aksen dari referensi greek
    matrixGreek = substractAllNew(path,pathOld)
    greekTranspose = np.transpose(matrixGreek)
    greekCovariance = np.matmul(matrixGreek,greekTranspose)
    return greekCovariance


def subtractNoFlat(S):
    # S adalah himpunan gambar 
    # return matrix 3 dimensi setelah dikurang rerata
    SS = np.copy(S)
    avg = averageImgV8(S)
    for i in range (len(S)):
        SS[i] = np.subtract(S[i], avg)
    return SS


def concatManual(S):
    # S adalah himpunan gambar yang sudah dikurang
    # return matrix 2 dimensi concat ke samping
    B = S[0]
    for i in range(len(S) - 1):
        B = np.concatenate((B, S[i+1]), axis=1)
    return B


def covarianceManual(path):
    # mendapatkan langsung nilai kovarian tanpa konversi
    # return matrix kovarian kotak
    S = getHimpunanImgV3(path)
    S_subtract = subtractNoFlat(S)
    A = concatManual(S_subtract)
    AT = np.transpose(A)
    cov = np.matmul(A, AT)
    return cov
    


''' 
def getEigenGreek(path):
    covGreek = covarianceGreek(path)
    greekMatrix = substractAll(path)
    eigValGreek, eigVecGreek = ev.eigenValVec(covGreek,iteration=100)
    eigVecReal = np.matmul(greekMatrix,eigVecGreek)
     '''

        
        
    