"""
import numpy as np
import math
from sympy import *

d, s = input().split()
d = float(d)
s = float(s)
print(d, s)

def l(a1, a2):
    return 2 * float(a1) * (sinh(a2 / 2 / a1))

x = symbols('x')
f = x * cosh(d / (2*x)) - s - x

def newtonsMethod(f, p0, tol, N):
    global x
    df = diff(f, x)
    for i in range(N):
        p = p0 - f.subs(x, p0) / df.subs(x, p0)
        print("p" + str(i+1) + ": " + str(float(p)))
        if abs(p - p0) < tol: 
            return p
        p0 = p

a = newtonsMethod(f, d/2, 1e-8, 500)
print("\n\n", a)
print(l(a, d))
"""
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

left = 70000
right = 70000
if (f(left) < 0):
    while(f(left) < 0):
        left -= 1000
        if (left == 0): left = 0.04
    right = left + 1000
else:
    while(f(right) > 0):
        right += 1000
    left = right - 1000
a = bisection(f, 0.04, 100001, 1e-8)
print(l(a, d))