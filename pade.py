
from numpy import *
from functools import lru_cache


def pade(z, zs, us):

    @lru_cache(maxsize=1024)
    def g(p, n):
        if p==0: return us[n]
        return (g(p-1, p-1) - g(p-1, n))/((zs[n]-zs[p-1])*g(p-1, n))
     
    #g.cache_clear()
        
    An1 = 0.0
    An  = g(0, 0)
    Bn1 = 1.0
    Bn  = 1.0
    
    for n,zn in enumerate(zs[:-1]):    
        a = g(n+1,n+1)
        An1, An = An, An + (z-zn)*a*An1
        Bn1, Bn = Bn, Bn + (z-zn)*a*Bn1
        
    print(g.cache_info())
        
    return An/Bn
