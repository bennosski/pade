# pade
Computes the N-point [Pade approximant](https://en.wikipedia.org/wiki/Pad%C3%A9_approximant) for a function in the complex plane. 

The Pade approximant often gives better approximation of the function than truncating its Taylor series, and it may still work where the Taylor series does not converge.

Useful for analytic continuation of complex functions such as single particle response functions in condensed matter physics computed on the imaginary axis.

Calculated following the algorithm provided in [H. J. Vidberg and J. W. Serene, J. Low Temp. Phys. 29,
179 (1977).](https://link.springer.com/article/10.1007%2FBF00655090)

Example usage:
```
# fit the pade approximant at points 'zs' with values 'us'
p = pade.fit(zs, us)    

# evaluate the pade approximant at point 'z'
p(z)
```
