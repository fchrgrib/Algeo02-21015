import eigenValVec as EV
import averageImage as AV 
import numpy as np  


def getOneImage (path):
    # Mengambil 1 image dari path
    img = AV.readImg(path)
    return img