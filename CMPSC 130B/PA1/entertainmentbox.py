from queue import PriorityQueue

def main():
    n, k = (int(i) for i in input().strip().split())
    times = list()
    for i in range(n):
        a, b = (int(i) for i in input().strip().split())
        times.append((a, b))
    times.sort()
    
    q = PriorityQueue()
    for i in range(k):
        q.put(-times[i][0])
        
    ans = k
    i = k
    while i < n:
        while (not q.empty()):
            item = q.get()
            if times[i][0] < item:
                q.put(item)
                break
        quede = k - q.qsize()
        for j in range(i, i + quede):
            q.put(-times[j][1])
        if quede > 0:
            i = i + quede - 1
        ans += quede
        i += 1
    print(ans)
    
    
if __name__ == "__main__" :
    main()