import numpy as np
import sympy as sym


def all_minus(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            matrix[i][j] = -matrix[i][j]


def eigenVal(matrix):
    lengthMatrix = len(matrix)
    symb = sym.symbols('k')
    all_minus(matrix)
    for i in range(lengthMatrix):
        matrix[i][i] += symb[i]
    matrix = sym.Matrix(matrix)
    det = sym.det(matrix)


