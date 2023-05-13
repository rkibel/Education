def main():
    N = int(input())
    coasters = [None for i in range(N)]
    for i in range(N):
        a, b, t = (int(j) for j in input().strip().split())
        coasters[i] = (a, b, t)
        
    dp = [[-1 for i in range(25001)] for j in range(N+1)]
    dp[0][0] = 0
    
    for i in range(1, N+1):
        a, b, t = coasters[i-1]
        for j in range(25001):
            dp[i][j] = dp[i-1][j]
            
        if b == 0:
            for j in range(25001):
                if j < t or dp[i][j-t] == -1: continue
                dp[i][j] = max(dp[i][j], dp[i][j-t] + a)
        
        else:
            for j in reversed(range(25001)):
                sum = fun = a
                time = t
                k = 1
                while time <= j and fun > 0:
                    if dp[i][j-time] != -1: 
                        dp[i][j] = max(dp[i][j], dp[i][j-time] + sum)
                    k += 1
                    time += t
                    fun = a - (k-1)**2 * b
                    sum += fun
        
    Q = int(input())
    ans = list()
    for i in range(Q):
        res = 0
        for i in range(int(input())+1): res = max(res, dp[N][i])
        ans.append(res)
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()