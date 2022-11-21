import covarianceRemake as CR
import averageImage as AV
import eigenValVec as EV
import numpy as np

print("=========================================================")

path = './././test/classes_pins_dataset/coba1'
S = CR.getHimpunanImgV3(path)
S_subtract = CR.subtractNoFlat(S)
S_concat = CR.concatManual(S)
print("shape S_subtract: ", S_subtract.shape)

print("=========================================================")

cov = CR.covarianceManual(path)
print(np.matrix(cov))
print(len(cov), ',',len(cov[0]))

print("=========================================================")

Q, R = EV.QR_decompositionV2(cov)
eigValFun = EV.getEigenValueQR(cov,20)
eigVecFun = EV.getEigenVectorQR(cov, eigValFun)
print(np.matrix(eigVecFun))

print("=========================================================")

''' eigVal, eigVec = np.linalg.eig(cov)
print(eigVec)
 '''
print("=========================================================")

''' eigFace = EV.getEigenFace(S_concat, eigVecFun)
print(len(eigFace), ',', len(eigFace[0]))
print((np.transpose(eigFace))) '''

print("=========================================================")