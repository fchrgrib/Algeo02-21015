import eigenValVec as EV
import covarianceRemake as CR
import eigenCompareRemake as ECR
import averageImage as AV
# import time
# from matplotlib import pyplot as plt
import numpy as np


def main(path, pathImg):
    # path merupakan path dari foldernya
    # pathImg merupakan path dari image yang mau dibandingkan

    # set up awal
    S = CR.getHimpunanImgV3(path)
    avgIm = CR.averageImgV8(S)
    S_substract = CR.substractAllHimpunan(S)
    # print(np.matrix(S_substract))

    cov_f = CR.covarianceGreekNew(path,path)
    # print("================================")
    # print(cov_f)

    eigValCov_f, eigVecCov_f = EV.QR_DecompositionV3(cov_f)


    # print("================================")


    eigFace = np.matmul(eigVecCov_f, S_substract)
    # print(np.matrix(eigFace))

    # eigConvert = CR.convertBackV2(eigFace)
    # print(len(eigConvert), ' ', len(eigConvert[0]), ' ', len(eigConvert[0][0]))

    # print("================================")
    # show = plt.imshow(eigConvert[1], cmap='gray')
    # plt.show()
    # print("================================")

    getOneImg = ECR.getOneImage(pathImg)
    oneImageMin = np.subtract(getOneImg,avgIm)
    oneImgFlat = oneImageMin.flatten()

    # print("================================")
    # show = plt.imshow(oneImageMin, cmap='gray')
    # plt.show()
    # print("================================")


    # print("================================")

    # print("================================")

    W = CR.getWeight(S_substract, eigFace)
    # print(np.matrix(W))

    # print(oneImgFlat)
    # print("================================")
    # W_T merupakan weight dari image yang ingin diuji
    W_T = CR.getWeightOne(oneImgFlat, eigFace)
    # print(W_T)

    # print("================================")
    # print("================================")


    dist, numberFile = CR.getDistanceW(W,W_T)
    # print(numberFile)
    
    result_path = AV.getcolorImageV2(numberFile,path)
    
    return result_path


# res = main('./././test/classes_pins_dataset/pins_Adriana_Lima', './././test/small_dataset/1/Adriana Lima26_149.jpg')
# print("=====================")
# print(res)
