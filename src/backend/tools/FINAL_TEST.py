import eigenValVec as EV
import covarianceRemake as CR
import eigenCompareRemake as ECR
import averageImage as AV
import time
# from matplotlib import pyplot as plt

def main(path, pathImg):
    # path merupakan path dari foldernya
    # pathImg merupakan path dari image yang mau dibandingkan

    ''' path = './././test/small_dataset/1' # path folder
    pathImg = './././test/small_dataset/1/Adriana Lima0_0.jpg' '''

    # setup awal
    S = CR.getHimpunanImgV3(path)
    avg = CR.averageImgV7(path)
    S_subtract = CR.subtractNoFlat(S)
    # S_concat = CR.concatManual(S)

    # dapatkan covariance
    cov = CR.covarianceManual(path)

    # dapatkan QR
    # Q, R = EV.QR_decompositionV2(cov)

    # dapatkan eigen
    eigValFun = EV.getEigenValueQR(cov,20)
    eigVecFun = EV.getEigenVectorQR(cov, eigValFun)
    eigFace = EV.getEigenFaceV2(S_subtract, eigVecFun)

    # dapatkan img training
    T = ECR.getOneImage(pathImg)
    T_subtract = ECR.subtractOneImage(T, avg)

    # dapatkan eigen Face training
    eigFaceNew = ECR.getEigenOneImg(T_subtract)

    # dapatkan closest eucli distance
    fileNum, jarak = ECR.getClosestImg(eigFace, eigFaceNew)

    # dapatkan path dari image yang didapat
    pathFinal = AV.getcolorImageV2(fileNum,path)
    
    return pathFinal


# path = main('./././test/small_dataset/1', './././test/small_dataset/1/Adriana Lima0_0.jpg')
# print(path)