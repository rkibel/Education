inf = 10000000
import numpy as np
 
# Function to minimize the cost to
# add the array elements to a single element
def minCost(a, i, j, k, prefix, dp):
     
    if (i >= j):
        return 0
 
    # Check if the value is
    # already stored in the array
    if (dp[i][j] != -1):
        return dp[i][j]
 
    best_cost = inf
    for pos in range(i, j):
 
        # Compute left subproblem
        left = minCost(a, i, pos,
                       k, prefix, dp)
 
        # Compute left subproblem
        right = minCost(a, pos + 1, j,
                        k, prefix, dp)
 
        # Calculate minimum cost
        best_cost = min(best_cost,
                        left + right +
                          (k * Combine(prefix, i, j)))
 
    # Store the answer to
    # avoid recalculation
    dp[i][j] = best_cost
     
    return dp[i][j]
 
# Function to generate the cost using
# Prefix Sum Array technique
def preprocess(a, n):
     
    p = [0] * n
    p[0] = a[0]
     
    for i in range(1, n):
        p[i] = p[i - 1] + a[i]
         
    return p
 
# Function to combine the sum
# of the two subproblems
def Combine(p, i, j):
     
    if (i == 0):
        return p[j]
    else:
        return p[j] - p[i - 1]
 
# Driver Code
if __name__ == "__main__":
     
    n = 6
    x = 10*np.random.random(10) + 1
    a = [int(x[i]) for i in range(len(x))]
    k = 1
 
    # Initialise dp array
    dp = [[-1 for x in range (n + 1)]
              for y in range (n + 1)]
 
    # Preprocessing the array
    prefix = preprocess(a, n)
 
    print(a)
    print(minCost(a, 0, n - 1, k, prefix, dp))
    print(dp)