import tools
import math

def compareImage(imageNew, imageOld):
    # Mendapatkan selisih antara image trainer dan nilai tengah
    imgNew = tools.subtractAvAndTrain(imageNew)
    imgOld = tools.subtractAvAndTrain(imageOld)
    
    vNew = tools.eigenValVec(imgNew)[1]
    vOld = tools.eigenValVec(imgOld)[1]
    
    newFace = tools.eigenFace(vNew, imageNew)
    oldFace = tools.eigenFace(vOld, imageOld)
    
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