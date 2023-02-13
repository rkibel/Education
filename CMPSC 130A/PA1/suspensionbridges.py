import numpy as np
import math

def f(x):
    return x * math.cosh(d / (2*x)) - s - x

def l(a1, a2):
    return 2 * a1 * math.sinh(a2 / 2 / a1)
    
def bisection(f, left, right, tol):
    signLeft = 1
    try:
        signLeft = np.sign(f(left))
    except:
        pass
    signRight = np.sign(f(right))
    if signLeft == signRight:
        raise Exception("The scalars a and b do not bound a root")        
    m = (left + right)/2
    if np.abs(f(m)) < tol: return m
    elif signLeft == np.sign(f(m)): return bisection(f, m, right, tol)
    return bisection(f, left, m, tol)

d, s = input().split()
d = int(d)
s = int(s)

a = bisection(f, 0.04, 125001, 1e-5)
print(l(a, d))