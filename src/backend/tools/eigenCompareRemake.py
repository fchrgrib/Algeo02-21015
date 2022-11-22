import eigenValVec as EV
import averageImage as AV 
import numpy as np  


def getOneImage (path):
    # Mengambil 1 image dari path
    img = AV.readImg(path)
    return img

def subtractOneImage (matrix, avg):
    # matrix merupakan image yang ingin dikurang
    # avg merupakan average dataset
    A = np.subtract(matrix,avg)
    return A
    