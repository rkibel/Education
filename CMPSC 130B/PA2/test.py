import math

def main():
    n = int(input())
    arr = [0 for i in range(n+1)]
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    
    # Problem 2 part a
    # for i in range(3, n+1):
    #     for j in range(1, i):
    #         arr[i] += arr[i-j]*arr[j]
    
    # Problem 2 part c
    for i in range(3, n+1):
       for j in range(1, i):
           arr[i] += arr[i-j]*arr[j]
           if j > 1 and abs(int(i / j) - (i / j)) < 1e-12:
               print(i, j)
               arr[i] += arr[j]*arr[int(i/j)]
    print(arr)
    
if __name__ == "__main__":
    main()