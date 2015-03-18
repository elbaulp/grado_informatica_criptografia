# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:49:35 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from random import randint

from ej3 import powerModInt
#import pdb

def MillerRabin(p):
    """
        Input: p integer such as p >= 5 and odd.
        
        Output: p is prime or probably prime
    """
#    pdb.set_trace()
    
    assert p >= 5    
    
    if 1 & p == 0:
        return False
    
    s = p - 1
    u = 0
    while (1 & s) == 0:
        s >>= 1
        u += 1 

    prime = False

    for _ in xrange(20):
        a = randint(2, p - 2)
        a = powerModInt(a,s,p)
        
        if a == 1 or a == p - 1:
            prime = True
            continue
        else:
            i = 1
            while i < u - 1:
                i += 1
                a = powerModInt(a,2,p)
                if a == p - 1:
                    prime = True
                    continue
                if a == 1:
                    prime = False
                    continue
#            prime = False
    return prime

#    for _ in xrange(20): # with k=20, test will output probably prime with a prob of 1/4**20
#        a = randint(2, p-2)
#        a = powerModInt(a,s,p)
#        if a != 1 and a != (p-1):
#            i = 1
#            while i < s and a != (p-1):
#                a = powerModInt(a,2,p)
#                if a == 1:
#                    return "Not prime"
#                i += 1
#            if a != (p-1):
#                return "Not prime"
#    return "Prime"

print MillerRabin(90221078753392184154149622269679731705920869572364323146777389106744249167893287091491005751893264013854756094230384816436985035887367570198390830836626929620930395458607390051335962764852769424941031051670131521265969408350800112779692655340042253991970492761524977413231930703094065023050574077317620529581736775256036443993928340221545607375549860405933153255776836414051570996984167934585339322850189347872718439350738428272565094611168867981011370318335242028953808721309056435214502065537377043)