import src.backend.tools.covariance as cov
import src.backend.tools.subtractAvAndTrain as sub
import numpy as np
import src.backend.tools.eigenValVec as EV
import src.backend.tools.averageImage as AV
import src.backend.tools.covarianceRemake as CR


def eigenFace(vector, path):
    subtract = sub.subtractAvAndTrain(path)
    all = len(subtract)
    eig = np.array([[[0 for i in range(256)] for j in range(256)]])
    for i in range(all):
        eig = np.dot(vector,subtract[i])
    # print(eig)
    return eig


''' path = './././test/small_dataset/1'
S = CR.getHimpunanImgV3(path)
covar = CR.covarianceManual(path)
eigVal = EV.getEigenValueQR(covar,30)
eigVec = EV.getEigenVectorQR(covar, eigVal)
tesFace = eigenFace(eigVec,path)

print(np.matrix(eigVec))
print(("=============================="))
e , v = np.linalg.eig(covar)
print(v)

print(("=============================="))

print(tesFace) '''