for t in range(int(input())):
    n = int(input())
    s = ''
    for i in range(9,0,-1):
        if i<=n:
            s = str(i)+s
            n-=i
    
    if n:
        print(-1)
    else:
        print(int(s))
