for i in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    l = a[:k]+b[:k]
    l.sort(reverse=True)
    print(sum(l[:k]+a[k:]))

