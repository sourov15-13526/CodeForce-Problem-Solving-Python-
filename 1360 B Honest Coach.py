for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    l = []
    for k in range(1,n):
        l.append(s[k]-s[k-1])
    print(min(l))




