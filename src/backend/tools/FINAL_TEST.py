import eigenValVec as EV
import covarianceRemake as CR
import eigenCompareRemake as ECR
import averageImage as AV


path = './././test/small_dataset/1' # path folder
pathImg = './././test/small_dataset/2/Alex Lawther77_139.jpg'

# setup awal
S = CR.getHimpunanImgV3(path)
avg = CR.averageImgV7(path)
S_subtract = CR.subtractNoFlat(S)
S_concat = CR.concatManual(S)

# dapatkan covariance
cov = CR.covarianceManual(path)

# dapatkan QR
Q, R = EV.QR_decompositionV2(cov)

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
file, jarak = ECR.getClosestImg(eigFace, eigFaceNew)
print(file)