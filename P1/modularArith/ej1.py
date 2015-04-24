# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:25:01 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from timeit import time

def main():
    start_time = time.time()
    print extGcd(5,-3)
    elapsed_time = time.time() - start_time
    print("%0.10f" % elapsed_time)

def extGcd(a,b):
    """
    Compute the Greatest Common Divisor d of a and b, and integers x and
    y satisfying ax + by = d.
    
    It returns a tuple (d,x,y)
    """
    
#    exange = False
#    if a < b:
#        a,b = b,a
#        exange = True

    if b == 0:
        return a,1,0
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    
    while b != 0:
        q = a//b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

#    if exange:
#        return map(int, (a, y2, x2))
#    else:
    if a < 0:
        return map(int, (-a, -x2, -y2))
    return map(int, (a, x2, y2))

if __name__ == '__main__':
    main()