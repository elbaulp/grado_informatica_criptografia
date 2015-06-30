# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:41 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys
import random

sys.path.append('../../P1')

from modularArith.ej4 import MillerRabin
from modularArith.ej3 import powerModInt
from modularArith.ej5 import babyGiantStep
from Utils import get_prime

def primitive(n):
    a = random.randint(2, n-2)
    while powerModInt(a, (n-1)/2, n) == 1:
        a = random.randint(2, n-2)
    return a

p = get_prime(76625397)
alpha = primitive(p)

print "p = %d" % p
print "alpha = %d" % alpha
birth = 19910210
print "log_%d(%d) = %d" % (alpha,birth, babyGiantStep(alpha, birth, p))
