from collections import defaultdict
import heapq as heap

def testCase():
    n, m, t = (int(i) for i in input().strip().split())
    s, g, h = (int(i) for i in input().strip().split())
    weights = [list() for i in range(n+1)]
    for i in range(m):
        a, b, d = (int(j) for j in input().strip().split())
        weights[a].append((b, d))
        weights[b].append((a, d))
    dests = [False for i in range(n+1)]
    for i in range(t):
        dests[int(input())] = True

    goneThroughPath = [False for i in range(n+1)]
    visited = set()
    pq = []
    nodeCost = defaultdict(lambda: float('inf'))
    nodeCost[s] = 0
    heap.heappush(pq, (0, s))
    while pq:
        _, node = heap.heappop(pq)
        visited.add(node)
        for adjNode, weight in weights[node]:
            if adjNode in visited: continue
            newCost = nodeCost[node] + weight
            if nodeCost[adjNode] > newCost:
                goneThroughPath[adjNode] = (node == g and adjNode == h) or (node == h and adjNode == g) or goneThroughPath[node]
                nodeCost[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))
            if nodeCost[adjNode] == newCost and ((node == g and adjNode == h) or (node == h and adjNode == g) or goneThroughPath[node]):
                goneThroughPath[adjNode] = True
                
    return [i for i in range(1, len(goneThroughPath)) if goneThroughPath[i] and dests[i]]

def main():
    testCases = int(input())
    res = list()
    for i in range(testCases):
        res.append(testCase())
    for r in res:
        if (len(r) != 0):
            print(' '.join(map(str, r)))
        
if __name__ == "__main__":
    main()