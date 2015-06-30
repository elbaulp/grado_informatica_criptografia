# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:41 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""
import random
import binascii

n = 48478872564493742276963
a0 = random.getrandbits(10)**2 % n
a1 = random.getrandbits(10)**2 % n
text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def h(b,x):
    return (x**2  * a0**b * a1**(1-b)) % n

def MerkleDamgard(sem,m):
    """Implementation of the MerkleDamgard hash function.
    :param sem: Seed of the function
    :param m: Message to hash
    :returns: H(m)
    """
    x = sem

    for i in xrange(len(m)):
        x = h(int(m[i]), x)
    return x

print "h(m) = %d" % MerkleDamgard(15, bin(int(binascii.hexlify(text), 16))[2:])
