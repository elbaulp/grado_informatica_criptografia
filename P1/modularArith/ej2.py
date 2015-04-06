# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:52:11 2015

Given a,b calculate the inverse of a modulus b, for all a,b integers and relative
primes.

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from timeit import time

from ej1 import extGcd

def main():
    a,n = 65398261921 , 89
    
    start_time = time.time()
    moduloInverse(a, n)
    elapsed_time = time.time() - start_time
    print("%0.10f" % elapsed_time)    
    
    print "Inverse of " + str(a) + " modulo " + str(n) + " is " + str(moduloInverse(a, n))    

def moduloInverse(a,n):
    """
        Returns the inverse of a modulo b, if it exists
    """      
    d,x,y = extGcd(a,n)

    if d > 1:
        return u' a inverse does not exist'
    else:
        return x


if __name__ == '__main__':
    main()