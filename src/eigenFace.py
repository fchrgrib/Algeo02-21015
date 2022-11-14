import covariance as cov
import subtractAvAndTrain as sub


def eigenFace(vector, path):
    subtract = sub.subtractAvAndTrain(path)
    all = len(subtract)
    eig = [[[0 for i in range(len(subtract))] for j in range(256)] for k in range(256)]
    for i in range(all):
        eig[i] = cov.multiplyMtrx(vector,subtract[i])
    return eig