import numpy as np
import math

def f(x):
    return x * math.cosh(d / (2*x)) - s - x

def l(a1, a2):
    return 2 * a1 * math.sinh(a2 / 2 / a1)
    
def bisection(f, left, right, tol): 
    if np.sign(f(left)) == np.sign(f(right)):
        raise Exception(
         "The scalars a and b do not bound a root")        
    m = (left + right)/2
    if np.abs(f(m)) < tol: return m
    elif np.sign(f(left)) == np.sign(f(m)): return bisection(f, m, right, tol)
    return bisection(f, left, m, tol)

d, s = input().split()
d = int(d)
s = int(s)

left = 7000
right = 7000
if (f(left) < 0):
    while(f(left) < 0):
        left -= 100
        if (left == 0): left = 0.04
    right = left + 100
else:
    while(f(right) > 0):
        right += 100
    left = right - 100
a = bisection(f, left, right, 1e-8)
print(l(a, d))