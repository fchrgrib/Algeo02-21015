import math

import numpy
import tools.covarianceRemake as cov
import tools.subtractAvAndTrain as sub
import tools.eigenValVec as eigenVec
import tools.eigenFace as eigFace
import numpy as np

def compareImage(imageNew, imageOld):
    # Mendapatkan selisih antara image trainer dan nilai tengah
    imgNew = cov.getHimpunanImgV3(imageNew)
    ImgOld = cov.getHimpunanImgV3(imageOld)
    subOld = sub.subtractAvAndTrain(imageOld)
    rataImgOld = cov.averageImgV7(imageOld)
    immNew = np.subtract(imgNew,rataImgOld)
    # print(len(immNew))
    # print(len(immNew[0]))

    # print(subNew)
    # subNewTrans = np.transpose(subNew)
    # print(len(subNew))
    # print(len(subNewTrans))
    # print(len(np.transpose(cov.substractAllHimpunan(imgNew))))
    subOldTrans =[0 for i in range(5)]
    for i in range (len(subOld)):
        subOldTrans[i] = np.transpose(subOld[i])
    covOld = cov.covarianceGreek(imageOld)
    # print(covNew)
    # print(covOld)
    # eigVecNew = eigenVec.getEigenVectorQR(np.linalg.,eigenVec.getEigenValueQR(imgNew,100))
    eigVecOld = [0 for i in range(5)]
    for i in range(5):
        eigVecOld[i] = eigenVec.getEigenVectorQR(covOld[i], eigenVec.getEigenValueQR(covOld[i],1))
    newFace = [0 for i in range(5)]
    for i in range(len(eigVecOld)):
        newFace[i] = np.matmul(eigVecOld[i],immNew)
    # eigVecNew = eigenVec.getEigenVectorQR(cov.covarianceManual(imageNew), eigenVec.getEigenValueQR(cov.covarianceManual(imageNew),100))
    # multEig = np.array([0 for i in range(5)])
    # multEig = np.dot(eigVecOld,image1[0])
    # print(multEig)
    # vNew = ([0 for i in range (len(imgNew))])
    # vOld = [0 for i in range(len(imgOld))]
    # for i in range (len(imgNew)):
    #     vNew[i] = eigenVec.eigenValVecVercit(np.matrix(imgNew[i]))[1]
    # for i in range(len(imgOld)):
    #     vOld[i] = eigenVec.eigenValVecVercit(np.matrix(imgOld[i]))[1]
    # vNew = eigenVec.eigenValVec(imgNew)
    # vOld = eigenVec.eigenValVec(imgOld)
    # print(vNew)
    # print(vOld)

    # newFace = eigenVec.getEigenFace(eigVecNew,imageOld)
    # oldFace = eigenVec.getEigenFace(eigVecOld,imageOld)
    # print(eigenVec.getRealEigenVector(imgNew,eigVecNew))
    # print(eigenVec.getEigenFace(imgNew,eigenVec.getRealEigenVector(imgNew,eigVecNew)))
    oldFace = [0 for i in range(5)]
    for i in range(5):
        oldFace[i] = eigenVec.getEigenFace(subOldTrans[i], eigenVec.getRealEigenVector(subOldTrans[i], eigVecOld[i]))
    # NnewFace = [[0 for i in range(256)]for j in range(len(newFace[0]))]
    # print(oldFace)
    
    result = 0
    # for i in range (len(newFace)):
    #     for j in range (len(oldFace)):
    # print(oldFace)
    result = (abs(np.subtract(newFace,oldFace)))**2
    result = np.sum(result)
    result = np.sqrt(result)
    print(result)
    return result

def compareAllImage(imageNew, AllImage):
    # Mendapatkan nilai minimum dari selisih image trainer dan nilai tengah
    min = compareImage(imageNew, AllImage+"/1")
    index = 0
    for i in range (10):
        result = compareImage(imageNew, AllImage+"/"+str(i+1))
        if (result < min):
            min = result
            index = i
                  
    return min,(index+1)

def compareAllImageV2(imageNew):
    # versi kedua dari compareAllImage
    # Asumsi : Semua dataset ada di dalam folder test
    AllImage = '../test/'
    min = compareImage(imageNew, AllImage)
    for i in range (len(AllImage)):
        result = compareImage(imageNew, AllImage[i])
        if result < min:
            min = result
                  
    return min