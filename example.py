import pade
from numpy import *

def f(z): return 1.0/(z-1.0+1.0j)*(z-2.0+2.0j)

xs = linspace(0.1, 5, 10)
zs = linspace(0, 20, 20)*1j
us = f(zs)

print('original f')
print(['%1.4f %1.4f'%(f(x).real, f(x).imag) for x in f(xs)])

p = pade.fit(zs, us)

print('\npade approximant')
print(['%1.4f %1.4f'%(p(x).real, p(x).imag) for x in xs])

print('\ndifference')
print(['%1.4f %1.4f'%(f(x).real-p(x).real, f(x).imag-p(x).imag) for x in xs])
