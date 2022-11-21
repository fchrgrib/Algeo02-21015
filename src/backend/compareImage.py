import math

import numpy

import tools.subtractAvAndTrain as sub
import tools.eigenValVec as eigenVec
import tools.eigenFace as eigFace
import numpy as np

def compareImage(imageNew, imageOld):
    # Mendapatkan selisih antara image trainer dan nilai tengah
    imgNew = sub.subtractAvAndTrain(imageNew)
    imgOld = sub.subtractAvAndTrain(imageOld)
    vNew = ([0 for i in range (len(imgNew))])
    vOld = [0 for i in range(len(imgOld))]
    for i in range (len(imgNew)):
        vNew[i] = eigenVec.eigenValVec(np.matrix(imgNew[i]))[1]
    for i in range(len(imgOld)):
        vOld[i] = eigenVec.eigenValVec(np.matrix(imgOld[i]))[1]
    # vNew = eigenVec.eigenValVec(imgNew)
    # vOld = eigenVec.eigenValVec(imgOld)
    # print(vNew)
    # print(vOld)
    newFace = eigFace.eigenFace(vNew, imageNew)
    oldFace = eigFace.eigenFace(vOld, imageOld)
    # NnewFace = [[0 for i in range(256)]for j in range(len(newFace[0]))]

    # print(oldFace)
    
    result = 0
    # for i in range (len(newFace)):
    #     for j in range (len(oldFace)):
    result = (abs(np.subtract(newFace,oldFace)))**2
    result = np.sqrt(result)
    result = np.sum(result)
    return result

def compareAllImage(imageNew, AllImage):
    # Mendapatkan nilai minimum dari selisih image trainer dan nilai tengah
    min = compareImage(imageNew, AllImage[0])
    for i in range (len(AllImage)):
        result = compareImage(imageNew, AllImage[i])
        if (result < min):
            min = result
                  
    return min

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