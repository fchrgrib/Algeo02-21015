import src.backend.tools.covariance as cov
import src.backend.tools.subtractAvAndTrain as sub


def eigenFace(vector, path):
    subtract = sub.subtractAvAndTrain(path)
    all = len(subtract)
    eig = [[[0 for i in range(len(256))] for j in range(256)] for k in range(subtract)]
    for i in range(all):
        eig[i] = cov.multiplyMtrx(vector,subtract[i])
    return eig