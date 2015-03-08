# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:25:01 2015

@author: Alejandro Alcalde
"""

from math import floor

def main():
    print GCD(458784567,478962)

def GCD(a,b):
    """
    Compute the Greatest Common Divisor d of a and b, and integers x and
    y satisfying ax + by = d.
    
    It returns a tuple (d,x,y)
    """
    if a <= 0 or b <= 0 or a < b:
        return u'a and b must be positive and a >= b'    
    if b == 0:
        return a,1,0
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    
    while b > 0:
        q = floor(a/b)
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return map(int, (a, x2, y2))

if __name__ == '__main__':
    main()