# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:22:47 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

def main():
    a = 10456
    k = 1454561
    n = 13443213244241434327893275285794573489532475089364564324132413244121324
    
    print str(a) + " times " + str(k) + " mod " + str(n) + " is " + str(powerModInt(a,k,n))

def powerModInt(a,k,n):
    """
        @input a in Z_n and integers 0 <= k <= n in binary representation
        
        @outup a times k mod n
    """
    b = 1
    if k == 0:
        return b
    A = a
    if 1 & k: # If the least significant bit is 1, a^1 = a
        b = a
    k = k >> 1
    while k:
        A = (A**2) % n
        if 1 & k:
            b = (b * A) % n
        k = k >> 1
        
    return b

if __name__ == '__main__':
    main()