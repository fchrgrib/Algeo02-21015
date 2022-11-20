import math
import tools.subtractAvAndTrain as sub
import tools.eigenValVec as eigenVec
import tools.eigenFace as eigFace
import numpy as np

def compareImage(imageNew, imageOld):
    # Mendapatkan selisih antara image trainer dan nilai tengah
    imgNew = sub.subtractAvAndTrain(imageNew)
    imgOld = sub.subtractAvAndTrain(imageOld)

    vNew = [0 for i in range (len(imgNew))]
    vOld = [0 for i in range(len(imgOld))]
    for i in range (len(imgNew)):
        vNew[i] = eigenVec.eigenValVec(np.matrix(imgNew[i]))
    for i in range(len(imgOld)):
        vOld[i] = eigenVec.eigenValVec(np.matrix(imgOld[i]))
    # vNew = eigenVec.eigenValVec(imgNew)
    # vOld = eigenVec.eigenValVec(imgOld)
    
    newFace = eigFace.eigenFace(vNew, imageNew)
    oldFace = eigFace.eigenFace(vOld, imageOld)
    
    result = 0
    for i in range (len(newFace)):
        for j in range (len(oldFace)):
            result += (abs(newFace[i][j] - oldFace[i][j]))**2
    result = math.sqrt(result)
    
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