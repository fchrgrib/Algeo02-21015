import cv2
import averageImage as av


def subtractAvAndTrain(path):
    # fungsi ini digunakan untuk mendapatkan selisih antara training image dan rata rata
    s = av.getHimpunanImgV2(path)
    n = len(s)
    rata = av.averageImgV6(path)

    subtract = [[[0 for i in range(n)] for j in range(256)] for k in range(256)]
    for i in range(n):
        s[i] = cv2.resize(s[i], (256, 256), fx=1, fy=1)
        for j in range(256):
            for k in range(256):
                subtract[i][j][k] = s[i][j][k] - rata[j][k]
    return subtract
