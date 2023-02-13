# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 16:40:05 2023
@author: Ron Kibel
@PERM: 5166087
"""

import math
import numpy as np

"""
# Section 1.3, Problem 4

n = 4
sum = 0
for i in range(1, n+1):
    sum += (-1)**(i+1) * (1/(2*i-1)) * (1/(2**(2*i-1)) + 1/(3**(2*i-1)))
sum *= 4
print(10**-3)
print(abs(sum-math.pi))

"""

"""
# The bisection method and the output of p and the error of p
# Used in most of Section 2.1
# To use this, modify f(x), the step count, and left and right bounds a and b


def f(x):
    return _

def bisection(f, a, b, steps): 
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("there is no root between a and b")
    mid = (a + b)/2
    if steps == 1:
        return mid
    if np.sign(f(a)) == np.sign(f(mid)):
        return bisection(f, mid, b, steps-1)
    return bisection(f, a, mid, steps-1)

steps = _
a = _
b = _

print("midpoint:", bisection(f, a, b, steps))
print("value:", f(bisection(f, a, b, steps)))

"""

"""
# The fixed point iteration method
# Used in most of Section 2.2
# To use this, modify g(x), the step count, and the beginning iteration (p0)

def g(x):
    return _

def fixedpt(g, p0, steps):
    p_n = p0
    for i in range(steps):
        p_n = g(p_n)
    return p_n

steps = _
p0 = _
for i in range(1, steps+1):
    print(fixedpt(g, p0, i))
"""

        
        
        
    