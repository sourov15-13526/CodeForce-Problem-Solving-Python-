for i in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    l = []
    for j in p:
        if j in l:
            pass
        else:
            l.append(j)
    print(*l)
