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
    subOld = sub.subtractAvAndTrain(imageOld)
    rataImgOld = cov.averageImgV7(imageOld)
    immNew = np.subtract(imgNew,rataImgOld)
    subOldTrans =[0 for i in range(5)]
    for i in range (len(subOld)):
        subOldTrans[i] = np.transpose(subOld[i])
    covOld = cov.covarianceGreek(imageOld)
    a,v = np.linalg.eig(covOld)
    eigVecOld = [0 for i in range(5)]
    for i in range(5):
        eigVecOld[i] = eigenVec.getEigenVectorQR(covOld[i], eigenVec.getEigenValueQR(covOld[i],1))
    newFace = [0 for i in range(5)]
    for i in range(len(eigVecOld)):
        newFace[i] = np.matmul(eigVecOld[i],immNew[0])
    oldFace = [0 for i in range(5)]
    for i in range(5):
        oldFace[i] = eigenVec.getEigenFace(subOldTrans[i], eigenVec.getRealEigenVector(subOldTrans[i], eigVecOld[i]))
    anu =0
    for i in range(5):
        anu = np.add(anu,newFace[i])
    arsult = [0 for i in range(5)]
    for i in range (5):
        arsult[i] = (abs(np.subtract(anu,oldFace[i])))
    result = np.sum(arsult)
    result = np.sqrt(result)
    print(result)
    return result

def compareAllImage(imageNew, AllImage):
    # Mendapatkan nilai minimum dari selisih image trainer dan nilai tengah
    min = compareImage(imageNew, AllImage+"/1")
    index = 0
    for i in range (10):
        result = compareImage(imageNew, AllImage+"/"+str(i+1))
        print(i+1)
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