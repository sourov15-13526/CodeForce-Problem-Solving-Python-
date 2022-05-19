for t in range(int(input())):
    n,m = map(int, input().split())
    for i in range(n-1):
        print('B'*m)
    print('B'*(m-1)+'W')