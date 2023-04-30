import math

def testCase():
    n, l, w = (int(i) for i in input().strip().split())
    intervals = list()
    for sprinkler in range(n):
        x, r = (int(i) for i in input().strip().split())
        if r > w/2: 
            dist = math.sqrt(r**2 - w**2/4)
            intervals.append([x - dist, x + dist])
    intervals.sort()

    start = end = count = i = 0
    while i < len(intervals):
        if (intervals[i][0] <= start):
            end = max(end, intervals[i][1])
            i += 1
        else:
            if end <= start: break
            start = end
            count += 1
            if (intervals[i][0] > end or end >= l): break
    if (end < l): return -1
    if (end > start): count += 1
    return count
    
def main():
    res = list()
    for i in range(35):
        try:
            res.append(testCase())
        except:
            break
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()