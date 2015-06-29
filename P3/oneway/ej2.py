# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:41 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys
sys.path.append('../../P1')

from modularArith.ej2 import moduloInverse

def get_prime(p):
    """Returns the next prime starting in the number p

    :param p: The number from when to start looking for pimes
    :returns: The next prime starting from p
    """
    prime = False
    while not prime:
        if MillerRabin(p):
            prime = True
        else:
            p += 2
    return p

def primitive(n):
    if not 0x1 & n:
        n += 1
    q = int((n-1)/2)
    p = get_prime(q)
    p2 = get_prime(2 * p + 1)
    n = p2

    ## Falta Jacobi
