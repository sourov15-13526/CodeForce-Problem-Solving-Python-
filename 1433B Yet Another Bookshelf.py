for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    while a[-1]==0:
        a.pop()
    while a[0]==0:
        a.pop(0)
    
    print(a.count(0))
    