# -*- coding: utf-8 -*-
"""
Created on Thu May 27 23:36:18 2021

@author: PC
"""


from sympy import sqrt

def DiscreteLog(g, h, p):
    '''
    Solve x such that g^x = h over GF(p).
    '''
    sqrt_n = int(sqrt(p-1))
    # Compute the baby steps and store them in the 'precomputed' hash table.
    precomputed = {}
    r = 1
    for i in range(sqrt_n + 1):
        precomputed[r] = i
        r = r * g % p
    # Now compute the giant steps and check the hash table for any matching.
    r = h
    s = pow(pow(g, -1, p), sqrt_n, p)
    for j in range(sqrt_n + 1):
        try:
            i = precomputed[r]
        except KeyError:
            pass
        else:
            # steps = sqrt_n + j
            logarithm = i + sqrt_n * j
            return logarithm
        r = r * s % p
        
def main():
    # 50-bit p: 3.3GB RAM  97,5,44
    g, h, p = 3, 525 ,809
    x = DiscreteLog(g, h, p)
    print(f"{g}^{x} % {p} == {h}")
    
if __name__ == '__main__':
    main()
