# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:38:28 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from ej1 import checkGolomg

def LFSR(coef,sem,longitud):
    
    assert(len(coef)==len(sem))
        
    l = sem
    for k in xrange(longitud - len(coef)):
        sj = 0
        for i in xrange(len(coef)):
            a = sem[i] & coef[i]
            sj = sj ^ a
        l.append(sj)
        sem = l[len(l) - len(coef) : len(l)]
 
    return l
    

if __name__ == '__main__':
    
    #print LFSR([1,0,1], [1,1,1], 12)
    #print LFSR([1,0,0,1], [0,1,1,0], 30)
    # primitive polynomial
    
    s = ''.join(map(str, LFSR([1,0,0,1,0], [1,1,1,1,1], 2**5 - 1)))
    p = ''.join(map(str, LFSR([1,0,0,1], [1,0,0,1], 2**4 - 1)))
    print p
    print checkGolomg(p)
