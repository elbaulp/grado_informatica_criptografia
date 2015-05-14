# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:17:26 2015

@author: hkr (elbauldelprogramador.com)
"""

def NLFSR(f, s, k):

    assert(len(f[0])==len(s))

    l = []
    
    for i in s:
        l.append(i)    
    
    for _ in xrange(k): 
        sj = 0
        for i in f:
            r = 1
            for j,seed in zip(i,s):
                if j == 1:
                    r = r * seed
            sj = sj ^ r
            
        l.append(sj)
        s = s + [sj] 
        
#        for i in xrange(len(s) - 1):
#            s[i] = s[i+1]
            
        s = s[:-1]

    return l
    
print NLFSR([[0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]], [1, 1, 1, 1], 20)