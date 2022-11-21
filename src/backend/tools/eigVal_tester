import eigenValVec as ev
import covarianceRemake as CR
import numpy as np


# S adalah himpunan gambar
# Bentuk: N x 256 x 256
S = CR.getHimpunanImgV3("./././test/small_dataset/1")

# avg_S adalah rata-rata himpunan gambar
# Bentuk: N x 256^2
avg_S = CR.averageImgV8(S)
subtracted_greeked = CR.substractAllHimpunan(S)
print(len(subtracted_greeked))
print(len(subtracted_greeked[0]))


# covarGreek adalah covariance greek
# N x N dengan N merupakan jumlah gambar
covarGreek = CR.covarianceGreek("./././test/small_dataset/1")
print(len(covarGreek))
print(len(covarGreek[0]))


# Q R merupakan hasil dekoposisi matrix covariance
Q, R = ev.QR_decompositionV2(covarGreek)
print(Q)
print(R)
print("========================")
Q1, R1 = np.linalg.qr(covarGreek)
print(Q1)
print(R1)

print("\n\n")

# eigVal merupakan eigen value dari matrix kovarian aksen
eigVal = ev.getEigenValueQR(covarGreek,145)
print(eigVal)
print("===========================================================")
eigVal1, eigVec1 = np.linalg.eig(covarGreek)
print(eigVal1)

print("\n\n")

# eigVec merupakan eigen vektor dari matrix kovarian aksen
eigVec = ev.getEigenVectorQR(covarGreek, eigVal) # fungsi buatan
print(np.matrix(eigVec)) 
print("===================================================================================")
print(eigVec1) # linalg


#eigVal2, eigVec2 = ev.eigen_qr_simple(covarGreek)
print("==============================================================================")
# print(eigVal2)

A = [[1,2,3],
     [9,9,9],
     [4,2,-5]]

eigVals = ev.getEigenValueQR(A,145)
eigVecs = ev.getEigenVectorQR(A,eigVals)

print("==================================================================")
print(np.matrix(eigVecs))
print("==================================================================")
print("==================================================================")
valTes, vecTes = np.linalg.eig(A)
print(vecTes)

print("==================================================================")
print("==================================================================")
himpGambar = np.transpose(subtracted_greeked)
realVector = ev.getRealEigenVector(himpGambar,eigVec)
print(len(realVector))
print(len(realVector[0]))
print(np.matrix(realVector))

print("==================================================================")
print("==================================================================")
eigFace = ev.getEigenFace(himpGambar, realVector)
print(np.matrix(eigFace))

print("==================================================================")
print("==================================================================")

