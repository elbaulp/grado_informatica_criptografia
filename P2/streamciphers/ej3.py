# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:17:26 2015

@author: hkr (elbauldelprogramador.com)
"""

def NLFSR(f, s, k):

    assert(len(f[0])==len(s))

    l = []
    
    for _ in range(0,k): 
        sj = 0
        for i in f:
            r = 1
            for j,seed in zip(i,s):
                r = (r + seed * j) % 2
            sj = sj ^ r
            
        l.append(sj)
        s = [sj] + s
        
        s = s[:-1]

    return l
    
print NLFSR([[0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]], [1, 0, 1, 1], 20)