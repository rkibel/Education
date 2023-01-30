def main():
    participants = list(int(num) for num in input().strip().split())
    strengths = list(int(num) for num in input().strip().split())
    speeds = list(int(num) for num in input().strip().split())
    speeds.sort()
    combinations = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    
    def canMakeSpeed(speed):
        p = participants.copy()
        kayaks = len(speeds)
        for i in range(kayaks):
            fails = True
            for _, n in enumerate(combinations):
                if p[n[0]] == 0 or p[n[1]] == 0: continue
                if speeds[i] * (strengths[n[0]] + strengths[n[1]]) < speed: continue
                if n[0] == n[1] and p[n[0]] < 2: continue
                p[n[0]]-=1
                p[n[1]]-=1
                fails = False
                break
            if (fails): return False
        return True
    
    
    left = 1
    right = 2000 * 100000
    ans = 0
    
    while left <= right:
        mid = int((left + right) / 2)
        if (canMakeSpeed(mid)):
            ans = mid
            left = mid + 1
        else: right = mid - 1
        
    print(ans)

if __name__ == "__main__":
    main()