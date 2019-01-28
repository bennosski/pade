
from numpy import *
from functools import lru_cache


class pade:
    def __init__(self, a, zs, us):
        self.a  = a
        self.zs = zs
        self.us = us
        
    def __call__(self, z):
        An1 = 0.0
        An  = self.a[0]
        Bn1 = 1.0
        Bn  = 1.0
    
        for n,zn in enumerate(self.zs[:-1]):    
            An1, An = An, An + (z-zn)*self.a[n+1]*An1
            Bn1, Bn = Bn, Bn + (z-zn)*self.a[n+1]*Bn1

        return An/Bn


def fit(zs, us, verbose=False):
    '''
    Computes the coefficients for the continued fraction representation of the Pade approximant

    verbose prints cache info
    '''
    
    @lru_cache(maxsize=None)
    def g(p, n):
        if p==0: return us[n]
        return (g(p-1, p-1) - g(p-1, n))/((zs[n]-zs[p-1])*g(p-1, n))

    a = [g(0,0)]
    for n,zn in enumerate(zs[:-1]):    
        a.append(g(n+1,n+1))
        
    if verbose: print(g.cache_info())
    
    return pade(a, zs, us)
