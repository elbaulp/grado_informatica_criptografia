# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:38:20 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys

sys.path.append('../../P1')

from modularArith.ej1 import extGcd

def compute_e(phi_n):
    """
    Calculate a number e such that gcd(e, phi_n) = 1.
    This number, along with n, will form a RSA public key (n,e)
    """
    
    e = phi_n + 2

    found = False
    while(not found):
        gcd = extGcd(e,phi_n)
        if(gcd[0] == 1):
            found = True
        else:
            e += 1

    return e

def ascii_print(v):
    """
    Print the contents of a file
    """
    with open(v, 'rb') as file:
        print file.read()

if __name__ == '__main__':
    pass