# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:38:28 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from ej1 import checkGolomg

def LFSR(coef,sem,longitud):
    
    assert(len(coef)==len(sem))
        
    l = []
    
    for k in xrange(longitud):
        sj = 0
        for i in xrange(len(coef)):
            a = sem[i] & coef[i]
            sj = sj ^ a
        l.append(sem[len(sem) - 1])
        sem = [sj] + sem
        sem = sem[:-1]
 
    return l
    
#print LFSR([1,0,1], [1,1,1], 12)
#print LFSR([1,0,0,1], [0,1,1,0], 30)
# primitive polynomial

#s = ''.join(map(str, LFSR([1,0,0,1,0], [1,1,1,1,1], 2**5 - 1)))
#
#print checkGolomg(s)

if __name__ == '__main__':
    pass