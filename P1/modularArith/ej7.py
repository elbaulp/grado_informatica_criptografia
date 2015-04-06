# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:51:44 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from math import ceil
from timeit import time

import gmpy

from ej3 import powerModInt
from ej1 import extGcd

def Pollard(n, iter1=50, iter2=10):
    """
        Implementation of the Pollard algorithn for factoring integers mod n
    """
    def f(t):
        """ 
            t**2 + 1 Mod n
        """
        return powerModInt(t, 2, n) + 1
    
    z = 1
    x = f(0)
    y = f(x)
    
    for _ in xrange(iter1):
        for _ in xrange(iter2):
            x = f(x) % n
            y = f(f(x)) % n
            z = (z * (x - y)) % n
            
        d = extGcd(z, n)[0]
        if d > 1:
            return d, n//d
#        if d == 1:
#            x = f(x)
#            y = f(f(x))
    return d, n//d
# 187, 4717, 278009, 63053699, 549314599, 7247123747459, 2097335995683611, 4274010960572200553847767
start_time = time.time()
print Pollard(1234567)
elapsed_time = time.time() - start_time
print("%0.10f" % elapsed_time) 


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def Fermat(n):
    """
        Implementa el Método de Fermat para factorización de enteros
    """
    if 1 & n == 0:
        return "The number is even"
    x = int(ceil(isqrt(n)))
    perfect = (x * x) - n
    isPerfect = False
    while not isPerfect:
        x += 1
        perfect = (x * x) - n
        if gmpy.is_square(perfect):
            isPerfect = True
    return x - isqrt(perfect)
    
start_time = time.time()
print Fermat(23)
elapsed_time = time.time() - start_time
print("%0.10f" % elapsed_time) 