from collections import defaultdict
import heapq as heap

def testCase():
    try:
        n, m = (int(i) for i in input().strip().split())
        weights = [list() for i in range(n+1)]
        for i in range(m):
            a, b, d = (int(j) for j in input().strip().split())
            weights[a].append((b, d))
            weights[b].append((a, d))
            
        visited = set()
        pq = []
        distanceFrom2 = defaultdict(lambda: float('inf'))
        distanceFrom2[2] = 0
        heap.heappush(pq, (0, 2))
        while pq:
            _, node = heap.heappop(pq)
            visited.add(node)
            
            for adjNode, weight in weights[node]:
                if adjNode in visited: continue
                
                newCost = distanceFrom2[node] + weight
                if distanceFrom2[adjNode] > newCost:
                    distanceFrom2[adjNode] = newCost
                    heap.heappush(pq, (newCost, adjNode))
        
        possiblePaths = [0 for i in range(n+1)]
        possiblePaths[1] = 1
        visited = set()
        pq = []
        heap.heappush(pq, 1)
        while pq:
            node = heap.heappop(pq)
            visited.add(node)
            for adjNode, _ in weights[node]:
                if distanceFrom2[adjNode] < distanceFrom2[node]: 
                    possiblePaths[adjNode] += possiblePaths[node]
                    if not adjNode in visited and not adjNode in pq: heap.heappush(pq, adjNode)
        
        return possiblePaths[2]
    except:
        return -1

def main():
    res = list()
    for i in range(10):
        r = testCase()
        if r == -1: break
        res.append(r)
    print('\n'.join(map(str, res)))
    
if __name__ == "__main__":
    main()