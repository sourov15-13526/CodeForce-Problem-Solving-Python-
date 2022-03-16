for t in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = max(l)
    n = min(l)
    print(m-n)