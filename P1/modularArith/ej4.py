# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:49:35 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from random import randint

from ej3 import powerModInt

def MillerRabin(p):
    """
        Input: p integer such as p >= 5 and odd.
        
        Output: p is prime or probably prime
    """
    
    if 1 & p == 0:
        return "Not Prime"
    
    s = p - 1
    u = 0
    while (1 & s) == 0:
        s >>= 1
        u += 1 
    
    for _ in xrange(20): # with k=20, test will output probably prime with a prob of 1/4**20
        a = randint(2, p-2)
        a = powerModInt(a,s,p)
        if a != 1 and a != (p-1):
            i = 1
            while i < s and a != (p-1):
                a = powerModInt(a,2,p)
                if a == 1:
                    return "Not prime"
                i += 1
            if a != (p-1):
                return "Not prime"
    return "Prime"

print MillerRabin(569)