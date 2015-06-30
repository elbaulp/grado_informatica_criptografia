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
from Utils import compute_e

p = 76625411 # Computed with http://www.wolframalpha.com/input/?i=next+prime+5
q = 19910227
n = p * q
phi_n = (p-1)*(q-1)

def ComputeD():
    e = compute_e(phi_n)
    d = moduloInverse(e,phi_n)
    return d,e

def RSA(x):
    d,e = ComputeD()
    return powerModInt(x, d, n)

print RSA(1234567890)
