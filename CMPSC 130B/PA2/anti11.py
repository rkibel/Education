def main():
    T = int(input())
    maxlen = 0
    lens = list()
    for i in range(T):
        length = int(input())
        lens.append(length)
        maxlen = max(maxlen, length)
        
    endswith = [[0, 0] for i in range(maxlen + 1)]
    endswith[1][0] = endswith[1][1] = 1
    
    for i in range(2, maxlen + 1):
        endswith[i][0] = (endswith[i-1][0] + endswith[i-1][1]) % (10**9 + 7)
        endswith[i][1] = endswith[i-1][0]
        
    for length in lens:
        print((endswith[length][0] + endswith[length][1]) % (10**9 + 7))

if __name__ == "__main__":
    main()