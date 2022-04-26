for t in range(int(input())):
    n,m,k = map(int, input().split())
    cost = (n-1)+((m-1)*n)
    if cost==k:
        print('YES')
    else:
        print('NO')