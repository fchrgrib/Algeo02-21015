import sympy
import sympy as sym
import math
import numpy as np
from sympy import Eq, solve, factor, solveset, init_printing, FiniteSet
from sympy.codegen.ast import real
from sympy.core import expr
init_printing(use_unicode=True)
x = sym.symbols('k2',real=True)
a = [[1,2,3],[2,3,4],[2,3,5]]

for i in range (len(a)):
    a[i][i] = a[i][i]*x
a = sym.Matrix(a)
det = x**2+4*x+1
anu = sym.det(a)
print(solveset(Eq(det,0),x))
print(solveset(Eq(anu,0),x))
