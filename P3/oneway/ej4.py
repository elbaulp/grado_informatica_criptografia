# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:41 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

def h(b,x):
    n = 48478872564493742276963
    a0 = 621137347346**2 % n
    a1 = 137252404096**2 % n
    
    return (x**2  * a0**b * a1**(1-b)) % n

def MerkleDamgard(li,x):
    cost = 0
    for i in xrange(len(li)):
        cost = h(li[i],x)    
        x = cost
    return cost
    
print MerkleDamgard([1,1,1,1], 789651975)
    
