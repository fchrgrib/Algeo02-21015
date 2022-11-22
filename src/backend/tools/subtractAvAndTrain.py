import cv2
import numpy as np

import src.backend.tools.covarianceRemake as av


def subtractAvAndTrain(path):
    # fungsi ini digunakan untuk mendapatkan selisih antara training image dan rata rata
    s = av.getHimpunanImgV3(path)
    n = len(s)
    rata = av.averageImgV7(path)
    subtract = [[[0 for i in range(256)] for j in range(256)] for k in range(n)]
    for i in range(n):
        s[i] = cv2.resize(s[i], (256, 256), fx=1, fy=1)
        # for j in range(256):
        #     for k in range(256):
        subtract[i] = np.subtract(s[i], rata)
    # print(subtract)
    return subtract