# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:38:28 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

def LFSR(coef,sem,longitud):
    
    assert(len(coef)==len(sem))
        
    fin_cadena = ""
    fin_lista = []
    
    #Por cada caracter a generar
    for k in xrange(0,longitud):
        #reiniciamos el feedback
        sj = 0
        #por cada coeficiente del polinomio
        for i in xrange(0,len(coef)):
            #se multiplica (and) y se hace el xor con la anterior sj
            a = sem[i] & coef[i]
            sj = sj ^ a
        #se anade la semilla a la cadena
        fin_cadena += str(sem[len(sem)-1])        
        fin_lista.append(int(sem[len(sem)-1]))
        #se anade al principio
        sem = [sj]+sem
        # y se desplaza la semilla
        sem = sem[0:len(sem)-1]

 
    return fin_cadena,fin_lista
    
print LFSR([0,1,1,0,0], [1,1,1,1,1], 100)