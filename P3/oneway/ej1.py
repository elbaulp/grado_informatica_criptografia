# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:17 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys
sys.path.append('../../P1')

from modularArith.ej2 import moduloInverse

# https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem

# priv key
q,w,r = 881, 706, 588

def cypher(m, li):
    # Pub key
    pub = []
    for i in xrange(len(li)):
        pub.append( (li[i] * r) % q)

    c = 0
    for i in xrange(len(pub)):
        c += int(m[i]) * pub[i]

    print "Pub: %s" % pub
    return c

def decypher(c, w):
    s = moduloInverse(r,q) * c % q

    m = []
    i = len(w) - 1
    while s != 0:
        if s >= w[i]:
            s -= w[i]
            m.append(1)
        else:
            m.append(0)
        i -= 1
    m.reverse()
    return chr(int(''.join(map(str, m)),2))

s = [2, 7, 11, 21, 42, 89, 180, 354]
c = cypher(bin(ord('b'))[2:].zfill(8), s)
m = decypher(c, s)

print 'E(m): %d' % c
print 'D(c): %s' % m

if __name__ == '__main__':
    pass
