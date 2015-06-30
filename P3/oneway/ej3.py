# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:41 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys
sys.path.append('../../P1')

from modularArith.ej1 import extGcd

def calculePQFromRabin():
    p = extGcd(48478872564493742276963,37659670402359614687722+12)
    q = extGcd(48478872564493742276963,37659670402359614687722-12)
    return p[0],q[0]

print calculePQFromRabin()