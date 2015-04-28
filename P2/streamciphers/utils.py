# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:09:08 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

def Runs(b):
    """
        @params: The bit sequence to calculate the runs
        
        @return: A dict with the number of runs, key = #run, value, how many 
        runs are for that run
    """
    # https://github.com/fnavarrogonzalez/criptography/blob/master/p2.py 
    
    runs = {}    
    run = 1
    
    i=0
    # Shift the string if begin and end are the same
    while b[0] == b[len(b)-1]:
        if i > len(b):
            return dict()
        b = b[1:] + b[0]
        i+=1
        
    # Add 0 or one to the end in order to count the last run
    if(b[len(b)-1]=="1"):
        b+="0"
    else:
        b+="1"

    for i in range(0,len(b)-1):
        if b[i] == b[i+1]:
            run+=1
        else:
            try:
                k = runs.get(run,0)
                runs[run] = k + 1
            except:
                runs[run]=[i]
            run = 1 

    return runs

def hamming(b):
    """
        Calculate the hamming distance of a bit sequence
        
        @param: b, the bit sequence
        
        @return: True or false if the sequence pass the hamming distance
    """
    distances = []
    distances.append(sum([ord(a) ^ ord(c) for a,c in zip(b,b[1:] + b[:1])]))
    
    for i in xrange(1, len(b)):
        shifted_b = b[i:] + b[:i]
        distances.append(sum([ord(a) ^ ord(c) for a,c in zip(b,shifted_b)]))
        if distances[i-1] != distances[i]:
            return False
    return True

if __name__ == '__main__':
    pass