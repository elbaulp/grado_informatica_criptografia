# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:47:06 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from math import ceil
from math import sqrt
from timeit import time

from ej3 import powerModInt
from ej2 import moduloInverse

def babyGiantStep(alpha, beta, p):
    """
        Compute discrete logarithm of alpha and beta, base p. For example
        given alpha, beta and p, We want to know which c times alpha is beta modulo p.
        Which is c = log_a b mod p
        
        Output: x = log_alpha (beta) mod p
    """
    m = int(ceil(sqrt(p - 1)))
    
    L = {}    
    for j in xrange(m):
        power = powerModInt(alpha, j, p)
        L[power] = j
    alphaInv = powerModInt(moduloInverse(alpha, p), m, p)
        
    for i in xrange(m - 1):
        y = (beta * powerModInt(alphaInv, i, p)) % p
        if L.get(y) != None:
            return i*m + L[y]



start_time = time.time()
print babyGiantStep(315654,51216931716,72345123259)
elapsed_time = time.time() - start_time
print("%0.10f" % elapsed_time) 