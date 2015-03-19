# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:51:44 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from ej3 import powerModInt
from fractions import gcd

def Pollard(n, iter1=200, iter2=100):
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
            x = f(x)
            y = f(f(x))
            z = (z * (x - y)) % n
            
        d = gcd(z, n)
        if d > 1:
            return d, n/d
#        if d == 1:
#            x = f(x)
#            y = f(f(x))
    return d, n/d

print Pollard(455459)
print Pollard(10403)