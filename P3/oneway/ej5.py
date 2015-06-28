# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:41 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys
sys.path.append('../../P1')

from modularArith.ej1 import extGcd
from modularArith.ej2 import moduloInverse
from modularArith.ej3 import powerModInt

p = 76625411 # Computed with http://www.wolframalpha.com/input/?i=next+prime+5
q = 19910227
n = p * q
phi_n = (p-1)*(q-1)

def ComputeE():
    e = phi_n + 2

    found = False
    while(not found):
        gcd = extGcd(e,phi_n)
        if(gcd[0] == 1):
            found = True
        else:
            e += 1
    return e

def ComputeD():
    e = ComputeE()
    d = moduloInverse(e,phi_n)#inverso de e mod p-1*q-1
    return d,e

def RSA(i):
    d,e = ComputeD()
    f_x = powerModInt(i,e,phi_n)
    f_minus_1 = moduloInverse(i, phi_n)
    return f_x, f_minus_1


print RSA(1234567890)
# print powerModInt(r, -1, n)
