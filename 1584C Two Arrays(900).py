for t in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    k = True
    for i in range(n):
        if b[i] != a[i] and b[i] != a[i]+1:
            print('NO')
            k = False
            break
    if k:
        print('YES')     