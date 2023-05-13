import math

def main():
    n = int(input())
    tree = [list() for i in range(n)]
    for i in range(n-1):
        A, B, X, T = (int(j) for j in input().strip().split())
        tree[A].append((B, X / 100.0, T))
    liquid = [0]
    liquidInput = input().strip().split()
    for i in liquidInput:
        liquid.append(int(i))
    root = 1
    
    def getLiquid(node):
        if (liquid[node] != -1):
            return liquid[node]
        m = 0
        for path in tree[node]:
            if (path[2] == 1):
                m = max(m, math.sqrt(getLiquid(path[0])) / path[1])
            else:
                m = max(m, getLiquid(path[0]) / path[1])
        liquid[node] = m
        return m
    
    for i in range(1, n):
        if (liquid[i] == -1):
            root = i
            getLiquid(i)
    print(liquid[root])
    
if __name__ == "__main__":
    main()