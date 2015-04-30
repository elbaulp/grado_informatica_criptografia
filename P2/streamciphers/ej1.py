# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:00:58 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

from utils import Runs
from utils import hamming

def checkGolomg(seq):
    """
        1. 0s and 1s in the sequence are as near as possible to n/2
        2. The number of runs of given length should halve when the length is in-
           creased by one (as long as possible), and where possible equally many runs
           of given length should consist of 0s as of 1s
        3. The out-of-phase autocorrelation should be constant (independent of the shift)
    """
    
    postulates = [True, True, True]

    ## Check postulate 1
    zeros = seq.count("0")
    ones = seq.count("1")
    
    if abs(zeros-ones) > 1:
        postulates[0] = False
    
    ## Postulate 2
    r = Runs(seq)
    keys = r.keys()
    
    if r:     
        for i in xrange(len(keys)-1):
            if keys[i] - keys[i+1] != -1:
                postulates[1] = False
                break
            if r[keys[i]] != 2 * r[keys[i+1]]:
                if r[keys[i]] != 1 and r[keys[i+1]] !=1: 
                    postulates[1] = False
                    break
    else:
        postulates[1] = False
    
    ## Postulate 3 
        
    postulates[2] = hamming(seq)
    
    return True if sum(postulates) == 3 else False 

if __name__ == '__main__':
    pass