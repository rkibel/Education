import numpy as np 
import sys
import math
import matplotlib.pyplot as plt

#
# f(i, x, y) should return the value of f_i(x, y) for all integers i >= 1 and integers x, y
# You need to fill in the code to correctly compute the function f. 
#
def f(i, x, y):
    arr = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    if (i == 1):
        for i in arr:
            if (x, y) == i: 
                return 1
        return 0
    
    if (x % 3 != 0) and (y % 3 != 0): return 0
    return f(i-1, math.floor((x+1)/3), math.floor((y+1)/3))
    
    
        
# Your code goes here    

# 
# b(i) should compute b_i (for i >= 1) 
#
def b(i):
    return int((pow(3, i) - 1) / 2)
# Your code goes here    

#
# Don't need to touch this code. To plot the grid for i=3 run "python snow.py 3" from the command line
# If you dont already have numpy and/or mathplotlib installed, run 
# pip install numpy 
# pip install mathplotlib
# in the command line first. 
#
def A(i):
    return [[1-f(i,x,y) for x in range(-b(i), b(i)+1)] for y in range(-b(i), b(i)+1)]


H = np.array(   A(   int(sys.argv[1])    )   )    

plt.axis('off')
plt.imshow(H, interpolation='none', cmap='gray', vmin=0, vmax=1)
plt.show()

