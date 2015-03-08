# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:52:11 2015

Given a,b calculate the inverse of a modulus b, for all a,b integers and relative
primes.

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from ej1 import extGcd

def moduloInverse(a,n):
    """
        Returns the inverse of a modulo b, if it exists
    """      
    d,x,y = extGcd(a,n)
    print d,x,y
    if d > 1:
        return u' a inverse does not exist'
    else:
        return x
        
a = 391
n = 1542

print "Inverse of " + str(a) + " modulo " + str(n) + " is " + str(moduloInverse(a, n))