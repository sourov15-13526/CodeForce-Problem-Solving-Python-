for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    f = 0
    for x in range(n):
        if a[0]==a[x]:
            f+=1
    if f==n:
        print(-1)
    else:
        m = max(a)
        for k in range(1,n):
            if a[k]>a[k-1] and a[k]==m:
                print(k+1)
                break
            elif a[k]<a[k-1] and a[k-1]==m:
                print(k)
                break
            
    