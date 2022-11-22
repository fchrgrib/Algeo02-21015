# Import modules -------------------------------------------

import cv2

# Import custom modules ------------------------------------

import src.backend.utils.averageImage as AV 

# Functions ------------------------------------------------

# 1. Get an image from path
def getOneImage (path):
    # Mengambil 1 image dari path
    img = AV.readImg(path)
    img = cv2.resize(img, (256,256), fx = 1, fy = 1)
    return img