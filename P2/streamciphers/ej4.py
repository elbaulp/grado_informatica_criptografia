# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:48:53 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from ej2 import LFSR

def geffe(coef1, s1, coef2, s2, coef3, s3, l):
    
    l1 = LFSR(coef1, s1, l)
    l2 = LFSR(coef2, s2, l)
    l3 = LFSR(coef3, s3, l)

    r = []   
    
    for i,j,k in zip(l1,l2,l3):
        x1 = i * j;
        x2 = j * k;
        x3 = k;
        f = (x1 ^ x2) ^ x3 
        r.append(f)
    
    return r
    
print geffe([1,1,0,0], [1,1,1,1],
            [1,0,1,0], [1,0,1,1],
            [1,1,0,1], [1,1,0,1], 
            25)