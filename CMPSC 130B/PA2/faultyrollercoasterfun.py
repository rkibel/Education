from operator import itemgetter

def main():
    N = int(input())
    coasters = [None for i in range(N)]
    minCoasterTime = 25001
    for i in range(N):
        a, b, t = (int(j) for j in input().strip().split())
        minCoasterTime = min(minCoasterTime, t)
        coasters[i] = (a, b, t)
    coasters = sorted(coasters, key=itemgetter(2))
    coasters.reverse()
    Q = int(input())
    visits = list()
    maxVisitTime = 0
    for i in range(Q):
        time = int(input())
        visits.append(time)
        maxVisitTime = max(maxVisitTime, time)
    
    # for a given amount of time in the park, stores 
    # which rides were ridden and for how many times  
    dp = [[0 for i in range(N)] for j in range(maxVisitTime + 1)]
    
    # what is the maximum fun value given that amount of time
    fun = [-1 for i in range(maxVisitTime + 1)]
    
    def mostFun(time):
        if (time < 0): return 0
        if (time < minCoasterTime):
            fun[time] = 0
            return fun[time]
        maxTotalFun = -1
        coasterToRide = -1
        for i, coaster in enumerate(coasters):
            past = time - coaster[2]
            if (past < 0): continue
            
            funUpToNow = fun[past]
            k = dp[past][i] + 1
            funValue = coaster[0] - ((k-1)**2 * coaster[1])
            if (funValue > 0 and funUpToNow + funValue > maxTotalFun):
                maxTotalFun = funUpToNow + funValue
                coasterToRide = i
        
        if (maxTotalFun > fun[time-1]):
            for i in range(N):
                dp[time][i] = dp[time - coasters[coasterToRide][2]][i]
            dp[time][coasterToRide] += 1
            fun[time] = maxTotalFun
            
        else:
            for i in range(N):
                dp[time][i] = dp[time - 1][i]
            fun[time] = fun[time-1]
            
        return fun[time]
    
    for i in range(maxVisitTime+1):
        mostFun(i)
    for visit in visits:
        print(fun[visit])
    
if __name__ == "__main__":
    main()