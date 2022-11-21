import src.backend.tools.covariance as cov
import src.backend.tools.subtractAvAndTrain as sub
import numpy as np


def eigenFace(vector, path):
    subtract = sub.subtractAvAndTrain(path)
    all = len(subtract)
    eig = np.array([[[0 for i in range(256)] for j in range(256)]])
    for i in range(all):
        eig = np.dot(vector,subtract[i])
    # print(eig)
    return eig