import numpy as np


def doTest():
    n = int(input())
    x = list(int(num) for num in input().strip().split())
    y = list(int(num) for num in input().strip().split())
    x.sort()
    y.sort(reverse=True)
    return np.dot(x, y)
    
def main():
    testCases = int(input())
    ans = []
    for i  in range(testCases):
        ans.append(doTest())
    for i in range(testCases):
        print('Case #' + str(i+1) + ': ' + str(ans[i]))

if __name__ == "__main__":
    main()
    