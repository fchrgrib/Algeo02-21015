# Import modules -------------------------------------------

import numpy as np

# Import custom modules ------------------------------------

import src.backend.utils.eigenValVec as EV
import src.backend.utils.covariance as CR
import src.backend.utils.eigenCompare as ECR
import src.backend.utils.averageImage as AV

# Main Program ---------------------------------------------

def main(path, pathImg):
    
    # Initial setup
    S = CR.getHimpunanImgV3(path)
    avgIm = CR.averageImgV8(S)
    S_substract = CR.substractAllHimpunan(S)
    
    # Get covarian
    cov_f = CR.covarianceGreekNew(path,path)
    
    # Get Eigen Vector
    eigValCov_f, eigVecCov_f = EV.QR_DecompositionV3(cov_f)
    
    # Get Eigen Face
    eigFace = np.matmul(eigVecCov_f, S_substract)
    
    # Compare Eigen
    getOneImg = ECR.getOneImage(pathImg)
    oneImageMin = np.subtract(getOneImg,avgIm)
    oneImgFlat = oneImageMin.flatten()
    W = CR.getWeight(S_substract, eigFace)
    W_T = CR.getWeightOne(oneImgFlat, eigFace)
    
    # Get Euclidian Distance
    numberFile, max, min = CR.getDistanceW(W,W_T)
    similarity = ((max - min)/max)*100
    result_path = AV.getcolorImageV2(numberFile,path)

    return result_path, similarity