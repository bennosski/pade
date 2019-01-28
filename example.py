import pade
from numpy import *

def f(z): return 1.0/(z-1.0+1.0j)*(z-2.0+2.0j)

xs = linspace(0.1, 5, 10)
zs = linspace(0, 20, 20)*1j
us = f(zs)

print('original f')
print(f(xs))

p = pade.fit(zs, us)

print('pade approximant')
print([p(z) for z in xs])

