# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:17 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys
sys.path.append('../../P1')

from modularArith.ej2 import moduloInverse

def super_creciente(li):
    #clave privada
    u,n,k = 41651,2097152,20
    sucesion = []
    for i in range(0,k):
        sucesion.append(2**i)
    #clave pública
    publica = []
    for i in range(0,k):
        publica.append((sucesion[i]*u)% n)
    #calculamos el valor
    coste = 0
    for i,j in zip(publica,li):
        coste = (coste + i*j) % n 
    return coste 

def super_creciente_inv(coste):
    #clave privada
    u,n,k = 41651,2097152,20
    sucesion = []
    for i in range(0,k):
        sucesion.append((2**i) % n)
    #inverso de 3, llave privada
    inverso = moduloInverse(u,2097152)
    s = (coste * inverso) %  n
    #lista de salida
    salida = []
    i = k
    while s !=0:
        if s >= sucesion[i-1]:
            s -= sucesion[i-1]
            salida.append(1)
        else:
            salida.append(0)
        i -= 1
    if len(salida) != k:
        for i in range(len(salida),k):
            salida.append(0)
    salida.reverse()
    return salida
    
print super_creciente([1,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1])

if __name__ == '__main__':
    pass