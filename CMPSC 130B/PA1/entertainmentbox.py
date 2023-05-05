def main():
    n, k = (int(i) for i in input().strip().split())
    times = list()
    for i in range(n):
        a, b = (int(i) for i in input().strip().split())
        times.append((a, b))
    times.sort(key = lambda x: x[1])
    records = list()
    count = 0
    for i in range(0, n):
        interval = times[i]
        kickout = -1
        for j in range(len(records)):
            if times[records[j]][1] <= interval[0] and (kickout == -1 or times[records[j]][1] > times[records[kickout]][1]):
                    kickout = j
        if kickout != -1:
            records[kickout] = i
            count += 1
        elif kickout == -1 and len(records) < k:
            records.append(i)
            count += 1
    print(count)
    
if __name__ == "__main__" :
    main()