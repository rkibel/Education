def main():
    words = input().strip().split()
    s = set()
    for word in words:
        if word in s: 
            print("no")
            return
        s.add(word)
    print("yes")
if __name__ == "__main__":
    main()