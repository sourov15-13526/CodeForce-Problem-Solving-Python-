for t in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    s = input()
    l = sorted([[s[i], p[i], i] for i in range(n)])
    T = [-1 for i in range(n)]
    for x in range(n):
        T[l[x][2]] = x + 1
    print(*T)