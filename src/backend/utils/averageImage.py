# Import modules -------------------------------------------

import cv2
import glob

# Functions ------------------------------------------------

# 1. Read image from path
def readImg (img_path):
    # membaca image dari file
    # return bentuk matriksnya
    img = cv2.imread(img_path,0)
    return img

# 2. Get original image
def getcolorImageV2(number, path):
    file = glob.glob(str(path)+"/*")
    new_file = []
    for i in range (len(file)):
        # print("Hello")
        new_file.append(file[i].replace("\\","/"))
        # print(new_file[i])
    return new_file[number]